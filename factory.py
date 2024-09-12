from abc import ABC, abstractmethod
from random import choice
class PlayerBase(ABC):
    chocies = ['r','p','s']
    @abstractmethod
    def move(self):
        pass

class HumanPlayer(PlayerBase):
    def move(self):
        m =input("choise your next move ...")
        return m
class SystemPlayer(PlayerBase):
    def move(self):
        c = choice(self.chocies)
        print(f"system move : {c}")
        return c


class Game:
    def start_game(self,game_type):
        if game_type == "s":
            p1 = HumanPlayer()
            p2 = SystemPlayer()
            
        elif game_type == "m":
            p1 = HumanPlayer()
            p2 = HumanPlayer()
            print(id(p1))
            print(id(p2))
        else:
            print("Invalid input")
            p1 = None
            p2 = None
        return p1,p2



if __name__ == "__main__":
    game = Game()
    game_type = input("please choose game type ('s' for single and 'm') for multiple player")
    player1,player2 = game.start_game(game_type)

    for player in [player1,player2]:
        player.move()