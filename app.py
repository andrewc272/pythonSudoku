from tkinter import *
import tkinter.font as font
from math import *
import solver

size = 4
block_size = int(sqrt(size))

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.setup_ui()

    def setup_ui(self):
        # Make 3 frames
        self.puzzleFrame = Frame(self)
        self.controlFrame = Frame(self)
        self.solutionFrame = Frame(self)

        # fill puzzleFrame
        entry_font = font.Font(family="Helvetica", size=24)
        self.cellEntries = []
        for row in range(0, size):
            rowEntries = []
            self.puzzleFrame.grid_rowconfigure(row, minsize=50)
            for column in range(0, size):
                box = (row//block_size)*block_size + column//block_size
                
                if block_size%2 == 1 or (block_size%2 == 0 and (row//block_size)%2 == 0):
                    if box%2 == 1:
                        entry = Entry(self.puzzleFrame, bg="lightgrey", width=2, justify="center", font=entry_font)
                    else:
                        entry = Entry(self.puzzleFrame, bg="white", width=2, justify="center", font=entry_font)
                elif block_size%2 == 0 and (row//block_size)%2 == 1:
                    if box%2 == 0:
                        entry = Entry(self.puzzleFrame, bg="lightgrey", width=2, justify="center", font=entry_font)
                    else:
                        entry = Entry(self.puzzleFrame, bg="white", width=2, justify="center", font=entry_font)


                entry.grid(row=row, column=column, ipadx = 10, ipady = 10)
                rowEntries.append(entry)
            self.cellEntries.append(rowEntries)

        # fill controlFrame
        # Algorithm Selector
        self.values = ["red", "green", "blue"]
        self.var = StringVar(value=self.values[0])
        self.optionMenu = OptionMenu(self.controlFrame, self.var, *self.values)
        
        # Solve and Clear Buttons
        self.solve = Button(self.controlFrame, text="Solve", bg="green", activebackground="lightgreen", command=self.solve)
        self.clear = Button(self.controlFrame, text="Clear", bg="red", activebackground="pink")

        buttonX = 100
        buttonY = 10
        self.optionMenu.pack(side=LEFT, ipadx=buttonX, ipady=buttonY)
        self.solve.pack(side=LEFT, ipadx=buttonX, ipady=buttonY)
        self.clear.pack(side=LEFT, ipadx=buttonX, ipady=buttonY)
        
        # Solution Frame
        self.solutionResult = Label(self.solutionFrame, text="Hit Solve!!")
        self.solutionResult.pack()

        # Pack it!!
        self.puzzleFrame.pack()
        self.controlFrame.pack()
        self.solutionFrame.pack()

    def solve(self):
        '''
        This will take all the entries make it into a puzzle and send it to the solver that will get the solution and print it to the user
        '''
        puzzle = []
        for row in range(size):
            puzzle_row = []
            for column in range(size):
                puzzle_row.append(self.cellEntries[row][column].get())
            puzzle.append(puzzle_row)
        print(puzzle)
        self.solutionResult.config(text="Puzzle Solved")


if __name__ == '__main__':
    app = App()
    app.mainloop()
