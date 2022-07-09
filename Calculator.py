import tkinter as tk
from tkinter import *
from tkinter import font
import tkinter.messagebox

LABEL_COLOR = "#25265E"
LIGHT_BLUE = "#CCEDFF"

root=Tk()
root.geometry("500x500")
class Calculator:
    def __init__(self):
        # root.resizable(0, 0)
        #
     
        root.title("Calculator")
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        root.bind("<Return>", lambda event: self.evaluate())
        
        for key in self.digits:
            root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            root.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        # self.create_square_button()
        self.create_Exit_button()
        self.create_back_space_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg='white',
                               fg=LABEL_COLOR, padx=24, font='arial')
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg='white',
                         fg=LABEL_COLOR, padx=24, font='arial')
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(root, height=350, bg=LIGHT_BLUE)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),bd=10, bg=LIGHT_BLUE, fg=LABEL_COLOR, font=('arial',16,'bold'),
                                command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bd=10,bg='cornsilk2', fg=LABEL_COLOR, font=('arial',16,'bold'),
                                command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="A C", bd=10,fg=LIGHT_BLUE,bg='red', font=('arial',16,'bold'),
                            command=self.clear)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def Exit(self):
        iexitc=tkinter.messagebox.askyesno("Exit Calculator","Confirm if you want to exit")
        if iexitc ==YES:
           Frame.destroy(self.buttons_frame)
           Label.destroy(self.display_frame)

        # root.destroy()

    def create_Exit_button(self):
        button = tk.Button(self.buttons_frame, text="Exit",bd=10, bg='red', fg=LIGHT_BLUE,font=('arial',16,'bold'),
                            command=self.Exit)
        button.grid(row=0, column=1, sticky=tk.NSEW)
    
    def create_back_space_button(self):
        button = tk.Button(self.buttons_frame, text="Clear",bd=10, bg='red', fg=LIGHT_BLUE,font=('arial',16,'bold'),
                            command=self.back_space)
        button.grid(row=0, column=2, sticky=tk.NSEW)        

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=",bd=10, bg="GREEN", fg=LABEL_COLOR, font=('arial',16,'bold'),
                            command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:100])
    
    def back_space(self):
        self.current_expression=self.current_expression[:-1]
        self.label.config(text=self.current_expression)


cal=Calculator()
root.mainloop()

