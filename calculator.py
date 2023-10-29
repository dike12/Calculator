from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        """Set up the main window of the application"""
        master.title("Calculator")  # Set the title of the window
        master.geometry("357x420+0+0")  # Set the size and position of the window
        master.config(bg="gray")  # Set the background color of the window
        master.resizable(False, False)  # Make the window non-resizable

        # StringVar is used to get the input from the entry widget and set the result
        self.equation = StringVar()
        self.entry_value = ""  # This will hold the input and result

        # Create the display where the input and result will be shown
        display = Entry(master, width=17, bg="#ccddff", font=("Arial Bold", 28), textvariable=self.equation)
        display.grid(row=0, column=0, columnspan=4)  # Place the display at the top of the window

        # Define the buttons and their positions in a list of tuples
        buttons = [
            ('(', 1, 0), (')', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
        ]

        # Create buttons using the information from the buttons list
        for (text, row, col) in buttons:
            if text == '=':
                # '=' button has a different background and the solve function as command
                btn = Button(master, text=text, relief="flat", bg="lightblue", command=self.solve)
            elif text == 'C':
                # 'C' button has the clear function as command
                btn = Button(master, text=text, relief="flat", command=self.clear)
            else:
                # Other buttons add their text value to the equation
                btn = Button(master, text=text, relief="flat", bg="white", command=lambda value=text: self.show(value))
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        # Make the grid cells expandable for a more responsive layout
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            master.grid_rowconfigure(i, weight=1)

    def show(self, value):
        """Function to add the value of the button pressed to the equation"""
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        """Function to clear the equation"""
        self.entry_value = ""
        self.equation.set("")

    def solve(self):
        """Function to evaluate the equation"""
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            # In case of an error (like division by zero), show "Error"
            self.equation.set("Error")
            self.entry_value = ""

# Create the main window and run the application
root = Tk()
calculator = Calculator(root)
root.mainloop()
