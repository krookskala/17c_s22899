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

#Task8
class CubicGenerator(SquareGenerator):
    def generate_list_of_squares(self, start, end):
        if end < start:
            raise ValueError("End Of The Range Must Be Greater Than Or Equal To The Start.")
        cubes = [num ** 3 for num in range(start, end + 1)]
        return cubes

cubic_gen = CubicGenerator()
start = 1
end = 5
try:
    cubes = cubic_gen.generate_list_of_squares(start, end)
    print("List Of Cubes From {} To {}: {}".format(start, end, cubes))
except ValueError as e:
    print("Error: ", e)

#Task9
class CubicGenerator(SquareGenerator):
    def generate_list_of_squares(self, start, end):
        if start < end:
            raise ValueError("Start Of The Range Must Be Greater Than Or Equal To The End.")
        cubes = [num ** 3 for num in range(start, end + 1)]
        return cubes

cubic_gen = CubicGenerator()
start = 1
end = 5
try:
    cubes = cubic_gen.generate_list_of_squares(start, end)
    print("List Of Cubes From {} To {}: {}".format(start, end, cubes))
except ValueError as e:
    print("Error: ", e)