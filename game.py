import random
import numpy as np
from functools import reduce

color = {
    0:"azul",
    1:"roxo"
}

cards_config = {
    0: { 'name': "Agora vai...", 'qty':10, 'color':0},
    1: { 'name': "Rá, EUREKA!", 'qty':3, 'color':0},
    2: { 'name': "chega mais...", 'qty':3, 'color':0},
    3: { 'name': "sai da frenteeee...", 'qty':3, 'color':0},
    4: { 'name': "Cristal? que Cristal?", 'qty':3, 'color':0},
    5: { 'name': "me faz um favor...", 'qty':8, 'color':0},
    6: { 'name': "não te pertence mais...", 'qty':8, 'color':0},
    7: { 'name': "opa! esse Cristal não é meu...", 'qty':8, 'color':0},
    8: { 'name': "nem meu!", 'qty':3, 'color':1},
    9: { 'name': "só por cima do meu cadáver!", 'qty':3, 'color':1},
    1: { 'name': "estou cansado...", 'qty':3, 'color':1},
}

gems_config = {
    0: ("Quartzo", 15, 1),
    1: ("Rubelita", 12, 2),
    2: ("Esmeralda", 10, 3),
    3: ("Safira", 7, 4),
    4: ("Rubi", 4, 6),
    5: ("Ambar", 2, 8),
    6: ("Autunita", 18, 0),
}

class Card:
    def __init__(self, card_id:int):
        self.card_id = card_id
        self.color = cards_config[card_id]['color']
        self.name = cards_config[card_id]['name']

    def run(self):
        pass


class Deck:
    def __init__(self):
        self.deck = None
        
        self.makeDeck()

    def makeDeck(self):
        deck = []
        for cid in cards_config:
            qty = cards_config[cid]['qty']
            for i in range(qty):
                deck.append(Card(cid))
        
        random.shuffle(deck)
        self.deck = deck

    def give(self, n):
        if n > len(self.deck):
            return []

        return [self.deck.pop() for x in range(n)]

class Player:
    def __init__(self, pid, name=None):
        self.pid = pid
        self.name = name
        if self.name is None:
            self.name = pid
        
        self.cards = []
        self.gems = []
        self.couins = 0
        self.protection = False
        self.chest = [None, None]

    def sell(self):
        
        gem_count = [0] * (len(gems_config)-1)
        for gem in self.gems:
            gem_count[gem] += 1

        gems_values = [gems_config[i][2] for i in self.gems]
        value = reduce(lambda x, y: x+y, gems_values)
        combo_value = value
        
        all_combos = [value]

        # test each combo
        # Sell x3
        has_combo = False
        combo_gem = -1
        for i, c in enumerate(gem_count):
            if c >= 3:
                has_combo = True
                combo_gem = i 
                break


        if has_combo:
            combo_value = value
            m = -1
            idx = -1
            for i, ci in enumerate(gem_count):
                if i != combo_gem and ci > 0:
                    combo_value = value + (ci * gems_config[i][2]) 
                    if combo_value > m:
                        idx = i
                        m = combo_value
            if m > combo_value:
                combo_value = m

            all_combos.append(combo_value)

        # Sell x4
        has_combo = False
        combo_gem = -1
        for i, c in enumerate(gem_count):
            if c >= 4:
                has_combo = True
                combo_gem = i 
                break

        gems_values = [gems_config[i][2] for i in self.gems]
        value = reduce(lambda x, y: x+y, gems_values)

        if has_combo:
            combo_value = value
            m = -1
            idx = -1
            for i, ci in enumerate(gem_count):
                if i != combo_gem and ci > 0:
                    for j, cj in enumerate(gem_count):
                        if i!=j and j != combo_gem and cj > 0:
                            combo_value = value + (ci * gems_config[i][2]) + (cj * gems_config[j][2]) 
                            if combo_value > m:
                                idx = i
                                m = combo_value
            if m > combo_value:
                combo_value = m
            all_combos.append(combo_value)

        # Sell 5!=
        if 0 in self.gems and 1 in self.gems and 2 in self.gems and 3 in self.gems and 4 in self.gems:
            combo_value = value + 8
            all_combos.append(combo_value)

        # Sell 6!=
        if 0 in self.gems and 1 in self.gems and 2 in self.gems and 3 in self.gems and 4 in self.gems and 5 in self.gems:
            combo_value = value + 12
            all_combos.append(combo_value)

        return np.max(all_combos)    

    def mine(self, mine):
        pass

    def useCard(self):
        pass

    def answerCard(self):
        pass

class Mine:
    def __init__(self):
        self.gems = []
        self.makeMine()

    def makeMine(self):
        mine = []
        for gid in gems_config:
            name, qty, value = gems_config[gid]
            for i in range(qty):
                mine.append(gid)


if __name__ == "__main__":
   player1 = Player(1)
   player1.gems = [0,0,0, 1]
   v = player1.sell()   
   print(v)