import tkinter as tk
from tkinter import filedialog
import hashlib

malware_signatures = {
    "e99a18c428cb38d5f260853678922e03": "Sample Malware 1",
    "d41d8cd98f00b204e9800998ecf8427e": "Sample Malware 2"
}

def scan_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in malware_signatures:
                result_label.config(text=f"Malware detected: {malware_signatures[file_hash]}")
            else:
                result_label.config(text="File is clean.")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("Scanner Scammer")
root.geometry("400x400")
root.resizable(False, False)

label = tk.Label(root, text="Click 'Scan' to select and scan a file")
label.pack(pady=20)

button = tk.Button(root, text="Scan", height=10, width=20, command=scan_file)
button.pack(pady=10)

result_label = tk.Label(root, text="No file scanned yet")
result_label.pack(pady=20)

root.mainloop()