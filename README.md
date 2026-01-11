<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-lightgrey.svg" alt="Platform">
</p>

<h1 align="center">👻 PhantomID Generator</h1>

<p align="center">
  <strong>Professional Fake Identity & Digital Fingerprint Generator</strong>
</p>

<p align="center">
  Generate realistic fake identities and browser fingerprints for security testing,<br>
  privacy protection, and cybersecurity research.
</p>

---

## ✨ Features

### Identity Generation
- **Personal Information** - Names, addresses, birthdates, phone numbers
- **Financial Data** - Credit cards, bank accounts (fake/test data)
- **Government IDs** - SSN, passport numbers, driver's licenses
- **Professional Info** - Companies, job titles, websites
- **Profile Pictures** - Auto-generated avatar URLs
- **Multi-locale Support** - 15+ languages and regions

### Digital Fingerprints
- **Browser Fingerprints** - User agents, engines, versions
- **Device Information** - OS, platform, screen resolution
- **Hardware Specs** - CPU cores, memory, GPU info
- **WebGL Data** - Vendor and renderer information
- **Canvas/Audio Hashes** - Unique fingerprint identifiers
- **Network Info** - IP addresses, connection types

### User Interfaces
- **Command Line** - Fast batch generation
- **GUI Application** - User-friendly Tkinter interface
- **Python API** - Integrate into your projects

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/BlackOussema/PhantomID-Generator.git
cd PhantomID-Generator

# Install dependencies
pip install -r requirements.txt
```

### Command Line Usage

```bash
# Generate profiles interactively
python main.py

# Generate specific number of profiles
python -c "from main import generate_multiple_profiles; generate_multiple_profiles(10)"
```

### GUI Application

```bash
# Launch the graphical interface
python gui.py
```

### Python API

```python
from identity_generator import IdentityGenerator
from fingerprint_generator import FingerprintGenerator

# Generate a fake identity
id_gen = IdentityGenerator(locale="en_US")
identity = id_gen.generate(
    include_financial=True,
    include_professional=True,
    min_age=25,
    max_age=45
)
print(identity.to_dict())

# Generate a browser fingerprint
fp_gen = FingerprintGenerator()
fingerprint = fp_gen.generate(
    device_type="Desktop",
    browser="chrome",
    os="windows"
)
print(fingerprint.to_dict())
```

---

## 📁 Project Structure

```
PhantomID-Generator/
├── identity_generator.py    # Identity generation module
├── fingerprint_generator.py # Fingerprint generation module
├── main.py                  # CLI entry point
├── gui.py                   # Tkinter GUI application
├── profiles/                # Generated profile storage
│   └── *.json              # Individual profile files
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🔧 Configuration

### Supported Locales

```python
SUPPORTED_LOCALES = [
    "en_US", "en_GB", "fr_FR", "de_DE", "es_ES",
    "it_IT", "pt_BR", "ar_SA", "ja_JP", "zh_CN",
    "ru_RU", "nl_NL", "pl_PL", "tr_TR", "ar_TN"
]
```

### Device Types

- `Desktop` - Full desktop computers
- `Laptop` - Portable computers
- `Mobile` - Smartphones
- `Tablet` - Tablet devices

### Browsers

- `chrome` - Google Chrome
- `firefox` - Mozilla Firefox
- `safari` - Apple Safari
- `edge` - Microsoft Edge

### Operating Systems

- `windows` - Windows 10/11
- `macos` - macOS versions
- `linux` - Linux distributions
- `android` - Android devices
- `ios` - iOS devices

---

## 📊 Sample Output

### Identity

```json
{
  "full_name": "John Smith",
  "first_name": "John",
  "last_name": "Smith",
  "username": "john.smith92",
  "email": "john.smith@gmail.com",
  "phone": "+1-555-123-4567",
  "address": "123 Main Street",
  "city": "New York",
  "country": "United States",
  "postal_code": "10001",
  "birthdate": "1992-05-15",
  "age": 31,
  "gender": "male",
  "national_id": "123-45-6789",
  "credit_card": "4532015112830366",
  "company": "Tech Solutions Inc.",
  "job_title": "Software Engineer",
  "profile_pic_url": "https://api.multiavatar.com/123456.png"
}
```

### Fingerprint

```json
{
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
  "browser_name": "Chrome",
  "browser_version": "120.0.0.0",
  "platform": "Win64",
  "os_name": "Windows",
  "os_version": "10",
  "device_type": "Desktop",
  "screen_resolution": "1920x1080",
  "language": "en-US",
  "timezone": "America/New_York",
  "cpu_cores": 8,
  "device_memory": 16,
  "webgl_vendor": "Google Inc. (NVIDIA)",
  "webgl_renderer": "ANGLE (NVIDIA GeForce RTX 3080)",
  "fingerprint_hash": "a1b2c3d4e5f6..."
}
```

---

## 🔒 Use Cases

### Security Testing
- Test authentication systems with varied user profiles
- Validate input sanitization with diverse data
- Simulate different browser environments

### Privacy Research
- Study browser fingerprinting techniques
- Develop anti-tracking solutions
- Test privacy-focused applications

### Development & QA
- Generate test data for applications
- Populate databases with realistic data
- Test internationalization (i18n)

### Education
- Learn about digital fingerprinting
- Understand identity data structures
- Study privacy implications

---

## ⚠️ Legal Disclaimer

**This tool is for educational and authorized testing purposes only.**

- Do NOT use generated data for fraud or illegal activities
- Do NOT use fake identities to deceive real people or services
- Generated credit card numbers are NOT valid for transactions
- Always comply with applicable laws and regulations
- The authors are not responsible for misuse

### Ethical Guidelines

1. Use only in controlled testing environments
2. Never submit fake data to real services
3. Respect privacy and data protection laws
4. Use for learning and legitimate security research

---

## 📋 Requirements

```
faker>=18.0.0
```

### Optional (for GUI)
```
tkinter (usually included with Python)
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Ideas for Contribution
- Add more locales
- Improve fingerprint realism
- Add export formats (CSV, XML)
- Create web interface
- Add more avatar services

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ghariani Oussema**
- GitHub: [@BlackOussema](https://github.com/BlackOussema)
- Email: oussemaghariani17@gmail.com
- Role: Cyber Security Researcher & Full-Stack Developer

---

<p align="center">
  Made with ❤️ in Tunisia 🇹🇳
</p>
