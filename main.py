
import random
import string
import pyperclip


def generate_password(length, use_upper, use_lower,
                      use_numbers, use_symbols,
                      exclude_chars):

    chars = ""

    if use_upper:
        chars += string.ascii_uppercase

    if use_lower:
        chars += string.ascii_lowercase

    if use_numbers:
        chars += string.digits

    if use_symbols:
        chars += string.punctuation

    # Remove excluded characters
    if exclude_chars:
        chars = ''.join(
            c for c in chars
            if c not in exclude_chars
        )

    # Safety check
    if not chars:
        return None

    password = ''.join(
        random.choice(chars)
        for _ in range(length)
    )

    return password


def password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak 🔴"

    elif score <= 4:
        return "Medium 🟠"

    else:
        return "Strong 🟢"


def yes_no_input(message):

    while True:
        choice = input(message).strip().lower()

        if choice in ["y", "yes"]:
            return True

        elif choice in ["n", "no"]:
            return False

        else:
            print("Please enter y/n")


def main():

    print("=" * 50)
    print("🔐 ADVANCED PASSWORD GENERATOR")
    print("=" * 50)

    # Length validation
    while True:
        try:
            length = int(
                input("Enter password length: ")
            )

            if length <= 0:
                print(
                    "Length must be greater than 0."
                )
                continue

            break

        except ValueError:
            print(
                "Please enter a valid number."
            )

    # Character preferences
    use_upper = yes_no_input(
        "Include uppercase letters? (y/n): "
    )

    use_lower = yes_no_input(
        "Include lowercase letters? (y/n): "
    )

    use_numbers = yes_no_input(
        "Include numbers? (y/n): "
    )

    use_symbols = yes_no_input(
        "Include symbols? (y/n): "
    )

    exclude_chars = input(
        "Enter characters to exclude (optional): "
    )

    password = generate_password(
        length,
        use_upper,
        use_lower,
        use_numbers,
        use_symbols,
        exclude_chars
    )

    if password is None:
        print(
            "\n❌ Error: No characters available."
        )
        print(
            "Select at least one type "
            "or remove exclusions."
        )
        return

    print("\n" + "=" * 50)
    print("✅ Generated Password:")
    print(password)

    strength = password_strength(password)

    print(f"\n🔒 Password Strength: {strength}")

    # Clipboard
    copy_choice = yes_no_input(
        "\nCopy password to clipboard? (y/n): "
    )

    if copy_choice:
        pyperclip.copy(password)
        print(
            "✅ Password copied to clipboard!"
        )

    print("=" * 50)


if __name__ == "__main__":
    main()

