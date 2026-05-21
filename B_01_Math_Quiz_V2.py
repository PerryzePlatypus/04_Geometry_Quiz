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
    *** 🔴🟧📐 GEOMETRY QUIZ 📐🟧🔴 ***
    
    1) To begin, select the amount of questions you want or infinite mode
    2) You will be given a random question that is either:
       - Angle Rules
         - Acute Angle    || An angle that that is inbetween 1° - 89°
         - Right Angle    || An angle that is exactly 90°
         - Obtuse Angle   || An angle that is inbetween 91° - 179°
         - Straight Angle || An angle that is exactly 180°
         - Reflex Angle   || An angle that is inbetween 181° - 359°
         
    You will be given a random angle inbetween 1° - 359° and you have to
    answer what type of angle it is.
    
    eg - "An angle measures 54°. What type of angle is it?"
    
          The correct answer would be Acute 
    
        - Interior Angles
          - Triangle      || Interior Sum - 180°
          - Quadrilateral || Interior Sum - 360°
          - Pentagon      || Interior Sum - 540°
          - Hexagon       || Interior Sum - 720°
          - Heptagon      || Interior Sum - 900°
          - Octagon       || Interior Sum - 1080°
          - Nonagon       || Interior Sum - 1260°
          - Decagon       || Interior Sum - 1440°
    
    You will be given a set of angles except for one and you will have to find out 
    what the missing angle is.
    
    eg - "A Triangle has 3 sides."
         "Interior angle sum = 180°"
         "Here are the angles!"
         [ 50, 60 ]
         
         "Find the missing angle:"
         
         The correct answer would be 70°
        

         Good Luck and Have Fun!!!!   
    """
          )


# checks for an integer more than 0 ( allows <enter> )

def int_check(question):
    # checks if users integer is equal or more than 1

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
        return True, f"An Angle measures {angle_rules}° What type of angle is it? || Your Answer: ({angle_type}) Correct✅✅✅)"
    else:
        print(f"WRONG! it's a {angle_type}")
        return False, f"An Angle measures {angle_rules}° What type of angle is it? || Your Answer: ({angle_type}) Wrong❌❌❌)"


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

    print(f"\nA {shape_name} has {sides} sides.")
    print(f"Interior angle sum = {total_sum}°")
    print("Here are the angles!"
          f"\n\033[95m{angles}\033[0m\n")
    print(f"PSSTT Here's the answer!!!:  {missing_angle} ") #Delete after testing!!!!

    print("\nFind the missing angle:")

    user_answer = int(input("\nAnswer: "))

    if user_answer == missing_angle:
        print(f"Correct! The missing angle was {missing_angle}°")
        return True, f"A {shape_name} has these angles {angles} What is the missing angle? || Your Answer: ({missing_angle}°) Correct✅✅✅"
    else:
        print(f"Wrong. The answer was {missing_angle}°")
        return False, f"A {shape_name} has these angles {angles} What is the missing angle? || Your Answer: ({missing_angle}°) Wrong❌❌❌)"



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
    num_questions = 5

while num_questions_asked < num_questions:

    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Question {num_questions_asked + 1} ( Infinite Mode )♾️♾️♾️"
    else:
        rounds_heading = f"\n🕹️🕹️🕹️ Question {num_questions_asked + 1} of {num_questions} 🕹️🕹️🕹️"

    print(rounds_heading)
    print()

    question_random = [angle_type_ques,missing_angle_gen]
    
    #randomly selects a question type
    correct, history_quiz_question = random.choice(question_random)()

    if correct:
        questions_right += 1
    else:
        questions_wrong += 1

    num_questions_asked += 1

    question_history.append(f"Question NO. {num_questions_asked+1-1} || {history_quiz_question} ")

    if mode == "infinite":
        num_questions += 1


    #main routine ends here

# prints out the users quiz statistics
print("\n📊📊📊QUIZ STATISTICS📊📊📊")
print(f"Total number of questions asked💬💬💬: {num_questions_asked}")
print(f"Total number of questions correct✅✅✅: {questions_right}")
print(f"Total number of questions wrong❌❌❌: {questions_wrong}")

# if the user has answered more than 0 questions it prints out their accuracy
if num_questions_asked > 0:
    accuracy = (questions_right / num_questions_asked) * 100
    print(f"🎯🎯Accuracy: {accuracy:.2f}%")

    #ask the user if they want to see their quiz question history
    see_history = string_checker("\nDo you want to see your game history?")
    if see_history == "yes":
        for item in question_history:
            print(item)

    print()
    print("🙌🙌🙌 Thanks for using Geometry Quiz 🙌🙌🙌")

