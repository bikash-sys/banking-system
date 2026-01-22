
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
    get_user_by_account_no,get_last_n_transactions
)


current_account_no = None

main_frame = None
login_page = None
signup_page = None
show_page = None
content_frame = None
send_money_page=None

name_entry = None
password_entry = None
pin_entry=None
account_entry=None
signup_success_page = None


bank_img = None
bg_photo = None
logo_img = None
adduser_img = None
login_img = None
signup_img1 = None
signup_img2 = None
bank_img1 = None
current_account_no=None



fullname_entry = None
mobile_entry = None
email_entry = None
Password_entry = None
Confirmpass_entry = None
Pin_entry=None
Confirmpin_entry = None


def build_pages(root):
    global main_frame, login_page, signup_page,signup_success_page, show_page,send_money_page,content_frame, name_entry, password_entry,bank_img, bg_photo, logo_img, adduser_img,login_img, signup_img1, signup_img2, bank_img1,pin_entry, name_entry, account_entry, password_entry
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

    img = Image.open("image/bank.png").resize((160, 160))
    bank_img = ImageTk.PhotoImage(img)
    lbl = tk.Label(left_frame, image=bank_img, bg="#0b1d3a")
    lbl.image = bank_img
    lbl.pack(pady=30)

    tk.Label(left_frame, text="Welcome", bg="#0b1d3a",
             fg="white", font=("Cinzel", 35, "bold")).pack()
    tk.Label(left_frame, text="     To     ", bg="#0b1d3a",
             fg="white", font=("Cinzel", 30, "bold")).pack()
    tk.Label(left_frame, text="Bank Management System",
             bg="#0b1d3a", fg="white",
             font=("Cinzel", 22, "bold")).pack(pady=10)

    right_frame = tk.Frame(main_frame, bg="#f2f5ff")
    right_frame.pack(side="right", fill="both", expand=True)

    bg_img = Image.open("image/bg.png").resize((800, 800))
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(right_frame, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(relwidth=1, relheight=1)
    bg_label.lower()

    login_card = tk.Frame(right_frame, bg="white", width=260, height=200,
                          highlightthickness=1, highlightbackground="#050427")
    login_card.pack(side="left", padx=50, pady=50)
    login_card.pack_propagate(False)

    tk.Label(login_card, text="Returning User",
             bg="white", font=("Arial", 14, "bold")).pack(pady=10)

    logoimg = Image.open("image/login.png").resize((100, 50))
    logo_img = ImageTk.PhotoImage(logoimg)
    lbl = tk.Label(login_card, image=logo_img)
    lbl.image = logo_img
    lbl.pack()

    tk.Button(
        login_card,
        text="Login",
        bg="#1e40af",
        fg="white",
        width=14,
        command=lambda: show_frame(login_page)
    ).pack(pady=20)

    signup_card = tk.Frame(right_frame, bg="white", width=260, height=200,
                           highlightthickness=1, highlightbackground="#050427")
    signup_card.pack(side="left", padx=10, pady=50)
    signup_card.pack_propagate(False)

    tk.Label(signup_card, text="New User",
             bg="white", font=("Arial", 14, "bold")).pack(pady=10)

    addimg = Image.open("image/adduser.png").resize((100, 50))
    adduser_img = ImageTk.PhotoImage(addimg)
    lbl = tk.Label(signup_card, image=adduser_img)
    lbl.image = adduser_img
    lbl.pack()

    tk.Button(
        signup_card,
        text="Sign Up",
        bg="#22c55e",
        fg="white",
        width=14,
        command=lambda: show_frame(signup_page)
    ).pack(pady=10)

    login_page = tk.Frame(root, bg="#050427")


    loginimg=Image.open("image/loginbg.jpeg")
    loginimg=loginimg.resize((1100,650))
    login_img=ImageTk.PhotoImage(loginimg)
    tk.Label(login_page,image=login_img).pack(pady=10)


    login_card2=tk.Frame(
         login_page,
         width=500,
         height=500,
         bg="white",
         highlightthickness=1, highlightbackground="#050427"
    )
    login_card2.place(relx=0.5, rely=0.5, anchor="center")
    login_card2.pack_propagate(False)


    img1 = Image.open("image/bank.png")
    img1 = img.resize((70,70))
    bank_img1 = ImageTk.PhotoImage(img1)
    tk.Label(login_card2,image=bank_img1).pack(padx=3)


    tk.Label(login_card2, text="User Login",bg="white", fg="#05024D",font=("Arial",18, "bold")).pack(padx=3)
    tk.Label(login_card2, text="Access your account securely",bg="white", fg="#05024D",font=("Arial",10, "bold")).pack(padx=5)


    name_entry = create_field(
    login_card2,
    "Name",
    "Enter your name"
   )

    account_entry = create_field(
    login_card2,
    "Account Number",
    "Enter account number"
    )

    pin_entry = create_field(
    login_card2,
    "PIN",
    "Enter PIN",
    is_password=True
    )

    password_entry = create_field(
    login_card2,
    "Password",
    "Enter password",
    is_password=True
    )

    tk.Button(
    login_card2,
    text="Login",
    font=("Arial", 13, "bold"),
    bg="#020327",
    fg="white",
    width=14,
    cursor="hand2",
    command=login_action
   
    ).place(x=70 ,y=450)

    tk.Button(
    login_card2,
    text="Back",
    font=("Arial", 13, "bold"),
    bg="#F1F1F1",
    fg="Black",
    width=14,
    cursor="hand2",
    command=lambda:show_frame(main_frame)

    ).place(x=300 ,y=450)





    signup_page=tk.Frame(root,bg="black")

    signupimg=Image.open("image/loginbg.jpeg")
    signupimg=signupimg.resize((1200,650))
    signup_img1=ImageTk.PhotoImage(signupimg)
    tk.Label(signup_page,image=signup_img1).pack(pady=10)


    signup_card2 = tk.Frame(
    signup_page,
    width=1000,
    height=600,
    bg="white",
    highlightthickness=1,
    highlightbackground="#050427"
    )
    signup_card2.place(relx=0.5, rely=0.5, anchor="center")
    signup_card2.pack_propagate(False)

    headerimg=Image.open("image/bank.png")
    headerimg=headerimg.resize((100,100))
    signup_img2=ImageTk.PhotoImage(headerimg)
    tk.Label(signup_card2, image=signup_img2, bg="white").pack(pady=5)

    tk.Label(
    signup_card2,
    text="Create Your New Account",
    font=("Cinzel", 20, "bold"),
    fg="#020327",
    bg="white"
    ).pack(pady=5)

    canvas = tk.Canvas(signup_card2, height=2, bg="white", highlightthickness=0)
    canvas.pack(fill="x")
    canvas.create_line(250, 1, 800, 1, fill="#010e25", width=2)

    tk.Label(
    signup_card2,
    text="Register to access bank services",
    font=("Cinzel", 10),
    fg="#020327",
    bg="white"
    ).pack(pady=10)




    fields_frame = tk.Frame(signup_card2, bg="white")
    fields_frame.pack(pady=20)


    fields_frame.grid_columnconfigure(0, minsize=320)
    fields_frame.grid_columnconfigure(1, minsize=320)



    fullname_entry=createsignup_field(fields_frame, 0, 0, "Full Name", "Enter full name")
    mobile_entry=createsignup_field(fields_frame, 0, 1, "Mobile Number", "Enter mobile number")

    email_entry=createsignup_field(fields_frame, 1, 0, "Email", "Enter email")

    Password_entry=createsignup_field(fields_frame, 1, 1, "Password", "Create password")

    Confirmpass_entry=createsignup_field(fields_frame, 2, 0, "Confirm Password", "Confirm password", True)
    Pin_entry=createsignup_field(fields_frame, 2, 1, "PIN", "Create Pin", True)

    Confirmpin_entry=createsignup_field(fields_frame, 3, 0, "Confirm PIN", " Confrim PIN", True)


    tk.Button(
    signup_card2,
    text="Sign Up",
    font=("Arial", 13, "bold"),
    bg="#22c55e",
    fg="white",
    width=14,
    cursor="hand2",
    command=lambda: signup_action(
        fullname_entry,
        mobile_entry,
        email_entry,
        Password_entry,
        Confirmpass_entry,
        Pin_entry,
        Confirmpin_entry
    )
   ).place(x=200,y=520)



    tk.Button(signup_card2,
          text="Back",
          font=("Arial", 13, "bold"),
          bg="#F1F1F1",
          fg="Black",
    width=14,
    cursor="hand2",
    command=show_login_page
    ).place(x=550 ,y=520)


    show_page = tk.Frame(root, bg="#E2E2CC")

    card = tk.Frame(
    show_page,
    bg="white",
    width=700,
    height=500,
    highlightthickness=1,
    highlightbackground="blue"
)
    card.place(relx=0.5, rely=0.5, anchor="center")
    card.pack_propagate(False)

    heading = tk.Frame(card, bg="blue", height=60)
    heading.pack(fill="x")

    tk.Label(
    heading,
    text="Welcome to Your Account",
    bg="blue",
    fg="white",
    font=("Arial", 20, "bold")
    ).pack(pady=12)

    content_frame = tk.Frame(card, bg="white")
    content_frame.pack(expand=True, fill="both", padx=120, pady=90)


    button_frame = tk.Frame(card, bg="blue",height=80)
    button_frame.pack(fill="x",side="bottom",ipady=20)
    button_frame.pack_propagate(False)

    tk.Button(
    button_frame,
      text="Send Money",
        bg="#22c55e",
          fg="white",
            font=("Arial", 12, "bold"), width=15,
            command=open_send_money_page).pack(side="left", padx=10)


    tk.Frame(button_frame, bg="blue").pack(side="left", expand=True) 

    tk.Button(button_frame,
           text="Show Balance", 
           bg="#1e40af",
             fg="white",
          font=("Arial", 12, "bold"), 
          width=15,
          command=show_balance).pack(side="left", pady=20)


    tk.Frame(button_frame, bg="blue").pack(side="left", expand=True)

    tk.Button(button_frame,
           text="History",
             bg="#f59e0b",
               fg="white",
              font=("Arial", 12, "bold"),
            width=15,
            command=show_history).pack(side="right", padx=10, pady=20) 

    tk.Button(
    button_frame,
    text="Back",
    bg="#ef4444",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15,
    command=show_login_page
     ).pack(side="right", padx=10)

    send_money_page=tk.Frame(root,bg="white")
    send_money_page.pack()
    card = tk.Frame(
    send_money_page,
    bg="white",
    width=700,
    height=500,
    highlightthickness=1,
    highlightbackground="blue"
    )
    card.place(relx=0.5, rely=0.5, anchor="center")
    card.pack_propagate(False)

    heading = tk.Frame(card, bg="blue", height=60)
    heading.pack(fill="x")

    tk.Label(
    heading,
    text="Send Money ",
    bg="blue",
    fg="white",
    font=("Arial", 20, "bold")
    ).pack(pady=12)


    form = tk.Frame(card, bg="white")
    form.pack(pady=10)
    
    receiver_name = create_field(
        form, "Receiver Name", "Enter receiver name"
    )

    receiver_acc = create_field(
        form, "Receiver Account No", "Enter account number"
    )

    amount_entry = create_field(
        form, "Amount", "Enter amount"
    )

    sender_pin_entry = create_field(
        form, "Your PIN", "Enter your PIN", is_password=True
    )

    btn_frame = tk.Frame(card, bg="white")
    btn_frame.pack(side="bottom", pady=20)
    
    tk.Button(
        btn_frame,
        text="Send",
        bg="#22c55e",
        fg="white",
        font=("Arial", 12, "bold"),
        width=14,
        cursor="hand2",
        command=lambda: send_money_action(
        receiver_name,
        receiver_acc,
        amount_entry,
        sender_pin_entry
    )
    ).pack(side="left", padx=10)


    for frame in (main_frame, login_page, signup_page, show_page,send_money_page):
        frame.place(relwidth=1, relheight=1)

    show_frame(main_frame)


def login_action():
    global current_account_no
    user = get_user_by_name_password(
        name_entry.get(), password_entry.get()
    )

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
    
    clear_signup_entries([
        (fullname_entry, "Enter full name", False),
        (mobile_entry, "Enter mobile number", False),
        (email_entry, "Enter email", False),
        (Password_entry, "Create password", True),
        (confirm_pass_entry, "Confirm password", True),
        (Pin_entry, "Create PIN", True),
        (confirm_pin_entry, "Confirm PIN", True)
    ])

    show_signup_success_page(account_no)




def show_signup_success_page(account_no):
    show_frame(signup_success_page)

    for w in signup_success_page.winfo_children():
        w.destroy()

    card = tk.Frame(
        signup_success_page,
        bg="white",
        width=500,
        height=300,
        highlightthickness=2,
        highlightbackground="#22c55e"
    )
    card.place(relx=0.5, rely=0.5, anchor="center")
    card.pack_propagate(False)

    tk.Label(
        card,
        text="✅ Account Created Successfully",
        font=("Arial", 18, "bold"),
        fg="#22c55e",
        bg="white"
    ).pack(pady=30)

    tk.Label(
        card,
        text=f"Your Account Number:\n{account_no}",
        font=("Arial", 13),
        bg="white"
    ).pack(pady=10)

    tk.Button(
        card,
        text="Go to Login",
        bg="#1e40af",
        fg="white",
        font=("Arial", 12, "bold"),
        width=16,
        command=lambda: show_frame(login_page)
    ).pack(pady=30)




def open_show_page(fullname, mobile, email, account_no):
    
     show_user_details(fullname, mobile, email, account_no)  
     show_frame(show_page)





def show_user_details(fullname, mobile, email, account_no):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    def info(title, value):
      line = tk.Frame(content_frame, bg="white")
      line.pack(fill="x", pady=6)
      
      tk.Label(
        line,
        text=title,
        fg="blue",
        bg="white",
        font=("Arial", 13, "bold"),
        width=15,
        anchor="w"
    ).pack(side="left")

      tk.Label(
        line,
        text=value,
        fg="black",
        bg="white",
        font=("Arial", 13),
        anchor="w",
        bd=1,            
        relief="solid",  
        padx=5, pady=2 
    ).pack(side="left")

    info("Name   :-", fullname)
    info("Account No   :-", account_no)
    info("Email  :-", email)
    info("Mobile  :-", mobile)





def show_balance():
    balance = get_balance(current_account_no)
    for w in content_frame.winfo_children():
        w.destroy()

    tk.Label(content_frame, text="Account Balance",
             font=("Arial", 18, "bold")).pack(pady=10)
    tk.Label(content_frame, text=f"₹ {balance}",
             font=("Arial", 26, "bold"),
             fg="green").pack()




def open_send_money_page():
    show_frame(send_money_page)








def send_money_action(receiver_name,
        receiver_acc,
        amount_entry,
        sender_pin_entry):
    r_name = receiver_name.get()
    r_acc = receiver_acc.get()
    amt = amount_entry.get()
    pin = sender_pin_entry.get()

    if not all([r_name, r_acc, amt, pin]):
        messagebox.showerror("Error", "All fields are required")
        return

    if not amt.isdigit() or int(amt) <= 0:
        messagebox.showerror("Error", "Invalid amount")
        return

    amt = int(amt)

    sender = get_user_by_account_no(current_account_no)
    # sender_pin_db = sender[6]
    sender_balance = sender[7]

  

    sender_pin_db = str(sender[6]).strip()
    pin = pin.strip()

    if pin != sender_pin_db:
        messagebox.showerror("Error", "Incorrect PIN")
        return

    if sender_balance < amt:
        messagebox.showerror("Error", "Insufficient balance")
        return

    receiver = get_user_by_account_no(r_acc)
    if not receiver:
        messagebox.showerror("Error", "Receiver not found")
        return

    receiver_balance = receiver[7]

    update_balance(current_account_no, sender_balance - amt)
    update_balance(r_acc, receiver_balance + amt)

    # transaction history
    # insert_transaction(
    #     current_account_no,
    #     r_acc,
    #     amt,
    #     "SUCCESS"
    # )


# sender history
    insert_transaction(
    current_account_no,
    "SEND",
    amt,
    sender_balance - amt
)

# receiver history
    insert_transaction(
    r_acc,
    "RECEIVE",
    amt,
    receiver_balance + amt
)

    show_frame(show_page)
    show_transaction_success(amt, r_acc)










def show_transaction_success(amount, receiver_acc):
    for w in content_frame.winfo_children():
        w.destroy()

    box = tk.Frame(
        content_frame,
        bg="white",
        width=420,
        height=300,
        highlightthickness=2,
        highlightbackground="#22c55e"
    )
    box.pack(expand=True)
    box.pack_propagate(False)

    tk.Label(
        box,
        text="✅ Transaction Successful",
        font=("Arial", 20, "bold"),
        fg="#22c55e",
        bg="white"
    ).pack(pady=25)

    tk.Label(
        box,
        text=f"₹ {amount} Sent Successfully",
        font=("Arial", 15, "bold"),
        bg="white"
    ).pack(pady=5)

    tk.Label(
        box,
        text=f"To Account No: {receiver_acc}",
        font=("Arial", 12),
        bg="white"
    ).pack(pady=5)

    tk.Button(
        box,
        text="Back to Home",
        bg="#1e40af",
        fg="white",
        font=("Arial", 12, "bold"),
        width=18,
        cursor="hand2",
        command=lambda: show_frame(main_frame)
    ).pack(pady=25) 



def clear_login_entries():
    if name_entry is not None:
        name_entry.delete(0, tk.END)
        name_entry.insert(0, "Enter your name")
    if account_entry is not None:
        account_entry.delete(0, tk.END)
        account_entry.insert(0, "Enter account number")
    if pin_entry is not None:
        pin_entry.delete(0, tk.END)
        pin_entry.insert(0, "Enter PIN")
        pin_entry.config(show="") 
    if password_entry is not None:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Enter password")
        password_entry.config(show="")  


def clear_signup_entries(entries):
    """
    entries: list of tuples [(entry_widget, placeholder, is_password), ...]
    """
    for entry, placeholder, is_password in entries:
        if entry is not None:
            entry.delete(0, tk.END)       
            entry.insert(0, placeholder)
            if is_password:
                entry.config(show="")
            else:
                entry.config(show="") 





def show_login_page():
    clear_login_entries()
    show_frame(login_page) 

def show_login_page():
    clear_login_entries()
    show_frame(login_page)



def deposit_money(account_no, amount):
    balance = get_balance(account_no)
    new_balance = balance + amount

    update_balance(account_no, new_balance)

    insert_transaction(
        account_no,
        "DEPOSIT",
        amount,
        new_balance
    )
     


def show_history():
    for w in content_frame.winfo_children():
        w.destroy()

    tk.Label(
        content_frame,
        text="Transaction History",
        font=("Arial", 18, "bold"),
        fg="blue"
    ).pack(pady=10)

    transactions = get_last_n_transactions(current_account_no, 5)

    if not transactions:
        tk.Label(content_frame, text="No transactions found").pack()
        return

    for txn in transactions:
        t_type, amt, bal, date = txn
        tk.Label(
            content_frame,
            text=f"{date} | {t_type} | ₹{amt} | Balance: ₹{bal}",
            font=("Arial", 12),
            anchor="w"
        ).pack(fill="x", padx=10, pady=2)


