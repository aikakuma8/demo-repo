import random
# Card, Deck and Hand classes, each for different concept

class Card: 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self): # this method is called when printing the object from this class 
        return f"{self.rank["rank"]} of {self.suit}"
class Deck: 
    def __init__(self):
        self.cards = [] #attribute associated with instance of class Deck
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11}, 
            {"rank": "2", "value": 2}, 
            {"rank": "3", "value": 3}, 
            {"rank": "4", "value": 4}, 
            {"rank": "5", "value": 5}, 
            {"rank": "6", "value": 6}, 
            {"rank": "7", "value": 7}, 
            {"rank": "8", "value": 8}, 
            {"rank": "9", "value": 9}, 
            {"rank": "10", "value": 10}, 
            {"rank": "J", "value": 10}, 
            {"rank": "Q", "value": 10}, 
            {"rank": "K", "value": 10}, 
        ]

        for suit in suits: 
            for rank in ranks: 
                self.cards.append(Card(suit, rank))

    def shuffle(self): 
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, n: int): 
        result = []
        for x in range(n):
            if len(self.cards) > 0:
                result.append(self.cards.pop())
        return result

class Hand: 
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    def add_card(self, card_list): 
        self.cards.extend(card_list)

    def calculate_value(self): 
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.rank["rank"] == "A": has_ace = True
            self.value += int(card.rank["value"])
        
        if has_ace and self.value > 21: 
            self.value -= 10 # setting A's value to 1 instead of 11

    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self): 
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards = False): 
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for idx, card in enumerate(self.cards):
            if self.dealer and idx == 0 \
                and not show_all_dealer_cards \
                    and not self.is_blackjack():  
                print("hidden")
                continue
            print(card)
        if not self.dealer: 
            print("Value:", self.get_value())
        print()

class Game: 
    # def __init__(self):
    #     pass
    def check_winner(self, player_hand: Hand, dealer_hand: Hand, game_over = False): 
        if not game_over:
            if player_hand.get_value() > 21: 
                print("You busted! Dealer wins")
                return True
            elif dealer_hand.get_value() > 21: 
                print("Dealer busted! You win")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack(): 
                print("Both players have a blackjack! Tie")
                return True
            elif dealer_hand.is_blackjack(): 
                print("Dealer has blackjack! Dealer wins")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack! You win")
                return True
        else: 
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie!")
            else:
                print("Dealer wins")
            return True
        return False
    
    def play(self): 
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try: 
                games_to_play = int(input("How many games do you want to play? "))
            except ValueError: 
                print("Please input a number")

        while game_number < games_to_play: 
            game_number += 1
            deck = Deck()
            deck.shuffle()  

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2): 
                dealer_hand.add_card(deck.deal(1))
                player_hand.add_card(deck.deal(1))
            
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

            dealer_hand.display()
            player_hand.display()

            if self.check_winner(player_hand=player_hand, dealer_hand=dealer_hand): 
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]: 
                choice = input("Please choose 'Hit' or 'Stand' (or H/S): ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]: 
                    choice = input("Please choose 'Hit' or 'Stand' (or H/S): ").lower()
                    print()
                if choice in ["h", "hit"]: 
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
                    
            if self.check_winner(player_hand=player_hand, dealer_hand=dealer_hand): 
                continue

            player_value = player_hand.get_value()
            dealer_value = dealer_hand.get_value()

            while dealer_value < 17: 
                dealer_hand.add_card(deck.deal(1))
                dealer_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand=player_hand, dealer_hand=dealer_hand): 
                continue

            print("Final Results")

            print("Your hand is ", player_value)
            print("Dealer's hand is ", dealer_value)
            self.check_winner(player_hand=player_hand, dealer_hand=dealer_hand, game_over= True)
            print("\nThanks for playing")

g = Game()
g.play()


# hand = Hand()
# hand.add_card(deck.deal(2))
# hand.display()