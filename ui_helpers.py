
import tkinter as tk
def show_frame(frame):
    frame.tkraise()
    

def create_field(parent,label_text,placeholder,is_password=False):
    tk.Label(parent,text=label_text,bg="white",fg="#374151",
             font=("Arial",12,"bold")).pack(anchor="w", padx=40, pady=(10,2))

    frame=tk.Frame(parent,bg="#eef2ff")
    frame.pack(fill="x", padx=40)

    entry=tk.Entry(frame,bd=0,bg="#eef2ff",font=("Arial",12))
    entry.pack(fill="x", ipady=10, padx=10)

    entry.insert(0,placeholder)
    entry.config(fg="gray")

    def on_in(e):
        if entry.get()==placeholder:
            entry.delete(0,tk.END)
            entry.config(fg="black")
            if is_password: entry.config(show="*")

    def on_out(e):
        if entry.get()=="":
            entry.insert(0,placeholder)
            entry.config(fg="gray")
            if is_password: entry.config(show="")

    entry.bind("<FocusIn>",on_in)
    entry.bind("<FocusOut>",on_out)
    return entry





def createsignup_field(parent, row, col, label_text, placeholder,
                       is_password=False):

   
    tk.Label(
        parent,
        text=label_text,
        bg="white",
        fg="#374151",
        font=("Arial", 11, "bold")
    ).grid(
        row=row*2,
        column=col,
        sticky="w",
        padx=30,
        pady=(10, 4)
    )

   
    border = tk.Frame(
        parent,
        bg="#d1d5db",
        width=260,
        height=38
    )
    border.grid(
        row=row*2 + 1,
        column=col,
        padx=30,
        pady=(0, 10)
    )
    border.grid_propagate(False)

    inner = tk.Frame(border, bg="#f9fafb")
    inner.pack(fill="both", padx=1, pady=1)

    entry = tk.Entry(
        inner,
        bd=0,
        bg="#f9fafb",
        fg="gray",
        font=("Arial", 11)
    )
    entry.pack(fill="both", padx=10)

    entry.insert(0, placeholder)

    def on_focus_in(e):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="#111827")
            if is_password:
                entry.config(show="*")

    def on_focus_out(e):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")
            if is_password:
                entry.config(show="")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

    return entry




    
  