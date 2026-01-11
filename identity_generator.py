#!/usr/bin/env python3
"""
PhantomID Identity Generator

Generates realistic fake identities for security testing and privacy protection.

Author: Ghariani Oussema
License: MIT
"""

import random
import string
from dataclasses import dataclass, asdict
from datetime import date, timedelta
from typing import Optional, Dict, Any, List

try:
    from faker import Faker
    FAKER_AVAILABLE = True
except ImportError:
    FAKER_AVAILABLE = False

# Locales for international identity generation
SUPPORTED_LOCALES = [
    "en_US", "en_GB", "fr_FR", "de_DE", "es_ES", 
    "it_IT", "pt_BR", "ar_SA", "ja_JP", "zh_CN",
    "ru_RU", "nl_NL", "pl_PL", "tr_TR", "ar_TN"
]

# Avatar services
AVATAR_SERVICES = [
    "https://api.multiavatar.com/{seed}.png",
    "https://avatars.dicebear.com/api/identicon/{seed}.svg",
    "https://robohash.org/{seed}?set=set4",
    "https://ui-avatars.com/api/?name={name}&background=random",
]


@dataclass
class Identity:
    """Represents a generated fake identity."""
    full_name: str
    first_name: str
    last_name: str
    username: str
    email: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    birthdate: str
    age: int
    gender: str
    national_id: str
    passport_number: Optional[str] = None
    driver_license: Optional[str] = None
    credit_card: Optional[str] = None
    credit_card_expiry: Optional[str] = None
    credit_card_cvv: Optional[str] = None
    bank_account: Optional[str] = None
    company: Optional[str] = None
    job_title: Optional[str] = None
    website: Optional[str] = None
    profile_pic_url: Optional[str] = None
    locale: str = "en_US"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


class IdentityGenerator:
    """
    Professional fake identity generator.
    
    Generates realistic fake identities with various personal,
    financial, and professional information.
    """
    
    def __init__(self, locale: str = "en_US", seed: Optional[int] = None):
        """
        Initialize the identity generator.
        
        Args:
            locale: Locale for generating localized data
            seed: Random seed for reproducible generation
        """
        if not FAKER_AVAILABLE:
            raise ImportError("Faker library is required. Install with: pip install faker")
        
        self.locale = locale if locale in SUPPORTED_LOCALES else "en_US"
        self.faker = Faker(self.locale)
        
        if seed is not None:
            Faker.seed(seed)
            random.seed(seed)
    
    def generate(
        self,
        include_financial: bool = True,
        include_professional: bool = True,
        min_age: int = 18,
        max_age: int = 65,
        gender: Optional[str] = None
    ) -> Identity:
        """
        Generate a complete fake identity.
        
        Args:
            include_financial: Include credit card and bank info
            include_professional: Include job and company info
            min_age: Minimum age for the identity
            max_age: Maximum age for the identity
            gender: Specific gender ('male', 'female', or None for random)
        
        Returns:
            Generated Identity object
        """
        # Determine gender
        if gender is None:
            gender = random.choice(["male", "female"])
        
        # Generate name based on gender
        if gender == "male":
            first_name = self.faker.first_name_male()
        else:
            first_name = self.faker.first_name_female()
        
        last_name = self.faker.last_name()
        full_name = f"{first_name} {last_name}"
        
        # Generate birthdate and calculate age
        birthdate = self.faker.date_of_birth(minimum_age=min_age, maximum_age=max_age)
        age = self._calculate_age(birthdate)
        
        # Generate username variations
        username = self._generate_username(first_name, last_name, birthdate.year)
        
        # Generate email
        email = self._generate_email(first_name, last_name)
        
        # Generate address components
        address = self.faker.street_address()
        city = self.faker.city()
        country = self.faker.country()
        postal_code = self.faker.postcode()
        
        # Generate IDs
        national_id = self.faker.ssn()
        passport_number = self._generate_passport_number()
        driver_license = self._generate_driver_license()
        
        # Financial info
        credit_card = None
        credit_card_expiry = None
        credit_card_cvv = None
        bank_account = None
        
        if include_financial:
            credit_card = self.faker.credit_card_number()
            credit_card_expiry = self.faker.credit_card_expire()
            credit_card_cvv = str(random.randint(100, 999))
            bank_account = self._generate_bank_account()
        
        # Professional info
        company = None
        job_title = None
        website = None
        
        if include_professional:
            company = self.faker.company()
            job_title = self.faker.job()
            website = f"https://{self.faker.domain_name()}"
        
        # Profile picture
        seed = random.randint(100000, 999999)
        avatar_template = random.choice(AVATAR_SERVICES)
        profile_pic_url = avatar_template.format(
            seed=seed,
            name=full_name.replace(" ", "+")
        )
        
        return Identity(
            full_name=full_name,
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone=self.faker.phone_number(),
            address=address,
            city=city,
            country=country,
            postal_code=postal_code,
            birthdate=str(birthdate),
            age=age,
            gender=gender,
            national_id=national_id,
            passport_number=passport_number,
            driver_license=driver_license,
            credit_card=credit_card,
            credit_card_expiry=credit_card_expiry,
            credit_card_cvv=credit_card_cvv,
            bank_account=bank_account,
            company=company,
            job_title=job_title,
            website=website,
            profile_pic_url=profile_pic_url,
            locale=self.locale
        )
    
    def generate_batch(
        self,
        count: int,
        **kwargs
    ) -> List[Identity]:
        """
        Generate multiple identities.
        
        Args:
            count: Number of identities to generate
            **kwargs: Arguments passed to generate()
        
        Returns:
            List of Identity objects
        """
        return [self.generate(**kwargs) for _ in range(count)]
    
    def _calculate_age(self, birthdate: date) -> int:
        """Calculate age from birthdate."""
        today = date.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age
    
    def _generate_username(
        self,
        first_name: str,
        last_name: str,
        birth_year: int
    ) -> str:
        """Generate a realistic username."""
        patterns = [
            f"{first_name.lower()}{last_name.lower()}",
            f"{first_name.lower()}.{last_name.lower()}",
            f"{first_name.lower()}_{last_name.lower()}",
            f"{first_name.lower()}{random.randint(1, 999)}",
            f"{first_name[0].lower()}{last_name.lower()}{str(birth_year)[-2:]}",
            f"{last_name.lower()}{first_name[0].lower()}{random.randint(1, 99)}",
        ]
        return random.choice(patterns)
    
    def _generate_email(self, first_name: str, last_name: str) -> str:
        """Generate a realistic email address."""
        domains = [
            "gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
            "protonmail.com", "icloud.com", "mail.com", "aol.com"
        ]
        
        patterns = [
            f"{first_name.lower()}.{last_name.lower()}",
            f"{first_name.lower()}{last_name.lower()}",
            f"{first_name[0].lower()}{last_name.lower()}",
            f"{first_name.lower()}{random.randint(1, 999)}",
        ]
        
        local_part = random.choice(patterns)
        domain = random.choice(domains)
        return f"{local_part}@{domain}"
    
    def _generate_passport_number(self) -> str:
        """Generate a fake passport number."""
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=7))
        return f"{letters}{numbers}"
    
    def _generate_driver_license(self) -> str:
        """Generate a fake driver's license number."""
        letters = ''.join(random.choices(string.ascii_uppercase, k=1))
        numbers = ''.join(random.choices(string.digits, k=12))
        return f"{letters}{numbers}"
    
    def _generate_bank_account(self) -> str:
        """Generate a fake bank account number."""
        return ''.join(random.choices(string.digits, k=16))


def generate_fake_identity(locale: str = "en_US") -> Dict[str, Any]:
    """
    Generate a single fake identity (backward compatible function).
    
    Args:
        locale: Locale for generating localized data
    
    Returns:
        Dictionary containing identity information
    """
    generator = IdentityGenerator(locale=locale)
    identity = generator.generate()
    return identity.to_dict()


if __name__ == "__main__":
    # Demo
    generator = IdentityGenerator(locale="en_US")
    identity = generator.generate()
    
    print("Generated Identity:")
    print("-" * 40)
    for key, value in identity.to_dict().items():
        if value:
            print(f"{key}: {value}")
