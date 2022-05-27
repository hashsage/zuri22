# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
        word = word.lower()
        anagram = anagram.lower()
        if(sorted(word) != sorted(anagram)):
            return False
        else:
            return True

#testing
#if find_anagram("words", "Sdrow"):
#    print("it is an anagram")


