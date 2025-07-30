import random

def generate_fingerprint():
    resolutions = ["1920x1080", "1366x768", "1440x900", "1280x720"]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 Chrome/89.0.4389.105 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/14.1 Safari/605.1.15"
    ]

    fingerprint = {
        "user_agent": random.choice(user_agents),
        "ip_address": f"192.168.{random.randint(0,255)}.{random.randint(0,255)}",
        "screen_resolution": random.choice(resolutions),
        "language": random.choice(["en-US", "fr-FR", "ar-TN", "es-ES"]),
        "timezone": random.choice(["UTC", "Europe/Paris", "Africa/Tunis", "Asia/Dubai"]),
        "device": random.choice(["Desktop", "Laptop", "Mobile"]),
        "os": random.choice(["Windows 10", "Linux Ubuntu", "macOS Catalina", "Android 11"]),
        "mac_address": ":".join(["%02x"%random.randint(0,255) for _ in range(6)])
    }

    return fingerprint
