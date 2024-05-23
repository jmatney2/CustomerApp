"""Models for the Customers app"""

from django.core.exceptions import ValidationError
from django.db import models
from localflavor.us.models import USStateField


def validate_zip(value: str):
    """Make sure zip codes are 5-digit numbers"""
    # Check that it is a number
    try:
        int(value)
    except ValueError as exc:
        raise ValidationError("Zip code must be numeric.") from exc

    # Check zip code length
    if len(value) != 5:
        raise ValidationError("Zip code must be 5 characters.")


class Customer(models.Model):
    """Represents a customer"""

    first_name = models.CharField("First Name", max_length=32)
    last_name = models.CharField("Last Name", max_length=32)
    address = models.CharField("Street Address", max_length=128)
    city = models.CharField("City", max_length=32)
    # Using text since zip codes can start with "0"
    zip_code = models.CharField(
        "Zip Code",
        max_length=5,
        validators=[validate_zip],
    )
    state = USStateField("State")

    class Meta:
        unique_together = (
            "first_name",
            "last_name",
            "address",
            "city",
            "zip_code",
            "state",
        )
