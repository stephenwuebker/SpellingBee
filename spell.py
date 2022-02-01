from nltk.corpus import words

all_words = words.words()

center_letter = 't'
letters = ['y','h','o','g','m','l']
letters.append(center_letter)

center_words = []
final_words = []

# get all words containing the center letter that are at least 4 letters long
for w in all_words:
    if center_letter in w and len(w) >= 4:
        center_words.append(w)

# find all words in the filtered list that have all characters in the letter list
bad_letter = False
for cw in center_words:
    for ch in cw:
        if ch not in letters:
            bad_letter = True
            break
    if bad_letter == False and final_words.count(cw.lower())==0:
        final_words.append(cw.lower())
    bad_letter = False


print(len(final_words))
print(final_words)                            