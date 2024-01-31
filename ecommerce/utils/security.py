from datetime import datetime, timedelta
import jwt
from django.conf import settings

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

import secrets
import hashlib
from django.core.mail import send_mail

def generate_verification_token():
    token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    return token_hash

def send_verification_email(email, verification_link):
    send_mail(
        'Verify Your Email',
        f'Please click on the link to verify your email: {verification_link}',
        'from@example.com',
        [email],
        fail_silently=False,
    )
