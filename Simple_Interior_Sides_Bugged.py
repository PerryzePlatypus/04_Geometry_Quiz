def interior_angle_sum(n):
    return (n - 2) * 180

user_answer = int(input("How many sides?:"))
num_sides = user_answer


print("Number of sides:", num_sides)
print("Sum of interior angles: ", interior_angle_sum(num_sides))