import tkinter as tk
from tkinter import messagebox
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from PIL import Image, ImageTk

# Load the dataset and preprocess it
df = pd.read_csv('Fertilizer_Recommendation.csv')

# Encoding categorical variables
label_encoders = {}
categorical_columns = ['Soil Type', 'Crop Type', 'Fertilizer Name']

for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Split the data into features and target
X = df.drop('Fertilizer Name', axis=1)
y = df['Fertilizer Name']

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# GUI Application
def recommend_fertilizer():
    try:
        # Gather inputs
        temp = int(entry_temp.get())
        humidity = int(entry_humidity.get())
        moisture = int(entry_moisture.get())
        soil_type = label_encoders['Soil Type'].transform([entry_soil_type.get()])[0]
        crop_type = label_encoders['Crop Type'].transform([entry_crop_type.get()])[0]
        nitrogen = int(entry_nitrogen.get())
        potassium = int(entry_potassium.get())
        phosphorous = int(entry_phosphorous.get())
        
        # Create input array
        input_data = [[temp, humidity, moisture, soil_type, crop_type, nitrogen, potassium, phosphorous]]
        
        # Predict the fertilizer
        fertilizer_code = model.predict(input_data)[0]
        fertilizer_name = label_encoders['Fertilizer Name'].inverse_transform([fertilizer_code])[0]
        
        # Show the result
        messagebox.showinfo("Recommendation", f"Recommended Fertilizer: {fertilizer_name}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize the GUI window
window = tk.Tk()
window.title("Fertilizer Recommendation System")
window.configure(background="light blue")

# Load and display the background image on the left side
bg_image = Image.open("image.jpg")
bg_image = bg_image.resize((400, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(window, image=bg_photo)
bg_label.pack(side=tk.LEFT, fill=tk.Y)

# Frame for the input fields on the right side
input_frame = tk.Frame(window, bg='lightblue', bd=5)
input_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Labels and entry fields
fields = [
    ("Temperature:", 0), ("Humidity:", 1), ("Moisture:", 2),
    ("Soil Type:", 3), ("Crop Type:", 4), ("Nitrogen:", 5),
    ("Potassium:", 6), ("Phosphorous:", 7)
]

entries = {}

for field, row in fields:
    tk.Label(input_frame, text=field, bg='lightblue', font=('Perpetua Titling MT', 10, 'bold')).grid(row=row, column=0, pady=5, sticky=tk.W)
    entry = tk.Entry(input_frame)
    entry.grid(row=row, column=1, pady=5)
    entries[field] = entry

entry_temp = entries["Temperature:"]
entry_humidity = entries["Humidity:"]
entry_moisture = entries["Moisture:"]
entry_soil_type = entries["Soil Type:"]
entry_crop_type = entries["Crop Type:"]
entry_nitrogen = entries["Nitrogen:"]
entry_potassium = entries["Potassium:"]
entry_phosphorous = entries["Phosphorous:"]

# Button to recommend fertilizer at the bottom of the input frame
recommend_button = tk.Button(input_frame, text="Recommend Fertilizer", font=('Perpetua Titling MT', 12, 'bold'), bg='Steel Blue', fg='white', command=recommend_fertilizer)
recommend_button.grid(row=8, column=0, columnspan=2, pady=36)

# Run the application
window.mainloop()
