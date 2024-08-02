import nltk
from nltk.corpus import wordnet

# Download the WordNet data if not already done
nltk.download('wordnet')

def get_words_starting_with(letter):
    words = set()
    for synset in wordnet.all_synsets():
        for lemma in synset.lemmas():
            word = lemma.name().lower()
            if word.startswith(letter):
                words.add(word)
    return sorted(words)

def main():
    while True:
        letter = input("Enter a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        words = get_words_starting_with(letter)
        if words:
            print(f"Words that start with '{letter}':")
            for word in words:
                print(word)
        else:
            print(f"No words found starting with the letter '{letter}'.")

        rerun = input("Do you want to run the program again? (y/n): ").strip().lower()
        if rerun != 'y':
            break

if __name__ == "__main__":
    main()
