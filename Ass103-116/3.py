class Games():
    def __init__(self, name):
        self.name = name

    def show_games(self):
        if type(self.name) == list:
            print(f"i have {len(self.name)} games :- ".title())
            for i in self.name:
                print(f"-- {i}")
            else:
                print("="*50)
        elif type(self.name) == int:
            print(f"i have {self.name} games".title())
            print("="*50)
        else:
            print("="*50)
            print(f"i have one game called {self.name}".title())
            print("="*50)


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)
my_game.show_games()
my_games_names.show_games()
my_games_count.show_games()
