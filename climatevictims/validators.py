from django.core.exceptions import ValidationError

def Climatevictims_v(value):
    filesize=value.size
    if filesize>10000000:
        raise ValidationError("maximum size is 20 mb")