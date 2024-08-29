import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")
        self.root.geometry("300x200")

        self.uploaded_files = []

        self.upload_button = tk.Button(self.root, text="Upload", command=self.upload_files)
        self.upload_button.pack(pady=20)

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_files)
        self.convert_button.pack(pady=20)

    def upload_files(self):
        filetypes = [
            ("Image files", "*.jpg *.jpeg *.png *.heic"),
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

        print(self.uploaded_files)

    def convert_files(self):
        if not self.uploaded_files:
            messagebox.showerror("Error", "No files selected for conversion.")
            return

        for file in self.uploaded_files:
            print(f"Конвертиране на файла: {file}")

        messagebox.showinfo("Success", "Files have been successfully converted!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
