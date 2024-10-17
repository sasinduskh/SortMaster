import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the app
class FileZenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FileZen - Smart File Organizer")
        self.root.geometry("400x200")
        
        # Add a label
        self.label = tk.Label(root, text="Choose a folder to organize:", font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Button to select folder
        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder, font=("Helvetica", 12))
        self.select_button.pack(pady=10)

        # Button to start sorting
        self.sort_button = tk.Button(root, text="Sort Files", command=self.sort_files, font=("Helvetica", 12))
        self.sort_button.pack(pady=10)

        self.folder_path = ""

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            messagebox.showinfo("Folder Selected", f"Folder chosen: {self.folder_path}")

    def sort_files(self):
        if not self.folder_path:
            messagebox.showerror("Error", "Please select a folder first!")
            return

        # File sorting logic
        self.organize_files_by_type(self.folder_path)
        messagebox.showinfo("Success", "Files have been organized!")

    def organize_files_by_type(self, folder):
        extensions = {
            'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
            'Documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx'],
            'Music': ['mp3', 'wav', 'flac', 'aac'],
            'Videos': ['mp4', 'mkv', 'avi', 'mov'],
            'Archives': ['zip', 'rar', '7z', 'tar'],
        }

        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                file_ext = file.split('.')[-1].lower()
                
                # Find the right folder for the file type
                for category, ext_list in extensions.items():
                    if file_ext in ext_list:
                        new_folder = os.path.join(folder, category)
                        os.makedirs(new_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(new_folder, file))
                        break

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FileZenApp(root)
    root.mainloop()
