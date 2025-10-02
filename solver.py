'''
This is intended to be where the solving happens
'''
import time

algorithms = ["Random", "DFS"]

def validate(puzzle):
    '''
    a puzzle is considered invalid if 
        there is the same number in the same row, column or block
        there is a number greater than the size of the puzzle
        there is a number less than 1
    '''
    blocks = []
    for row in range(len(puzzle)):
        for col in range(len(puzzle)):
            print(puzzle[row][col])


def solve_puzzle(puzzle):
    return puzzle

def solve(puzzle, algorithm):
    validate(puzzle)
    start = time.time()
    solution = solve_puzzle(puzzle)
    end = time.time()

    return (solution, f'Puzzle solved in {end-start:.6f} secounds by {algorithm}')
    
