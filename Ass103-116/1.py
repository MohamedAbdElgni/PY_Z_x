#game_one = Game("Ys", "Falcom", 2010, 50)
class Game():
    def __init__(self, game_name, game_dev, year, price):
        self.g_name = game_name
        self.g_dev = game_dev
        self.y_p = year
        self.p_p = price


game_one = Game("Ys", "Falcom", 2010, 50)
print(f"Game Name Is \"{game_one.g_name}\", ", end="")
print(f"Developer Is \"{game_one.g_dev}\", ", end="")
print(f"Release Date Is \"{game_one.y_p}\", ", end="")
print(f"Price In Egypt Is {game_one.p_p*15}", end="")
