import random
suits = ('Hearts', 'Clever', 'Diamond', 'Spade')
ranks = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = ranks[rank]
    
    def __str__(self):
        return '{} of {}'.format(self.rank,self.suit)

class Deck:
    
    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                new_card = Card(rank, suit)
                self.deck.append(new_card)
        
    def __str__(self):
        
        return '{}'.format(self.deck)
    
    def shuffle_deck(self):

        random.shuffle(self.deck)
        
    def grab_card(self):
        
        return self.deck.pop()
    
    def show_card(self, cards, name):
        print('{} cards:'.format(name))
        total = 0
        for index, card in enumerate(cards):
            print('card {}: {}'.format(index, card))
            total = total + card.value
        print('Sum: {}'.format(total))
            
    def show_dealer_card(self,cards):
        print('Dealer cards:')
        for index, card in enumerate(cards):
            if index == 0:
                print('card {}: (hidden)'.format(index))
            else:
                print('card {}: {}\n'.format(index, card))
    
class Dealer:
    
    def __init__(self):
        
        self.cards = []
        self.decision = ''
        
    def take_decision(self):
        
        if sum([x.value for x in self.cards]) <= 17:
            return 'hit'
        
        else:
            return 'stand'

class Player:
    
    def __init__(self, name):
        
        self.name = name
        self.cards = []
        self.money = 1000
        self.bet = 0
        self.decision = 'hit'
        
    def bet_money(self):
        
        self.bet = input
    
    def take_decision(self):
        
        decision = input('What you like to do?(Type "hit" or "stand"): ')
        
        if decision == 'hit' or decision == 'HIT' or decision == 'Hit':
            return 'hit'
        
        elif decision == 'stand' or decision == 'STAND' or decision == 'Stand':
            return 'stand'
        
        else:
            self.take_decision()

game_on = True

while game_on == True:
    
    print('\t----------> Black Jack Starts <-----------\n')
    
    name = input('Please enter your name(or Type "exit" to quit):')

    if name == 'exit' or name == 'Exit' or name == 'EXIT':
        game_on = False
        quit()

    else:
        game_on = True
    
    # Dealer creation
    
    dealer = Dealer()
    
    # Deck creation
    
    deck = Deck()
    deck.shuffle_deck()
    
    # Player Creation
    
    player = Player(name)
    
    # Bet
    
    player.bet = int(input('How much you like to bet?(Your money: {0}) '.format(player.money)))
    print('You bets: {}'.format(player.bet))
    print('Dealer bets: {}'.format(player.bet))
    
    # First round
    
    player.cards.append(deck.grab_card())
    dealer.cards.append(deck.grab_card())
    
    player.cards.append(deck.grab_card())
    dealer.cards.append(deck.grab_card())
    
    while True:
    
        # Show cards

        deck.show_dealer_card(dealer.cards)
        deck.show_card(player.cards, player.name)

        # Ask for decision
        
        if(sum([x.value for x in player.cards]) < 21):

            player.decision = player.take_decision()

            if player.decision == 'stand':

                dealer.decision = dealer.take_decision()

                while dealer.decision == 'hit' and sum([x.value for x in dealer.cards]):
                    
                    dealer.cards.append(deck.grab_card())
                    continue    
                
                deck.show_card(dealer.cards,player.name)
                deck.show_card(player.cards,name='Dealer')
                    
                if sum([x.value for x in dealer.cards]) > 21:
                        
                    player.money = player.money + player.bet
                    print('{} Won!!! Dealer bust!!! Your money: {}'.format(player.name, player.money))
                    break

                elif sum([x.value for x in player.cards]) > 21:

                    player.money = player.money - player.bet
                    print('{} Lost!!! Dealer won!!! Your money: {}'.format(player.name, player.money))
                    break
                    
                elif sum([x.value for x in dealer.cards]) < sum([x.value for x in player.cards]):
                        
                    player.money = player.money + player.bet
                    print('{} Won!!! Dealer lost!!! Your money: {}'.format(player.name, player.money))
                    break
                        
                else:
                        
                    player.money = player.money - player.bet
                    print('{} Lost!!! Dealer won!!! Your money: {}'.format(player.name, player.money))
                    break

            else:
                
                player.cards.append(deck.grab_card())
                continue
                            
        elif(sum([x.value for x in player.cards]) == 21):

            if(sum([x.value for x in dealer.cards]) == 21):

                deck.show_card(player.cards, player.name)
                deck.show_card(dealer.cards, name='Dealer')
                print('<------------Match draw--------------->\n')
                print('{} Money: {}'.format(player.name,player.money))
                break
            
            else:

                deck.show_card(player.cards, player.name)
                deck.show_card(dealer.cards, name='Dealer')
                print('<------------ {} WON --------------->\n',player.name)
                print('{} Money: {}'.format(player.name, player.money+player.bet))
                break

        else:
            
            if(sum([x.value for x in dealer.cards]) > 21):
            
                deck.show_card(player.cards, player.name)
                deck.show_card(dealer.cards, name='Dealer')
                print('<------------Match draw--------------->\n')
                print('{} Money: {}'.format(player.name,player.money))
                break
            
            else:

                deck.show_card(player.cards, player.name)
                deck.show_card(dealer.cards, name='Dealer')
                print('<------------ Dealer WON --------------->\n')
                print('{} Money: {}'.format(player.name, player.money-player.bet))
                break