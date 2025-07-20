from wordbomb_helper import WordBombHelper

def test_wordbomb_helper():
    helper = WordBombHelper()
    
    # Test with the example provided: "to"
    print("Testing with sequence 'to':")
    words = helper.find_words_with_sequence("to")
    print(f"Found {len(words)} words:")
    for word in words[:10]:  # Show first 10 results
        print(f"  {word}")
    if len(words) > 10:
        print(f"  ... and {len(words) - 10} more")
    print()
    
    # Test with a 3-character sequence
    print("Testing with sequence 'the':")
    words = helper.find_words_with_sequence("the")
    print(f"Found {len(words)} words:")
    for word in words[:10]:  # Show first 10 results
        print(f"  {word}")
    if len(words) > 10:
        print(f"  ... and {len(words) - 10} more")
    print()
    
    # Test with another 2-character sequence
    print("Testing with sequence 'an':")
    words = helper.find_words_with_sequence("an")
    print(f"Found {len(words)} words:")
    for word in words[:10]:  # Show first 10 results
        print(f"  {word}")
    if len(words) > 10:
        print(f"  ... and {len(words) - 10} more")
    print()

if __name__ == "__main__":
    test_wordbomb_helper() 