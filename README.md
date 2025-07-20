# Word Bomb Helper

A Python tool that helps with the game Word Bomb by finding words containing specific character sequences.

## How it works

The Word Bomb Helper takes a string of 2-3 characters and finds all words in its dictionary that contain that sequence of characters in order. For example, if you input "to", it will find words like:
- into
- together  
- toward
- today
- tomorrow
- and many more

The characters must stay together in the same order within the word.

## Features

- **MIT 10,000 Word List**: Uses the comprehensive MIT word list for excellent coverage
- **Automatic Loading**: Downloads the word list automatically from MIT's server
- **Sequence Matching**: Finds words where the characters stay together in order
- **Smart Sorting**: Results sorted by length (longest first), then alphabetically
- **Case Insensitive**: Works with any case input
- **Error Handling**: Validates input length and handles errors gracefully
- **Extensible**: Can add custom words to the dictionary

## Usage

### Interactive Mode
Run the main script to use the helper interactively:

```bash
python wordbomb_helper.py
```

Then enter 2-3 character sequences when prompted.

### Programmatic Usage
You can also use the helper in your own Python code:

```python
from wordbomb_helper import WordBombHelper

helper = WordBombHelper()
words = helper.find_words_with_sequence("to")
print(words)
```

### Testing
Run the test script to see examples:

```bash
python test_wordbomb.py
```

### Demo
Run the comprehensive demo:

```bash
python demo.py
```

## Word List

The helper uses the MIT 10,000 word list (https://www.mit.edu/~ecprice/wordlist.10000) which provides:
- 10,000 common English words
- Excellent coverage for Word Bomb games
- Automatic download on first run

## Requirements

- Python 3.6+
- Internet connection (for word list download)

## Files

- `wordbomb_helper.py` - Main helper class and interactive interface
- `test_wordbomb.py` - Test script with examples
- `demo.py` - Comprehensive demonstration with multiple examples
- `README.md` - This documentation file 