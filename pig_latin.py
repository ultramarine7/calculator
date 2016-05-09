""" pig latin script """

word = raw_input("Enter a word for pig latin: ")

# Checks if user typed anything and checks if the input is alphabetical
if len(word) > 0 and word.isalpha():
    # Set the word to lower case
    lower_word = word.lower()
    # Extract the first letter
    first_letter = word[0]
    pig_word = lower_word + first_letter + "ay"
    pig_word = pig_word[1:len(pig_word)]
    print pig_word
else:
    print "You didn't enter a word."