import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database and tasks table if they don't exist
def initialize_database():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        activity TEXT NOT NULL,
        time TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Function to add a task to the database
def add_task():
    user = user_entry.get()
    activity = activity_entry.get()
    time = time_entry.get()
    
    if user and activity and time:
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (user, activity, time) VALUES (?, ?, ?)', (user, activity, time))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Task added successfully!')
        user_entry.delete(0, tk.END)
        activity_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'Please fill all fields')

# Function to view all tasks
def view_tasks():
    tasks_list.delete(0, tk.END)
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        tasks_list.insert(tk.END, row)

# Function to clear the task list
def clear_tasks():
    tasks_list.delete(0, tk.END)

# Initialize the database
initialize_database()

# Create the main application window
app = tk.Tk()
app.title('To-Do List')

# Create and place the labels and entry widgets
tk.Label(app, text='User').grid(row=0, column=0, padx=10, pady=10)
user_entry = tk.Entry(app)
user_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text='Activity').grid(row=1, column=0, padx=10, pady=10)
activity_entry = tk.Entry(app)
activity_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text='Time').grid(row=2, column=0, padx=10, pady=10)
time_entry = tk.Entry(app)
time_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the buttons
tk.Button(app, text='Add Task', command=add_task).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(app, text='View Tasks', command=view_tasks).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(app, text='Clear Tasks', command=clear_tasks).grid(row=5, column=0, columnspan=2, pady=10)

# Create and place the listbox to display tasks
tasks_list = tk.Listbox(app, width=50)
tasks_list.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
app.mainloop()
