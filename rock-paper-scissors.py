import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


ask = input("Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

box = [rock, paper, scissors]

cp = len(box) - 1

computer = random.randint(0, cp)

kill = box[computer]

user = box[int(ask)]
print("\n\nYou Chose: ")
print(user)
print("\n\nComputer Chose: ")
print(kill)

if user == kill:
    print("It's a draw")
elif user == scissors and kill == paper:
    print("You Win")
elif user == paper and kill == scissors:
    print("You Lose")
elif user == rock and kill == paper:
    print("You Lose")
elif user == paper and kill == rock:
    print("You Lose")
elif user == rock and kill == scissors:
    print("You Win")
elif user == scissors and kill == rock:
    print("You Lose")
 

