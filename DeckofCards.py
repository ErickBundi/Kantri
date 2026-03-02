import random


class Card:
    """A class to represent a playing card with rank and suit properties."""
    
    def __init__(self, rank, suit):
        """
        Initialize a Card object.
        
        Args:
            rank (str): The rank of the card (A, 2-10, J, Q, K)
            suit (str): The suit of the card (Hearts, Diamonds, Clubs, Spades)
        """
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        """Return string representation of the card."""
        return f"{self.rank} of {self.suit}"


class Deck:
    """A class to represent a deck of playing cards."""
    
    def __init__(self):
        """Initialize a Deck with all 52 cards."""
        self.deck = []
        self.dealt_cards = []
        self._create_deck()
    
    def _create_deck(self):
        """Create a standard 52-card deck."""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
    
    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)
    
    def deal(self, num_cards):
        """
        Deal cards from the deck.
        
        Args:
            num_cards (int): The number of cards to deal
            
        Returns:
            list: A list of Card objects dealt to the player
        """
        dealt = []
        
        # Deal cards from the deck
        for _ in range(num_cards):
            if len(self.deck) > 0:
                card = self.deck.pop()
                dealt.append(card)
                self.dealt_cards.append(card)
            else:
                print("Not enough cards left in the deck!")
                break
        
        return dealt
    
    def get_remaining_cards(self):
        """
        Get the number of cards remaining in the deck.
        
        Returns:
            int: The number of cards left in the deck
        """
        return len(self.deck)
    
    def get_dealt_count(self):
        """
        Get the number of cards that have been dealt.
        
        Returns:
            int: The number of cards dealt
        """
        return len(self.dealt_cards)


def main():
    """Main function to run the Card Dealer program."""
    print("Card Dealer")
    print("I have shuffled a deck of 52 cards.\n")
    
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()
    
    while True:
        try:
            # Get number of cards user wants
            num_cards = int(input("How many cards would you like? "))
            
            # Validate input
            if num_cards <= 0:
                print("Please enter a positive number.")
                continue
            
            if num_cards > deck.get_remaining_cards():
                print(f"There are only {deck.get_remaining_cards()} cards left in the deck.")
                continue
            
            # Deal the cards
            print("\nHere are your cards:")
            dealt_cards = deck.deal(num_cards)
            
            for card in dealt_cards:
                print(f"  {card}")
            
            # Display remaining cards
            remaining = deck.get_remaining_cards()
            print(f"\nThere are {remaining} cards left in the deck.\n")
            
            # Ask if user wants to continue
            while True:
                continue_choice = input("Good luck!\nWant to continue...? ")
                
                if continue_choice.lower().strip() in ['y', 'yes', 'n', 'no']:
                    break
                else:
                    # If they just press enter or give unclear input, continue asking
                    if continue_choice.lower().strip() in ['y', 'n']:
                        break
            
            if continue_choice.lower().strip() in ['n', 'no']:
                print("\nThanks for playing!")
                break
        
        except ValueError:
            print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
