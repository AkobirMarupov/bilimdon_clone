import jwt


from dotenv import load_dotenv
import os


load_dotenv()

HASH_SECRET = os.getenv("HASH_SECRET", "hash_secret")


def hash_password(password: str) -> str:
    hashed_password = jwt.encode({'password': password}, key=HASH_SECRET, algorithm='HS256')
    return hashed_password


def dehash_password(hashed_password: str) -> str:
    password = jwt.decode(hashed_password, key=HASH_SECRET, algorithm='HS256')
    return password
