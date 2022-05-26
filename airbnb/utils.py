import bcrypt


def hash_password(password: str):
    password = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)


def validate_password(user_password, hashed_password):
    user_password = user_password.encode()
    hashed_password = hashed_password.encode()
    return bcrypt.checkpw(user_password, hashed_password)


if __name__ == "__main__":
    passw = (hash_password("pass123"))
    print(validate_password("pass123", passw))
