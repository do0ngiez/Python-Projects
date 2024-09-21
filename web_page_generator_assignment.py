# Import the needed modules
import tkinter as tk 
import webbrowser
import os 

# Create Web Page Generator class
class PageGenerator:
    def __init__(self, master):
        self.master = master
        # Set window title
        self.master.title("Web Page Generator") 
        
        # Create label for instructions
        self.label = tk.Label(master, text="Enter a word: ")
        self.label.pack(pady=10)
        
        # Add text entry widget
        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack(pady=10, padx=20)
        
        # Add button
        self.generate_button = tk.Button(master, text="Generate Web Page", command=self.generate_web_page)
        self.generate_button.pack(pady=20)

    def generate_web_page(self):
        """Generates a simple HTML file with user input as the content."""
        user_input = self.text_entry.get()  # Get the input text from the text entry widget

        # Simple HTML script 
        html_content = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Web Page Generated</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    color: #333;
                }}
                p {{
                    font-size: 16px;
                    line-height: 1.5;
                    color: #555;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Generated Content:</h1>
                <p>{user_input}</p>
            </div>
        </body>
        </html>"""
        
        # File path for the HTML file
        fpath = "web_page_generated.html"

        # Write the HTML content to the file
        with open(fpath, 'w') as file:
            file.write(html_content)

        # Open the HTML file in the web browser
        webbrowser.open('file://' + os.path.realpath(fpath))

if __name__ == "__main__":
    root = tk.Tk()  # Create main window
    app = PageGenerator(root)  # Initialize the app
    root.mainloop()  # Start event loop for the GUI
