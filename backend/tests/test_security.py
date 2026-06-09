"""
Security Tests
"""

import pytest
from app.core.security import hash_password, verify_password, create_access_token, decode_token


def test_password_hashing():
    """Test password hashing."""
    password = "test_password_123"
    hashed = hash_password(password)
    
    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("wrong_password", hashed)


def test_jwt_token_creation():
    """Test JWT token creation and decoding."""
    subject = "test_user_id"
    token = create_access_token(subject)
    
    assert token is not None
    decoded = decode_token(token)
    
    assert decoded is not None
    assert decoded["sub"] == subject
    assert decoded["type"] == "access"


def test_invalid_token_decoding():
    """Test decoding invalid token."""
    invalid_token = "invalid.token.here"
    decoded = decode_token(invalid_token)
    
    assert decoded is None