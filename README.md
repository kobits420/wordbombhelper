# Word Bomb Helper

A Python tool that helps with Word Bomb by finding words containing specific character sequences.

## How it works

Enter 2-3 characters and get all words containing that sequence in order. For example, "to" finds: into, together, toward, today, etc.

**New: Add a number to filter by length!** Try "to 3" for only 3-letter words.

## Features

- **300,000+ words** from multiple sources (vs 10,000 in original)
- **Length filtering** - specify exact word length (e.g., "to 3")
- **Lightning fast** O(1) search with indexing
- **Smart caching** - instant loading after first run
- **Zero duplicates** - automatic cleanup
- **Case insensitive** - works with any input

## Usage

### Enhanced Version (Recommended)
```bash
python wordbomb_enhanced.py
```

### Length Filtering Examples
```
to        # All words containing "to"
to 3      # Only 3-letter words containing "to"
the 5     # Only 5-letter words containing "the"
an 7      # Only 7-letter words containing "an"
```

### Original Version
```bash
python wordbomb_helper.py
```

### In Your Code
```python
from wordbomb_enhanced import EnhancedWordBombHelper

helper = EnhancedWordBombHelper()
words = helper.find_words_with_sequence("to", 3)  # 3-letter words only
print(words)
```

## Performance

| Feature | Original | Enhanced |
|---------|----------|----------|
| Words | 10,000 | 300,000+ |
| Speed | O(n) | O(1) |
| Search Time | ~0.3s | ~0.001s |

## Files

- `wordbomb_enhanced.py` - **Enhanced version** (Recommended)
- `wordbomb_helper.py` - Original version
- `demo_length_filter.py` - Length filtering examples
- `demo.py` - See it in action
- `test_duplicates.py` - Verify no duplicates

## Requirements

- Python 3.6+
- Internet connection (first run only)
- ~50MB disk space

## Word Sources

Combines multiple word lists automatically:
- MIT 10,000 word list
- GitHub English words (466k+)
- Custom Word Bomb terms

The tool downloads everything once, caches it locally, and removes duplicates automatically. 