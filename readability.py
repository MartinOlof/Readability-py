text = input(text)

# Making the text into an array, then calculating how many values in the array
words = len(text.split())

# Calculating the amount of letter though boolean expression
letters = sum(letters.isalpha() for letters in text)

# Calculating the amount of '!', '?' and '.'
sentences = text.count('!') + text.count('?') + text.count('.')

letterAvg = 100 * letters / words

sentenceAvg = 100 * sentences / words

index = round(0.0588 * letterAvg - 0.296 * sentenceAvg - 15.8)

if index < 16 and index >= 1:
    print(f"Grade {index}")
elif index >= 16:
    print("Grade 16+")
else:
    print("Before Grade 1")
