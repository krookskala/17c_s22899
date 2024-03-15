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

