def interior_angle_sum(n):
    return (n - 2) * 180

def int_check():
    error = "Please enter an integer more than 2"
    while True:
        try:
            user_answer = int(input("How many sides: "))

            if user_answer < 3:
                print(error)
            else:
                return user_answer

        except ValueError:
            print(error)

num_sides = int_check()

print("Number of sides:", num_sides)
print("Sum of interior angles: ", interior_angle_sum(num_sides))
