import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox


def order_manager_ablak():
    current_ID = None
    orders = None
    background_color = "#2a202e"
    root = tkinter.Tk()
    root.title("Order Manager")
    root.geometry("700x500")
    root.resizable(False, False)
    root.configure(bg=background_color)

    kapcsolat = sqlite3.connect("DB/orders.db")
    ab = kapcsolat.cursor()


    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            ab.close()
            kapcsolat.close()


    root.protocol("WM_DELETE_WINDOW", on_closing)

    ID_string = tkinter.StringVar()
    name_string = tkinter.StringVar()
    address_string = tkinter.StringVar()
    item_string = tkinter.StringVar()
    amount_string = tkinter.StringVar()


    def refresh_treeview():
        global current_ID, orders
        ab.execute("SELECT * FROM orders")
        orders = ab.fetchall()
        db_treeview.delete(*db_treeview.get_children())
        count = 0
        for record in orders:
            db_treeview.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1],
                                                                                   record[2], record[3], record[4]))
            count += 1
        current_ID = orders[count-1][0]


    def add_order():
        global current_ID
        print("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", (current_ID+1, name_string.get(),
                                                            address_string.get(),
                                                            item_string.get(),
                                                            amount_string.get()))
        ab.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
                   (current_ID+1, name_string.get(),
                    address_string.get(),
                    item_string.get(),
                    amount_string.get()))
        kapcsolat.commit()
        refresh_treeview()
        ID_string.set(current_ID)


    def remove_order():
        print("DELETE FROM orders WHERE orderID = ?", (ID_string.get()))
        ab.execute("DELETE FROM orders WHERE orderID = ?", (ID_string.get(),))
        kapcsolat.commit()
        refresh_treeview()


    def update_order():
        print("UPDATE orders SET name = ?, address = ?, product = ?, amount = ? WHERE orderID = ?", (name_string.get(),
                                                                                                     address_string.get(),
                                                                                                     item_string.get(),
                                                                                                     amount_string.get(),
                                                                                                     ID_string.get()))
        ab.execute("UPDATE orders SET name = ?, address = ?, product = ?, amount = ? WHERE orderID = ?",
                   (name_string.get(),
                    address_string.get(),
                    item_string.get(),
                    amount_string.get(),
                    ID_string.get()))
        kapcsolat.commit()
        refresh_treeview()


    img = (Image.open("Assets/truck.jpg"))
    resized_image = img.resize((335,180))
    photo = ImageTk.PhotoImage(resized_image)

    logo = tkinter.Label(root, image=photo, bg=background_color)
    logo.image = photo
    logo.grid(row=0, column=2, rowspan=5, columnspan=4)

    focim = tkinter.Label(root, text="Order Manager", bg=background_color, fg="white", font=("TkMenuFont", 14))
    focim.grid(row=0, column=0, sticky="w", pady=10, padx=10)
    idLabel = tkinter.Label(root, text="ID:", bg=background_color, fg="white", font=("TkMenuFont", 10))
    idLabel.grid(row=1, column=0, sticky="w", pady=5, padx=30)
    nameLabel = tkinter.Label(root, text="Név:", bg=background_color, fg="white", font=("TkMenuFont", 10))
    nameLabel.grid(row=2, column=0, sticky="w", pady=5, padx=30)
    addressLabel = tkinter.Label(root, text="Lakcím:", bg=background_color, fg="white", font=("TkMenuFont", 10))
    addressLabel.grid(row=3, column=0, sticky="w", pady=5, padx=30)
    itemLabel = tkinter.Label(root, text="Rendelt tárgy:", bg=background_color, fg="white", font=("TkMenuFont", 10))
    itemLabel.grid(row=4, column=0, sticky="w", pady=5, padx=30)
    amountLabel = tkinter.Label(root, text="Rendelt mennyiség:", bg=background_color, fg="white", font=("TkMenuFont", 10))
    amountLabel.grid(row=5, column=0, sticky="w", pady=5, padx=30)

    idEntry = tkinter.Entry(root, width=20, textvariable=ID_string)
    idEntry.grid(row=1, column=1, sticky="w")
    nameEntry = tkinter.Entry(root, width=20, textvariable=name_string)
    nameEntry.grid(row=2, column=1, sticky="w")
    addressEntry = tkinter.Entry(root, width=20, textvariable=address_string)
    addressEntry.grid(row=3, column=1, sticky="w")
    itemEntry = tkinter.Entry(root, width=20, textvariable=item_string)
    itemEntry.grid(row=4, column=1, sticky="w")
    amountEntry = tkinter.Entry(root, width=20, textvariable=amount_string)
    amountEntry.grid(row=5, column=1, sticky="w")

    db_treeview = ttk.Treeview(root)

    db_treeview['columns'] = ("Order ID", "Name", "Address", "Item", "Amount")

    db_treeview.column("#0", width=0, stretch=False)
    db_treeview.column("Order ID", anchor="w", width=75)
    db_treeview.column("Name", anchor="w", width=150)
    db_treeview.column("Address", anchor="w", width=300)
    db_treeview.column("Item", anchor="w", width=100)
    db_treeview.column("Amount", anchor="w", width=75)

    db_treeview.heading("#0", text="", anchor="w")
    db_treeview.heading("Order ID", text="Order ID", anchor="w")
    db_treeview.heading("Name", text="Name", anchor="w")
    db_treeview.heading("Address", text="Address", anchor="w")
    db_treeview.heading("Item", text="Item", anchor="w")
    db_treeview.heading("Amount", text="Amount", anchor="w")

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Treeview", background="#775a82",
                    fieldbackground="#775a82", foreground="white")

    db_treeview.grid(row=6, column=0, columnspan=6, pady=20)

    refresh_treeview()

    button_add = tkinter.Button(root, text="Hozzáadás", command=add_order, width=10)
    button_add.grid(row=5, column=2)
    button_update = tkinter.Button(root, text="Módosítás", command=update_order, width=10)
    button_update.grid(row=5, column=3)
    button_remove = tkinter.Button(root, text="Törlés", command=remove_order, width=10)
    button_remove.grid(row=5, column=4)


    root.mainloop()
