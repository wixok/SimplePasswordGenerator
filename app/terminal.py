import os
import platform


class Terminal:

    @staticmethod
    def set_cli_title(title: str) -> None:
        """Set the title of the command-line window."""
        print(f"\33]0;{title}\a", end="", flush=True)

    @staticmethod
    def clear_cli() -> None:
        """Clear the terminal screen based on the operating system."""
        if platform.system().lower() == "windows":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def pause(message: str = "Press ENTER to continue...") -> None:
        """Pause program execution until the user presses Enter."""
        input(message)

    @staticmethod
    def ask_yes_no(prompt: str) -> bool:
        """Ask the user a yes/no question and return True or False accordingly."""
        while True:
            choice = input(prompt + " (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                return True
            if choice in ("n", "no"):
                return False
            print("Please enter 'y' or 'n'.")
