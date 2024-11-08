# explain the rules \,
# choose characteristics \,
# run through the senarios and different generations
# need a variable for how many alive and how many dead \,

import random

global dog1
global alive
global dead

class dog:
    def __init__(self, height, fur_colour, fur_length, tail, ears, teeth, alive, dead):
        
        self.height = height #done
        self.fur_colour = fur_colour #done
        self.fur_length = fur_length #done
        self.tail = tail #done
        self.ears = ears #done
        self.teeth = teeth #done
        self.alive = alive #done
        self.dead = dead #done


    def __str__(self):
        return f"{self.height}, {self.fur_colour}, {self.fur_length}, {self.tail}, {self.ears}, {self.teeth}, {self.alive}, {self.dead}"
    
    def heatwave(self):
        if self.fur_length == "short":
            self.alive += 10
            print("\nThere has been a heatwave, since you have short fur you survive and reproduce.")
        else:
            print("\nThere has been a heatwave, since you have long fur only some of your kind survive.")
            if self.fur_colour == "white":
                self.alive += 4
                self.dead += 6
                print("However, as you have white fur, the effect is less disastrous.")
            else:
                self.alive += 2
                self.dead += 8

        print(self.alive, self.dead)
        
    def flood(self):
        if self.height == "tall":
            self.alive += 10
            print("\nThere has been a flood, since you are tall your longer feet allow you to swim to safety and reproduce.")
        elif self.height == "average":
            self.alive += 5
            self.dead += 5
            print("\nThere has been a flood, since you are average some of you to swim to safety and reproduce.")
        else:
            self.alive += 2
            self.dead += 8
            print("\nThere has been a flood, since you are short you struggle to swim and only some of your kind survive.")

        print(self.alive, self.dead)
    
    def food_shortage(self):
        if self.teeth == "blunt":
            self.alive += 10
            print("\nThere has been an increase in hunting, there is a shortage of wild birds in the area, since your diet mostly consists of nuts due to your blunt teeth, you are unaffected and reproduce.")
        else:
            self.alive += 2
            self.dead += 8
            print("\nThere has been an increase in hunting, there is a shortage of wild birds in the area, since your diet mostly consists of these birds due to your sharp teeth, some of you are malnurished.")

        
        print(self.alive, self.dead)

    def territory(self):
        if self.tail == "long":
            self.alive += 10
            print("\nA rival pack of vicious dogs have began circling your territory, however they cower in fear once they see your long tail, you will eat plenty tonight.")
        if self.tail == "curly":
            self.alive += 5
            self.dead += 5
            print("\nA rival pack of vicious dogs have began circling your territory, they attempt to overpower you and you lose some brave dogs, however using your curly tail's lasso abilities, they quickly flee.")
        if self.tail == "short":
            self.alive += 2
            self.dead += 8
            print("\nA rival pack of vicious dogs have began circling your territory, they see your short stubby tail and point and laugh at your obvious weakness, many of your pack are brutally killed.")

        print(self.alive, self.dead)


    def the_purge(self):
        if self.fur_colour == "black" or self.fur_colour == "brown":
            self.alive += 2
            self.dead += 18
            print("\nThere has been a new legislation, the ghost of the Queen has ordered that any proud British dogs must show their loyalty to the country by wearing the colours of the Union Jack in their fur. \nYou have disobeyed this order and therefore you must pay penace with your descendants as sacrifice.")
        if self.fur_colour == "white" or self.fur_colour == "blue" or self.fur_colour == "red":
            self.alive += 25
            print("\nThere has been a new legislation, the ghost of the Queen has ordered that any proud British dogs must show their loyalty to the country by wearing the colours of the Union Jack in their fur. \nAs you are following this law, you have been gifted a successful lineage from the Queen herself.")
        
        print(self.alive, self.dead)
        
    def concert(self):
        if self.ears == "floppy":
            self.alive += 10
            print("\n The long awaited Taylor Swift has finally arrived in Sticky Dog Land. Since you have payed a small fortune to preorder the tickets, you prepare ahead of time to make sure nothing goes wrong. As you have floppy ears and brought earbuds you are pretected from the harsh sound waves. This is the best day of your life")
        if self.ears == "pointy":
            self.alive += 2
            self.dead += 8
            print("\n The long awaited Taylor Swift has finally arrived in Sticky Dog Land. Since you have payed a small fortune to preorder the tickets, you expect to have an amazing time. Unfortunately, you failed to consider that you would need earbuds adn your pointed ears recieve an onslaught of harsh sound waves. You leave the concert with ringing ears, unable to form coherent thought.")

    def end(self):
        print("congratulations!!!")
        print("You have finished the game with", str(self.alive), "dogs alive, and", str(self.dead), "dogs have been killed.")





example_dog = dog("tall", "red", "short", "curly", "floppy", "sharp", 10, 0)


def choose_height():
    print("""\nWhat height are you?
1. tall
2. average
3. short""")
    
    height = input()
    if height == "1":
        height = "tall"
        
    elif height == "2":
        height = "average"
        
    elif height == "3":
        height = "short"
        
    else:
        print("Invalid input")
        choose_height()
    return height

def choose_fur_colour():
    print("""\nWhat colour is your fur?
1. brown
2. black
3. white
4. red
5. blue""")
    
    fur = input()
    if fur == "1":
        fur = "brown"

    elif fur == "2":
        fur = "black"

    elif fur == "3":
        fur = "white"

    elif fur == "4":
        fur = "red"

    elif fur == "5":
        fur = "blue"
    else:
        print("Invalid input")
        choose_fur_colour()
    return fur
    


def choose_fur_length():
    print("""\nHow long is your fur?
1. long
2. short""")
    
    fur_length = input()
    if fur_length == "1":
        fur_length = "long"

    elif fur_length == "2":
        fur_length = "short"

    else:
        print("Invalid input")
        choose_fur_length()
    return fur_length



def choose_tail():
    print("""\nWhat tail do you have?
1. curly
2. long
3. short""")
    
    tail = input()
    if tail == "1":
        tail = "curly"

    elif tail == "2":
        tail = "long"

    elif tail == "3":
        tail = "short"

    else:
        print("Invalid input")
        choose_tail()
    return tail



def choose_ear():
    print("""\nWhat ears do you have?
1. floppy
2. pointy""")
    
    ear = input()
    if ear == "1":
        ear = "floppy"

    elif ear == "2":
        ear = "pointy"

    else:
        print("Invalid input")
        choose_ear()
    return ear


def choose_teeth():
    print("""\nWhat teeth do you have?
1. sharp
2. blunt""")
    
    teeth = input()
    if teeth == "1":
        teeth = "sharp"

    elif teeth == "2":
        teeth = "blunt"

    else:
        print("Invalid input")
        choose_teeth()
        exit()
    return teeth





def customisation():
    print("---------------------------------------------")
    print("Welcome to sticky dog land!")
    print("You need to create your dog")
    height = choose_height()
    fur_colour = choose_fur_colour()
    fur_length = choose_fur_length()
    tail = choose_tail()
    ear = choose_ear()
    teeth = choose_teeth()


    dog1 = dog(height, fur_colour, fur_length, tail, ear, teeth, 10, 0)
    print("\nYour dog is " + dog1.height + ", has " + dog1.fur_length + ", " + dog1.fur_colour + " fur with a " + dog1.tail + " tail, " + dog1.teeth + " teeth and " + dog1.ears + " ears")
    print("""Are you ready to continue?
1. yes
2. restart customisation
3. exit""")
    answer = input()
    if answer == "1":
        return dog1
    elif answer == "2":
        customisation()
    elif answer == "3":
        quit()


def wait():
    input()



def main():
    dog1 = customisation()
    
    num_list = [1,2,3,4,5,6]

    for i in range(6):
        rand_num = random.choice(num_list)
        if rand_num == 1:
            dog1.heatwave()
            num_list[0] = ""
            wait()
        elif rand_num == 2:
            dog1.flood()
            num_list[1] = ""
            wait()
        elif rand_num == 3:
            dog1.food_shortage()
            num_list[2] = ""
            wait()
        elif rand_num == 4:
            dog1.territory()
            num_list[3] = ""
            wait()
        elif rand_num == 5:
            dog1.the_purge()
            num_list[4] = ""
            wait()
        elif rand_num == 6:
            dog1.concert()
            num_list[5] = ""
            wait()
        else:
            continue

    dog1.end()

main()





    
##dog1 = customisation()
##num_list = [1,2,3,4,5]
##
##    
##for i in range(6):
##    rand_num = random.choice(num_list)
##    if rand_num == 1:
##        dog1.heatwave()
##        num_list[0] = ""
##        wait()
##    elif rand_num == 2:
##        dog1.flood()
##        num_list[1] = ""
##        wait()
##    elif rand_num == 3:
##        dog1.food_shortage()
##        num_list[2] = ""
##        wait()
##    elif rand_num == 4:
##        dog1.territory()
##        num_list[3] = ""
##        wait()
##    elif rand_num == 5:
##        dog1.the_purge()
##        num_list[4] = ""
##        wait()













# this doesnt work? need to find a new way to randomise the senarios
# maybe generate a random number and then use if statement????

""" def test_func():
    print("hi")

def test_func2():
    print("hey")

def test_func3():
    print("hello")

test_list = [test_func, test_func2, test_func3]

print(random.choice(test_func(), test_func2(), test_func3())) """



"""     if dog1.height == "tall":
        alive += 10
        print(alive)
    else:
        alive += 2
        dead += 8
        print(alive)
        print(dead) """
