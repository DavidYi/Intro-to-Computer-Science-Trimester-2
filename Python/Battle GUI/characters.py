import random

#
# No changes are required in this file.
#
 
class Character (object):
   
    def __init__ (self, name, hit_points, strength, defense, hp, stren, dexterity, small_image, large_image):
        ''' 
        Set the instance variables of name, hit_points, strength, and dexerity
        based upon the passed parameters. 
        '''
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.defense = defense
        self.hp = hp
        self.strength1 = stren
        self.dexterity = dexterity
        self.small_image = small_image
        self.large_image = large_image
        
    def attack (self, enemy, is_crit, crit_defend, battlechoice):
        ''' 
        In this method, self attempts to attack the enemy.  First, the method determines if 
        a hit occurs using randomness.  If the opponents had the same defense, the probability 
        of a hit would be 50%.  If the defense of self is higher than that of enemy, the probability
        of a hit increases.  If the defense of self is lower than that of enemy, the probability
        of a hit decreases.  The exact implementation of this probability is up to you, but 
        make it as fair as possible.
        
        If a hit occurs, hit_points damage should be a random number between 0 and the self.strength.
        
        The method should then print the result of the attack to the user.
        '''
        if battlechoice == "battle1":
            critdamage = self.strength//2
            damage = self.strength//2
            if damage%2 == 1:
                damage +=1
            
            x = damage // 2
            critdamage += x
            
            critdamage -= enemy.defense//8
            damage -= enemy.defense//8
            
            if is_crit == True:
                enemy.hit_points -= int(critdamage)
                if crit_defend == True:
                    result = self.name + " defends against " + enemy.name + "'s critical hit and returns " + str(critdamage) + " damage."
                else:
                    result = self.name + " crits " + enemy.name + " for a total of " + str(critdamage) + " damage."
        
            else:
                enemy.hit_points -= damage
                result = self.name + " hits " + enemy.name +" causing " + str(damage) + " damage."
    
        else:
            total_dex = self.dexterity + enemy.dexterity
            hit_attempt = random.randrange(0,total_dex)        
            if (hit_attempt<=self.dexterity):
                damage = random.randrange (0, self.strength1)
                enemy.hp -= damage
                result = self.name + " hits " + enemy.name +" causing " + str(damage) + " damage."
            else:
                result = self.name + " misses " + enemy.name + "."
                    
        return result   
        
    def die (self):
        ''' Prints a death message. '''
        return self.name + ": Ahhhhh.. too much damage!  I have died."
        
    def __str__ (self):
        ''' Prints the name, hit points, strength, and defense of the object. '''
        return self.name + "; HP: " + str(self.hit_points) + "; Strength: " + str(self.strength) + "; defense: " + str(self.defense)        
        
class CharacterList (object):
    def __init__ (self, file_name):
        ''' 
        This method initializes a new CharacterList object by loading
        a list of Characters from file_name.  
        The file is in comma, separated format.  The fields of the file include:
            <Name>,<Hit Points>,<Strength>,<defense>
        '''
        self.character_list = []
        
        text_file = open(file_name,"r")
        
        for line in text_file:
            line = line.strip()
            my_fields = line.split(",")
            character = Character (my_fields[0], int(my_fields[1]), int(my_fields[2]), int(my_fields[3]), int(my_fields[4]), int(my_fields[5]), int(my_fields[6]), my_fields[7], my_fields[8])
            self.character_list.append(character)
    
    def print_list (self):
        ''' 
        Prints the list of characters_base, using the __str__ function of Character object.
        '''
        for i in range (len(self.character_list)):
            print (str(i) +": " + str(self.character_list[i]))        
    
    def get_and_remove_character (self, i):
        ''' 
        Gets and returns the "ith" Character from the list, then removes the 
        character from the list.  (Doing so prevents the user and computer from 
        using the same character.
        '''
        ch = self.character_list[i]
        self.character_list.remove(self.character_list[i])
        return ch
    
    def get_random_character (self):
        ''' Gets and returns a random character from the list (for the computer). '''
        return random.choice(self.character_list)
    
    def get_number_of_characters (self):
        ''' Returns the number of characters_base in the list. '''
        return len(self.character_list)

