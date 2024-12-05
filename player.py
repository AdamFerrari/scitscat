from cards import get_suit, get_card_value, get_card_name

class Player:
    def __init__(self):
        """Initialize a player with an empty hand and no pickup card"""
        self.hand = []
        self.pickup_card = None
    
    def add_card(self, card):
        """
        Add a card to the player's hand and sort the hand in ascending order
        """
        if len(self.hand) >= 3:
            raise ValueError("Cannot add more than 3 cards to hand")
        self.hand.append(card)
        self.hand.sort()  # Sort cards in ascending order
    
    def get_hand_value(self):
        """
        Calculate the highest sum of cards of the same suit in the player's hand.
        Returns 0 if hand is empty.
        """
        if not self.hand:
            return 0
            
        # Create a dictionary to store sum of values for each suit
        suit_sums = {'Hearts': 0, 'Diamonds': 0, 'Clubs': 0, 'Spades': 0}
        
        # Calculate sum for each suit
        for card in self.hand:
            suit = get_suit(card)
            value = get_card_value(card)
            suit_sums[suit] += value
        
        # Return the highest suit sum
        return max(suit_sums.values())

    def __str__(self):
        """String representation of the player's hand and pickup card"""
        if not self.hand:
            return "Empty hand"
        
        hand_str = "Hand: "
        for card in self.hand:
            hand_str += f"[{get_card_name(card)}] "
        if self.pickup_card is not None:
            hand_str += f"\nPickup: [{get_card_name(self.pickup_card)}]"
        hand_str += f"\n(Value: {self.get_hand_value()})"
        return hand_str

    def discard(self, index):
        """
        Remove and return a card at the specified index (0, 1, or 2).
        If there's a pickup card, it will replace the discarded card in the hand.
        """
        if index not in [0, 1, 2]:
            raise ValueError("Index must be 0, 1, or 2")
        if index >= len(self.hand):
            raise ValueError("No card at specified index")
        
        discarded = self.hand.pop(index)
        
        # If there's a pickup card, add it to the hand
        if self.pickup_card is not None:
            self.add_card(self.pickup_card)
            self.pickup_card = None
        
        return discarded

    def discard_pickup(self):
        """
        Discard the pickup card instead of a card from hand.
        Returns the pickup card and clears it.
        """
        if self.pickup_card is None:
            raise ValueError("No pickup card to discard")
        
        discarded = self.pickup_card
        self.pickup_card = None
        return discarded

    def pickup(self, card):
        """Set the pickup card for this turn"""
        if self.pickup_card is not None:
            raise ValueError("Already have a pickup card")
        self.pickup_card = card


# Example usage:
if __name__ == "__main__":
    # Create a player and test with some cards
    player = Player()
    
    # Test case 1: 2 of hearts, 3 of hearts, 10 of clubs
    test_cards = [0, 1, 34]  # Using our card representation
    
    for card in test_cards:
        player.add_card(card)
    
    print("Initial state:")
    print(player)
    
    # Pick up a card
    player.pickup(12)  # Pick up Ace of Hearts
    print("\nAfter pickup:")
    print(player)
    
    # Discard from hand and automatically add pickup to hand
    print("\nDiscarding index 1 (with pickup):")
    discarded = player.discard(1)
    print(f"Discarded: {get_card_name(discarded)}")
    print(player)
    
    # Pick up another card and discard it
    player.pickup(25)  # Pick up some card
    print("\nAfter new pickup:")
    print(player)
    print("\nDiscarding pickup card:")
    discarded = player.discard_pickup()
    print(f"Discarded: {get_card_name(discarded)}")
    print(player)