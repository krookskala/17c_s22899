import math

import math

class SquareGenerator:
    def generate_list_of_squares(self, start, end):
        if end < start:
            raise ValueError("End Of The Range Must Be Greater Than Or Equal To The Start.")
        squares = [num ** 2 for num in range(start, end + 1)]
        return squares

square_gen = SquareGenerator()

start = 1
end = 10
try:
    squares = square_gen.generate_list_of_squares(start, end)
    print("List Of Squares From {} To {}: {}".format(start, end, squares))
except ValueError as e:
    print("Error:", e)
