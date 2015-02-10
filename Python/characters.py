import random

class Character (object):
    ''' 
    The maximum dexterity of any character is 100.  This value is used in attack()
    to determine the likelihood of the Character hitting the enemy. 
    '''    
    MAX_DEXTERITY = 100
    
    def __init__ (self, name, hit_points, strength, dexterity):
        ''' 
        Set the instance variables of name, hit_points, strengthength, and dexterity
        based upon the passed parameters. 
        '''
        self.name = name
        self.hit_points = int(hit_points)
        self.strength = int(strength)
        self.dex = int(dexterity)
        
    def attack (self, enemy):
        ''' 
        In this method, self attempts to attack the enemy.  First, the method determines if 
        a hit occurs using randomness.  If the opponents had the same dexterity, the probability 
        of a hit would be 50%.  If the dexterity of self is higher than that of enemy, the probability
        of a hit increases.  If the dexterity of self is lower than that of enemy, the probability
        of a hit decreases.  The exact implementation of this probability is up to you, but 
        make it as fair as possible.
        
        If a hit occurs, hit_poi1nts damage should be a random number between 0 and the self.strengthength.
        
        The method should then print the result of the attack to the user.
        '''
        factor = abs(self.dex-enemy.dex)
        if self.dex == enemy.dex:
            prob=50
            
        elif self.dex > enemy.dex:
            prob = 60 + (factor//5)
            
        elif self.dex < enemy.dex:
            prob = 40 - (factor//10)
        
        hitprob = random.randint(1,100)
        
        if hitprob<=prob:
            dmg= random.randint(0,self.strength)
            print(self.name + " has dealt", dmg ,"damage to", enemy.name+".")
            enemy.hit_points-=dmg
        else:
            print(self.name+"'s attack has missed",enemy.name,".")
            
    def die (self):
        ''' Prints a death message. '''
        print(self.name+": Arghhhhh U3PRO5ME!!!! I have no hit_points right now. I am dying. I will kill you next time. I will rek u scrub. I...\n"\
              +self.name+" has died\n"+self.name+"'s words echos... I WILL BE BACK. GET READY TO GET SHREKT!")
    
    def __str__ (self):
        ''' Prints the name, hit points, strength, and dexterity of the object. '''
        return self.name+"; HP: " + str(self.hit_points)+"; Strength: "+ str(self.strength)+"; Dexterity:" + str(self.dex)
        
class CharacterList (object):
    def __init__ (self, file_name):
        ''' 
        This method initializes a new CharacterList object by loading
        a list of Characters from file_name.  The list is stored as an
        instance variable of this CharacterList object.
        
        The file is comma, separated format.  The fields of the file include:
            <Name>,<Hit Points>,<strength>,<Dexterity>
        '''
        file = open("battle_characters.txt", "r")
        
        self.namelist=[]
        
        for line in file:
            stats= line.split(",")
            stats[3]=stats[3].strip("\n")
            character = Character(stats[0], stats[1], stats[2], stats[3])
            self.namelist.append(character)
        
    def print_list (self):
        ''' 
        Prints the list of characters, using the __strength__ function of Character object.
        '''
        n=0
        for character in self.namelist:
            print(str(n)+":", Character.__str__(character))
            n+=1
            
    def get_and_remove_character (self, i):
        ''' 
        Gets and returns the "ith" Character from the list, then removes the 
        character from the list.  (Doing so prevents the user and computer from 
        using the same character.
        '''
        player = self.namelist[i]
        del(self.namelist[i])
        return player
    
    def get_random_character (self):
        ''' Gets and returns a random character from the list (for the computer). '''
        x=len(self.namelist)
        char = random.randrange(x)
        return self.namelist[char]
    
    def get_number_of_characters (self):
        ''' Returns the number of characters in the list. '''
        return len(self.namelist)
