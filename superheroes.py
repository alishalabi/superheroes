import random

class Ability:
    def __init__(self, name, attack_strength):
        # Set ability name
        self.name = name
        #Set attack strength
        self.attack_strength = attack_strength

    def attack(self):
        # Calculate lowest attack value as an integer.
        min_strength = self.attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        #Return attack value between 0 and the full attack
        return random.randint(min_strength, self.attack_strength)


    def update_attack(self, attack_strength):
        #Update attack value
        self.attack_strength = attack_strength

class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        #Append ability to self.abilities
        self.abilities.append(ability)

    def attack(self):
        self.total_attack = 0
        # Call the attack method on every ability in our ability list
        for ability in self.abilities:
            self.total_attack += ability.attack()
        # Add up and return the total of all attack_strength
        return self.total_attack

    def defend(self):
        # This method should run the defend method on each piece of armor and calculate the total defense.
        # If the hero's health is 0, the hero is out of play and should return 0 defense points.
        self.total_defense = 0
        for armor_piece in self.armors:
            self.total_defense += armor_piece.defend()
        return self.total_defense


    def take_damage(self, damage_amt):
        # This method should subtract the damage amount from the hero's health.
        # If the hero dies update number of deaths.
        self.damage_amt = damage_amt
        self.health_reduction = self.damange_amt - self.total_defense
        self.health -= self.health_reduction
        if self.health < 0:
            self.deaths += 1
            return self.deaths

    def add_kill(self, num_kills):
        # This method should add the number of kills to self.kills
        self.num_kills = num_kills
        self.kills += self.num_kills

    def status(self):
        # We want to print our the hero's name, all of their abilities,
        # all of their kills and all of their deaths
        print("Hero - " + self.name)
        enumerated_names = []
        for ability_name in self.abilities:
            enumerated_names.append(ability_name)
        print("All abilities -" + ", ".join(enumerated_names))
        print("Hero kills - " + str(self.kills))
        print("Hero deaths - " + str(self.deaths))


class Weapon(Ability):
    def attack(self):
        self.weapon_strength = random.randint(0, self.attack_strength)
        return self.weapon_strength

class Team:
    def __init__(self, team_name):
        # Instantiate resources
        self.name = team_name
        self.heroes = list()
        self.team_kills = 0
    def add_hero(self, Hero):
        # Add hero object to heroes list
        self.heroes.append(Hero)
    def remove_hero(self, name):
        #Remove hero from heroes list
        #if Hero isn't found retrun 0
        found = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found = True
        if not found:
            return 0

    def find_hero(self, name):
        #Find and return hero from heroes list
        #If hero isn't found return 0
        self.name = name
        found = False
        for hero in self.heroes:
            if hero.name == name:
                # print(type(name))
                print(hero)
                found = True
                return hero
        if not found:
            return 0

    def view_all_heroes(self):
        #Print out all heroes to the console
        for hero_object in self.heroes:
            print(hero_object.name)

    def attack(self, other_team):
        # This method should total our teams attack strength and call the
        # defend() method on the rival team that is passed in.
        # It should call add_kill() on each hero with the number of kills made.
        self.total_team_attack = 0
        for hero_attack in self.heroes:
            print(hero.name)
            self.total_team_attack += hero.attack()
        round_kills = other_team.defend(total_team_attack)
        self.team_kills += round_kills
        for hero in self.heroes:
            hero.add_kill(round_kills)

    def defend(self, damage_amt):
        # This method should calculate our team's total defense.
        # Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        # Return number of heroes killed in attack.
        team_defense = 0
        for hero in self.heroes:
            team_defense += hero.defend()
        if (damage_amt > total_defense):
            return ''' insert code to deal damage'''
        return 0

    def deal_damage(self, damage):
        # Divide the total damage amongst all heroes.
        # Return the number of heros that died in attack.
        deaths = 0

        return 0

    def revive_heroes(self, health=100):
        # This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        # This method should print the ratio of kills/deaths
        # for each member of the team to the screen.
        # This data must be output to the terminal.
        print("Stats for " + self.name)
        for hero in self.heroes:
            hero.status()

    def update_kills(self):
        # This method should update each hero when there is a team kill.
        return self.team_kills

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense
    def defend(self):
        # Return a random value between 0 and the initialized defend Strength
        self.random_defense = random.randint(0, self.defense)
        return self.random_defense

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        # This method should allow a user to build team one.

    def build_team_two(self):
        # This method should allow user to build team two.

    def team_battle(self):
        # This method should continue to battle teams until
        # one or both teams are dead.

    def show_stats(self):
        # This method should print out the battle statistics 
        # including each heroes kill/death ratio.

# if __name__ == "__main__":
#     hero = Hero("Wonder Woman")
#     print(hero.attack())
#     ability = Ability("Divine Speed", 300)
#     hero.add_ability(ability)
#     print(hero.attack())
#     new_ability = Ability("Super Human Strength", 800)
#     hero.add_ability(new_ability)
#     print(hero.attack())
