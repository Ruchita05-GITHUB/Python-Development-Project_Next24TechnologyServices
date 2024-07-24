import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    
    # Here you can add validation or processing of the input data
    if name and email and age:
        messagebox.showinfo("Submission Successful", f"Name: {name}\nEmail: {email}\nAge: {age}")
    else:
        messagebox.showerror("Input Error", "All fields are required!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=10)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
