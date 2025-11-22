import random
import string


class Helper:

    @staticmethod
    def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):

        if not (use_uppercase or use_lowercase or use_digits or use_symbols):
            raise ValueError("At least one character type must be selected.")

        required_chars = []
        all_chars = ''

        if use_uppercase:
            char = random.choice(string.ascii_uppercase)
            required_chars.append(char)
            all_chars += string.ascii_uppercase

        if use_lowercase:
            lowercase_letters = string.ascii_lowercase.replace('l', '')  # Exclude 'l'
            char = random.choice(lowercase_letters)
            required_chars.append(char)
            all_chars += lowercase_letters

        if use_digits:
            char = random.choice(string.digits)
            required_chars.append(char)
            all_chars += string.digits

        if use_symbols:
            symbols = "$@#!%*?"
            char = random.choice(symbols)
            required_chars.append(char)
            all_chars += symbols

        if length < len(required_chars):
            raise ValueError("Password length too short to include all selected character types.")

        remaining_length = length - len(required_chars)
        password_chars = required_chars + [random.choice(all_chars) for _ in range(remaining_length)]
        random.shuffle(password_chars)

        return ''.join(password_chars)
