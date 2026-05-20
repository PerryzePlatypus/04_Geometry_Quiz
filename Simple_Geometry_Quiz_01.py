import random


# formula to calculate the total sum of interior angles in a shape ( where n is how many sides it has )
def interior_angle_sum(n):
    return (n - 2) * 180


# a list of shapes with the number of sides
shape_list = {
    "Triangle" : 3,
    "Quadrilateral": 4,
    "Polygon": 5,
    "Hexagon": 6,
    "Heptagon": 7,
    "Octagon": 8,
    "Nonagon": 9,
    "Decagon": 10,
}


# grabs the shape name and how many sides it has from the list
shape_name = random.choice(list(shape_list.keys()))
sides = shape_list[shape_name]
angle_sum = interior_angle_sum(sides)
remaining_sum = angle_sum


#Generates a list of angles except for one which the user has to find
while True:
    angles = [] # puts the angles in a list
    remaining_sum = angle_sum

    for i in range(sides - 1 ):
            angle = random.randint(80,140)
            angles.append(angle)
            remaining_sum -= angle

    missing_angle = remaining_sum

    if 40<= remaining_sum <=180:
        break


print(f"A {shape_name} has {sides} sides. The sum of all interior angles is {angle_sum}.\n"
      f"Using the angles below find out what the missing angle is:  ")

print(angles)

# ask the user what the answer is
user_answer = int(input("What is the answer?: "))

# if the user finds the missing angle and is correct, it will congratulate them, if not it will say their wrong and provide them the correct answer
if user_answer == missing_angle:
    print(f"Good Job, The missing angle was {missing_angle}°")
else:
    print(f"WRONG. The answer was {missing_angle}°")












