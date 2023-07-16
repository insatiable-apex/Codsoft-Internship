from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

task_no = 0

def add_task():
    global task_no
    task = item_box.get() 
    if task:
        task_no+=1
        task_box.insert(task_no,"-> "+task)
        item_box.delete(0,END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def edit_task():
    
    task_selected = task_box.curselection()

    if task_selected:
        edited_task = item_box.get()
        if edited_task:
            task_box.delete(task_selected) 
            task_box.insert(task_selected,"> "+edited_task)
            item_box.delete(0,END)
        else:
            messagebox.showwarning("Editing Failed","Please enter task in add-task box to edit ")

def delete_task():

    task_selected = task_box.curselection()

    if task_selected:
        confirmation_message = messagebox.askyesno("Confirm deletion","Are you sure you want to delete this task!!")
        if confirmation_message:
            task_box.delete(task_selected)

       

if __name__=="__main__":

    app = Tk()

    app.geometry("900x550")

    app.title("TODO App")

    header = Label(app,text="Todo - List",font=('Times',25,'italic','bold'),bg="black",fg="white")
    header.pack(ipadx=800,ipady=20)

    bg_image = ImageTk.PhotoImage(file="Todo_app/111.jpg")

    canvas = Canvas(app,width=800,height=500)
    canvas.pack(fill="both",expand=True)
    
    canvas.create_image(0,0,image=bg_image,anchor=NW)

    add_item_label = Label(app,text="Add Something",font=('Times',15,'bold'),fg="cyan",bg ="black",justify='left')
    add_item_label.place(relx=0.1,y=140)

    item_box = Entry(app,font=("arial",14),width=35,fg="black",bg="aquamarine")
    item_box.place(relx=0.1,y=177)

    task_item_label = Label(app,text="Your Tasks",font=("Times",15,"bold"),bg="black",fg="plum1",justify="left")
    task_item_label.place(relx=0.1,y=250)
    
    task_box = Listbox(app,height=10,width=50,font=("arial",14,'bold'),fg="black",bg="misty rose")
    task_box.place(relx=0.1,y=295)

    add_task_button = Button(app,text="Create Task",padx=20,fg="black",bg="green2",font=("Amasis MT pro black",11,'bold'),command=add_task)
    add_task_button.place(relx=0.75,y=177)

    edit_task_button = Button(app,text="Edit task",padx=25,fg="white",bg="orange",font=("Amasis MT pro black",11,'bold'),command=edit_task)
    edit_task_button.place(relx=0.75,y=295)

    delete_task_button = Button(app,text="Delete Task",padx=20,fg="white",bg="red",font=("Amasis MT pro black",11,'bold'),command=delete_task)
    delete_task_button.place(relx=0.75,y=360)

    

   
    app.mainloop()