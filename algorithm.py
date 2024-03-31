

class Team:
    def __init(self, name):
        self.name = name
        self.players = []

        def add_player(self, player):
            self.players.append(player)

class Game:
    def __init__(self, opponent, points, minutes):
        self.opponent = opponent
        self.points = points
        self.minutes = minutes

class Player:
    def __init__(self, name, team, pos, age, gp, mpg, usg, to, fta, ft, twopa, twop, threepa, threep, efgp, tsp, ppg, rpg, apg, spg, bpg, tpg, pplusr, pplusa, pplusrplusa, vi, ortg, drtg):
        self.name = name
        self.team = team
        self.pos = pos
        self.age = age
        self.gp = gp
        self.mpg = mpg
        self.usg = usg
        self.to = to
        self.fta = fta
        self.ft = ft
        self.twopa = twopa
        self.twop = twop
        self.threepa = threepa
        self.threep = threep
        self.efgp = efgp
        self.tsp = tsp
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg
        self.spg = spg
        self.bpg = bpg
        self.tpg = tpg
        self.pplusr = pplusr
        self.pplusa = pplusa
        self.pplusrplusa = pplusrplusa
        self.vi = vi
        self.ortg = ortg
        self.drtg = drtg

    def __str__(self):
        return (f"{self.name}, {self.team}, {self.pos}, {self.age}, {self.gp}, {self.mpg}, "
                f"{self.usg}, {self.to}, {self.fta}, {self.ft}, {self.twopa}, {self.twop}, "
                f"{self.threepa}, {self.threep}, {self.efgp}, {self.tsp}, {self.ppg}, "
                f"{self.rpg}, {self.apg}, {self.spg}, {self.bpg}, {self.tpg}, {self.pplusr}, "
                f"{self.pplusa}, {self.pplusrplusa}, {self.vi}, {self.ortg}, {self.drtg}")

        