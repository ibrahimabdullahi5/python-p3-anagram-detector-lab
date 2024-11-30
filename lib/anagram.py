# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        
        # Store matches in a list
        matches = []

        # Sort the original word
        sorted_word = sorted(self.word)

        # Iterate over the list of words
        for w in words:


            # If sorted letters of the current word match the sorted original word
            if sorted(w) == sorted_word:


                # Add to matches list
                matches.append(w)

        # Return the list of matches
        return matches