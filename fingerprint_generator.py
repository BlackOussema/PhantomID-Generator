#!/usr/bin/env python3
"""
PhantomID Digital Fingerprint Generator

Generates realistic browser and device fingerprints for security testing.

Author: Ghariani Oussema
License: MIT
"""

import hashlib
import random
import string
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional

# Browser configurations
BROWSERS = {
    "chrome": {
        "name": "Chrome",
        "versions": ["120.0.0.0", "119.0.0.0", "118.0.0.0", "117.0.0.0", "116.0.0.0"],
        "engine": "Blink",
    },
    "firefox": {
        "name": "Firefox",
        "versions": ["121.0", "120.0", "119.0", "118.0", "117.0"],
        "engine": "Gecko",
    },
    "safari": {
        "name": "Safari",
        "versions": ["17.2", "17.1", "17.0", "16.6", "16.5"],
        "engine": "WebKit",
    },
    "edge": {
        "name": "Edge",
        "versions": ["120.0.0.0", "119.0.0.0", "118.0.0.0"],
        "engine": "Blink",
    },
}

# Operating systems
OPERATING_SYSTEMS = {
    "windows": {
        "name": "Windows",
        "versions": ["10", "11"],
        "platforms": ["Win32", "Win64"],
        "user_agent_part": "Windows NT {version}",
    },
    "macos": {
        "name": "macOS",
        "versions": ["14.2", "14.1", "14.0", "13.6", "13.5"],
        "platforms": ["MacIntel"],
        "user_agent_part": "Macintosh; Intel Mac OS X {version}",
    },
    "linux": {
        "name": "Linux",
        "versions": ["x86_64", "i686"],
        "platforms": ["Linux x86_64", "Linux i686"],
        "user_agent_part": "X11; Linux {version}",
    },
    "android": {
        "name": "Android",
        "versions": ["14", "13", "12", "11", "10"],
        "platforms": ["Linux armv8l", "Linux armv7l"],
        "user_agent_part": "Linux; Android {version}",
    },
    "ios": {
        "name": "iOS",
        "versions": ["17.2", "17.1", "17.0", "16.7", "16.6"],
        "platforms": ["iPhone", "iPad"],
        "user_agent_part": "iPhone; CPU iPhone OS {version} like Mac OS X",
    },
}

# Screen resolutions
SCREEN_RESOLUTIONS = [
    {"width": 1920, "height": 1080, "device": "Desktop"},
    {"width": 2560, "height": 1440, "device": "Desktop"},
    {"width": 3840, "height": 2160, "device": "Desktop"},
    {"width": 1366, "height": 768, "device": "Laptop"},
    {"width": 1440, "height": 900, "device": "Laptop"},
    {"width": 1536, "height": 864, "device": "Laptop"},
    {"width": 1280, "height": 720, "device": "Laptop"},
    {"width": 390, "height": 844, "device": "Mobile"},
    {"width": 414, "height": 896, "device": "Mobile"},
    {"width": 375, "height": 812, "device": "Mobile"},
    {"width": 360, "height": 800, "device": "Mobile"},
    {"width": 820, "height": 1180, "device": "Tablet"},
    {"width": 768, "height": 1024, "device": "Tablet"},
]

# Languages
LANGUAGES = [
    "en-US", "en-GB", "en-AU", "en-CA",
    "fr-FR", "fr-CA", "de-DE", "es-ES",
    "it-IT", "pt-BR", "pt-PT", "nl-NL",
    "ru-RU", "ja-JP", "zh-CN", "zh-TW",
    "ko-KR", "ar-SA", "ar-TN", "tr-TR",
    "pl-PL", "sv-SE", "da-DK", "fi-FI",
]

# Timezones
TIMEZONES = [
    {"name": "America/New_York", "offset": -5},
    {"name": "America/Los_Angeles", "offset": -8},
    {"name": "America/Chicago", "offset": -6},
    {"name": "Europe/London", "offset": 0},
    {"name": "Europe/Paris", "offset": 1},
    {"name": "Europe/Berlin", "offset": 1},
    {"name": "Asia/Tokyo", "offset": 9},
    {"name": "Asia/Shanghai", "offset": 8},
    {"name": "Asia/Dubai", "offset": 4},
    {"name": "Australia/Sydney", "offset": 11},
    {"name": "Africa/Tunis", "offset": 1},
    {"name": "UTC", "offset": 0},
]

# WebGL vendors and renderers
WEBGL_CONFIGS = [
    {"vendor": "Google Inc. (NVIDIA)", "renderer": "ANGLE (NVIDIA GeForce RTX 3080)"},
    {"vendor": "Google Inc. (NVIDIA)", "renderer": "ANGLE (NVIDIA GeForce RTX 4070)"},
    {"vendor": "Google Inc. (AMD)", "renderer": "ANGLE (AMD Radeon RX 6800 XT)"},
    {"vendor": "Google Inc. (Intel)", "renderer": "ANGLE (Intel UHD Graphics 630)"},
    {"vendor": "Apple Inc.", "renderer": "Apple M1"},
    {"vendor": "Apple Inc.", "renderer": "Apple M2"},
    {"vendor": "Mesa/X.org", "renderer": "Mesa Intel(R) UHD Graphics"},
    {"vendor": "Qualcomm", "renderer": "Adreno (TM) 650"},
]


@dataclass
class Fingerprint:
    """Represents a browser/device fingerprint."""
    # Browser info
    user_agent: str
    browser_name: str
    browser_version: str
    browser_engine: str
    
    # System info
    platform: str
    os_name: str
    os_version: str
    device_type: str
    
    # Screen
    screen_width: int
    screen_height: int
    screen_resolution: str
    color_depth: int
    pixel_ratio: float
    
    # Locale
    language: str
    languages: List[str]
    timezone: str
    timezone_offset: int
    
    # Network
    ip_address: str
    connection_type: str
    
    # Hardware
    cpu_cores: int
    device_memory: int
    max_touch_points: int
    
    # WebGL
    webgl_vendor: str
    webgl_renderer: str
    
    # Canvas fingerprint
    canvas_hash: str
    
    # Audio fingerprint
    audio_hash: str
    
    # Misc
    do_not_track: Optional[str]
    cookies_enabled: bool
    local_storage: bool
    session_storage: bool
    indexed_db: bool
    
    # MAC address (for local network simulation)
    mac_address: str
    
    # Unique fingerprint hash
    fingerprint_hash: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


class FingerprintGenerator:
    """
    Professional browser/device fingerprint generator.
    
    Generates realistic fingerprints that mimic real browser
    and device configurations.
    """
    
    def __init__(self, seed: Optional[int] = None):
        """
        Initialize the fingerprint generator.
        
        Args:
            seed: Random seed for reproducible generation
        """
        if seed is not None:
            random.seed(seed)
    
    def generate(
        self,
        device_type: Optional[str] = None,
        browser: Optional[str] = None,
        os: Optional[str] = None
    ) -> Fingerprint:
        """
        Generate a complete browser fingerprint.
        
        Args:
            device_type: Specific device type ('Desktop', 'Mobile', 'Tablet')
            browser: Specific browser ('chrome', 'firefox', 'safari', 'edge')
            os: Specific OS ('windows', 'macos', 'linux', 'android', 'ios')
        
        Returns:
            Generated Fingerprint object
        """
        # Select device type
        if device_type is None:
            device_type = random.choice(["Desktop", "Laptop", "Mobile", "Tablet"])
        
        # Select OS based on device type
        if os is None:
            if device_type in ["Desktop", "Laptop"]:
                os = random.choice(["windows", "macos", "linux"])
            elif device_type == "Mobile":
                os = random.choice(["android", "ios"])
            else:  # Tablet
                os = random.choice(["android", "ios"])
        
        os_config = OPERATING_SYSTEMS[os]
        os_version = random.choice(os_config["versions"])
        platform = random.choice(os_config["platforms"])
        
        # Select browser
        if browser is None:
            if os == "ios":
                browser = "safari"
            elif os == "android":
                browser = random.choice(["chrome", "firefox"])
            else:
                browser = random.choice(list(BROWSERS.keys()))
        
        browser_config = BROWSERS[browser]
        browser_version = random.choice(browser_config["versions"])
        
        # Generate user agent
        user_agent = self._generate_user_agent(
            browser, browser_version, os, os_version, device_type
        )
        
        # Select screen resolution
        matching_resolutions = [
            r for r in SCREEN_RESOLUTIONS 
            if r["device"] == device_type or device_type == "Laptop" and r["device"] == "Desktop"
        ]
        if not matching_resolutions:
            matching_resolutions = SCREEN_RESOLUTIONS
        
        resolution = random.choice(matching_resolutions)
        
        # Select language and timezone
        language = random.choice(LANGUAGES)
        languages = [language]
        if "-" in language:
            base_lang = language.split("-")[0]
            languages.append(base_lang)
        
        tz = random.choice(TIMEZONES)
        
        # Generate IP address (private range for safety)
        ip_address = self._generate_private_ip()
        
        # Hardware specs based on device type
        if device_type in ["Desktop", "Laptop"]:
            cpu_cores = random.choice([4, 6, 8, 12, 16])
            device_memory = random.choice([8, 16, 32, 64])
            max_touch_points = 0
        else:
            cpu_cores = random.choice([4, 6, 8])
            device_memory = random.choice([4, 6, 8, 12])
            max_touch_points = random.choice([5, 10])
        
        # WebGL
        webgl = random.choice(WEBGL_CONFIGS)
        
        # Generate hashes
        canvas_hash = self._generate_hash("canvas")
        audio_hash = self._generate_hash("audio")
        
        # MAC address
        mac_address = self._generate_mac_address()
        
        # Create fingerprint
        fingerprint = Fingerprint(
            user_agent=user_agent,
            browser_name=browser_config["name"],
            browser_version=browser_version,
            browser_engine=browser_config["engine"],
            platform=platform,
            os_name=os_config["name"],
            os_version=os_version,
            device_type=device_type,
            screen_width=resolution["width"],
            screen_height=resolution["height"],
            screen_resolution=f"{resolution['width']}x{resolution['height']}",
            color_depth=random.choice([24, 32]),
            pixel_ratio=random.choice([1.0, 1.25, 1.5, 2.0, 3.0]),
            language=language,
            languages=languages,
            timezone=tz["name"],
            timezone_offset=tz["offset"] * 60,
            ip_address=ip_address,
            connection_type=random.choice(["wifi", "ethernet", "4g", "5g"]),
            cpu_cores=cpu_cores,
            device_memory=device_memory,
            max_touch_points=max_touch_points,
            webgl_vendor=webgl["vendor"],
            webgl_renderer=webgl["renderer"],
            canvas_hash=canvas_hash,
            audio_hash=audio_hash,
            do_not_track=random.choice([None, "1", "0"]),
            cookies_enabled=True,
            local_storage=True,
            session_storage=True,
            indexed_db=True,
            mac_address=mac_address,
            fingerprint_hash=""
        )
        
        # Generate unique fingerprint hash
        fingerprint.fingerprint_hash = self._generate_fingerprint_hash(fingerprint)
        
        return fingerprint
    
    def generate_batch(self, count: int, **kwargs) -> List[Fingerprint]:
        """
        Generate multiple fingerprints.
        
        Args:
            count: Number of fingerprints to generate
            **kwargs: Arguments passed to generate()
        
        Returns:
            List of Fingerprint objects
        """
        return [self.generate(**kwargs) for _ in range(count)]
    
    def _generate_user_agent(
        self,
        browser: str,
        browser_version: str,
        os: str,
        os_version: str,
        device_type: str
    ) -> str:
        """Generate a realistic user agent string."""
        os_config = OPERATING_SYSTEMS[os]
        
        # Format OS version for user agent
        if os == "windows":
            os_ua = f"Windows NT {'10.0' if os_version == '10' else '11.0'}"
        elif os == "macos":
            os_ua = f"Macintosh; Intel Mac OS X {os_version.replace('.', '_')}"
        elif os == "linux":
            os_ua = f"X11; Linux {os_version}"
        elif os == "android":
            os_ua = f"Linux; Android {os_version}"
        elif os == "ios":
            os_ua = f"iPhone; CPU iPhone OS {os_version.replace('.', '_')} like Mac OS X"
        else:
            os_ua = os_config["user_agent_part"].format(version=os_version)
        
        # Build user agent based on browser
        if browser == "chrome":
            return f"Mozilla/5.0 ({os_ua}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version} Safari/537.36"
        elif browser == "firefox":
            return f"Mozilla/5.0 ({os_ua}; rv:{browser_version}) Gecko/20100101 Firefox/{browser_version}"
        elif browser == "safari":
            return f"Mozilla/5.0 ({os_ua}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{browser_version} Safari/605.1.15"
        elif browser == "edge":
            return f"Mozilla/5.0 ({os_ua}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version} Safari/537.36 Edg/{browser_version}"
        
        return f"Mozilla/5.0 ({os_ua})"
    
    def _generate_private_ip(self) -> str:
        """Generate a private IP address."""
        ranges = [
            (10, 0, 0, 0, 255, 255, 255),      # 10.0.0.0/8
            (172, 16, 0, 0, 31, 255, 255),     # 172.16.0.0/12
            (192, 168, 0, 0, 0, 255, 255),     # 192.168.0.0/16
        ]
        
        r = random.choice(ranges)
        return f"{r[0]}.{random.randint(r[1], r[4])}.{random.randint(r[2], r[5])}.{random.randint(r[3], r[6])}"
    
    def _generate_mac_address(self) -> str:
        """Generate a random MAC address."""
        return ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)])
    
    def _generate_hash(self, prefix: str) -> str:
        """Generate a random hash."""
        data = f"{prefix}_{random.random()}_{random.randint(0, 1000000)}"
        return hashlib.sha256(data.encode()).hexdigest()[:32]
    
    def _generate_fingerprint_hash(self, fp: Fingerprint) -> str:
        """Generate a unique hash for the fingerprint."""
        data = f"{fp.user_agent}|{fp.screen_resolution}|{fp.timezone}|{fp.language}|{fp.webgl_renderer}"
        return hashlib.sha256(data.encode()).hexdigest()


def generate_fingerprint() -> Dict[str, Any]:
    """
    Generate a single fingerprint (backward compatible function).
    
    Returns:
        Dictionary containing fingerprint information
    """
    generator = FingerprintGenerator()
    fingerprint = generator.generate()
    return fingerprint.to_dict()


if __name__ == "__main__":
    # Demo
    generator = FingerprintGenerator()
    fp = generator.generate()
    
    print("Generated Fingerprint:")
    print("-" * 40)
    for key, value in fp.to_dict().items():
        print(f"{key}: {value}")
