from faker import Faker
import random

fake = Faker()

def generate_fake_identity():
    identity = {
        "full_name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address().replace("\n", ", "),
        "birthdate": str(fake.date_of_birth(minimum_age=18, maximum_age=60)),
        "national_id": fake.ssn(),
        "credit_card": fake.credit_card_number(),
        "profile_pic_url": f"https://api.multiavatar.com/{random.randint(100000,999999)}.png"
    }
    return identity
