from cryptography.fernet import Fernet

def encrypt_secret_message(secret_message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(secret_message.encode())
    return encrypted_message

def decrypt_secret_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def generate_secret_poem():
    # Your secret message goes here
    secret_message = "db472ddae81d449b0793c200c5c8051831af4bdf4bfdb09715527f28e2d835d9"

    # Generate a key for encryption
    key = Fernet.generate_key()

    # Encrypt the secret message
    encrypted_secret = encrypt_secret_message(secret_message, key)

    # A long and intricate poem
    poem = f"""
    In realms of code where shadows dance,
    A secret hides in a cryptic trance.
    Through loops and branches, it weaves its tale,
    A message obscured, beyond the veil.

    The variables whisper, the functions hum,
    A puzzle encrypted, yet to be undone.
    In lines of Python, the secret lies,
    Decode the verses, unveil the prize.

    Amidst the bytes and lines of code,
    A riddle formed, in secrets bestowed.
    Fernet's embrace, a cryptic kiss,
    Unravel the mystery, in scripts like this.

    Beyond the print and console's glare,
    The secret beckons, if you dare.
    For those who seek with curious might,
    A hidden phrase, bathed in digital light.

    Decrypt the essence, reveal the lore,
    Python's magic, forevermore.
    The secret unveiled, like morning dew,
    A poetic script, crafted just for you.

    And now, dear coder, the time has come,
    To decrypt the secret, the chosen one.
    Decrypt the message, set it free,
    Your hidden phrase, for only thee.

    Secret Phrase: {decrypt_secret_message(encrypted_secret, key)}
    Key: {key.decode()}
    """

    print(poem)

# Generate and display the secret poem
generate_secret_poem()
//RC2
