# intern_project_staxtech

Project 1

# 🔐 GUI-Based Password Generator

A customizable, GUI-based password generator built using Python and Tkinter, developed as part of my internship at **Staxtech**. This tool enables users to generate secure, random passwords with fine-grained control over character types and length.

## 📌 Features

- ✅ Customizable password length  
- 🔠 Option to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (!@#$%...)
- 📋 One-click copy to clipboard using `pyperclip`
- ⚠️ Input validation with user-friendly error messages
- 🧠 Secure password generation using `random` and `string`


## 🖥️ GUI Preview


![WhatsApp Image 2025-06-03 at 07 56 33_a826ccde](https://github.com/user-attachments/assets/9f1c13c2-f525-471d-9240-0999ddd590a6)
![WhatsApp Image 2025-06-03 at 07 57 11_4fe1cab0](https://github.com/user-attachments/assets/5d305e47-2410-4441-8409-fcbacf5d1613)
![WhatsApp Image 2025-06-03 at 07 57 58_257afac5](https://github.com/user-attachments/assets/78b56d79-2d7f-4dbe-b71d-226a18ed0818)
![WhatsApp Image 2025-06-03 at 07 58 09_1c442bcf](https://github.com/user-attachments/assets/dd4de2db-16a0-447e-9aca-a7eccc2cb39a)
![WhatsApp Image 2025-06-03 at 07 58 29_99c35695](https://github.com/user-attachments/assets/7baccc1c-6901-443d-b06b-60cb19a17ad3)
![WhatsApp Image 2025-06-03 at 07 58 43_95382d39](https://github.com/user-attachments/assets/3b81dd89-648b-4bcf-b242-e289c9b85679)
![WhatsApp Image 2025-06-03 at 07 58 58_46fdd252](https://github.com/user-attachments/assets/0bf3254a-b6d0-4bc7-a319-cfa747afd4a4)
![WhatsApp Image 2025-06-03 at 07 59 17_23df625a](https://github.com/user-attachments/assets/1e989dc4-40ee-4071-91f9-0a2ee7413f0d)
![WhatsApp Image 2025-06-03 at 07 59 29_def69d1f](https://github.com/user-attachments/assets/9b3bfda7-2959-4bc5-b30a-d6a89070c5f2)
![WhatsApp Image 2025-06-03 at 07 59 47_13993a16](https://github.com/user-attachments/assets/2f6c1c27-d560-4d94-97d9-07b569aa703a)
![WhatsApp Image 2025-06-03 at 08 01 00_e419bab9](https://github.com/user-attachments/assets/c16e9b2d-6f3f-449e-8641-22a8878f9375)


## 🚀 Technologies Used

- Python 3.x
- Tkinter (standard GUI library)
- pyperclip (for clipboard functionality)


## 🧩 Installation

1. **Clone the Repository**:
   
   https://github.com/Santhoshcoder001/intern_project_staxtech.git
  
2. **Install Required Package**:

      pip install pyperclip
   
4. **Run the Application**:

   python password_generator.py


## Example Output

User Input:

  Length: 12
  Include: Uppercase ✅, Lowercase ✅, Digits ✅, Special Characters ✅

  Generated Password:

    W$z9qK2@pM1!

PROJECT 2

# 💱 Currency Converter - Python Tkinter GUI

A simple and intuitive Currency Converter built using Python and Tkinter that converts amounts between Indian Rupee (INR) and major world currencies using static exchange rates (as of June 14, 2025). This is ideal for learning GUI development and basic financial computations.

---

## 🚀 Features

- Convert amounts between INR and:
  - USD (US Dollar)
  - EUR (Euro)
  - GBP (British Pound)
  - AUD (Australian Dollar)
  - CAD (Canadian Dollar)
  - SGD (Singapore Dollar)
  - CHF (Swiss Franc)
  - MYR (Malaysian Ringgit)
  - JPY (Japanese Yen)
  - CNY (Chinese Yuan Renminbi)
- Clean and responsive UI using Tkinter
- Handles invalid inputs gracefully

---

## 🖥️ GUI Preview

![WhatsApp Image 2025-06-14 at 06 52 53_02919475](https://github.com/user-attachments/assets/68706fa9-c272-46dc-9e9f-bc986012449f)
![WhatsApp Image 2025-06-14 at 06 53 09_23896669](https://github.com/user-attachments/assets/1c13262b-36da-4f16-8208-1076d94ad9f3)
![WhatsApp Image 2025-06-14 at 06 53 24_296f2e16](https://github.com/user-attachments/assets/82b7e667-0192-4e9c-ba98-a8e1870af076)
![WhatsApp Image 2025-06-14 at 06 53 59_26d32b14](https://github.com/user-attachments/assets/fb80a18e-5f04-4881-924c-15972d144544)

---

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **GUI Toolkit:** Tkinter (built-in)
- No external packages required

---







PROJECT 3

# 📚 Thirukkural Tamil to English Translator with NLP

A sophisticated command-line application that provides Tamil to English translations of Thirukkural verses using Natural Language Processing techniques. Built as part of the internship project at **Staxtech**, this tool offers intelligent search capabilities and comprehensive access to the ancient Tamil wisdom of Thiruvalluvar.

---

## 🌟 Features

- **Intelligent Search**: Advanced NLP-powered search using difflib for text similarity and fuzzy matching
- **Multiple Search Methods**:
  - Search by meaning/keywords (e.g., "friendship", "love", "virtue")
  - Search by specific kural number (1-1330)
  - Search by chapter names
  - Search by themes
- **Rich Content**: 
  - Original Tamil text
  - English translations
  - Detailed meanings and explanations
  - Transliteration (Tamil to English phonetics)
  - Thematic categorization
- **Interactive CLI**: User-friendly command-line interface with multiple interaction modes
- **Relevance Scoring**: Smart ranking of search results based on relevance
- **Random Inspiration**: Get random kurals for daily wisdom

---

## 🖥️ Usage Examples

### Command Line Mode:
```bash
# Get help
python thirukkural_translator.py help

# Search by keyword
python thirukkural_translator.py search friendship

# Get specific kural
python thirukkural_translator.py number 421

# Get random kural
python thirukkural_translator.py random
```

### Interactive Mode:
```bash
python thirukkural_translator.py

thirukkural> search love
thirukkural> number 391
thirukkural> theme virtue
thirukkural> random
thirukkural> chapters
thirukkural> quit
```

---

## 🧠 NLP Techniques Used

1. **Text Similarity**: Using `difflib.SequenceMatcher` for overall text similarity
2. **Fuzzy Matching**: `difflib.get_close_matches` for approximate word matching
3. **Word Indexing**: Pre-built indices for faster theme and keyword searches
4. **Relevance Scoring**: Multi-factor scoring algorithm considering:
   - Exact phrase matches
   - Individual word matches
   - Fuzzy similarity scores
   - Theme relevance
   - Word frequency

---

## 📋 Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `search <query>` | Search by meaning/keywords | `search friendship` |
| `number <num>` | Get specific kural by number | `number 421` |
| `chapter <name>` | Search by chapter name | `chapter "Praise of God"` |
| `theme <theme>` | Search by theme | `theme love` |
| `random` | Display random kural | `random` |
| `chapters` | List all chapters | `chapters` |
| `themes` | List all themes | `themes` |
| `stats` | Show database statistics | `stats` |
| `help` | Show help information | `help` |
| `quit/exit` | Exit the application | `quit` |

---

## 🛠️ Technologies Used

- **Language**: Python 3.x
- **NLP Libraries**: 
  - `difflib` (built-in) for text similarity and fuzzy matching
  - `re` (built-in) for regular expressions and text processing
  - `unicodedata` (built-in) for Unicode text handling
- **Data Structures**: Optimized indices for fast searching
- **CLI Interface**: Interactive command-line experience

---

## 📖 About Thirukkural

திருக்குறள் (Thirukkural) is a classical Tamil sangam literature consisting of 1330 short couplets (kurals) written by the ancient Tamil poet **Thiruvalluvar** around 2000 years ago. The work is divided into three main sections:

1. **Aram** (Virtue/Righteousness) - 38 chapters
2. **Porul** (Wealth/Politics) - 70 chapters  
3. **Inbam** (Love/Pleasure) - 25 chapters

Each kural contains profound wisdom about ethics, governance, economics, love, and human nature, making it one of the world's greatest works on ethics and morality.

---

## 🚀 Installation & Running

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Santhoshcoder001/intern_project_staxtech.git
   cd intern_project_staxtech
   ```

2. **Run the Application**:
   ```bash
   # Interactive mode
   python thirukkural_translator.py
   
   # Command line mode
   python thirukkural_translator.py search wisdom
   ```

---

## 📊 Sample Output

```
============================================================
Kural 421 - Chapter: Help in Trouble (#43)
============================================================

Tamil:
உடுக்கை இழந்தவன் கைபோல ஆங்கே
இடுக்கண் களைவான் நட்பு.

Transliteration:
Udukkai izhandavan kaipol aangke
Idukkan kalaivaann natpu.

English Translation:
Like a hand when the dress slips off,
Friendship should promptly help in times of distress.

Meaning:
True friendship acts as quickly as a hand that adjusts a slipping garment.

Themes: friendship help loyalty
```

---

Author
Developed by Santhosh K.R. during internship at StaxTech.

Connect on LinkedIn : https://www.linkedin.com/in/santhosh-k-r-5b4462254/ 
