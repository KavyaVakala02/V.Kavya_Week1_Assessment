# Function to get user input
def get_user_input():
    user_string = input("Enter a string: ")
    return user_string
# Function to analyze the string
def analyze_string(input_string):
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_char_count = 0
    for character in input_string:
        if character.lower() in "aeiou":
            vowel_count += 1
        elif character.isalpha():
            consonant_count += 1
        elif character.isdigit():
            digit_count += 1
        elif not character.isspace():
            special_char_count += 1
    reversed_string = input_string[::-1]
    return (vowel_count, consonant_count, digit_count, special_char_count, reversed_string)
# Main function to execute the program
def main():
    user_input = get_user_input()  # Get input from the user
    vowels, consonants, digits, special_chars, reversed_str = analyze_string(user_input)  # Analyze string
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")
    print(f"Special Characters: {special_chars}")
    print(f"Reversed String: {reversed_str}")

# Run the program
main()
