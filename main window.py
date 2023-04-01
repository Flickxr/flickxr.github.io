import tkinter as tk
from tkinter import messagebox
import time
import random
import datetime
import openai
import os
import requests
import selenium
from tkinter import filedialog
import webbrowser 

#UPDATE LOG
# v1.0.6 adds the welcome message working, but the colour is not correctly set 1/4/23

# Define the welcome message
WELCOME_MESSAGE = "Hello! I'm Lixun, How can I assist you today?"

# Define function to handle user input
def handle_input():
    user_input = input_field.get().lower() # Convert input to lowercase
    input_field.delete(0, tk.END)  # Clear input field


    # if 'python' in input do something (try later)
    responses = {
        "hello": ["Hello there!", "Hi!", "Greetings!", "What's Up?", "Howdy!", "Bonjour!"],
        "hi": ["Hello there!", "Hi!", "Greetings!", "What's Up?", "Howdy!", "Bonjour!"],
        "hey": ["Hello there!", "Hi!", "Greetings!", "What's Up?", "Howdy!", "Bonjour!"],
        "how are you?": ["I'm doing well thank you!", "Not bad, thank you for asking!", "I'm fine, how are you?" ],
        "hows it going?": ["I'm doing well thank you!", "Not bad, thank you for asking!", "I'm fine, how are you?" ],
        "goodbye": ["Goodbye!", "See you later!", "Take care!"],
        "what is the weather?": ["Follow this link for the Bureau Of Meteorology!: http://www.bom.gov.au/places/vic/ringwood/"],
        "what time is it?": ["The current time is " + datetime.datetime.now().strftime("%I:%M %p"), "It's " + datetime.datetime.now().strftime("%I:%M %p"), "Right now it's " + datetime.datetime.now().strftime("%I:%M %p")],
        "who are you?": ["I am Linux AI Bot, created by Flickxr! I am programmed to answer any questions and provide any useful information you may require!"],
        "what is your birthday?": ["My birthday is the 26th of March, 2023."],
        "what is your favourite colour?": ["My favourite colour is Blue!"],
        "how do you make chloroform?": ["Chloroform is prepared in the laboratory by heating ethanol with bleaching powder. The reaction is called the haloalkane reaction."],
        "shit": ["-Gasp- that is a naughty word!"],
        "frick": ["-Gasp- that is a naughty word!"],
    }

# Check if input is a math equation
    try:
        result = eval(user_input)
        response = f"The answer is {result}"
    except:

        # Check if input is in responses, otherwise use default response
        if user_input in responses:
            response = random.choice(responses[user_input])
        else:
            response = "Sorry, I couldn't understand what you said!"
    input_text = f"You: {user_input}\n"
    response_text = f"Lix.ai: {response}\n\n"
    chat_history_text.configure(state="normal")
    chat_history_text.insert(tk.END, input_text)
    for char in response_text:
        chat_history_text.insert(tk.END, char, "Lix.ai")
        chat_history_text.update()
        time.sleep(0.05)
    chat_history_text.configure(state="disabled")

# Define 'Open_link' statement
def open_link():

    # Replace "https://www.google.com" with the link you want to open
    webbrowser.open("https://docs.google.com/document/d/1tB2a9IlY0qGEycBVIqVGhYXtrxsi37cAf315vRxbhcE/edit")

# Create Main Window
root = tk.Tk()
root.title("Lix.AI v1.0.6")
root.withdraw()
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 800
window_height = 600
root.configure(bg="#36393F")
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Create the button and pack it onto the window
link_button = tk.Button(root, text="Update Log", command=open_link)
link_button.pack()

def open_link():
    webbrowser.open('https://drive.google.com')
    button = tk.Button(root, text="Click me!")
    button.pack()   

# Show the window
root.deiconify()

# Animate the window by fading it in and scaling it up
for alpha in range(0, 100):
    root.attributes("-alpha", alpha / 100)
    root.update_idletasks()
    root.geometry(f"{int(window_width * alpha / 100)}x{int(window_height * alpha / 100)}+{window_x}+{window_y}")
    time.sleep(0.005)
root.attributes("-alpha", 1.0)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


# Create a label for the chat input
input_label = tk.Label(root, text="What can Lixun do for you?",
                       font=("Courier New", 18, "bold"),
                       fg="#adf0f7")
input_label.pack(pady=10)

# Create a text box for the user input
input_field = tk.Entry(root, font=("Helvetica", 16),
                        highlightthickness=3,
                        highlightcolor="#adf0f7",
                        highlightbackground="#36393F")
input_field.pack(padx=50, pady=10)

# Set the border color when the entry field is not focused
input_field.bind("<FocusIn>", lambda event: input_field.config(highlightbackground="#adf0f7"))
input_field.bind("<FocusOut>", lambda event: input_field.config(highlightbackground="#36393F"))

# Create a button to submit user input
def handle_submit():

    # Animate the button by changing its background color and text
    submit_button.config(text="Sending...", bg="#adf0f7")
    root.after(500, lambda: submit_button.config(text="Sent!", bg="#36393F"))

    # Call the actual function to handle the input
    handle_input()

submit_button = tk.Button(root, text="Send", font=("Helvetica", 12), command=handle_submit)
submit_button.pack(pady=10)

 # Create a button to clear the chat history
def handle_clear():
    
    # Animate the clear button by changing its text
    clear_button.config(text="Clearing...", state="disabled")
    root.after(500, lambda: clear_chat_history())
    root.after(1000, lambda: clear_button.config(text="Clear", state="normal"))

clear_button = tk.Button(root,
                         text="Clear",
                         command=handle_clear,
                         bg="#4CAF50",
                         fg="#000000",
                         font=("Helvetica", 12))
clear_button.pack(pady=10)

# Create a label for the chat history
chat_history_label = tk.Label(root,
                              text="Your Amazing Conversation With Lixun Bot",
                              font=("Courier New", 18, "bold"),
                              bg="#36393F",
                              fg="#adf0f7")
chat_history_label.pack()


# Create a text box for the chat history
chat_history_text = tk.Text(root,
                            height=20,
                            bg="#36393F",
                            fg="#DCDDDE",
                            font=("Courier New", 18, "bold"),
                            state="disabled",
                            yscrollcommand=set,
                            highlightthickness=3,
                            highlightcolor="#adf0f7",
                            highlightbackground="#36393F")
chat_history_text.tag_config("Lix.ai", foreground="#adf0f7")  # Set bot response color
chat_history_text.pack(pady=10)

# Add welcome message to chat history
chat_history_text.configure(state="normal")
chat_history_text.tag_config("Lix.ai", foreground="#adf0f7", background="#36393F")
welcome_message = "Lix.ai: " + WELCOME_MESSAGE + "\n\n"
for char in welcome_message:
    chat_history_text.insert(tk.END, char)
    chat_history_text.update()
    time.sleep(0.05)
chat_history_text.configure(state="disabled")

# Set the border color when the text box is not focused
chat_history_text.bind("<FocusIn>", lambda event: chat_history_text.config(highlightbackground="#adf0f7"))
chat_history_text.bind("<FocusOut>", lambda event: chat_history_text.config(highlightbackground="#36393F"))


root.bind('<Return>', lambda event=None: submit_button.invoke())

# Create a function to clear the chat history
def clear_chat_history():
    chat_history_text.configure(state="normal")
    chat_history_text.delete("1.0", "end")
    chat_history_text.configure(state="disabled")

    # Add an animation to clear the chat history
    for i in range(10):
        chat_history_text.configure(bg="#36393F" if i % 2 == 0 else "#36393F")
        chat_history_text.update()
        chat_history_text.after(50)

root.mainloop()
