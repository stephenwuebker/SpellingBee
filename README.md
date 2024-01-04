Python script to help solve NY Times Spelling Bee game.

# Installing NLTK

```pip install --user -U nltk```

Then run ```python```

In the interpreter, we now need to install NLTK data
```
>>> import nltk
>>> nltk.download('words')
```

# Usage

Set the center letter and the list of all the other letters.

Script will load a list of words from nltk and loop through it, keeping only words that contain the center letter and are at least 4 letters long.

Then it will loop through the filtered list, keeping only words where every letter of the word is in the letter list.

Limitations: 
Does not exclude "obscure" or other words that the NY Times might leave out. 
It's possible the word list is incomplete and doesn't contain words the NY Times might use.
