## <---------- Caesar Cipher Encoder Function ---------->

def encode_message(message, shift):
    """Encodes a message using a Caesar cipher with the specified shift."""
    encoded_message = ""
    for char in message:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift % 26  # Normalize shift within alphabet range
            if char.isupper():
                # Shift uppercase letters using ASCII values
                encoded_char = chr((ord(char) - 65 + shift_amount) % 26 + 65)
            else:
                # Shift lowercase letters using ASCII values
                encoded_char = chr((ord(char) - 97 + shift_amount) % 26 + 97)
            encoded_message += encoded_char
        else:
            # Keep non-letter characters unchanged
            encoded_message += char
    return encoded_message


## <---------- Caesar Cipher Decoder Function ---------->

def decode_message(encoded_message, shift):
    """Decodes a message using a Caesar cipher with the specified shift."""
    return encode_message(encoded_message, -shift)  # Reuse encoder with negative shift


## <---------- User Interface Function (Menu Driven) ---------->

def user_menu():
    """Displays a menu for user interaction."""
    print("Welcome to the Secret Code Generator!")  # Program welcome message
    while True:
        print("\nPlease choose an option:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")  # Get user's menu selection

        if choice == '1':
            # Encoding path
            message = input("Enter the message to encode: ")
            shift = int(input("Enter the shift number: "))
            encoded = encode_message(message, shift)
            print(f"Encoded Message: {encoded}")

        elif choice == '2':
            # Decoding path
            encoded_message = input("Enter the message to decode: ")
            shift = int(input("Enter the shift number: "))
            decoded = decode_message(encoded_message, shift)
            print(f"Decoded Message: {decoded}")

        elif choice == '3':
            # Exit path
            print("Exiting the program. Goodbye!")
            break

        else:
            # Handle invalid menu options
            print("Invalid choice. Please enter 1, 2, or 3.")


## <---------- Program Entry Point ---------->

# Run the menu only if script is executed directly
if __name__ == "__main__":
    user_menu()
