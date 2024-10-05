import random


def generate_sms_code():
    return str(random.randint(1000,9999))