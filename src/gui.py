"""
This module contains the GUI for the application.

Author: ItachiDL
Date: 10. Juli 2024
Version: 0.1
"""

import tkinter as tk
from tkinter import ttk
from budget_system import BudgetSystem
from tkinter import messagebox

class BudgetAppWindow:
    """
    A class to represent the budget application GUI.
    1. Insert your budget with category, amount and description.
    2. Show all budget entries.
    3. Make changes to the budget entries.
    """

    def __init__(self, title="Advanced Window", width=600, height=400):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

        self.create_widgets()

    def create_widgets(self):
        self.create_input_frame()
        self.create_output_frame()

    def create_input_frame(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_dropdown(self.input_frame)
        self.create_number_input(self.input_frame)
        self.create_description_input(self.input_frame)
        self.create_submit_button(self.input_frame)

    def create_output_frame(self):
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.output_text = tk.Text(self.output_frame, state='disabled', wrap='word')
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.output_frame, command=self.output_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.output_text['yscrollcommand'] = self.scrollbar.set

    def create_dropdown(self, frame):
        self.label_dropdown = tk.Label(frame, text="Wählen Sie eine Option:")
        self.label_dropdown.pack(pady=5)

        self.options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])

        self.dropdown = tk.OptionMenu(frame, self.selected_option, *self.options)
        self.dropdown.pack(pady=5)

    def create_number_input(self, frame):
        self.label_number = tk.Label(frame, text="Geben Sie eine Zahl ein:")
        self.label_number.pack(pady=5)

        self.entry_number = tk.Entry(frame)
        self.entry_number.pack(pady=5)

    def create_description_input(self, frame):
        self.label_description = tk.Label(frame, text="Geben Sie eine Beschreibung ein:")
        self.label_description.pack(pady=5)

        self.text_description = tk.Text(frame, height=4, width=30)
        self.text_description.pack(pady=5)

    def create_submit_button(self, frame):
        self.submit_button = tk.Button(frame, text="Absenden", command=self.process_input)
        self.submit_button.pack(pady=10)

    def process_input(self):
        selected_option = self.selected_option.get()
        try:
            number = float(self.entry_number.get())
        except ValueError:
            messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie eine gültige Zahl ein.")
            return

        description = self.text_description.get("1.0", tk.END).strip()

        output_message = (f"Ausgewählte Option: {selected_option}\n"
                          f"Eingegebene Zahl: {number}\n"
                          f"Beschreibung: {description}\n")

        self.display_output(output_message)

    def display_output(self, message):
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.config(state='disabled')
        self.output_text.yview(tk.END)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    window= BudgetAppWindow()
    window.run()