morse_dict = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}

print("enter input")
text = input().lower()


# MORSE TO TEXT
if not (set(text) - {'.','-',' '}):
    words = text.strip().split('  ')
    normal_text = ''
    for i in words:
        letters = i.split(' ')
        for j in letters:
            for key,value in morse_dict.items():
                if value == j:
                    normal_text += key
        normal_text += ' '
    print(normal_text)
        
# TEXT TO MORSE
else:
    morse_text = ''
    for i in text:
        if i != ' ':
            morse_text += morse_dict[i] + ' '
        else:
            morse_text += ' '
    print(morse_text)