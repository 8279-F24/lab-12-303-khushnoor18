morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

def prompt_user():
    sentence = input("Enter a sentence: ").lower()
    return sentence

def remove_non_morse_chars(sentence):
    morse_chars = [char for char in sentence if char in morse_code_dict or char == ' ']
    return ''.join(morse_chars)

def convert_to_morse_code(sentence):
    morse_code_list = []
    for char in sentence:
        if char == ' ':
            morse_code_list.append(' ' * 7)  # 7 units for word space
        else:
            morse_code_list.append(morse_code_dict[char] + ' ' * 3)  # 3 units for character space
    return morse_code_list

def main():
    sentence = prompt_user()
    sentence = remove_non_morse_chars(sentence)
    morse_code_list = convert_to_morse_code(sentence)
    morse_code_string = ''.join(morse_code_list)
    print("Morse code equivalent:")
    print(morse_code_string)

if __name__ == "__main__":
    main()