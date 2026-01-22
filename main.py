
import tkinter as tk
from database import create_table,create_transactions_table
from pages import build_pages

create_table()
create_transactions_table()
root = tk.Tk()
root.title("Bank Management System")
root.geometry("1100x650")
root.configure(bg="#e6e6e6")
root.resizable(False, False)

build_pages(root)

root.mainloop()
