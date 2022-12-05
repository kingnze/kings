from django.core.exceptions import ValidationError

def vulnerable_v(value):
    filesize=value.size
    if filesize>10000000:
        raise ValidationError("maximum size is 100 mb")