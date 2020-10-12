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

class EnglandIPL(Team):
    def __init__(self,name_of_the_team, number_of_players, number_of_batsman, number_of_bowlers, number_of_allrounders, budget, number_of_lefthandedbatsman):
        Team.__init__(self, name_of_the_team, number_of_players, number_of_batsman, number_of_bowlers, number_of_allrounders, budget)
        self.number_of_lefthandedbatsman = number_of_lefthandedbatsman
        
epl_2020 = EnglandIPL("Mumbai Indians", 11, 4, 4, 3, 250, 2)
print(epl_2020.number_of_players) # => 11
print(epl_2020.number_of_bowlers) # => 4
print(epl_2020.number_of_lefthandedbatsman) # => 2
