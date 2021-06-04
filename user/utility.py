from .models import UserProfile
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def isvalid(context):
    # import pdb
    # pdb.set_trace()
    if context.get('first_name') is None:
        return False, 'First name not provided'
    else:
        first_name = context['first_name'].strip()
        if len(first_name) == 0:
            msg = 'First name not valid'
            return False, msg

    if context.get('last_name') is None:
        msg = 'Last name not provided'
        return False, msg
    else:
        last_name = context['last_name'].strip()
        if len(last_name) == 0:
            msg = 'Last name not valid'
            return False, msg

    if context.get('phone') is None:
        msg = 'Phone number not provided'
        return False, msg
    else:
        phone = context['phone'].strip()
        if len(phone) == 0:
            msg = 'Phone number not valid'
            return False, msg

        # import pdb
        # pdb.set_trace()

        user = UserProfile.objects.filter(phone=context.get('phone')).first()
        if user is not None:
            msg = 'Phone number already registered'
            return False, msg

    if context.get('password') is None:
        msg = 'Password not Provided'
        return False, msg
    else:
        password = context['password'].strip()
        if len(password) < 8:
            msg = 'Length of password must be greater than 8 char'
            return False, msg

    email = context.get('email')
    if email is not None and len(email) > 0:
        email = email.strip()
        try:
            validate_email(email)
            valid_email = True
        except ValidationError:
            msg = "Email is not Valid!!"
            return False, msg


    return True, " "