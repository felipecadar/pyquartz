import random
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
    3: ("Esmeralda", 10, 3),
    4: ("Safira", 7, 4),
    5: ("Rubi", 4, 6),
    6: ("Ambar", 2, 8),
    7: ("Autunita", 18, 0),
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
        
        all_values = [0] * (len(gems_config)-1)
        for gem in self.gems:
            all_values[gem] += gems_config[gem][2]
            
        return reduce(lambda x1, x2: x1 + x2 , all_values)

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