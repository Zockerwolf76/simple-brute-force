import itertools

def brute_force():

    # Verfügbare Zeichen
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    attempts = 0

    # Eingabe des gesuchten Passworts
    password = input("Bitte geben Sie das Passwort ein: ")

    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            print(f"attempt: {attempts}, guess: {guess}")
            if guess == password:

                # Gesuchts Passwort wurde gefunden
                print("\n----------------------------------")
                print("FOUND PASSWORD:")
                print(f"Attempt: {attempts}")
                print(f"Final password: {guess}")
                print("---------------------------------- \n")
                return (guess, attempts)


if __name__ == "__main__":
    while True:
        brute_force()