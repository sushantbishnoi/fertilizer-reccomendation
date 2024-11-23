bg_image = Image.open("")
bg_image = bg_image.resize((500, 400), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)