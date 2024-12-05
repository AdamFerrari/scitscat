import random
from cards import get_card_name
from player import Player

class Game:
    def __init__(self, num_players):
        """
        Initialize game state with specified number of players
        """
        if num_players < 2:
            raise ValueError("Game requires at least 2 players")
            
        # Initialize deck (0-51)
        self.deck = list(range(52))
        random.shuffle(self.deck)
        
        # Initialize empty discard pile
        self.discard_pile = []
        
        # Initialize players
        self.players = [Player() for _ in range(num_players)]
        
        # Deal initial hands
        self._deal_initial_hands()
        
        # Add first card to discard pile
        self.discard_pile.append(self.deck.pop())
    
    def _deal_initial_hands(self):
        """Deal 3 cards to each player"""
        for _ in range(3):
            for player in self.players:
                player.add_card(self.deck.pop())
    
    def get_top_discard(self):
        """Return the top card of the discard pile without removing it"""
        if not self.discard_pile:
            raise ValueError("Discard pile is empty")
        return self.discard_pile[-1]
    
    def draw_from_deck(self):
        """Draw and return a card from the deck"""
        if not self.deck:
            # If deck is empty, shuffle discard pile (except top card) to create new deck
            if len(self.discard_pile) <= 1:
                raise ValueError("No cards available to draw")
            
            top_discard = self.discard_pile.pop()
            self.deck = self.discard_pile
            self.discard_pile = [top_discard]
            random.shuffle(self.deck)
            
        return self.deck.pop()
    
    def draw_from_discard(self):
        """Draw and return a card from the discard pile"""
        if not self.discard_pile:
            raise ValueError("Discard pile is empty")
        return self.discard_pile.pop()
    
    def add_to_discard(self, card):
        """Add a card to the discard pile"""
        self.discard_pile.append(card)
    
    def __str__(self):
        """String representation of the game state"""
        game_str = f"Game State:\n"
        game_str += f"Cards in deck: {len(self.deck)}\n"
        game_str += f"Top discard: {get_card_name(self.get_top_discard())}\n"
        for i, player in enumerate(self.players):
            game_str += f"Player {i + 1}: {player}\n"
        return game_str
    
    def play_game(self):
        """
        Start the game loop, allowing players to take turns picking up and discarding cards
        """
        current_player = 0
        
        while True:
            player = self.players[current_player]
            print(f"\nPlayer {current_player + 1}'s turn")
            print(player)
            print(f"Top of discard pile: {get_card_name(self.get_top_discard())}")
            
            # Get pickup choice
            while True:
                choice = input("Pick up from (t)op of deck or (d)iscard pile? ").lower()
                if choice in ['t', 'd']:
                    break
                print("Invalid choice. Please enter 't' or 'd'")
            
            # Handle pickup
            if choice == 't':
                card = self.draw_from_deck()
                print(f"Drew {get_card_name(card)}")
                player.pickup(card)
            else:
                card = self.draw_from_discard()
                print(f"Drew {get_card_name(card)}")
                player.pickup(card)
                
            print(player)
            
            # Get discard choice
            while True:
                choice = input("Discard which card? (0-2 for hand, p for pickup): ").lower()
                if choice in ['0', '1', '2', 'p']:
                    break
                print("Invalid choice. Please enter '0', '1', '2', or 'p'")
            
            # Handle discard
            try:
                if choice == 'p':
                    discarded = player.discard_pickup()
                else:
                    discarded = player.discard(int(choice))
                
                print(f"Discarded: {get_card_name(discarded)}")
                self.add_to_discard(discarded)
                
            except ValueError as e:
                print(f"Error: {e}")
                continue
                
            print(player)
            
            # Move to next player
            current_player = (current_player + 1) % len(self.players)


# Example usage:
if __name__ == "__main__":
    # Create a game with 2 players
    game = Game(2)
    print("Initial game state:")
    print(game)
    
    # Start the game loop
    game.play_game() 