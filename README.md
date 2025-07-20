# Word Bomb Helper

A Python tool that helps with Word Bomb by finding words containing specific character sequences.

## How it works

Enter 2-3 characters and get all words containing that sequence in order. For example, "to" finds: into, together, toward, today, etc.

## Features

- **300,000+ words** from multiple sources (vs 10,000 in original)
- **Lightning fast** O(1) search with indexing
- **Smart caching** - instant loading after first run
- **Zero duplicates** - automatic cleanup
- **Case insensitive** - works with any input

## Usage

### Enhanced Version (Recommended)
```bash
python wordbomb_enhanced.py
```

### Original Version
```bash
python wordbomb_helper.py
```

### In Your Code
```python
from wordbomb_enhanced import EnhancedWordBombHelper

helper = EnhancedWordBombHelper()
words = helper.find_words_with_sequence("to")
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