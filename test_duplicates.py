from wordbomb_enhanced import EnhancedWordBombHelper

def test_duplicate_handling():
    print("Testing Duplicate Handling in Enhanced Word Bomb Helper")
    print("=" * 60)
    
    # Test with a small sample to verify duplicate removal
    helper = EnhancedWordBombHelper(use_cache=False)  # Force fresh load
    
    # Check for duplicates in the final word set
    word_list = list(helper.words)
    word_set = set(helper.words)
    
    print(f"Total words loaded: {len(word_list)}")
    print(f"Unique words after deduplication: {len(word_set)}")
    print(f"Duplicates removed: {len(word_list) - len(word_set)}")
    
    # Test specific sequences to see results
    test_sequences = ["to", "the", "an", "in"]
    
    for sequence in test_sequences:
        words = helper.find_words_with_sequence(sequence)
        unique_words = set(words)
        
        print(f"\nSequence '{sequence}':")
        print(f"  Total results: {len(words)}")
        print(f"  Unique results: {len(unique_words)}")
        print(f"  Duplicates in results: {len(words) - len(unique_words)}")
        
        # Show first few results
        print(f"  Sample results: {words[:5]}")
    
    # Test case sensitivity handling
    print(f"\nCase Sensitivity Test:")
    print(f"  'TO' in words: {'TO' in helper.words}")
    print(f"  'to' in words: {'to' in helper.words}")
    print(f"  'To' in words: {'To' in helper.words}")
    
    # Test whitespace handling
    print(f"\nWhitespace Test:")
    print(f"  '  to  ' in words: {'  to  ' in helper.words}")
    print(f"  'to' in words: {'to' in helper.words}")

if __name__ == "__main__":
    test_duplicate_handling() 