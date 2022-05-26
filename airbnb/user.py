import json
from pathlib import Path
from utils import validate_password, hash_password

user = {
    "first_name": "Amaka",
    "last_name": "Stephen",
    "email": "amaka@gmail.com",
    "phone": "0800404014",
    "username": "any_special",
    "password": "pass123",
    "role": "OWNER"
}


def get_file_path():
    path = Path("../data/users/users.json").resolve()

    if not path.exists():
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch(exist_ok=True)
    return path


def get_user():
    file_path = get_file_path()

    with file_path.open(mode='r', encoding='utf-8') as file:
        try:
            users = json.load(file)
            return users
        except json.decoder.JSONDecodeError:
            return []


def save_users(user):
    user['password'] = hash_password(user['password'])

    file_path = get_file_path()
    users = get_user()

    if [u for u in users if u['username'] == user['username']]:
        print(f"User with username {user['username']} already exist")
        return

    users.append(user)

    with file_path.open(mode='w', encoding='utf-8') as file:
        json.dump(users, file)


def get_user_by_username(username):
    users = get_user()
    user_list = [u for u in user if u['username'] == username]
    if user_list:
        return user_list[0]
    return f"User with username{username} not found"


if __name__ == "__main__":
    print("inside user main")
    save_users(user)
    print(get_user_by_username('any_special'))
