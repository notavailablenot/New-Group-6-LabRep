from tkinter import *
from tkinter import filedialog

def browse_files():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

    if filename:
        label_file_explorer.config(text="File Location: " + filename)

def exit_app():
    window.destroy()

window = Tk()
window.title('File Explorer')
window.geometry("800x150")
window.config(background="purple")

label_file_explorer = Label(
    window,
    text="FILE EXPLORER",
    width=130,
    height=4,
    fg="black"
)

button_explore = Button(
    window,
    text="Search",
    command=browse_files
)

button_exit = Button(
    window,
    text="Exit",
    command=exit_app
)

label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2, pady=10)
button_exit.grid(column=1, row=3, pady=10)

window.mainloop()
