
class Team:
    def __init__(self, name_of_the_team, number_of_players, number_of_batsman, number_of_bowlers, number_of_allrounders, budget ):
        self.name_of_the_team = name_of_the_team   # attributes
        self.number_of_players = number_of_players # attributes
        self.number_of_batsman = number_of_batsman # attributes
        self.number_of_bowlers = number_of_bowlers # attributes
        self.number_of_allrounders = number_of_allrounders # attributes
        self._budget = budget # attribute ( hide the budget ) 
        
    @property  # getters
    def number_of_players(self):
        return self.__number_of_players
    
    @number_of_players.setter    # setters
    def number_of_players(self, number):
        self.__number_of_players = number
       
    def team_theme(self): # methods
        print('JIO DHAN DHANADHAN')
        
# Create your team from Team Class        
team_mumbai_indians = Team("Mumbai Indians", 11, 4, 4, 3, 250) 
print (team_mumbai_indians)

print(team_mumbai_indians.number_of_players)

# Set your number of players after instance/object is created. 

team_mumbai_indians.number_of_players = 12 # setting number of players to 12
print(team_mumbai_indians.number_of_players) # 12

team_mumbai_indians.team_theme()
