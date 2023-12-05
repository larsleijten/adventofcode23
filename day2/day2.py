

file = open("day2/input.txt", "r")
lines = file.readlines()


class Game():
    def __init__(self, text, max_red, max_green, max_blue):
        self.max_red = max_red
        self.max_green = max_green
        self.max_blue = max_blue

        # Extract game results
        [prefix, gameinfo] = text.split(": ")
        self.gameid = int(prefix.split("Game ")[-1])
        self.game_results = gameinfo.split("; ")

        # Parse game results
        self.reds = []
        self.greens = []
        self.blues = []

        for result in self.game_results:
            red = 0
            green = 0
            blue = 0
            components = result.split(",")
            for component in components:
                component = component.strip()
                number, color = component.split(" ")

                if color == "red":
                    red = int(number)
                elif color == "green":
                    green = int(number)
                elif color == "blue":
                    blue = int(number)
            self.reds.append(red)
            self.greens.append(green)
            self.blues.append(blue)

        if max(self.reds) > self.max_red:
            self.valid = False
        elif max(self.greens) > self.max_green:
            self.valid = False
        elif max(self.blues) > self.max_blue:
            self.valid = False
        else:
            self.valid = True

    def get_power(self):
        required_red = max(self.reds)
        required_green = max(self.greens)
        required_blue = max(self.blues)
        power = required_red * required_green * required_blue
        return power


games = []
for line in lines:
    game = Game(line, 12, 13, 14)
    games.append(game)

valid_indices = []
powers = []
for game in games:
    if game.valid:
        valid_indices.append(game.gameid)
    powers.append(game.get_power())

print(f"Sum of valid indices: {sum(valid_indices)}")
print(f"Sum of all powers: {sum(powers)}")
