# Constants for suits and special card names
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
SPECIAL_CARDS = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

def get_suit(card):
    """
    Get the suit of a card (0-51)
    Returns one of: 'Hearts', 'Diamonds', 'Clubs', 'Spades'
    """
    return SUITS[card // 13]

def get_card_name(card):
    """
    Get the full name of a card (e.g., "Ace of Hearts")
    """
    # Get the face value (2-14)
    face_value = (card % 13) + 2
    
    if face_value in SPECIAL_CARDS:
        name = SPECIAL_CARDS[face_value]
    else:
        name = str(face_value)
    
    return f"{name} of {get_suit(card)}"

def get_card_value(card):
    """
    Get the game value of a card:
    - Number cards (2-10): face value
    - Face cards (Jack, Queen, King): 10
    - Ace: 11
    """
    face_value = (card % 13) + 2
    
    # Ace is worth 11
    if face_value == 14:  # Ace (14)
        return 11
    # Face cards are worth 10
    elif face_value > 10:  # Jack (11), Queen (12), King (13)
        return 10
    # Number cards are worth their face value
    else:
        return face_value

# Example usage:
if __name__ == "__main__":
    # Test with a few cards
    test_cards = [0, 12, 13, 50]  # 2 of Hearts, Ace of Hearts, 2 of Diamonds, King of Spades
    
    for card in test_cards:
        print(f"Card {card}:")
        print(f"Name: {get_card_name(card)}")
        print(f"Suit: {get_suit(card)}")
        print(f"Value: {get_card_value(card)}")
        print() 