import random
from turtle import *
# Random Password Generator
rand_numlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
rand_letterlist = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
rand_charlist = ['!',"@","#","$","%","^","&","*"]
random_password = ""
for x in range(4):
    lucky_numbers = random.choice(rand_numlist)
    random_password += str(lucky_numbers)
for letter in range(2): 
    lucky_letter = random.choice(rand_letterlist)
    random_password += lucky_letter
for char in range(2):
    lucky_char = random.choice(rand_charlist)
    random_password += lucky_char
print(random_password)


# grade test homework
member_list = ["Anri", "Dato", "Saba", "Salo", "Giorgi", "Rati"]
for name in range(len(member_list)):
    rand_member = random.choice(member_list)
    question = input("{} answered correctly? ".format(rand_member))
    if question == "Yes":
        print(rand_member + " +10 points, Great job")
    elif question == "No":
        print(rand_member + " -5 points, Try harder next time")
    member_list.remove(rand_member)

# Piece of Art
rand_forward = random.randint(50,150)
rand_left = random.randint(90,180)
rand_right = random.randint(90,180)
color_list = ["red","green","blue","orange","purple","pink"]
rand_color = random.choice(color_list)
rand_place = random.randint(30,40)
for i in range(50):
    speed(7)
    color(rand_color)
    forward(120)
    left(rand_left)
    forward(rand_forward)
    left(rand_left)
    forward(rand_forward)
    left(rand_left)
    forward(rand_forward)
    right(rand_right)
    forward(rand_forward)
    left(rand_left)
    forward(30)
exitonclick()




