import pytest
from pydantic import ValidationError
from app.schemas import UserCreate


def test_email_is_lowercased():
    new_user = UserCreate(email='EXAMPLE@EXAMPLE.COM', password='longenough')
    assert new_user.email == "example@example.com"


def test_invalid_email_is_Rejected():
    with pytest.raises(ValidationError):
        UserCreate(email='invalid-email', password='longenough')

def test_password_shorter_than_8_is_rejected():
    with pytest.raises(ValidationError) as exc_info:
        UserCreate(email='example@example.com', password='short')
    assert exc_info.value.errors()[0]["loc"] == ("password",)


def test_password_with_length_7_is_rejected():
    with pytest.raises(ValidationError) as exc_info:
        UserCreate(email='example@example.com', password='1234567')
    assert exc_info.value.errors()[0]["loc"] == ("password",)


def test_password_shorter_than_9_is_accepted():
    new_user = UserCreate(email='example@example.COM', password='longenough')

    assert new_user.email == "example@example.com"

