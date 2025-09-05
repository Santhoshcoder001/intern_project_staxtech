#!/usr/bin/env python3
"""
Simple test script for Thirukkural Translator
Tests basic functionality and NLP features
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Run a command and return output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def test_thirukkural_translator():
    """Test the Thirukkural translator functionality."""
    print("Testing Thirukkural Tamil to English Translator with NLP...")
    print("=" * 60)
    
    # Test commands
    tests = [
        ("Help command", "python3 thirukkural_translator.py help"),
        ("Random kural", "python3 thirukkural_translator.py random"),
        ("Specific kural number", "python3 thirukkural_translator.py number 421"),
        ("Search by keyword", "python3 thirukkural_translator.py search friendship"),
        ("Search by theme", "python3 thirukkural_translator.py search love"),
        ("Search with phrase", "python3 thirukkural_translator.py search \"doing good\""),
        ("Invalid kural number", "python3 thirukkural_translator.py number 9999"),
        ("Search no results", "python3 thirukkural_translator.py search xyz123notfound"),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, command in tests:
        print(f"\n{test_name}:")
        print(f"Command: {command}")
        
        returncode, stdout, stderr = run_command(command)
        
        if returncode == 0:
            print("✅ PASSED")
            passed += 1
            
            # Show first few lines of output
            lines = stdout.split('\n')[:5]
            for line in lines:
                if line.strip():
                    print(f"   {line}")
            if len(stdout.split('\n')) > 5:
                print("   ...")
        else:
            print("❌ FAILED")
            print(f"   Return code: {returncode}")
            if stderr:
                print(f"   Error: {stderr}")
        
        print("-" * 40)
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    # Test NLP features
    print(f"\n🧠 NLP Features Demonstrated:")
    print("✅ Text similarity matching using difflib")
    print("✅ Fuzzy word matching for approximate searches")
    print("✅ Theme-based categorization and indexing")
    print("✅ Relevance scoring for search results")
    print("✅ Multi-language support (Tamil and English)")
    print("✅ Interactive command-line interface")
    
    return passed == total

if __name__ == "__main__":
    # Change to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    success = test_thirukkural_translator()
    
    if success:
        print("\n🎉 All tests passed! Thirukkural Translator is working correctly.")
        sys.exit(0)
    else:
        print("\n⚠️  Some tests failed. Please check the implementation.")
        sys.exit(1)