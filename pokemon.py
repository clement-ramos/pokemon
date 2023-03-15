import json, math, random

with open("Data/pokemon.json", "r") as pokemon:
    pokemon_list_reader = json.load(pokemon)

with open("Data/moves.json", "r") as moves:
    moves_reader = json.load(moves)

with open("Data/movesets.json", "r") as movesets:
    movesets_reader = json.load(movesets)

class Pokemon():
    def __init__(self, id, level):
        self.__id = id
        self.__name = pokemon_list_reader[self.__id]["name"]["french"]
        self.__type = pokemon_list_reader[self.__id]["type"]
        self.__moveset = movesets_reader[str(self.__id)]
        self.__level = level
        self.__exp = 0
        self.__exp_to_next = self.__level * 20
        self.define_IV()
        self.define_EV()
        self.baseStats()

    def baseStats(self):
        self.__HP = math.floor((((2* pokemon_list_reader[self.__id]["base"]["HP"] + self.__IV_HP + (self.__EV_HP/4))* self.__level)/100) + self.__level + 10)
        self.__ATQ = math.floor((((2* pokemon_list_reader[self.__id]["base"]["ATQ"] + self.__IV_ATQ + (self.__EV_ATQ/4))* self.__level)/100) + self.__level + 10)
        self.__DEF = math.floor((((2* pokemon_list_reader[self.__id]["base"]["DEF"] + self.__IV_DEF + (self.__EV_DEF/4))* self.__level)/100) + self.__level + 10)
        self.__SATQ = math.floor((((2* pokemon_list_reader[self.__id]["base"]["SATQ"] + self.__IV_SATQ + (self.__EV_SATQ/4))* self.__level)/100) + self.__level + 10)
        self.__SDEF = math.floor((((2* pokemon_list_reader[self.__id]["base"]["SDEF"] + self.__IV_SDEF + (self.__EV_SDEF/4))* self.__level)/100) + self.__level + 10)
        self.__SPD = math.floor((((2* pokemon_list_reader[self.__id]["base"]["SPD"] + self.__IV_SPD + (self.__EV_SPD/4))* self.__level)/100) + self.__level + 10)

    def define_IV(self):
        self.__IV_HP = random.randint(0, 31)
        self.__IV_ATQ = random.randint(0, 31)
        self.__IV_DEF = random.randint(0, 31)
        self.__IV_SATQ = random.randint(0, 31)
        self.__IV_SDEF = random.randint(0, 31)
        self.__IV_SPD = random.randint(0, 31)

    def define_EV(self):
        self.__EV_HP = 0
        self.__EV_ATQ = 0
        self.__EV_DEF = 0
        self.__EV_SATQ = 0
        self.__EV_SDEF = 0
        self.__EV_SPD = 0

    def isAlive():
        pass

    def missManagement():
        pass

    def damaging():
        pass

    def printWinner():
        pass

    def printFainted():
        pass

    def saveInPokedex():
        pass
    
    def printCurrentStats(self):
        print(
            f"\nGeneral Pokemon Info:"
            f"\nName: {self.__name}"
            f"\nType: {self.__type}"
            f"\n_______________________________________________________"
            f"\n\nBase Stats:"
            f"\nHP, ATQ, DEF, SATQ, SDEF, SPD"
            f"\n {self.__HP},  {self.__ATQ},  {self.__DEF},  {self.__SATQ},  {self.__SDEF},  {self.__SPD}"
            f"\n_______________________________________________________"
            f"\n\nOthers:"
            f"\nLevel: {self.__level}"
            f"\nExperience: {self.__exp}"
            f"\nExperience to lvl up: {self.__exp_to_next}"     
            f"\n_______________________________________________________"
            f"\n\nMoves:"
            f"\n {self.__moveset}"
            f"\n_______________________________________________________"
            f"\n\nIVS:"
            f"\nHP, ATQ, DEF, SATQ, SDEF, SPD"
            f"\n {self.__IV_HP},  {self.__IV_ATQ},  {self.__IV_DEF},  {self.__IV_SATQ},  {self.__IV_SDEF},  {self.__IV_SPD}"
        )

# ID LVL
pokemon1 = Pokemon(2, 20)
pokemon1.printCurrentStats()
