import re
import urllib.request
from typing import List, Set

class WordBombHelper:
    def __init__(self):
        # Common English words dictionary
        self.words = self._load_words()
    
    def _load_words(self) -> Set[str]:
        """Load the MIT 10,000 word list."""
        # Load from MIT word list
        url = "https://www.mit.edu/~ecprice/wordlist.10000"
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            words = set(word.strip().lower() for word in content.split('\n') if word.strip())
        
        print(f"Successfully loaded {len(words)} words from MIT word list")
        return words
    
    def find_words_with_sequence(self, sequence: str) -> List[str]:
        """
        Find all words that contain the given character sequence in order.
        
        Args:
            sequence: A string of 2-3 characters to search for
            
        Returns:
            List of words containing the sequence
        """
        if not sequence or len(sequence) < 2 or len(sequence) > 3:
            raise ValueError("Sequence must be 2-3 characters long")
        
        sequence = sequence.lower()
        matching_words = []
        
        for word in self.words:
            word_lower = word.lower()
            if sequence in word_lower:
                matching_words.append(word)
        
        # Sort by length (longest first) and then alphabetically
        matching_words.sort(key=lambda x: (-len(x), x.lower()))
        return matching_words
    
    def add_custom_words(self, words: List[str]):
        """Add custom words to the dictionary."""
        for word in words:
            if isinstance(word, str) and word.strip():
                self.words.add(word.strip().lower())

def main():
    helper = WordBombHelper()
    
    print("Word Bomb Helper")
    print("Enter a 2-3 character sequence to find words containing it.")
    print("Type 'quit' to exit.")
    print()
    
    while True:
        try:
            user_input = input("Enter sequence: ").strip()
            
            if user_input.lower() == 'quit':
                break
            
            if not user_input:
                print("Please enter a sequence.")
                continue
            
            if len(user_input) < 2 or len(user_input) > 3:
                print("Please enter a sequence of 2-3 characters.")
                continue
            
            words = helper.find_words_with_sequence(user_input)
            
            if words:
                print(f"\nWords containing '{user_input}':")
                for word in words:
                    print(f"  {word}")
                print(f"\nFound {len(words)} word(s)")
            else:
                print(f"\nNo words found containing '{user_input}'")
            
            print()
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print()

if __name__ == "__main__":
    main() 