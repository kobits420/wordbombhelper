from wordbomb_enhanced import EnhancedWordBombHelper

def demo_length_filter():
    print("Word Bomb Helper - Length Filter Demo")
    print("=" * 50)
    
    helper = EnhancedWordBombHelper(use_cache=True)
    
    # Example searches with length filters
    examples = [
        ("to", None, "All words containing 'to'"),
        ("to", 3, "3-letter words containing 'to'"),
        ("to", 4, "4-letter words containing 'to'"),
        ("to", 5, "5-letter words containing 'to'"),
        ("the", None, "All words containing 'the'"),
        ("the", 4, "4-letter words containing 'the'"),
        ("the", 6, "6-letter words containing 'the'"),
        ("an", None, "All words containing 'an'"),
        ("an", 3, "3-letter words containing 'an'"),
        ("an", 7, "7-letter words containing 'an'"),
    ]
    
    for sequence, length_filter, description in examples:
        print(f"\n{description}:")
        print("-" * 40)
        
        words = helper.find_words_with_sequence(sequence, length_filter)
        
        if words:
            print(f"Found {len(words)} word(s):")
            for word in words[:10]:  # Show first 10
                print(f"  {word}")
            if len(words) > 10:
                print(f"  ... and {len(words) - 10} more")
        else:
            print("No words found")
    
    print(f"\n" + "=" * 50)
    print("Length filtering is perfect for Word Bomb when you need specific word lengths!")
    print("Try: 'to 3', 'the 5', 'an 7', etc.")

if __name__ == "__main__":
    demo_length_filter() 