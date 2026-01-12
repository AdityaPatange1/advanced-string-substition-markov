# 🕉️ Manipuraka Text Tools

A tiny toolkit for text transformation and content safety.

## ✨ What's Inside

**assm.py** - Content moderation helper that redacts sensitive terms (multilingual!).
- Supports English, Hindi, Urdu, Spanish, French, German, Italian, Russian, Turkish & more.
- Replaces flagged content with `[REDACTED_SV]`.

**llmmprktxblst.sh** - Fun text transformer.
- Replaces words with random Sanskrit/Chakra terms.
- 117 spiritual words like Kundalini, Chakra, Prana, Shakti.

## 🚀 Quick Start

```bash
# Create virtual environment
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt

# Run the content filter
python assm.py -i input.txt -o output.txt

# Run the text blaster
chmod +x llmmprktxblst.sh
./llmmprktxblst.sh
```

## 📝 Requirements

- Python 3.12+.
- regex library.

## 📜 License

MPL-2.0.

---
*Powered by Sadhguru Shri Brahma.* 🙏
