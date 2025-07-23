import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

# Load or initialize contacts
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def refresh_listbox(show_favorites=False):
    contact_list.delete(0, tk.END)
    display_list = [c for c in contacts if c.get("favorite", False)] if show_favorites else contacts
    for contact in display_list:
        fav_symbol = "★" if contact.get("favorite", False) else "☆"
        contact_list.insert(tk.END, f"{fav_symbol} {contact['name']} - {contact['phone']}")

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address, "favorite": False})
    save_contacts()
    refresh_listbox()
    clear_entries()
    messagebox.showinfo("Success", "Contact added!")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact to delete!")
        return
    index = selected[0]
    contact = contacts.pop(index)
    save_contacts()
    refresh_listbox()
    messagebox.showinfo("Deleted", f"Deleted contact: {contact['name']}")

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone:")
    if not query:
        return
    results = [c for c in contacts if query.lower() in c["name"].lower() or query in c["phone"]]
    if results:
        result_text = "\n".join([f"{c['name']} - {c['phone']}" for c in results])
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No contacts found!")

def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact to update!")
        return
    index = selected[0]
    contact = contacts[index]

    name = simpledialog.askstring("Update", "Enter Name:", initialvalue=contact["name"])
    phone = simpledialog.askstring("Update", "Enter Phone:", initialvalue=contact["phone"])
    email = simpledialog.askstring("Update", "Enter Email:", initialvalue=contact["email"])
    address = simpledialog.askstring("Update", "Enter Address:", initialvalue=contact["address"])

    contacts[index] = {"name": name, "phone": phone, "email": email, "address": address, "favorite": contact.get("favorite", False)}
    save_contacts()
    refresh_listbox()
    messagebox.showinfo("Updated", f"Updated contact: {name}")

def toggle_favorite():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact to favorite/unfavorite!")
        return
    index = selected[0]
    contacts[index]["favorite"] = not contacts[index].get("favorite", False)
    save_contacts()
    refresh_listbox()

def show_favorites():
    refresh_listbox(show_favorites=True)

def show_all():
    refresh_listbox(show_favorites=False)

# Main Window
root = tk.Tk()
root.title("Contact Book with Favorites")
root.geometry("550x550")
root.configure(bg="#f2f2f2")

contacts = load_contacts()

title = tk.Label(root, text="Contact Book", font=("Arial", 20, "bold"), bg="#f2f2f2")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=5)

tk.Label(frame, text="Name:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Phone:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, sticky="e")
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Email:", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0, sticky="e")
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Address:", font=("Arial", 12), bg="#f2f2f2").grid(row=3, column=0, sticky="e")
address_entry = tk.Entry(frame, width=30)
address_entry.grid(row=3, column=1, pady=5)

btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact", width=15, command=add_contact, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update Contact", width=15, command=update_contact, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Contact", width=15, command=delete_contact, bg="#f44336", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Search Contact", width=15, command=search_contact, bg="#FF9800", fg="white").grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="★ Toggle Favorite", width=15, command=toggle_favorite, bg="#9C27B0", fg="white").grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Show Favorites", width=15, command=show_favorites, bg="#795548", fg="white").grid(row=2, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Show All", width=15, command=show_all, bg="#607D8B", fg="white").grid(row=3, column=0, columnspan=2, pady=5)

contact_list = tk.Listbox(root, width=60, height=12, font=("Arial", 12))
contact_list.pack(pady=10)

refresh_listbox()

root.mainloop()
