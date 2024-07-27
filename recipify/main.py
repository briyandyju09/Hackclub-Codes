import openai
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk



openai.api_key = ''


class RecipeChatbotGUI:

    def __init__(self, master):
        self.master = master
        master.title("Recipify It!")
        self.style = ttk.Style()
        master.set_theme("arc")
        self.title_label = ttk.Label(master,
                                     text="Recipify Anything and Everything!",
                                     font=('Helvetica', 16, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.ingredients_label = ttk.Label(master,
                                           text="Input Ingriedients You Have:",
                                           font=('Helvetica', 14))
        self.ingredients_label.grid(row=1,
                                    column=0,
                                    padx=10,
                                    pady=10,
                                    sticky="e")
        self.ingredients_entry = ttk.Entry(master, width=50)
        self.ingredients_entry.grid(row=1, column=1, padx=10, pady=10)
        self.dish_type_label = ttk.Label(master,
                                         text="Course Type:",
                                         font=('Helvetica', 14))
        self.dish_type_label.grid(row=2,
                                  column=0,
                                  padx=10,
                                  pady=10,
                                  sticky="e")
        self.dish_type_var = tk.StringVar()
        self.dish_type_var.set("Basic Convo")
        self.dish_type_buttons = [
            ttk.Radiobutton(master,
                            text="Main Course",
                            variable=self.dish_type_var,
                            value="Main Course"),
            ttk.Radiobutton(master,
                            text="Snack",
                            variable=self.dish_type_var,
                            value="Snack"),
            ttk.Radiobutton(master,
                            text="Drinks",
                            variable=self.dish_type_var,
                            value="Drinks"),
        ]
        for i, button in enumerate(self.dish_type_buttons):
            button.grid(row=2 + i, column=1, padx=5, pady=5, sticky="w")
        self.submit_button = ttk.Button(master,
                                        text="Get Recipe",
                                        command=self.get_recipe)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=20)
        self.output_label = ttk.Label(master, text="", font=('Helvetica', 12))
        self.output_label.grid(row=6, column=0, columnspan=2, pady=10)
