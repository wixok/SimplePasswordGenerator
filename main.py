from app.terminal import Terminal
from app.helper import Helper

# Set the CLI window title
Terminal.set_cli_title("Simple Password Generator")

def ask_bool(prompt, default=True):
    """Prompt the user for a yes/no answer and return a boolean value."""
    default_text = "Y/n" if default else "y/N"

    while True:
        ans = input(f"{prompt} ({default_text}): ").strip().lower()

        if ans == "":
            return default  # Use the default value when the user presses Enter
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False

def run_generator():
    """Handle user input for password settings and generate multiple passwords."""
    print("\n=== Password Generator ===\n")

    # Request a password length from the user
    while True:
        raw = input("Enter password length (default 12): ").strip()
        if raw == "":
            length = 12
            break
        try:
            length = int(raw)
            if length > 0:
                break
            print("Length must be a positive integer.")
        except ValueError:
            print("Please enter a valid number.")

    # Ask the user which character types to include
    use_upper = ask_bool("Include uppercase letters?", default=True)
    use_lower = ask_bool("Include lowercase letters?", default=True)
    use_digits = ask_bool("Include digits?", default=True)
    use_symbols = ask_bool("Include symbols?", default=True)

    try:
        print("\nYour generated passwords:\n")

        # Generate and display a list of passwords
        for i in range(10):
            password = Helper.generate_password(
                length=length,
                use_uppercase=use_upper,
                use_lowercase=use_lower,
                use_digits=use_digits,
                use_symbols=use_symbols,
            )
            print(f"{i+1}. {password}")

        print()  # Print final newline for clean output

    except ValueError as e:
        print(f"\nError: {e}")

def main():
    """Main loop for the password generator application."""
    while True:
        Terminal.clear_cli()
        run_generator()

        again = ask_bool("Do you want to generate more passwords?", default=False)
        if not again:
            print("\nGoodbye!\n")
            break

# Entry point of the program
if __name__ == "__main__":
    main()
