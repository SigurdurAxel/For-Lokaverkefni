import random, time

#players health
ph = 120

class beast:

    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health


    def battle(self):
        global ph
        print ("Enemy spoted " + self.name , "health:" , self.health)
        print (" ")
        time.sleep(1)
        while ph > 0 and self.health > 0:
            self.attack_enemy()
            if self.health <=0:
               break
            self.enemy_attack()
            if ph <=0:
                break
        if self.health <= 0:
            time.sleep(1)
            print ("You killed the " + self.name)

        if ph <= 0:
            time.sleep(1)
            print ("GAME OVER")
                

    def attack_enemy(self):
        time.sleep(1)
        print ("what move would you like to make? (Slash, kick, punch or selfheal + 60 - 50/50 change of working?)")
        print(" ")
        svar = input("Your move -->")

        if svar == "slash":
            self.health = self.health - (random.randint(1,100)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif svar == "kick":
            self.health = self.health - (random.randint(1,100)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif svar == "punch":
            self.health = self.health -   (random.randint(1,100)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif svar == "selfheal":
            global ph
            bla3 = random.randint(1,2)
            if bla3 == 1:
                ph = ph + 60
                print(" ")
                print("Your health is now" , ph)
                print(" ")
            else:
                print("Failed to heal")
        else:
            print("your attack failed")

        time.sleep(1)

        print (self.name + "'s health is now: " + str(int(self.health)))
        print("")

        return int(self.health)

    def enemy_attack(self):
        global ph
        time.sleep(1)
        print ("The enemy " + self.name + " " + "attacks...")
        print("")
        ph = ph - (self.strength * random.uniform(0.1, 1.4))
        ph = int(ph)
        time.sleep(1)
        print ("Your health is now " + str(int(ph)))
        print ("")
        return int(ph)

enemies = [beast("Angry Rabbit", 10, 5, 100), beast("Ghost", 15, 5, 120), beast("Fox", 20, 10, 100), beast("Zombie", 30, 20, 100), beast ("Boss", 40, 30, 130)]


print("Þessi leikur færð þú random skrímsli til að berjast við")
blub = input("Press enter to start")
print(" ")

random_beast = random.choice(enemies) 
random_beast.battle()





