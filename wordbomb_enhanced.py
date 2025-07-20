import urllib.request
import json
import os
import pickle
from typing import List, Set, Dict, Optional
from collections import defaultdict
import time

class EnhancedWordBombHelper:
    def __init__(self, use_cache=True):
        self.cache_file = "word_cache.pkl"
        self.words = self._load_words(use_cache)
        self.word_index = self._build_word_index()
        
    def _load_words(self, use_cache=True) -> Set[str]:
        """Load words from multiple sources with caching and duplicate tracking."""
        if use_cache and os.path.exists(self.cache_file):
            print("Loading cached word list...")
            with open(self.cache_file, 'rb') as f:
                words = pickle.load(f)
            print(f"Loaded {len(words)} words from cache")
            return words
        
        print("Downloading word lists...")
        words = set()
        total_loaded = 0
        duplicates_found = 0
        
        # Multiple high-quality word sources
        word_sources = [
            "https://www.mit.edu/~ecprice/wordlist.10000",
            "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt",
            "https://raw.githubusercontent.com/words/an-array-of-english-words/master/words.json"
        ]
        
        for source in word_sources:
            try:
                print(f"Downloading from {source}...")
                with urllib.request.urlopen(source) as response:
                    content = response.read().decode('utf-8')
                    
                    source_words = set()
                    if source.endswith('.json'):
                        # Handle JSON format
                        word_list = json.loads(content)
                        source_words = {word.lower().strip() for word in word_list if word.strip()}
                    else:
                        # Handle text format
                        word_list = content.split('\n')
                        source_words = {word.lower().strip() for word in word_list if word.strip()}
                    
                    # Track duplicates
                    before_count = len(words)
                    words.update(source_words)
                    after_count = len(words)
                    new_words = after_count - before_count
                    duplicates = len(source_words) - new_words
                    
                    total_loaded += len(source_words)
                    duplicates_found += duplicates
                        
                print(f"  Source words: {len(source_words):,}")
                print(f"  New unique words: {new_words:,}")
                print(f"  Duplicates in this source: {duplicates:,}")
                print(f"  Total unique words so far: {len(words):,}")
                
            except Exception as e:
                print(f"Warning: Could not load from {source}: {e}")
        
        # Add common Word Bomb words that might be missing
        additional_words = {
            "sublimedirectory", "knowledgestorm", "administrators", "investigators",
            "photographers", "semiconductor", "contributors", "distributors",
            "introductory", "investigator", "laboratories", "photographer",
            "photographic", "authentication", "strengthening", "hypothetical",
            "mathematical", "nevertheless", "furthermore", "mathematics",
            "motherboard", "netherlands", "theoretical", "therapeutic",
            "hypothesis", "strengthen", "themselves", "thereafter",
            "organizational", "simultaneously", "transformation", "transportation",
            "announcements", "circumstances", "manufacturers", "manufacturing",
            "mediterranean", "miscellaneous", "organisations", "organizations",
            "significantly", "starsmerchant", "substantially"
        }
        
        before_count = len(words)
        words.update(additional_words)
        additional_new = len(words) - before_count
        
        print(f"\nDuplicate Summary:")
        print(f"  Total words loaded from sources: {total_loaded:,}")
        print(f"  Duplicates removed: {duplicates_found:,}")
        print(f"  Additional custom words: {len(additional_words)}")
        print(f"  New words from custom list: {additional_new}")
        print(f"  Final unique word count: {len(words):,}")
        
        # Cache the results
        if use_cache:
            with open(self.cache_file, 'wb') as f:
                pickle.dump(words, f)
            print(f"Cached {len(words)} words to {self.cache_file}")
        
        return words
    
    def _build_word_index(self) -> Dict[str, List[str]]:
        """Build an index for faster searching."""
        print("Building word index for faster searches...")
        index = defaultdict(list)
        
        for word in self.words:
            # Index by all possible 2-3 character sequences
            for i in range(len(word) - 1):
                for j in range(i + 2, min(i + 4, len(word) + 1)):
                    sequence = word[i:j]
                    if 2 <= len(sequence) <= 3:
                        index[sequence].append(word)
        
        # Remove duplicates from index (in case any slipped through)
        for sequence in index:
            index[sequence] = list(set(index[sequence]))
        
        print(f"Built index with {len(index)} sequences")
        return dict(index)
    
    def find_words_with_sequence(self, sequence: str, length_filter: Optional[int] = None) -> List[str]:
        """
        Find all words that contain the given character sequence in order.
        Uses optimized indexing for O(1) lookup.
        
        Args:
            sequence: A string of 2-3 characters to search for
            length_filter: Optional integer to filter words by exact length
            
        Returns:
            List of words containing the sequence, optionally filtered by length
        """
        if not sequence or len(sequence) < 2 or len(sequence) > 3:
            raise ValueError("Sequence must be 2-3 characters long")
        
        if length_filter is not None and (length_filter < 1 or length_filter > 50):
            raise ValueError("Length filter must be between 1 and 50")
        
        sequence = sequence.lower()
        
        # Use index for O(1) lookup instead of O(n) search
        if sequence in self.word_index:
            matching_words = self.word_index[sequence].copy()
        else:
            # Fallback to original method if not in index
            matching_words = []
            for word in self.words:
                if sequence in word.lower():
                    matching_words.append(word)
        
        # Apply length filter if specified
        if length_filter is not None:
            matching_words = [word for word in matching_words if len(word) == length_filter]
        
        # Ensure no duplicates in results
        matching_words = list(set(matching_words))
        
        # Sort by length (longest first) and then alphabetically
        matching_words.sort(key=lambda x: (-len(x), x.lower()))
        return matching_words
    
    def parse_input(self, user_input: str) -> tuple[str, Optional[int]]:
        """
        Parse user input to extract sequence and optional length filter.
        
        Args:
            user_input: String like "to" or "to 3" or "the 5"
            
        Returns:
            Tuple of (sequence, length_filter)
        """
        parts = user_input.strip().split()
        
        if not parts:
            raise ValueError("Please enter a sequence")
        
        sequence = parts[0].lower()
        
        # Check for length filter
        length_filter = None
        if len(parts) > 1:
            try:
                length_filter = int(parts[1])
                if length_filter < 1 or length_filter > 50:
                    raise ValueError("Length must be between 1 and 50")
            except ValueError:
                raise ValueError("Length filter must be a number between 1 and 50")
        
        return sequence, length_filter
    
    def get_stats(self) -> Dict:
        """Get statistics about the word database."""
        return {
            "total_words": len(self.words),
            "indexed_sequences": len(self.word_index),
            "avg_words_per_sequence": sum(len(words) for words in self.word_index.values()) / len(self.word_index) if self.word_index else 0,
            "cache_file_exists": os.path.exists(self.cache_file)
        }
    
    def add_custom_words(self, words: List[str]):
        """Add custom words to the dictionary and rebuild index."""
        for word in words:
            if isinstance(word, str) and word.strip():
                self.words.add(word.strip().lower())
        
        # Rebuild index with new words
        self.word_index = self._build_word_index()
        
        # Update cache
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.words, f)

def main():
    print("Enhanced Word Bomb Helper")
    print("=" * 50)
    
    # Initialize with caching
    start_time = time.time()
    helper = EnhancedWordBombHelper(use_cache=True)
    load_time = time.time() - start_time
    
    print(f"Initialization took {load_time:.2f} seconds")
    
    # Show stats
    stats = helper.get_stats()
    print(f"\nDatabase Statistics:")
    print(f"  Total words: {stats['total_words']:,}")
    print(f"  Indexed sequences: {stats['indexed_sequences']:,}")
    print(f"  Average words per sequence: {stats['avg_words_per_sequence']:.1f}")
    print(f"  Using cache: {stats['cache_file_exists']}")
    
    print("\nEnter a 2-3 character sequence to find words containing it.")
    print("Add a number to filter by length (e.g., 'to 3' for 3-letter words).")
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
            
            # Parse input for sequence and length filter
            try:
                sequence, length_filter = helper.parse_input(user_input)
            except ValueError as e:
                print(f"Error: {e}")
                continue
            
            if len(sequence) < 2 or len(sequence) > 3:
                print("Please enter a sequence of 2-3 characters.")
                continue
            
            # Time the search
            start_time = time.time()
            words = helper.find_words_with_sequence(sequence, length_filter)
            search_time = time.time() - start_time
            
            # Build display message
            if length_filter:
                display_msg = f"Words containing '{sequence}' with length {length_filter}"
            else:
                display_msg = f"Words containing '{sequence}'"
            
            if words:
                print(f"\n{display_msg} (found in {search_time:.3f}s):")
                for word in words:
                    print(f"  {word}")
                print(f"\nFound {len(words)} word(s)")
            else:
                print(f"\nNo words found for {display_msg}")
            
            print()
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print()

if __name__ == "__main__":
    main() 