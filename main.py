morse_code_dictionary = {
"A": ".-",
"B": "-...",
"C": "-.-.",
"D": "-..",
"E": ".",
"F": "..-.",
"G": "--.",
"H": "....",
"I": "..",
"J": ".---",
"K": "-.-",
"L": ".-..",
"M": "--",
"N": "-.",
"O": "---",
"P": ".--.",
"Q": "--.-",
"R": ".-.",
"S": "...",
"T": "-",
"U": "..-",
"V": "...-",
"W": ".--",
"X": "-..-",
"Y": "-.--",
"Z": "--..",
}

word = input("Write Your Word to Convert it in Morse Code: ").upper()
word_list = list(word)
word_in_morse = ""
for letter in word_list:
    for key in morse_code_dictionary:
        if key == letter:
            word_in_morse += morse_code_dictionary[key]
print(f"Your Converted Word in Morse Code: {word_in_morse}")


