import random

angle_type = ["obtuse", "reflex", "acute","right", "straight angle"]

angle_rules = random.randint(1,359)

if angle_rules < 90:
    angle_type = "acute"
elif angle_rules == 90:
    angle_type = "right"
elif 90 < angle_rules <180:
    angle_type = "obtuse"
elif angle_rules == 180:
    angle_type = "straight angle"
elif angle_rules >180:
    angle_type = "reflex"

print(angle_type)
print(angle_rules)