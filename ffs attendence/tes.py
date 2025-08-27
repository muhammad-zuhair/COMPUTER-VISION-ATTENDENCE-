
import tkinter as tk
from tkinter import filedialog
import subprocess
from tkinter  import *
from PIL import ImageTk,Image
web = Tk()




web.mainloop()
class RunScriptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Run Python Script")
        self.run_button = tk.Button(root, text="Take Attendence", command=self.run_script,bg='blue')
        self.run_button.pack(pady=10)
        
      


    def run_script(self):
        script_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])

        if script_path:
            subprocess.run(["python", script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = RunScriptApp(root)
    root.mainloop()
#fronend
