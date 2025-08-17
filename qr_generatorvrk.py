import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage




def generate_qr():
    data = entry.get()
    if not data.strip():
        messagebox.showerror("Error", "enter the url.")
        return
    
    qr = qrcode.QRCode(version=1, box_size= 25, border=7)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="blue")
    
    # Ask where to save
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", f"vedant has saved ur qr code  {file_path}")

# Tkinter UI
root = tk.Tk()
root.title("VEDANT'S QR CODE GENERATOR")
background_image = PhotoImage(file="qr_code.png")
root.geometry("400x600")

label = tk.Label(root, text="Enter text or URL:", font=("Helvetica", 24))
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 20))
generate_btn.pack(pady=10)


root.mainloop()
