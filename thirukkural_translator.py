#!/usr/bin/env python3
"""
Thirukkural Tamil to English Translator
Command-line version with Natural Language Processing features

This application provides English translations for Thirukkural verses
and includes intelligent search capabilities using NLP techniques.
"""

import re
import difflib
import random
import json
import sys

class ThirukuralCLITranslator:
    def __init__(self):
        """Initialize the Thirukkural translator with sample data."""
        # Sample Thirukkural data - in a full implementation, this would be loaded from a database
        self.kurals_data = {
            1: {
                "tamil": "அகர முதல எழுத்தெல்லாம் ஆதி\nபகவன் முதற்றே உலகு.",
                "english": "A is the beginning of all letters;\nEven so, God is the beginning of all worlds.",
                "transliteration": "Akara mudhal ezhuttellaam aadhi\nBhagavan mutrre ulagu.",
                "chapter": "Praise of God",
                "chapter_num": 1,
                "meaning": "Just as the letter 'A' is the first of all letters, God is the first of all worlds.",
                "theme": "spirituality"
            },
            2: {
                "tamil": "கற்றதனால் ஆய பயனென்கொல் வாலறிவன்\nநற்றாள் தொழாஅர் எனின்.",
                "english": "What use is learning's end achieved\nIf one does not worship the feet of the good Lord?",
                "transliteration": "Katradhanaal aaya payanenkol vaalariwan\nNatraal thozhaarar enin.",
                "chapter": "Praise of God", 
                "chapter_num": 1,
                "meaning": "What is the use of all learning if one does not worship God?",
                "theme": "education spirituality"
            },
            3: {
                "tamil": "மலர்மிசை ஏகினான் மாணடி சேர்ந்தார்\nநிலமிசை நீடுவாழ் வார்.",
                "english": "Those who join the beautiful feet of Him who walks on flowers\nWill live long and flourish on earth.",
                "transliteration": "Malarmisai eeginan maanadi seerndaar\nNilamisai needuvaazh vaar.",
                "chapter": "Praise of God",
                "chapter_num": 1,
                "meaning": "Those who worship God will live prosperously on earth.",
                "theme": "spirituality prosperity"
            },
            10: {
                "tamil": "பிறவிப் பெருங்கடல் நீந்துவர் நீந்தார்\nஇறைவன் அடி சேராதார்.",
                "english": "They who reach the feet of God will cross\nThe great sea of birth; others will not cross.",
                "transliteration": "Piravip perungadal neenduvar neendaar\nIraivan adi seeraadhaar.",
                "chapter": "Praise of God",
                "chapter_num": 1,
                "meaning": "Only those who surrender to God can cross the ocean of births and deaths.",
                "theme": "spirituality liberation"
            },
            391: {
                "tamil": "இன்னாசெய் தாரை ஒறுத்தல் அவர்நாண\nநன்னயம் செய்து விடல்.",
                "english": "The best way to punish those who do evil\nIs to put them to shame by doing good to them.",
                "transliteration": "Innaasey dhaarai oruttal avarnana\nNannayam seydhu vidal.",
                "chapter": "Not Doing Evil",
                "chapter_num": 40,
                "meaning": "The best revenge against those who harm you is to do good to them and make them feel ashamed.",
                "theme": "ethics forgiveness goodness"
            },
            421: {
                "tamil": "உடுக்கை இழந்தவன் கைபோல ஆங்கே\nஇடுக்கண் களைவான் நட்பு.",
                "english": "Like a hand when the dress slips off,\nFriendship should promptly help in times of distress.",
                "transliteration": "Udukkai izhandavan kaipol aangke\nIdukkan kalaivaann natpu.",
                "chapter": "Help in Trouble",
                "chapter_num": 43,
                "meaning": "True friendship acts as quickly as a hand that adjusts a slipping garment.",
                "theme": "friendship help loyalty"
            },
            621: {
                "tamil": "அன்பிற் சிறப்பு ஒழியார் செம்மாந்து\nநன்றி பயப்பார் மக.",
                "english": "Those who show affection and live righteously\nWill never lose their excellence and will do good to others.",
                "transliteration": "Anbir sirappu ozhiyaar semmaandhu\nNandri payappaar maka.",
                "chapter": "Love",
                "chapter_num": 63,
                "meaning": "People who live with love and righteousness never lose their greatness.",
                "theme": "love righteousness virtue"
            },
            761: {
                "tamil": "அறன்எனப் பட்டது எல்லாம் உயிர்நிலை\nமறந்து யவர்க்குச் செயின்.",
                "english": "All that is called virtue consists in\nForgetting one's own life for the sake of others.",
                "transliteration": "Aranena pattadhu ellaam uyirnilai\nMarandhu avarkkuch seyin.",
                "chapter": "Righteousness",
                "chapter_num": 77,
                "meaning": "True righteousness is in sacrificing oneself for the welfare of others.",
                "theme": "virtue sacrifice righteousness"
            },
            850: {
                "tamil": "செவ்வியான் செய்த உதவி நெஞ்சத்து\nநிற்றல் நிறுத்தலிற் கூற்று.",
                "english": "The help done by a perfect person\nStands firm in the heart, harder to remove than death.",
                "transliteration": "Sevviyaan seydha udhavi nenjattu\nNitral niruttalir kootru.",
                "chapter": "Gratitude",
                "chapter_num": 85,
                "meaning": "Good deeds done by noble people remain permanently etched in our hearts.",
                "theme": "gratitude kindness memory"
            },
            1330: {
                "tamil": "இன்பம் விழையார் இடும்பைகள் செய்து\nஅன்பொடு ஆற்றும் மக.",
                "english": "Those who do not desire pleasures for themselves\nBut work with love, bearing hardships for others.",
                "transliteration": "Inbam vizhaiyaar idumbaigal seydhu\nAnbodu aatrum maka.",
                "chapter": "Love",
                "chapter_num": 133,
                "meaning": "The greatest souls are those who bear hardships with love for others' benefit.",
                "theme": "love sacrifice selflessness"
            }
        }
        
        # Create indices for faster searching
        self.chapters = self._build_chapter_index()
        self.themes = self._build_theme_index()
        self.word_index = self._build_word_index()
        
    def _build_chapter_index(self):
        """Build an index of kurals by chapter."""
        chapters = {}
        for kural_num, data in self.kurals_data.items():
            chapter = data["chapter"]
            if chapter not in chapters:
                chapters[chapter] = []
            chapters[chapter].append(kural_num)
        return chapters
    
    def _build_theme_index(self):
        """Build an index of kurals by theme."""
        themes = {}
        for kural_num, data in self.kurals_data.items():
            theme_words = data.get("theme", "").split()
            for theme in theme_words:
                if theme not in themes:
                    themes[theme] = []
                themes[theme].append(kural_num)
        return themes
    
    def _build_word_index(self):
        """Build a word index for faster text searching."""
        word_index = {}
        for kural_num, data in self.kurals_data.items():
            # Index words from English translation, meaning, and themes
            text = f"{data['english']} {data['meaning']} {data.get('theme', '')}".lower()
            words = re.findall(r'\b\w+\b', text)
            
            for word in words:
                if word not in word_index:
                    word_index[word] = []
                if kural_num not in word_index[word]:
                    word_index[word].append(kural_num)
        
    
    def search_by_meaning(self, query):
        """
        Search kurals by meaning using NLP techniques.
        
        Args:
            query (str): Search query
            
        Returns:
            list: List of tuples (kural_num, relevance_score)
        """
        query_lower = query.lower()
        results = []
        
        # Split query into words for better matching
        query_words = re.findall(r'\b\w+\b', query_lower)
        
        for kural_num, data in self.kurals_data.items():
            # Combine all searchable text
            searchable_text = (
                f"{data['english']} {data['meaning']} {data['chapter']} "
                f"{data.get('theme', '')} {data.get('transliteration', '')}"
            ).lower()
            
            # Calculate relevance score
            score = self._calculate_relevance_score(query_lower, query_words, searchable_text)
            
            if score > 10:  # Threshold for relevance
                results.append((kural_num, score))
        
        # Sort by relevance score (descending)
        results.sort(key=lambda x: x[1], reverse=True)
        return results
    
    def _calculate_relevance_score(self, query, query_words, text):
        """Calculate relevance score using multiple NLP techniques."""
        score = 0
        
        # 1. Exact phrase matching (highest priority)
        if query in text:
            score += 100
        
        # 2. Word-by-word matching
        for word in query_words:
            if word in text:
                score += 50
                
                # Bonus for word frequency
                word_count = text.count(word)
                score += min(word_count * 10, 30)  # Cap bonus at 30
        
        # 3. Fuzzy matching using difflib
        words_in_text = re.findall(r'\b\w+\b', text)
        for query_word in query_words:
            close_matches = difflib.get_close_matches(
                query_word, words_in_text, n=3, cutoff=0.7
            )
            if close_matches:
                # Score based on similarity
                for match in close_matches:
                    similarity = difflib.SequenceMatcher(None, query_word, match).ratio()
                    score += similarity * 25
        
        # 4. Overall text similarity
        similarity = difflib.SequenceMatcher(None, query, text).ratio()
        score += similarity * 20
        
        # 5. Theme matching (bonus for thematic relevance)
        for word in query_words:
            if word in self.themes:
                score += 30
        
        return score
    
    def search_by_number(self, kural_num):
        """Search by kural number."""
        try:
            num = int(kural_num)
            if num in self.kurals_data:
                return [(num, 100)]
            else:
                return []
        except ValueError:
            return []
    
    def search_by_chapter(self, chapter_query):
        """Search by chapter name."""
        results = []
        query_lower = chapter_query.lower()
        
        for chapter, kural_nums in self.chapters.items():
            if query_lower in chapter.lower():
                # Add all kurals from matching chapters
                for num in kural_nums:
                    results.append((num, 75))  # Medium relevance for chapter matches
        
        return results
    
    def search_by_theme(self, theme_query):
        """Search by theme."""
        results = []
        query_lower = theme_query.lower()
        
        for theme, kural_nums in self.themes.items():
            if query_lower in theme.lower():
                for num in kural_nums:
                    results.append((num, 80))  # High relevance for theme matches
        
        return results
    
    def get_random_kural(self):
        """Get a random kural."""
        kural_num = random.choice(list(self.kurals_data.keys()))
        return self.kurals_data[kural_num], kural_num
    
    def format_kural_display(self, kural_num, show_transliteration=False):
        """Format a kural for display."""
        data = self.kurals_data[kural_num]
        
        output = []
        output.append(f"{'='*60}")
        output.append(f"Kural {kural_num} - Chapter: {data['chapter']} (#{data['chapter_num']})")
        output.append(f"{'='*60}")
        output.append("")
        output.append("Tamil:")
        output.append(data['tamil'])
        output.append("")
        
        if show_transliteration and 'transliteration' in data:
            output.append("Transliteration:")
            output.append(data['transliteration'])
            output.append("")
        
        output.append("English Translation:")
        output.append(data['english'])
        output.append("")
        output.append("Meaning:")
        output.append(data['meaning'])
        
        if 'theme' in data:
            output.append("")
            output.append(f"Themes: {data['theme']}")
        
        output.append("")
        
        return "\n".join(output)
    
    def display_search_results(self, results, query, max_results=5):
        """Display search results."""
        if not results:
            print(f"\nNo results found for '{query}'.")
            print("\nSuggestions:")
            print("• Try searching for themes like: love, friendship, virtue, wisdom")
            print("• Search by kural number: 1-1330")
            print("• Search by chapter: 'Praise of God', 'Help in Trouble', etc.")
            return
        
        print(f"\nSearch Results for '{query}' ({len(results)} found):")
        print("="*60)
        
        # Show top results
        for i, (kural_num, score) in enumerate(results[:max_results], 1):
            print(f"\n{i}. {self.format_kural_display(kural_num)}")
            if i < len(results[:max_results]):
                print("-" * 60)
        
        if len(results) > max_results:
            print(f"\n... and {len(results) - max_results} more results.")
            print("Use 'search --all' flag to see all results.")
    
    def display_help(self):
        """Display help information."""
        help_text = """
திருக்குறள் - Thirukkural Tamil to English Translator
===================================================

DESCRIPTION:
    This application provides English translations for Thirukkural verses
    and includes intelligent search capabilities using NLP techniques.
    
    Thirukkural is a classic Tamil text consisting of 1330 couplets written
    by the ancient Tamil poet Thiruvalluvar around 2000 years ago.

COMMANDS:
    search <query>          - Search by meaning, keywords, or themes
    number <kural_number>   - Get specific kural by number (1-1330)
    chapter <chapter_name>  - Search by chapter name
    theme <theme_name>      - Search by theme (love, friendship, virtue, etc.)
    random                  - Display a random kural
    chapters                - List all available chapters
    themes                  - List all available themes
    stats                   - Show database statistics
    help                    - Show this help message
    quit/exit               - Exit the application

EXAMPLES:
    search friendship       - Find kurals about friendship
    search "doing good"     - Find kurals about doing good deeds
    number 421             - Show kural number 421
    chapter "Praise of God" - Show kurals from "Praise of God" chapter
    theme love             - Show kurals with love theme
    random                 - Show a random kural for inspiration

FEATURES:
    • Intelligent search using Natural Language Processing
    • Fuzzy matching for approximate searches
    • Theme-based categorization
    • Tamil text with English translations and meanings
    • Relevance scoring for search results
        """
        print(help_text)
    
    def list_chapters(self):
        """List all available chapters."""
        print("\nAvailable Chapters:")
        print("="*40)
        for i, (chapter, kurals) in enumerate(sorted(self.chapters.items()), 1):
            print(f"{i:2d}. {chapter} ({len(kurals)} kurals)")
    
    def list_themes(self):
        """List all available themes."""
        print("\nAvailable Themes:")
        print("="*30)
        for i, (theme, kurals) in enumerate(sorted(self.themes.items()), 1):
            print(f"{i:2d}. {theme} ({len(kurals)} kurals)")
    
    def show_stats(self):
        """Show database statistics."""
        print("\nThirukkural Database Statistics:")
        print("="*35)
        print(f"Total Kurals: {len(self.kurals_data)}")
        print(f"Chapters: {len(self.chapters)}")
        print(f"Themes: {len(self.themes)}")
        print(f"Indexed Words: {len(self.word_index)}")
        
        print(f"\nChapter Distribution:")
        for chapter, kurals in sorted(self.chapters.items()):
            print(f"  {chapter}: {len(kurals)} kurals")
    
    def run_interactive(self):
        """Run the interactive command-line interface."""
        print("Welcome to Thirukkural Tamil to English Translator!")
        print("Type 'help' for commands or 'quit' to exit.")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nthirukkural> ").strip()
                
                if not user_input:
                    continue
                
                parts = user_input.split(None, 1)
                command = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""
                
                if command in ['quit', 'exit']:
                    print("வணக்கம்! (Goodbye!)")
                    break
                
                elif command == 'help':
                    self.display_help()
                
                elif command == 'search':
                    if not args:
                        print("Please provide a search query. Example: search friendship")
                        continue
                    results = self.search_by_meaning(args)
                    self.display_search_results(results, args)
                
                elif command == 'number':
                    if not args:
                        print("Please provide a kural number. Example: number 421")
                        continue
                    results = self.search_by_number(args)
                    if results:
                        kural_num = results[0][0]
                        print(f"\n{self.format_kural_display(kural_num, show_transliteration=True)}")
                    else:
                        print(f"Kural number '{args}' not found or invalid.")
                
                elif command == 'chapter':
                    if not args:
                        print("Please provide a chapter name. Example: chapter 'Praise of God'")
                        continue
                    results = self.search_by_chapter(args)
                    self.display_search_results(results, f"Chapter: {args}")
                
                elif command == 'theme':
                    if not args:
                        print("Please provide a theme. Example: theme love")
                        continue
                    results = self.search_by_theme(args)
                    self.display_search_results(results, f"Theme: {args}")
                
                elif command == 'random':
                    kural_data, kural_num = self.get_random_kural()
                    print(f"\n{self.format_kural_display(kural_num, show_transliteration=True)}")
                
                elif command == 'chapters':
                    self.list_chapters()
                
                elif command == 'themes':
                    self.list_themes()
                
                elif command == 'stats':
                    self.show_stats()
                
                else:
                    print(f"Unknown command '{command}'. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n\nInterrupted by user. Type 'quit' to exit gracefully.")
            except EOFError:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    """Main function to run the application."""
    translator = ThirukuralCLITranslator()
    
    # Check if command line arguments are provided
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'random':
            kural_data, kural_num = translator.get_random_kural()
            print(translator.format_kural_display(kural_num, show_transliteration=True))
        
        elif command == 'search' and len(sys.argv) > 2:
            query = ' '.join(sys.argv[2:])
            results = translator.search_by_meaning(query)
            translator.display_search_results(results, query)
        
        elif command == 'number' and len(sys.argv) > 2:
            results = translator.search_by_number(sys.argv[2])
            if results:
                kural_num = results[0][0]
                print(translator.format_kural_display(kural_num, show_transliteration=True))
            else:
                print(f"Kural number '{sys.argv[2]}' not found.")
        
        elif command == 'help':
            translator.display_help()
        
        else:
            print("Usage: python thirukkural_translator.py [command] [args]")
            print("Commands: random, search <query>, number <num>, help")
            print("Or run without arguments for interactive mode.")
    
    else:
        # Run interactive mode
        translator.run_interactive()

if __name__ == "__main__":
    main()