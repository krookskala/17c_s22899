#Task1
squares = [num ** 2 for num in range(1, 11)]
print("List Of Squares From 1 To 10:", squares)

#Task2
def generates_list_of_squares(start, end):
    squares = [num ** 2 for num in range(start, end + 1)]
    return squares
start = 1
end = 10
squares = generates_list_of_squares(start, end)
print("List Of Squares From {} To {}: {}".format(start, end, squares))

#Task3
class SquareGenerator:
    def generate_list_of_squares(self, start, end):
        squares = [num ** 2 for num in range(start, end + 1)]
        return squares
if __name__ == "__main__":
    square_gen = SquareGenerator()
    start = 1
    end = 10
    squares = square_gen.generate_list_of_squares(start, end)
    print("List Of Squares From {} To {}: {}".format(start, end, squares))

#Task4
class SquareGenerator:
    def generate_list_of_squares(self, start, end):
        squares = [num ** 2 for num in range(start, end + 1)]
        square_roots = [math.sqrt(num) for num in squares]
        return square_roots
    print("List Of Squares From {} To {}: {}".format(start, end, squares))

#Task5
import math
def generates_list_of_squares(start, end):
    if end < start:
        raise ValueError("End Of The Range Must Be Greater Than Or Equal To The Start.")
    squares = [num ** 2 for num in range(start, end + 1)]
    square_roots = [math.sqrt(num) for num in squares]
    return squares
start = 10
end = 5
try:
    squares = generates_list_of_squares(start, end)
    print("List of squares from {} to {}: {}".format(start, end, squares))
except ValueError as e:
    print("Error:", e)

#Task6 & 7
from square_generator.square_generator import SquareGenerator

#Task8 & 9 & 10 in the square_generator.py

