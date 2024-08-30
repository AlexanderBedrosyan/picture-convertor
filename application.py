import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from type_of_pictures import *


class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.root.configure(bg='#add8e6')

        self.root.iconbitmap("icon.ico")

        self.uploaded_files = []

        self.upload_button = tk.Button(
            self.root,
            text="Upload",
            command=self.upload_files,
            bg='#ffcccb',
            fg='black'
        )
        self.upload_button.bind("<Enter>", lambda e: self.on_hover(self.upload_button, '#f08080'))
        self.upload_button.bind("<Leave>", lambda e: self.on_leave(self.upload_button, '#ffcccb'))
        self.upload_button.pack(pady=20)

        self.convert_button = tk.Button(
            self.root,
            text="Convert",
            command=self.convert_files,
            bg='#90ee90',
            fg='black'
        )
        self.convert_button.bind("<Enter>", lambda e: self.on_hover(self.convert_button, '#76c893'))
        self.convert_button.bind("<Leave>", lambda e: self.on_leave(self.convert_button, '#90ee90'))
        self.convert_button.pack(pady=20)

    def on_hover(self, button, hover_color):
        button['bg'] = hover_color

    def on_leave(self, button, leave_color):
        button['bg'] = leave_color

    def upload_files(self):
        filetypes = [
            ("Image files", "*.heic"),
            ("All files", "*.*")
        ]
        filenames = filedialog.askopenfilenames(
            title="Select images",
            filetypes=filetypes
        )
        if filenames:
            for file_path in filenames:
                self.uploaded_files.append(file_path)

        messagebox.showinfo("Selected Files", f"Selected {len(self.uploaded_files)} files.")

    def convert_files(self):
        if not self.uploaded_files:
            messagebox.showerror("Error", "No files selected for conversion.")
            return

        pictures_convertor = PictureConvertor(self.uploaded_files)
        pictures_convertor.used_web_for_changing_the_format()

        messagebox.showinfo("Success", "Files have been successfully converted!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
