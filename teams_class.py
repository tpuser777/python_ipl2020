
class Team:
    def __init__(self, name_of_the_team, number_of_players, number_of_batsman, number_of_bowlers, number_of_allrounders, budget ):
        self.name_of_the_team = name_of_the_team
        self.number_of_players = number_of_players
        self.number_of_batsman = number_of_batsman
        self.number_of_bowlers = number_of_bowlers
        self.number_of_allrounders = number_of_allrounders
        self.budget = budget
        
    @property  # getters
    def number_of_players(self):
        return self.__number_of_players
    
    @number_of_players.setter    # setters
    def number_of_players(self, number):
        self.__number_of_players = number
        
# Create your team from Team Class        
team_mumbai_indians = Team("Mumbai Indians", 11, 4, 4, 3, 250) 
print (team_mumbai_indians)

print(team_mumbai_indians.number_of_players)

# Set your number of players after instance/object is created. 

team_mumbai_indians.number_of_players = 12 # setting number of players to 12
print(team_mumbai_indians.number_of_players) # 12
