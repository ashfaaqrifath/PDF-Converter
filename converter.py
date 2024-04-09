import os
import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import messagebox, filedialog
from docx2pdf import convert

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def convert_file():
    docx_file = file_entry.get()

    convert(docx_file, "output.pdf")
    messagebox.showinfo("Convert Success", "Converted file")

def callback(url):
    webbrowser.open_new_tab(url)

# Create Tkinter window
root = tk.Tk()
#root.geometry("370x370")
root.resizable(False, False)
root.title("PDF Converter v1.0.0")
root.config(background="#a30000")



app_banner = Label(root, text="PDF Converter",
                        padx=15,
                        pady=15,
                        bg="#a30000",
                        fg="white",
                        font="Magneto 20 bold")
app_banner.grid(row=0,
                    column=1,
                    padx=5,
                    columnspan=3)

copyright_label = Label(root, text="Copyright © Ashfaaq Rifath",
                    padx=0,
                    pady=0,
                    bg="#a30000",
                    fg="white",)
copyright_label.grid(row=1,
                column=1,
                pady=0,
                padx=0,
                columnspan=3)



# File Selection
file_label = Label(root,
                    text="Selected file:",
                    fg="white",
                    bg="#a30000",
                    font=("Helvetica", 10, "bold"))

file_label.grid(row=2, column=1, padx=5, pady=5)

file_entry = Entry(root, width=50)
file_entry.grid(row=2, column=2, padx=5, pady=5)

select_btn = Button(root,
                    text="Select file",
                    command=select_file,
                    width=10,
                    bg="#ffc800",
                    pady=4,
                    padx=10,
                    relief=GROOVE,
                    font="Arial 10 bold")

select_btn.grid(row=2, column=3, padx=5, pady=5)


# Convert Button
convert_btn = Button(root,
                    text="Convert",
                    command=convert_file,
                    width=10,
                    bg="#1fab00",
                    pady=10,
                    padx=15,
                    relief=GROOVE,
                    font="Arial 11 bold")

convert_btn.grid(row=3, column=2, padx=5, pady=5)






github_link = Label(root, text="GitHub", font="Arial 10", fg="white", bg="#a30000", cursor="hand2")
github_link.grid(row=8,
                column=2,)
github_link.bind("<Button-1>", lambda e:
callback("https://github.com/ashfaaqrifath/YouTube-Downloader"))

# Run the Tkinter event loop
root.mainloop()
