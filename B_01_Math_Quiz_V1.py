import random


def string_checker(question, valid_ans=('yes', 'no')):
    error = f"\n\033[95m  [!] Please enter a valid option from the following list: {valid_ans}\033[0m\n"

    while True:
        user_response = input(question).lower()

        for item in valid_ans:
            # Checks if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        print(error)
        print()


def instructions():
    """Prints instructions"""

    print("""
    *** GEOMETRY QUIZ ***

    """
          )


# checks for an integer more than 0 ( allows <enter>)

def int_check(question):
    # checks if users integer is equal or more than 13

    while True:
        error = "Please enter an integer that is 1 or more | press <enter> to play infinite mode"

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# equation to find total interior angles of a polygon
def interior_angle_sum(n):
    return (n - 2) * 180

# generates angle type questions
def angle_type_ques():
    angle_rules = random.randint(1, 359)  # generates an angle between 1 and 359

    if angle_rules < 90:  # if the angle is below 90° then it's an acute angle
        angle_type = "acute"
    elif angle_rules == 90:  # if the angle is equal to 90° then it's a right angle
        angle_type = "right"
    elif 90 < angle_rules < 180:  # if the angle is not below 90° and below 180° then it's an obtuse angle
        angle_type = "obtuse"
    elif angle_rules == 180:  # if the angle is equal to 180° then it's a straight angle
        angle_type = "straight angle"
    elif angle_rules > 180:  # if the angle is above 180° then it's a reflex angle
        angle_type = "reflex"

    print(f"An angle measures {angle_rules}°. What type of angle is it?")  # prints out the question

    user_answer = input("What type of angle is it?  ").lower()

    if user_answer == angle_type:
        print("Your CORRECT!")
    else:
        print(f"WRONG! it's a {angle_type}")


# formula for sum of interior angles

def missing_angle_gen():
    shape_list = {
        "Triangle": 3,
        "Quadrilateral": 4,
        "Pentagon": 5,
        "Hexagon": 6,
        "Heptagon": 7,
        "Octagon": 8,
        "Nonagon": 9,
        "Decagon": 10,
    }


    shape_name, sides = random.choice(list(shape_list.items())) # chooses a random shape with the number of sides it has

    total_sum = interior_angle_sum(sides) # Uses the formula to find out the total sum of interior angles ( eg - 3-2 * 180 = 180 )

    while True:

        angles = [] #Puts the angles in a list except for one
        current_sum = 0

        for i in range(sides - 1):

            max_possible = total_sum - current_sum - 40

            angle = random.randint(40, min(160, max_possible))

            angles.append(angle)
            current_sum += angle

        missing_angle = total_sum - current_sum #generates the missing angle for the user to solve

        if 40 <= missing_angle < 180: # A safety measure so that the missing angle won't have an unrealistic number
            break

    print(missing_angle)
    print(f"\nA {shape_name} has {sides} sides.")
    print(f"Interior angle sum = {total_sum}°")

    print("\nFind the missing angle:")
    print(angles)

    user_answer = int(input("\nAnswer: "))

    if user_answer == missing_angle:
        print(f"Correct! The missing angle was {missing_angle}°")
    else:
        print(f"Wrong. The answer was {missing_angle}°")



# MAIN ROUTINE
# initialize game variable
mode = "regular"
num_questions_asked = 0
questions_right = 0
questions_wrong = 0

question_history = []

print("📏📐 GEOMETRY QUIZ 📐📏")
print()

# ask users if they want to see the instruction and display them
# if requested

want_instructions = string_checker("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite

num_questions = int_check(" How many questions would you like? Push <enter> for infinite mode:  ")

if num_questions == "infinite":
    mode = "infinite"
    num_questions = 9999999999999999999999

while num_questions_asked < num_questions:

    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ ROUND {num_questions_asked + 1} ( Infinite Mode )♾️♾️♾️"
    else:
        rounds_heading = f"\n🕹️🕹️🕹️ Round {num_questions_asked + 1} of {num_questions} 🕹️🕹️🕹️"

    print(rounds_heading)
    print()

    question_random = [angle_type_ques,missing_angle_gen]
    
    #randomly selects a question type
    random.choice(question_random)()

    num_questions_asked += 1

    print()
    print("Thanks for playing!!!🦦")

