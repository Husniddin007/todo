import random


def sms_code_validate():
    return str(random.randint(1000,9999))

code = sms_code_validate()
print(f'okk {code}')