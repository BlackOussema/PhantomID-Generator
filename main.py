from identity_generator import generate_fake_identity
from fingerprint_generator import generate_fingerprint
import json
import os

def save_profile_to_file(profile, filename):
    with open(filename, "w") as f:
        json.dump(profile, f, indent=4)
    print(f"[✔] File saved: {filename}")

def generate_multiple_profiles(count=5):
    os.makedirs("profiles", exist_ok=True)
    for i in range(1, count + 1):
        identity = generate_fake_identity()
        fingerprint = generate_fingerprint()
        profile = {
            "identity": identity,
            "fingerprint": fingerprint
        }
        filename = f"profiles/fake_profile_{i}.json"
        save_profile_to_file(profile, filename)

if __name__ == "__main__":
    number = int(input("Enter number of profiles to generate: "))
    generate_multiple_profiles(number)
