import winsound
import time

def get_text(text):
    words = text.strip().split('  ')
    normal_text = ''
    for i in words:
        letters = i.split(' ')
        for j in letters:
            for key,value in morse_dict.items():
                if value == j:
                    normal_text += key
        normal_text += ' '
    return normal_text

def get_morse(text):
    morse_text = ''
    for i in text:
        if i != ' ':
            morse_text += morse_dict[i] + ' '
        else:
            morse_text += ' '
    return morse_text

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



# while 1:
print("enter input")
text = input().lower()


# MORSE TO TEXT
if not (set(text) - {'.','-',' '}):
    text = get_text(text)
    print(text)
        
# TEXT TO MORSE
else:
    text = get_morse(text)
    print(text)
    for i in text:
        if i == '.':
            winsound.Beep(600,100)
        elif i == "-":
            winsound.Beep(600,250)
        else:
            time.sleep(1.0)

    