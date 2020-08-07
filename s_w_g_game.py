import random
list1=['s','w','g','w','g','s']
play_time=10
no_of_chance=0
computer_point=0
your_point=0

print("play snake water gun game please")
print(" gun for g\n water for w\n snake for s\n")

while no_of_chance < play_time:
    _input=input("g,w,s:\n")
    _random=random.choice(list1)

    if _input==_random:
        print("tie both get 0 point for this chance\n")
        print(f"you guess {_input} and computer guess {_random} \n")
        print(f"computer point is:{computer_point}  \n your point is:{your_point}")
    #if user enter the s
    elif _input=="s" and _random=="g":
        computer_point=computer_point+1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("computer win one point")
        print(f"computer point is:{computer_point}  \n your point is:{your_point}")

    elif _input=="s" and _random=="w":
        your_point=your_point+1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("you win one point")
        print(f"computer point is:{computer_point}  \n your point is:{your_point}")

    #if user enter the w

    elif _input=="w" and _random=="g":
        your_point = your_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("you win one point")
        print(f"computer point is:{computer_point}  \n your point is:{your_point}")

    elif _input=="w" and _random=="s":
        computer_point = computer_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("computer win one point")
        print(f"computer point is:{computer_point}  \n your point is:{your_point}")

    #if user enter g

    elif _input=="g" and _random=="s":
        your_point = your_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("you win one point")
        print(f"computer point is:{computer_point} \n your point is:{your_point}")

    elif _input=="g" and _random=="w":
        computer_point = computer_point + 1
        print(f"you guess {_input} and computer guess {_random} \n")
        print("computer win one point")
        print(f"computer point is:{computer_point}  \n your point is:{your_point}")

    else:
        print("you play wrong please fllow right instruction")

    no_of_chance=no_of_chance+1
    print(f"{play_time-no_of_chance} is left out of {play_time}")


if computer_point>your_point:
    print(f"you loss the game and your point is {your_point} and computer point is {computer_point}")
elif computer_point<your_point:
    print(f"you win this game")
    print(f"your point is:{your_point} ")
    print(f"computer point is:{computer_point}")

else:
    print(f"game tie your point is:{your_point} and computer point is:{computer_point}")

print("game over")


