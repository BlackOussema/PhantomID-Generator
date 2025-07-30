import tkinter as tk
from tkinter import messagebox, font
from identity_generator import generate_fake_identity
from fingerprint_generator import generate_fingerprint
import json
import os

def save_profile_to_file(profile, filename):
    with open(filename, "w") as f:
        json.dump(profile, f, indent=4)

def generate_and_save(count):
    os.makedirs("profiles", exist_ok=True)
    for i in range(1, count + 1):
        identity = generate_fake_identity()
        fingerprint = generate_fingerprint()
        profile = {
            "identity": identity,
            "fingerprint": fingerprint
        }
        filename = f"profiles/fake_profile_{i}.json"
        save_profile_to_file(profile, filename)

def on_generate():
    try:
        count = int(entry.get())
        if count <= 0:
            messagebox.showerror("Error", "Please enter a positive integer")
            return
        generate_and_save(count)
        messagebox.showinfo("Success", f"{count} profiles generated successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

root = tk.Tk()
root.title("Fake Identity Generator")
root.geometry("400x220")
root.configure(bg="#1e1e2f")

signature_font = font.Font(family="Courier New", size=10, weight="bold", slant="italic")

label = tk.Label(root, text="Number of profiles to generate:", fg="#eeeeee", bg="#1e1e2f", font=("Helvetica", 14))
label.pack(pady=(20,5))

entry = tk.Entry(root, font=("Helvetica", 14), width=15, justify='center')
entry.pack(pady=5)

btn = tk.Button(root, text="Generate", command=on_generate, bg="#4caf50", fg="white", font=("Helvetica", 14), activebackground="#388e3c", padx=20, pady=5)
btn.pack(pady=20)

signature = tk.Label(root, text="Created by oussema ghariani 🇹🇳", fg="#bbbbbb", bg="#1e1e2f", font=signature_font)
signature.pack(side="bottom", pady=10)

root.mainloop()
