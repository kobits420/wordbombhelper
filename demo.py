from wordbomb_helper import WordBombHelper

def demo_wordbomb():
    helper = WordBombHelper()
    
    print("Word Bomb Helper Demo")
    print("=" * 50)
    
    # Example 1: "to" (as mentioned in the original request)
    print("\nExample 1: Finding words containing 'to'")
    print("-" * 40)
    words = helper.find_words_with_sequence("to")
    print(f"Found {len(words)} words containing 'to':")
    for i, word in enumerate(words[:15], 1):  # Show first 15
        print(f"  {i:2d}. {word}")
    if len(words) > 15:
        print(f"  ... and {len(words) - 15} more")
    
    # Example 2: "the" (3-character sequence)
    print("\nExample 2: Finding words containing 'the'")
    print("-" * 40)
    words = helper.find_words_with_sequence("the")
    print(f"Found {len(words)} words containing 'the':")
    for i, word in enumerate(words[:15], 1):  # Show first 15
        print(f"  {i:2d}. {word}")
    if len(words) > 15:
        print(f"  ... and {len(words) - 15} more")
    
    # Example 3: "an" (2-character sequence)
    print("\nExample 3: Finding words containing 'an'")
    print("-" * 40)
    words = helper.find_words_with_sequence("an")
    print(f"Found {len(words)} words containing 'an':")
    for i, word in enumerate(words[:15], 1):  # Show first 15
        print(f"  {i:2d}. {word}")
    if len(words) > 15:
        print(f"  ... and {len(words) - 15} more")
    
    # Example 4: "in" (2-character sequence)
    print("\nExample 4: Finding words containing 'in'")
    print("-" * 40)
    words = helper.find_words_with_sequence("in")
    print(f"Found {len(words)} words containing 'in':")
    for i, word in enumerate(words[:15], 1):  # Show first 15
        print(f"  {i:2d}. {word}")
    if len(words) > 15:
        print(f"  ... and {len(words) - 15} more")
    
    print("\n" + "=" * 50)
    print("Demo completed!")
    print("\nTo use interactively, run: python wordbomb_helper.py")

if __name__ == "__main__":
    demo_wordbomb() 