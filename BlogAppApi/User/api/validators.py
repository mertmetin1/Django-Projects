# User/api/validators.py
import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    phone_regex = re.compile(r'^\d{10,15}$')  # Telefon numarası 10 ila 15 rakam arasında olmalı
    if not phone_regex.match(value):
        raise ValidationError(
            "Phone number must be entered as digits only. Between 10 and 15 digits allowed."
        )
# User/api/validators.py
def validate_phone_code(value):
    code_regex = re.compile(r'^\+\d{1,4}$')  # Alan kodu '+123' formatında olmalı
    if not code_regex.match(value):
        raise ValidationError(
            "Phone code must be entered in the format: '+123'. Between 1 and 4 digits allowed."
        )
