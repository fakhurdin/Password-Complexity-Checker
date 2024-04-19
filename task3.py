import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
import winsound
# ------------------------------------------------ password integrity   ------------------------------------------------ # 
# Important function to check complexity
def check_password_complexity(password):
    pass_length = len(password)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = 0
    if pass_length >= 8:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    return score

def update_score(*args):
    password = password_var.get()
    complexity_score = check_password_complexity(password)
    score_label.config(text=f"Score: {complexity_score}")

def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
        eye_icon.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        eye_icon.config(text="Show Password")

# ------------------------------------------------------------------------------------------------------------------------------#

# ------------------------------------------ Loading Animation -----------------------------------------------------------------#
def show_loading_screen():
    loading_frame = tk.Frame(root, bg='lightblue')
    loading_frame.pack(pady=10)

    progress = Progressbar(
        loading_frame, orient='horizontal', length=200, mode='determinate')
    progress.pack(padx=20, pady=10)

    def fill_progress(value):
        progress['value'] = value
        if value < 100:
            loading_frame.after(18, fill_progress, value + 1)
        else:
            loading_frame.destroy()
            show_feedback()

    fill_progress(0)
# ------------------------------------------------------------ show feedback ------------------------------------------------------# 
def show_feedback():
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    password = password_var.get()
    complexity_score = check_password_complexity(password)
    feedback = ""
    color = ""
    if complexity_score == 5:
        feedback = "Your password is strong! Keep it up!"
        color = "green"
    elif complexity_score >= 3:
        feedback = "Your password is good, but you can make it stronger by adding characters, numbers, and special characters!"
        color = "orange"
    else:
        feedback = "Your password is weak. Please consider adding more characters, numbers, and special characters."
        color = "red"
    
    feedback_label.config(text=feedback, fg=color)

# ------------------------------------------------------- GUI - DESIGN - COLOR AND BUTTONS --------------------------------------- #
root = tk.Tk()
root.title("Password Complexity Checker")
root.configure(bg='lightblue')

font_style = ("Montserrat Alternates", 14)

label = tk.Label(root, text="Enter your password:", font=font_style, bg='lightblue')
label.pack(pady=20)

password_var = tk.StringVar()
password_entry = tk.Entry(
    root, show="*", font=font_style, textvariable=password_var)
password_entry.pack(pady=5)
password_var.trace_add("write", update_score)

score_label = tk.Label(root, text="Score: 0", font=font_style, bg='lightblue')
score_label.pack(pady=10)

show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_checkbox.pack(pady=5)

eye_icon = tk.Label(root, text="Show Password", bg='lightblue')
eye_icon.pack_forget() 

style = ttk.Style()
style.configure('Custom.TButton', foreground='black', background='lightblue', font=font_style)
check_button = ttk.Button(root, text="Check Complexity", command=show_loading_screen, style='Custom.TButton')
check_button.pack(pady=10)

feedback_label = tk.Label(root, text="", font=font_style, bg='lightblue')
feedback_label.pack(pady=10)

root.mainloop()
