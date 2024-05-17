class car:
    def __init__(self, model, health):
        self.model = model
        self.health = health

    def is_alive(self):
        return self.health > 0

lamborghini = car('lamborghini', 50)
trackhawk = car('trackhawk', 100)

import os 
os.system('cls' if os.name == 'nt' else 'clear')

def error_statement():
    print('\nthat is not valid otpion, try again:')

def choose_your_car():
    print()
    your_car = True
    while your_car == True:
        choosing_car = input('choose your car: ')
        if choosing_car == '1':
            your_car = lamborghini
        elif choosing_car == '2':
            your_car = trackhawk
        else:
            error_statement()
        os.system('cls|clear')
        print(your_car)
        return your_car

choose_your_car()

def play_game():
   
    while lamborghini.health > 0 and trackhawk.health > 0:
        print(f"the lamborghnini has {lamborghini.health} health ")
        print(f"The trackhawk has {trackhawk.health} health ")
        print()
        print("On your mark, Get set...GO")
        print("1. GO")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # the start of the race, first place
            print('you are in first place')
        elif user_input == "2":
            print('why would you do that? you are last!')
        elif user_input == "3":
            print("you have been blown up. YOU LOSE HAHA!")
            break
        else:
            print(f"Invalid input {user_input}")

    
    while lamborghini.health > 0 and trackhawk.health > 0:
        print(f"the lamborghnini has {lamborghini.health} health")
        print(f"the trackhawk has {trackhawk.health} health")
        print()
        print("choose your FATE!")
        print("1. shortcut right turn!")
        print("2. shortcut left turn!")
        print("3. flee")
        print("< ",)



            
  
        your_car = choose_your_car()
play_game()