import random
import string

def generate_unique_email(domain="example.com", length=8):
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    return f"{username}@{domain}"

def generate_password(length=12, use_special_chars=True):
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += "!@#$%^&*()-_=+"
    return ''.join(random.choice(chars) for _ in range(length))

