import unittest
import game

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player1 = game.Player(1)
        self.player2 = game.Player(2)

    def test_id(self):
        self.assertEqual(self.player1.pid, 1) 

    def test_sell(self):
        self.player1.gems = [0,0,0]
        self.assertEqual(self.player1.sell(), 3)
        

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = game.Deck()
        
    def test_give(self):
        cards = self.deck.give(5)
        self.assertEqual(len(cards), 5) 

    def test_give_too_much(self):
        cards = self.deck.give(500)
        self.assertEqual(len(cards), 0) 





if __name__ == '__main__':
    unittest.main()