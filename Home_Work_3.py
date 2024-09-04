class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name  
        self.__endurance = endurance  
        self.__sprint = sprint  
        self.__dribble = dribble  
        self.__passing = passing  
        self.__shooting = shooting  

    #getter và setter cho name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    #getter và setter cho endurance
    def get_endurance(self):
        return self.__endurance
    def set_endurance(self, endurance):
        self.__endurance = endurance

    #getter và setter cho sprint
    def get_sprint(self):
        return self.__sprint
    def set_sprint(self, sprint):
        self.__sprint = sprint

    #getter và setter cho dribble
    def get_dribble(self):
        return self.__dribble
    def set_dribble(self, dribble):
        self.__dribble = dribble

    #getter và setter cho passing
    def get_passing(self):
        return self.__passing
    def set_passing(self, passing):
        self.__passing = passing

    #getter và setter cho shooting
    def get_shooting(self):
        return self.__shooting
    def set_shooting(self, shooting):
        self.__shooting = shooting

    def __str__(self):
        return (f"Player: {self.__name}\n"
                f"Endurance: {self.__endurance}\n"
                f"Sprint: {self.__sprint}\n"
                f"Dribble: {self.__dribble}\n"
                f"Passing: {self.__passing}\n"
                f"Shooting: {self.__shooting}\n")

class Team:
    def __init__(self, name, rating):
        self.__name = name  
        self.__rating = rating  
        self.__players = [] 

    #getter và setter cho name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    #getter và setter cho rating
    def get_rating(self):
        return self.__rating
    def set_rating(self, rating):
        self.__rating = rating

    #getter cho players
    def get_players(self):
        return self.__players
    

    #thêm cầu thủ vào đội
    def add_player(self, player):
        self.__players.append(player)
    #xoá cầu thủ khỏi đội
    def remove_player(self, player_name):
        for player in self.__players:
            if player.get_name() == player_name:
                self.__players.remove(player)
                return player 
        return f"Player {player_name} ko có trong đội"


    def __str__(self):
        players_info = "\n".join(str(player) for player in self.__players)
        return (f"Team: {self.__name}\n"
                f"Rating: {self.__rating}\n"
                f"Players:\n{players_info}\n")




player1 = Player("Quang Hải", 80, 85, 78, 90, 88)
player2 = Player("Công Phương", 75, 80, 85, 70, 75)
player3 = Player("Văn Thanh", 70, 75, 80, 85, 80)

team = Team("Việt Nam", 85)

print(team.add_player(player1))  
print(team.add_player(player2))  
print(team.add_player(player1))  

print(team.remove_player("Quang Hải"))  
print(team.remove_player("Hải Dương"))  

print(team) 