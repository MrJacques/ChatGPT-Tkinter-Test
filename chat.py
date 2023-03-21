
from tkinter import *
import customtkinter
import openai
import os
import pickle

pickle_file_name = "api_key.pickle"

# initiate app
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x500')
root.iconbitmap('ai_lt.ico')
root.config(highlightthickness=5, highlightbackground="red")

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# Set color scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def get_api_key():
    try:
        if os.path.isfile(pickle_file_name):
            input_file = open(pickle_file_name, 'rb')
            file_contents = pickle.load(input_file)
            input_file.close()

            return file_contents
    except Exception as e:
        my_text.insert(
            END, f"\n\nThere was an error loading the pickle\n\n{e}")
    return None


api_key_value = get_api_key()


def speak():
    if (not chat_entry.get()):
        my_text.insert(END, "Hey you need to type something.\n")

    elif (not api_key_value):
        my_text.insert(END, "You need to add an API key.\n")
    else:
        my_text.insert(END,f"\n\n==> {chat_entry.get()}")
        chat_entry.delete(0, END)
        chat_entry.insert(0, "Working...")

        openai.api_key = api_key_value
        openai.Model.list()
        response = openai.Completion.create(
           model="text-davinci-003",
		   prompt = chat_entry.get(),
		   temperature=0,
		   max_tokens=3500,
		   top_p=1.0,
		   frequency_penalty=0.0,
		   presence_penalty=0.0
		)			
		
        display_text = response["choices"][0]["text"]
        my_text.insert(END,f"{display_text}\n")
        my_text.see(END)
        chat_entry.delete(0, END)


def clear():
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)


def key():
    api_entry.delete(0, END)
    api_entry.insert(0, api_key_value)

    root.geometry('600x630')
    api_frame.pack(pady=30)
    api_button.configure(state=DISABLED)


def save_key():
    try:
        api_key_value = api_entry.get()
        output_file = open(pickle_file_name, 'wb')
        pickle.dump(api_key_value, output_file)
        output_file.close()
    except Exception as e:
        my_text.insert(END, f"\n\nThere was an error saving the pickle\n\n{e}")

    api_frame.pack_forget()
    root.geometry('600x500')
    api_button.configure(state=NORMAL)


# Create text frame
text_frame = customtkinter.CTkFrame(root, border_color="red", border_width=5)
text_frame.pack(pady=20, padx=20, fill="both")
text_frame.grid_columnconfigure(0, weight=1)
text_frame.grid_rowconfigure(0, weight=1)

# Add test widget to get ChatGPT responses
my_text = Text(text_frame,
               bg="#343638",
               width=65,
               bd=1,
               fg="#d6d6d6")
my_text.grid(row=0, column=0, sticky=NSEW)

# Create Scroll bar
text_scroll = customtkinter.CTkScrollbar(text_frame,
                                         command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky=NS)

my_text.configure(yscrollcommand=text_scroll.set)

# Entry widget to type stuff
chat_entry = customtkinter.CTkEntry(root,
                                    placeholder_text="Type Something to ChatGPT...",
                                    # width=535,
                                    height=50,
                                    border_width=1)
chat_entry.pack(pady=10, padx=20, fill=X)

# vCreate Buttons
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

submit_button = customtkinter.CTkButton(button_frame,
                                        text="Submit to ChatGPT",
                                        command=speak)
submit_button.grid(row=0, column=0, padx=25)

clear_button = customtkinter.CTkButton(button_frame,
                                       text="Clear Response",
                                       command=clear)
clear_button.grid(row=0, column=1, padx=35)

api_button = customtkinter.CTkButton(button_frame,
                                     text="Update API Key",
                                     command=key)
api_button.grid(row=0, column=2, padx=25)

api_frame = customtkinter.CTkFrame(root, border_width=2)
api_frame.pack(pady=30)

api_entry = customtkinter.CTkEntry(api_frame,
                                   placeholder_text="API Key",
                                   width=350,
                                   height=50,
                                   border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

api_save_button = customtkinter.CTkButton(api_frame,
                                          text="Save Key",
                                          command=save_key)
api_save_button.grid(row=0, column=1, padx=10)

root.mainloop()
