import random
import logging

existing_ids = set()


def generate_random_number():
    return f"{random.randint(0, 9)}{random.randint(0, 9)}"


def create_unique_account():
    while True:
        random_num = generate_random_number()
        user_id = f"test_{random_num}"
        if user_id not in existing_ids:
            existing_ids.add(user_id)
            password = f"{user_id}{random_num}"
            return {"user_id": user_id, "password": password, "username": "TEST"}


sample_account = create_unique_account()
logging.info(
    f"ID: {sample_account['user_id']}, Password: {sample_account['password']}, Username: {sample_account['username']}"
)
