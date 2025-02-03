import os
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

class PrimePath:
    def __init__(self, root):
        self.root = root
        self.root.title("PrimePath - Customizable GUI Enhancer")
        self.root.geometry("800x600")

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Icon Set", command=self.open_icon_set)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Change Background Color", command=self.change_bg_color)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.layout_label = tk.Label(self.root, text="Select Layout:")
        self.layout_label.pack(side=tk.LEFT, padx=(10, 0))

        self.layout_option = tk.StringVar(self.root)
        self.layout_option.set("Grid")
        self.layout_menu = tk.OptionMenu(self.root, self.layout_option, "Grid", "List", "Custom", command=self.change_layout)
        self.layout_menu.pack(side=tk.LEFT, padx=(0, 10))

    def open_icon_set(self):
        file_path = filedialog.askopenfilename(title="Open Icon Set", filetypes=(("Icon files", "*.ico"), ("All files", "*.*")))
        if file_path:
            messagebox.showinfo("Icon Set Selected", f"Selected Icon Set: {os.path.basename(file_path)}")

    def change_bg_color(self):
        color_code = colorchooser.askcolor(title="Choose Background Color")
        if color_code:
            self.canvas.config(bg=color_code[1])

    def change_layout(self, layout_type):
        messagebox.showinfo("Layout Changed", f"Layout changed to: {layout_type}")

    def show_about(self):
        messagebox.showinfo("About PrimePath", "PrimePath v1.0\nEnhance your Windows GUI with customizable icon sets and layouts.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PrimePath(root)
    root.mainloop()