import tkinter as tk
from tkinter import messagebox,filedialog


class To_Do_Liste:

    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")
        self.root.title("My ToDoList")
        self.root.configure(bg='#a2d2ff')
        self.label=tk.Label(self.root,text="My To-Do:",bg='#a2d2ff',font=("Bodoni MT",18),fg="#023e8a")
        self.label.pack(padx=10,pady=10)
        #menu bare:
        self.menubar=tk.Menu(self.root)
        self.filemenu=tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Open tasks",command=self.openTaskFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save",command=self. save_tasks)
        self.menubar.add_cascade(menu=self.filemenu,label="File")
        self.root.config(menu=self.menubar) 
        self.root.config(menu=self.menubar) 
        

        self.task_count = 0 
        self.tasks=[]

        #bottonframe
        # Button frame
        self.buttonframe = tk.Frame(self.root, bg='#a2d2ff')

        self.Addbtn = tk.Button(self.buttonframe, text="Add task", font=("Arial", 10), bg="#08bdbd", width=10, height=2, command=self.add_task)
        self.Addbtn.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.deletebtn = tk.Button(self.buttonframe, text="Delete task", font=("Arial", 10), bg="#ef476f", width=10, height=2, command=self.delete_task)
        self.deletebtn.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.Modifiebtn = tk.Button(self.buttonframe, text="Update task", font=("Arial", 10), bg="#ffd166", width=10, height=2, command=self.update_task)
        self.Modifiebtn.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.Trackbtn = tk.Button(self.buttonframe, text="Track task", font=("Arial", 10), bg="#06d6a0", width=10, height=2, command=self.track_task)
        self.Trackbtn.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        
        # Pack button frame to the left
        self.buttonframe.pack(side='left', fill='y', padx=10, pady=10)

        #Champ d'entre la nouvelle tache :
        self.task_entry_label = tk.Label(self.root, text="Enter a task:",bg="#a2d2ff",font=("Bodoni MT",14),fg="#023e8a")
        self.task_entry_label.pack(pady=(10, 0))
        self.myentry=tk.Entry(self.root,bg="#bde0fe")
        self.myentry.pack(padx=10)

        # Champ d'entrée pour le numéro de la tâche à mettre à jour ou à supprimer
        self.task_number_label = tk.Label(self.root, text="Enter task number:",bg="#a2d2ff",font=("Bodoni MT",14),fg="#023e8a")
        self.task_number_label.pack(pady=(10, 0))
        self.task_number_entry = tk.Entry(self.root,bg="#bde0fe")
        self.task_number_entry.pack(padx=10)


         # Textbox
        
        self.textbox = tk.Text(self.root,height=5,font=('Script MT Bold', 18),fg="#03045e",bg="#bde0fe",state='disabled')
        self.textbox.pack(padx=10, pady=10, expand=True, fill='both')

       
         # Button frame2 (at the bottom right)
        self.buttonframe2 = tk.Frame(self.root, bg="#a2d2ff")

        # Clear button
        self.clearbtn = tk.Button(self.buttonframe2, text="Clear", bg="#06d6a0", font=("Arial", 10), width=10, height=2, command=self.clear_All)
        self.clearbtn.grid(row=0, column=0, sticky=tk.E, padx=10)

        # Place the buttonframe2 at the bottom right of the window
        self.buttonframe2.pack(side='bottom', anchor='e', padx=10, pady=10)
        self.root.mainloop()


    def add_task(self):
        self.task=self.myentry.get()
        if self.task:
            self.task_count +=1
            self.tasks.append(self.task)
            self.refresh_textbox()
            self.myentry.delete(0,tk.END)
    def delete_task(self):
        task_number = int(self.task_number_entry.get())  # Supposons que l'utilisateur entre le numéro de la tâche à supprimer
        if 1 <= task_number <= len(self.tasks): # Vérifie si le numéro de tâche est valide
            self.tasks.pop(task_number - 1)  # Supprime la tâche de la liste
            self.task_number_entry.delete(0,tk.END)
            self.refresh_textbox()
            if not self.tasks:
                self.task_count=0
        else:
            messagebox.showwarning(messagebox.showwarning("Warning", "Invalid task number."))
    def refresh_textbox(self):
        self.textbox.config(state='normal')
        self.textbox.delete("1.0", tk.END)  # Efface tout le contenu du textbox
        for i, task in enumerate(self.tasks, 1):  # Réinsère les tâches restantes
            self.textbox.insert(tk.END, f"{i}. {task}\n")
        self.textbox.config(state='disabled')

    def update_task(self):
        task_number=int(self.task_number_entry.get())   
        if 1 <= task_number <= len(self.tasks):
            new_task=self.myentry.get()
            self.tasks[task_number-1]=new_task
            self.myentry.delete(0,tk.END)
            self.task_number_entry.delete(0,tk.END)
            self.refresh_textbox()
        else:
            messagebox.showwarning(messagebox.showwarning("Warning", "Invalid task number."))
    def track_task(self):
        task_number=int(self.task_number_entry.get())

        if(1<= task_number<= len(self.tasks)):
            start_index=f"{task_number}.0"
            end_index=f"{task_number}.end"
            #utiliser la fonction tag_add de texbox:
            self.textbox.config(state="normal")
            self.textbox.tag_add("completed",start_index,end_index)
            self.textbox.tag_config("completed",overstrike=True)
            self.textbox.config(state='disabled')
            self.task_number_entry.delete(0,tk.END)
        else:
            messagebox.showwarning(messagebox.showwarning("Warning", "Invalid task number."))

    def clear_All(self):
       
        self.tasks.clear()
        self.task_count=0
        self.refresh_textbox()

    def openTaskFile(self):
        file_name=filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt")])
        try:
            if file_name:
                with open(file_name,"r") as file:
                    self.tasks=file.read().splitlines()
                self.task_count=len(self.tasks)
                self.refresh_textbox()
                messagebox.showinfo("Open", "Tasks loaded successfully!")
        except Exception as e:
                messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")


    def save_tasks(self):
        file_name=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt")])
        try:                           
            if file_name:
                with open(file_name,"w") as file:
                    for task in self.tasks:
                        file.write(task+"\n")
                messagebox.showinfo("Save","Tasks saved successfully!")
        except Exception as e:
                messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")


        



To_Do_Liste()
