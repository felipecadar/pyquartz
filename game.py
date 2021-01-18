color = {
    0:"azul",
    1:"roxo"
}

cards_config = [
    (0,  "Agora vai...", 10, 0), 
    (1,  "Rá, EUREKA!", 3, 0),
    (2,  "chega mais...", 3, 0),
    (3,  "sai da frenteeee...", 3, 0),
    (4,  "Cristal? que Cristal?", 3, 0),
    (5,  "me faz um favor...", 8, 0),
    (6,  "não te pertence mais...", 8, 0),
    (7,  "opa! esse Cristal não é meu...", 8, 0),
    (8,  "nem meu!", 3, 1),
    (9,  "só por cima do meu cadáver!", 3, 1),
    (10, "estou cansado...", 3, 1),
]

gems_config = [
    (0, "Quartzo", 15, 1),
    (1, "Rubelita", 12, 2),
    (3, "Esmeralda", 10, 3),
    (4, "Safira", 7, 4),
    (5, "Rubi", 4, 6),
    (6, "Ambar", 2, 8),
    (7, "Autunita", 18, 0),
]

class Card:
    def __init__(self, card_id:int, back:int):
        self.card_id = card_id
        self.back = back

    def run(self):
        raise NotImplementedError()


class Deck:
    pass

