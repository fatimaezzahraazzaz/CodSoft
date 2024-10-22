import tkinter as tk
from tkinter import messagebox, ttk

class Contact_Book:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x600")
        self.root.title("MY Contact Book")
        self.root.config(bg="#f0f0f0")  # Background color for the window
        
        # Title Label
        self.label = tk.Label(self.root, text="Contact Book", font=("Arial", 20, "bold"), fg="#333", bg="#f0f0f0")
        self.label.pack(padx=10, pady=10)

        # Button frame
        self.buttonframe = tk.Frame(self.root, bg="#f0f0f0")
        self.buttonframe.place(x=10, y=60)

        button_style = {"font": ("Arial", 12, "bold"), "width": 10, "bg": "#4CAF50", "fg": "white"}

        # Add Button
        self.Addbtn = tk.Button(self.buttonframe, text="Add", command=self.add_Contact, **button_style)
        self.Addbtn.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        # Update Button
        self.Updatebtn = tk.Button(self.buttonframe, text="Update", command=self.Up_Contact, **button_style)
        self.Updatebtn.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        # Delete Button
        self.Deletebtn = tk.Button(self.buttonframe, text="Delete", command=self.Del_Contact, **button_style)
        self.Deletebtn.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        # Search Button
        self.Searchbtn = tk.Button(self.buttonframe, text="Search", command=self.search_Contact, **button_style)
        self.Searchbtn.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        # Fields (Name, Phone, etc.)
        entry_style = {"font": ("Arial", 11), "bg": "#e6e6e6", "fg": "#333"}

        self.nameLabel = tk.Label(self.root, text="Name:", font=("Arial", 11, "bold"), bg="#f0f0f0")
        self.nameEntry = tk.Entry(self.root, **entry_style)
        self.nameLabel.place(x=150, y=80)
        self.nameEntry.place(x=250, y=80)

        self.PhoneLabel = tk.Label(self.root, text="Phone:", font=("Arial", 11, "bold"), bg="#f0f0f0")
        self.PhoneEntry = tk.Entry(self.root, **entry_style)
        self.PhoneLabel.place(x=150, y=120)
        self.PhoneEntry.place(x=250, y=120)

        self.EmailLabel = tk.Label(self.root, text="Email:", font=("Arial", 11, "bold"), bg="#f0f0f0")
        self.EmailEntry = tk.Entry(self.root, **entry_style)
        self.EmailLabel.place(x=150, y=160)
        self.EmailEntry.place(x=250, y=160)

        self.ADDRLabel = tk.Label(self.root, text="Address:", font=("Arial", 11, "bold"), bg="#f0f0f0")
        self.ADDREntry = tk.Entry(self.root, **entry_style)
        self.ADDRLabel.place(x=150, y=200)
        self.ADDREntry.place(x=250, y=200)

        # Treeview for contacts
        self.contact_tree = ttk.Treeview(self.root, columns=('Name', 'Phone', 'Email', 'Address'), show='headings', height=15)
        self.contact_tree.heading('Name', text='Name')
        self.contact_tree.heading('Phone', text='Phone')
        self.contact_tree.heading('Email', text='Email')
        self.contact_tree.heading('Address', text='Address')
        
        # Set column widths
        self.contact_tree.column('Name', width=100)
        self.contact_tree.column('Phone', width=100)
        self.contact_tree.column('Email', width=150)
        self.contact_tree.column('Address', width=150)
        
        self.contact_tree.place(x=150, y=240)
        self.contact_tree.bind("<<TreeviewSelect>>", self.on_select)

        self.root.mainloop()

    def add_Contact(self):
        name = self.nameEntry.get().strip()
        phone = self.PhoneEntry.get().strip()
        email = self.EmailEntry.get().strip()
        address = self.ADDREntry.get().strip()
        
        if name and phone and email and address:
            self.contact_tree.insert("", "end", values=(name, phone, email, address))
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Tous les champs doivent être remplis !")

    def clear_entries(self):
        self.nameEntry.delete(0, tk.END)
        self.PhoneEntry.delete(0, tk.END)
        self.EmailEntry.delete(0, tk.END)
        self.ADDREntry.delete(0, tk.END)

    def Up_Contact(self):
        selected_item = self.contact_tree.selection()
        if selected_item:
            name = self.nameEntry.get().strip()
            phone = self.PhoneEntry.get().strip()
            email = self.EmailEntry.get().strip()
            address = self.ADDREntry.get().strip()
            
            if name and phone and email and address:
                self.contact_tree.item(selected_item, values=(name, phone, email, address))
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Tous les champs doivent être remplis !")
        else:
            messagebox.showerror("Error", "Veuillez sélectionner un contact à mettre à jour.")

    def Del_Contact(self):
        selected_item = self.contact_tree.selection()
        if selected_item:
            self.contact_tree.delete(selected_item)
        else:
            messagebox.showerror("Error", "Veuillez sélectionner un contact à supprimer.")

    def search_Contact(self):
        search_name = self.nameEntry.get().strip().lower()
        search_phone = self.PhoneEntry.get().strip()

        if not search_name and not search_phone:
            messagebox.showerror("Error", "Veuillez entrer un nom ou un numéro de téléphone pour rechercher.")
            return

        found = False
        for item in self.contact_tree.get_children():
            values = self.contact_tree.item(item, 'values')
            if (search_name and search_name in values[0].lower()) or (search_phone and search_phone in values[1]):
                self.contact_tree.selection_set(item)
                found = True
                break

        if not found:
            messagebox.showinfo("Résultats de la recherche", "Aucun contact correspondant trouvé.")

    def on_select(self, event):
        # Get the selected item
        selected_item = self.contact_tree.selection()
        if selected_item:
            # Get the values of the selected item
            values = self.contact_tree.item(selected_item, 'values')
            # Pre-fill the entry fields
            self.nameEntry.delete(0, tk.END)
            self.nameEntry.insert(0, values[0])
            self.PhoneEntry.delete(0, tk.END)
            self.PhoneEntry.insert(0, values[1])
            self.EmailEntry.delete(0, tk.END)
            self.EmailEntry.insert(0, values[2])
            self.ADDREntry.delete(0, tk.END)
            self.ADDREntry.insert(0, values[3])

Contact_Book()
