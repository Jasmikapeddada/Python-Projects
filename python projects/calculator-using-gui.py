import tkinter as tk

class Calculator:
    def __init__(self):
        self.current_expression = ""
        self.board = [["7","8","9","/"],["4","5","6","X"],["1","2","3","-"],["AC","0","=","+"]]
        self.window = tk.Tk()
        self.window.title("CALCULATOR")

        self.buttonGrid = []
        
        self.display = tk.Text(self.window, width = 25, height = 2, font = ("Arial", 18))
        self.display.grid(row = 0, column = 0, columnspan = 4)

        for i, row_values in enumerate(self.board):
            row = []
            for j, value in enumerate(row_values):
                button = tk.Button(self.window, text = value, width = 8, height = 3, font = ("Arial", 16), command = lambda value = value: self.click_button(value))
                button.grid(row = i+1, column = j)
                row.append(button)
            self.buttonGrid.append(row)

    def click_button(self, value):
        if value == "AC":
            self.current_expression = ""
            self.update_display()
        elif value == "=":
            try:
                expression = self.current_expression.replace("X", "*")
                result = eval(expression)
                self.current_expression = str(result)
                self.update_display()
            except Exception as e:
                self.current_expression = "Error"
                self.update_display()
        else:
            self.current_expression += value
            self.update_display()
    
    def update_display(self):
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, self.current_expression)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Calculator()
    game.run()