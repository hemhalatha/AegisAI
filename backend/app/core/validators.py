import re


def validate_password_strength(value: str) -> str:
    """Validate password strength consistently across the app.

    Raises ValueError on failure to allow use from pydantic validators.
    """
    errors = []
    if len(value) < 8:
        errors.append("at least 8 characters")
    if not re.search(r'[A-Z]', value):
        errors.append("at least one uppercase letter")
    if not re.search(r'\d', value):
        errors.append("at least one digit")
    if not re.search(r'[!@#$%^&*]', value):
        errors.append("at least one special character (!@#$%^&*)")
    if errors:
        raise ValueError("Password must contain: " + ", ".join(errors))
    return value
