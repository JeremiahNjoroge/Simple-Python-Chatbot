#import modules
import json
import random
import re
import random_responses
import requests
import tkinter as tk
from datetime import date,datetime


# Load JSON data
def load_json(file):
    with open(file,encoding="utf-8") as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)



# Store JSON data
response_data = load_json("bot.json")

#Function to get user input and return response
def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []
    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]
        
        # Check if there are required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("
    #check if input is date
    if input_string == "date":
        current_date = date.today().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}"
    #check if input is time
    if input_string == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The time is {current_time}"
    #check if user input is country return city
    
    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]
    else:
        return random_responses.random_string()

#Generate a gui using Tkinter
def send_message(event=None):
    user_input = entry.get()
    if user_input:
        response = get_response(user_input)
        chat_text.insert(tk.END, "You: " + user_input + "\n")
        chat_text.insert(tk.END, "Bot: " + response + "\n\n")
        entry.delete(0, tk.END)

def quit_session(event=None):
    root.destroy()

# Create GUI window
root = tk.Tk()
root.title("Chatbot GUI")
#set background color
root.configure(bg="light green")

# Create chat display area
chat_text = tk.Text(root, height=20, width=100)
chat_text.pack()

# Create user input entry field
entry = tk.Entry(root, width=40)
entry.pack()

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()
# Bind Enter key to send_message function
entry.bind("<Return>", send_message)

# Create quit button
quit_button = tk.Button(root, text="Quit", command=quit_session)
quit_button.pack()
#Bind esc key to quit function
entry.bind("<Escape>",quit_session)

root.mainloop()


