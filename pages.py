import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from ui_helpers import show_frame, create_field, createsignup_field
from database import (
    insert_user,
    get_user_by_name_password,
    get_balance,
    generate_account_no,
    update_balance,
    insert_transaction,
    get_user_by_account_no,
    get_last_n_transactions
)

current_account_no = None

main_frame = None
login_page = None
signup_page = None
show_page = None
content_frame = None
send_money_page = None
signup_success_page = None

name_entry = None
password_entry = None
pin_entry = None
account_entry = None

fullname_entry = None
mobile_entry = None
email_entry = None
Password_entry = None
Confirmpass_entry = None
Pin_entry = None
Confirmpin_entry = None


def add_top_back_button(parent, target_frame):
    btn = tk.Button(
        parent,
        text="⬅ Back",
        bg="#ef4444",
        fg="white",
        activebackground="#dc2626",
        activeforeground="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2",
        highlightthickness=0,
        command=lambda: show_frame(target_frame)
    )
    btn.place(x=10, y=10)
    btn.lift()


def build_pages(root):
    global main_frame, login_page, signup_page, signup_success_page
    global show_page, send_money_page, content_frame
    global name_entry, password_entry, pin_entry, account_entry
    global fullname_entry, mobile_entry, email_entry
    global Password_entry, Confirmpass_entry, Pin_entry, Confirmpin_entry

    signup_success_page = tk.Frame(root, bg="#e6e6e6")
    signup_success_page.place(relwidth=1, relheight=1)

    main_frame = tk.Frame(root, bg="#e6e6e6")

    header = tk.Frame(main_frame, bg="#0b1d3a", height=60)
    header.pack(fill="x")

    tk.Label(
        header,
        text="BANK MANAGEMENT SYSTEM",
        bg="#0b1d3a",
        fg="white",
        font=("Arial", 22, "bold")
    ).pack(pady=10)

    left_frame = tk.Frame(main_frame, bg="#0b1d3a", width=400)
    left_frame.pack(side="left", fill="y")
    left_frame.pack_propagate(False)

    img = Image.open("Bank_Management_System1/image/bank.png").resize((160, 160))
    bank_img = ImageTk.PhotoImage(img)
    tk.Label(left_frame, image=bank_img, bg="#0b1d3a").pack(pady=30)
    left_frame.image = bank_img

    tk.Label(left_frame, text="Welcome", bg="#0b1d3a",
             fg="white", font=("Cinzel", 35, "bold")).pack()

    right_frame = tk.Frame(main_frame, bg="#f2f5ff")
    right_frame.pack(side="right", fill="both", expand=True)

    login_card = tk.Frame(right_frame, bg="white", width=260, height=200)
    login_card.pack(side="left", padx=50, pady=50)
    login_card.pack_propagate(False)

    tk.Label(login_card, text="Returning User",
             bg="white", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(
        login_card,
        text="Login",
        bg="#1e40af",
        fg="white",
        activebackground="#1e3a8a",
        activeforeground="white",
        width=14,
        command=lambda: show_frame(login_page)
    ).grid(row=10, column=0, columnspan=2, pady=20)


    signup_card = tk.Frame(right_frame, bg="white", width=260, height=200)
    signup_card.pack(side="left", padx=10, pady=50)
    signup_card.pack_propagate(False)

    tk.Label(signup_card, text="New User",
             bg="white", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(
        signup_card,
        text="Sign Up",
        bg="#22c55e",
        fg="white",
        activebackground="#16a34a",
        activeforeground="white",
        width=14,
        command=lambda: show_frame(signup_page)
    ).pack(pady=10)

    login_page = tk.Frame(root, bg="#050427")
    add_top_back_button(login_page, main_frame)

    name_entry = create_field(login_page, "Name", "Enter your name")
    account_entry = create_field(login_page, "Account Number", "Enter account number")
    pin_entry = create_field(login_page, "PIN", "Enter PIN", True)
    password_entry = create_field(login_page, "Password", "Enter password", True)

    tk.Button(
        login_page,
        text="Login",
        bg="#020327",
        fg="white",
        activebackground="#020327",
        activeforeground="white",
        command=login_action
    ).grid(row=10, column=0, columnspan=2, pady=20)

    signup_page = tk.Frame(root, bg="black")
    add_top_back_button(signup_page, main_frame)

    fullname_entry = createsignup_field(signup_page, 0, 0, "Full Name", "Enter full name")
    mobile_entry = createsignup_field(signup_page, 0, 1, "Mobile", "Enter mobile")
    email_entry = createsignup_field(signup_page, 1, 0, "Email", "Enter email")
    Password_entry = createsignup_field(signup_page, 1, 1, "Password", "Create password", True)
    Confirmpass_entry = createsignup_field(signup_page, 2, 0, "Confirm Password", "Confirm password", True)
    Pin_entry = createsignup_field(signup_page, 2, 1, "PIN", "Create PIN", True)
    Confirmpin_entry = createsignup_field(signup_page, 3, 0, "Confirm PIN", "Confirm PIN", True)

    tk.Button(
        signup_page,
        text="Sign Up",
        bg="#22c55e",
        fg="white",
        activebackground="#16a34a",
        activeforeground="white",
        command=lambda: signup_action(
            fullname_entry,
            mobile_entry,
            email_entry,
            Password_entry,
            Confirmpass_entry,
            Pin_entry,
            Confirmpin_entry
        )
    ).grid(row=10, column=0, columnspan=2, pady=20)

    show_page = tk.Frame(root, bg="#E2E2CC")
    add_top_back_button(show_page, login_page)

    content_frame = tk.Frame(show_page, bg="white")
    content_frame.pack(expand=True)

    tk.Button(
        show_page,
        text="Send Money",
        bg="#22c55e",
        fg="white",
        activebackground="#16a34a",
        activeforeground="white",
        command=open_send_money_page
    ).pack(side="left", padx=10, pady=10)

    tk.Button(
        show_page,
        text="Show Balance",
        bg="#1e40af",
        fg="white",
        activebackground="#1e3a8a",
        activeforeground="white",
        command=show_balance
    ).pack(side="left", padx=10, pady=10)

    tk.Button(
        show_page,
        text="History",
        bg="#f59e0b",
        fg="white",
        activebackground="#d97706",
        activeforeground="white",
        command=show_history
    ).pack(side="left", padx=10, pady=10)

    send_money_page = tk.Frame(root, bg="white")
    add_top_back_button(send_money_page, show_page)

    add_top_back_button(signup_success_page, login_page)

    for frame in (
        main_frame,
        login_page,
        signup_page,
        show_page,
        send_money_page,
        signup_success_page
    ):
        frame.place(relwidth=1, relheight=1)

    show_frame(main_frame)


def login_action():
    global current_account_no
    user = get_user_by_name_password(name_entry.get(), password_entry.get())
    if user:
        fullname, mobile, email, account_no, pwd, pin = user
        current_account_no = account_no
        open_show_page(fullname, mobile, email, account_no)
    else:
        messagebox.showerror("Error", "Invalid credentials")


def signup_action(
    fullname_entry,
    mobile_entry,
    email_entry,
    Password_entry,
    confirm_pass_entry,
    Pin_entry,
    confirm_pin_entry
):
    fullname = fullname_entry.get().strip()
    mobile = mobile_entry.get().strip()
    email = email_entry.get().strip()
    password = Password_entry.get().strip()
    confirm_password = confirm_pass_entry.get().strip()
    pin = Pin_entry.get().strip()
    confirm_pin = confirm_pin_entry.get().strip()

    if not all([fullname, mobile, email, password, confirm_password, pin, confirm_pin]):
        messagebox.showerror("Error", "All fields are required")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    if pin != confirm_pin:
        messagebox.showerror("Error", "PINs do not match")
        return

    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror("Error", "Enter valid 10-digit mobile number")
        return

    account_no = generate_account_no()

    insert_user(
        fullname,
        mobile,
        email,
        account_no,
        password,
        pin
    )

    show_signup_success_page(account_no)


def show_signup_success_page(account_no):
    show_frame(signup_success_page)
    for w in signup_success_page.winfo_children():
        w.destroy()

    card = tk.Frame(signup_success_page, bg="white", width=500, height=300)
    card.place(relx=0.5, rely=0.5, anchor="center")
    card.pack_propagate(False)

    tk.Label(card, text="Account Created Successfully",
             font=("Arial", 18, "bold"), fg="green").grid(row=10, column=0, columnspan=2, pady=20)

    tk.Label(card, text=f"Account Number: {account_no}",
             font=("Arial", 14)).pack(pady=10)


def open_show_page(fullname, mobile, email, account_no):
    show_user_details(fullname, mobile, email, account_no)
    show_frame(show_page)


def show_user_details(fullname, mobile, email, account_no):
    for w in content_frame.winfo_children():
        w.destroy()

    tk.Label(content_frame, text=f"Name: {fullname}").pack()
    tk.Label(content_frame, text=f"Account No: {account_no}").pack()
    tk.Label(content_frame, text=f"Email: {email}").pack()
    tk.Label(content_frame, text=f"Mobile: {mobile}").pack()


def show_balance():
    for w in content_frame.winfo_children():
        w.destroy()
    balance = get_balance(current_account_no)
    tk.Label(content_frame, text=f"₹ {balance}",
             font=("Arial", 26, "bold"), fg="green").pack()


def open_send_money_page():
    show_frame(send_money_page)


def show_history():
    for w in content_frame.winfo_children():
        w.destroy()

    transactions = get_last_n_transactions(current_account_no, 5)

    if not transactions:
        tk.Label(content_frame, text="No transactions found").pack()
        return

    for txn in transactions:
        t_type, amt, bal, date = txn
        tk.Label(
            content_frame,
            text=f"{date} | {t_type} | ₹{amt} | Balance: ₹{bal}",
            font=("Arial", 12)
        ).pack(anchor="w")
