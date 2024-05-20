import random

class car:
    def __init__(self, model, health):
        self.model = model
        self.health = health
        

    def is_alive(self):
        return self.health > 0

    
    def damage(self, damage):
            self.health -= damage

    
    def event_chance():
         return random.randint(1,10)
            
lamborghini = car('lamborghini', 70)
trackhawk = car('trackhawk', 100)
car_munu = {
    '1': lamborghini,
    '2': trackhawk
}

import os 
os.system('cls' if os.name == 'nt' else 'clear')

def error_statement():
    print('\nthat is not valid otpion, try again:')




def play_game():
    print("welcome to: the escape from prison by car game")
    print("we are giving you a chance to escape from prison")
    print("BUT there is only 1 path to escape. HAHA! GOOD LUCK")
    print()
    print("1. lamborghnini")
    print("2. trackhawk")
    choosing_car = input('choose your car: ')
    back_to_phase3 = False
           
    while lamborghini.health > 0 and trackhawk.health > 0:
        print(f"the lamborghnini has {lamborghini.health} health ")
        print(f"the lamborghnini has {trackhawk.health} health ")
        print()
        print("you must try to escape by car")
        print("1. GO")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1" and back_to_phase3 == False:
            # the start of the escape
            print('find the rigth path')
            print()
            if user_input:
                print("choose your FATE!")
                print("1. shortcut right turn!")
                print("2. shortcut left turn!")
                print("3. stay on path")
                print("< ",)
                user2_input = input()
                if user2_input == '1':
                    # next stage of the escape
                    print('great choice, you have a good path')
                    print()
                    if user2_input:
                        print('choose your FATE!')
                        print('1. drive over upgrade.')
                        print('2. shortcut right turn!')
                        print('3. do nothing')
                        print('< ',)
                        phase4_input = input()
                        if phase4_input == '1':
                            print('you have a nitrous upgrade')
                            print()
                            phase6_input = True
                            if phase6_input == True:
                                print("you can see the escape exit. what you going to do next?")
                                print("1. use your nitrous upgrade")
                                print("2. shortcut left turn")
                                print("3. stay on path")
                                phase6_input = input()
                                if phase6_input == "1":
                                    print("HAHA! again NO your DEAD! try again")
                                    car_munu.get(choosing_car).damage(100)
                                elif phase6_input == "2":
                                    print("wrong way. HAHA! your dead again")
                                    car_munu.get(choosing_car).damage(100)
                                elif phase6_input == "3":
                                    print("not so fast HAHA! DEAD!")
                                    car_munu.get(choosing_car).damage(100)
                        elif phase4_input == '2':
                            print('DEAD!')
                            car_munu.get(choosing_car).damage(100)
                        elif phase4_input == '3':
                            print("taking you back")
                            back_to_phase3 = True
                elif user2_input == '2':    
                    print('the roof of the car has been taken off')
                    car_munu.get(choosing_car).damage(100)
                elif user2_input == '3':
                    print("guess you don't wanna escape faster.")
        elif user_input == "2" or back_to_phase3 == True:
            print('why would you do that? lets try again')
            print()
            phase3_input = True
            if phase3_input == True:
                print('lets try this again!')
                print('1. drive over upgrade.')
                print('2. shortcut left turn')
                print('< ',)
                phase3_input = input()
                if phase3_input == "1":
                    print('now your getting it. you have a nitrous upgrade.')
                    print()
                    phase5_input = True
                    if phase5_input == True:
                        print('the escape exit is right there. what do you want to do next?')
                        print('1. use nitrous upgrade')
                        print("2. it's right there. stay on path")
                        print("3. shortcut right turn")
                        print("< ",)
                        phase5_input = input()
                        if phase5_input == "1":
                            print("HAHA! you have been blown up")
                            car_munu.get(choosing_car).damage(100)
                        elif phase5_input ==  "2":
                            print("WOW! you thought it would be that easy. DEAD! try again")
                            car_munu.get(choosing_car).damage(100)
                        elif phase5_input == "3":
                            print("YAYYYY YOU HAVE ESCAPED. YOU WIN")
                            break
                elif phase3_input == "2":
                    print('haha! gotcha! you just took alot of damage')
                    car_munu.get(choosing_car).damage(40) 
                    print()  
                    lastphase_input = True
                    if lastphase_input == True:
                        print('choose your FATE!')
                        print('1. drive over upgrade.')
                        print('2. stay on the path')
                        print('< ',)
                        lastphase_input = input()
                        if lastphase_input == '1':
                            print('HAHA! decoy upgrade you have been blown up')
                            car_munu.get(choosing_car).damage(100)
                        elif lastphase_input == '2':
                            print('did you think it would be that easy HAHA! DEAD!')
                            car_munu.get(choosing_car).damage(100)
        elif user_input == "3":
            print("you have been thrown in the hole. YOU LOSE HAHA!")
            break
        else:
            print(f"Invalid input {user_input}")

            
play_game()