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


import random

choose = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n")

if choose == '0':
  print(rock)
if choose == '1':
  print(paper)
if choose == '2':
  print(scissors)

list = [rock, paper, scissors]
random_1 = random.randint(0, 2)
choose_pc = list[random_1]

print(f"Computer choose:\n{choose_pc}")

if choose == '0' and random_1 == 1 or choose == '1' and random_1 == 2 or choose == '2' and random_1 == 0:
    print("You lose")
elif choose == '1' and random_1 == 0 or choose == '2' and random_1 == 1 or choose == '0' and random_1 == 2:
    print("You win")
else:
    print("Egality")