from sys import argv

def main(argv):
    letters = argv[1].upper()
    min_len = 0

    if len(argv) == 3:
    	min_len = int(argv[2])

    result = []
    with open('collins2019.txt', 'r') as words_file:
        for line in words_file:
            word = line.strip()
            if can_spell(letters, word):
                result.append(word)

    result = sorted(result, key=lambda w: len(w), reverse=True)

    for word in [word for word in result if len(word) >= min_len]:
    	print(word)

def can_spell(letters, word):
    letters = sorted(letters, reverse=True)
    word = list(word)

    for letter in letters:
        if len(word) == 0:
            return True
        elif letter == '?':
            word.pop()
        elif letter in word:
            word.remove(letter)

    return len(word) == 0


if __name__ == '__main__':
    main(argv)