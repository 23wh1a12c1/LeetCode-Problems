# PYTHON3




class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if not word.isalnum():
            return False

        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False

        for ch in word:
            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant







#   C




#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

bool is_valid_word(const char *word) {
    int length = strlen(word);

    // Condition 1: At least 3 characters
    if (length < 3)
        return false;

    bool has_vowel = false;
    bool has_consonant = false;

    for (int i = 0; i < length; i++) {
        char c = word[i];

        // Condition 2: Only letters or digits
        if (!isalnum(c)) {
            return false;
        }

        // Check for vowels and consonants
        if (isalpha(c)) {
            char lower = tolower(c);
            if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
                has_vowel = true;
            } else {
                has_consonant = true;
            }
        }
    }

    // Condition 3 & 4: At least one vowel and one consonant
    return has_vowel && has_consonant;
}

// Example usage
int main() {
    printf("%s\n", is_valid_word("234Adas") ? "true" : "false");  // true
    printf("%s\n", is_valid_word("b3") ? "true" : "false");       // false
    printf("%s\n", is_valid_word("a3$e") ? "true" : "false");     // false
    return 0;
}
