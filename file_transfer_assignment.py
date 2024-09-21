# Import the needed modules
import tkinter as tk
from tkinter import filedialog
import shutil
import os

class FileCheckerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Checker App")

        # Variables to store folder paths
        self.check_folder = ""
        self.copy_folder = ""

        # Label for selecting the folder to check for files
        self.label_check = tk.Label(master, text="Select folder to check for files: ")
        self.label_check.pack(pady=10)

        # Button to browse for the folder to check
        self.button1 = tk.Button(master, text="Browse", command=self.browse_check_folder)
        self.button1.pack(pady=5)

        # Label for selecting the folder to copy files to
        self.label_copy = tk.Label(master, text="Select folder to copy files to: ")
        self.label_copy.pack(pady=5)

        # Button to browse for the folder to copy files to
        self.button2 = tk.Button(master, text="Browse", command=self.browse_copy_folder)
        self.button2.pack(pady=5)

        # Button to initiate the file check process
        self.check_button = tk.Button(master, text="Check Files", command=self.check_files)
        self.check_button.pack(pady=20)

        # Exit button
        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)

    def browse_check_folder(self):
        """Open a dialog to select the folder to check for files."""
        self.check_folder = filedialog.askdirectory()  # Ask user to select a directory
        if self.check_folder:  # If a folder was selected
            print(f"Selected folder to check: {self.check_folder}")

    def browse_copy_folder(self):
        """Open a dialog to select the folder to copy files to."""
        self.copy_folder = filedialog.askdirectory()  # Ask user to select a directory
        if self.copy_folder:  # If a folder was selected
            print(f"Selected folder to copy to: {self.copy_folder}")

    def check_files(self):
        """Check for files in the specified folder and copy them to the destination."""
        if not self.check_folder or not self.copy_folder:
            print("Please select both folders.")
            return

        # Example file check: Copy all text files from the check folder to the copy folder
        for filename in os.listdir(self.check_folder):
            if filename.endswith('.txt'):  # Check for text files
                source = os.path.join(self.check_folder, filename)
                destination = os.path.join(self.copy_folder, filename)
                shutil.copy(source, destination)  # Copy the file
                print(f"Successfully copied {source} to {destination}")

        print("File check complete.")

    def exit_app(self):
        """Close the application."""
        self.master.quit()  # Exit the Tkinter main loop

if __name__ == "__main__":
    root = tk.Tk()  # Create main window
    app = FileCheckerApp(root)  # Initialize the application
    root.mainloop()  # Start event loop for the GUI
