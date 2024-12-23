import time
import board
import neopixel

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

def prompt_unit_length():
    while True:
        unit_length = input("Enter the length of a unit (in seconds, between 0 and 1): ")
        try:
            unit_length = float(unit_length)
            if 0 < unit_length <= 1:
                return unit_length
            else:
                print("Please enter a value between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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
            morse_code_list.append(' ' * 7)  # 7 spaces to separate words
        else:
            morse_code_list.append(morse_code_dict[char.upper()] + ' ' * 3)  # 3 spaces to separate letters
    return morse_code_list

def display_morse_code(morse_code_list, unit_length):
    for code in morse_code_list:
        for symbol in code:
            if symbol == '.':
                light_led(unit_length)
            elif symbol == '-':
                light_led(3 * unit_length)
            else:
                time.sleep(7 * unit_length)  # Sleep for 7 * unit length for word separation
        time.sleep(3 * unit_length)  # Sleep for 3 * unit length for inter-letter pause

def light_led(duration):
    pixels.fill((255, 0, 0))  # Turn on the LED (red color)
    pixels.show()
    time.sleep(duration)
    pixels.fill((0, 0, 0))  # Turn off the LED
    pixels.show()

def main():
    unit_length = prompt_unit_length()  # Get the unit length for timing
    sentence = prompt_user()  # Get the sentence from the user
    cleaned_sentence = remove_non_morse_chars(sentence)  # Clean the sentence (remove invalid chars)
    morse_code_list = convert_to_morse_code(cleaned_sentence)  # Convert to Morse code
    display_morse_code(morse_code_list, unit_length)  # Display the Morse code with LED

if __name__ == "__main__":
    main()
#source chatgpt
