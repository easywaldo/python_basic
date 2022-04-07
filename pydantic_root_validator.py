from pydantic import BaseModel, ValidationError, root_validator


class UserModel(BaseModel):
    username: str
    password1: str
    password2: str

    @root_validator(pre=True)
    def check_card_number_omitted(cls, values):
        pw1, pw2 = values.get('password1'), values.get('password2')
        card_number = values.get('card_number')
        print(pw1)
        print(pw2)
        print(card_number)
        if len(pw1) > 0 and len(pw2) > 0 and card_number is None:
            raise ValueError('card_number should be included')
        return values

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get('password1'), values.get('password2')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return values


try:
    UserModel(
        username='waldo',
        password1='pw2',
        password2='pw2',
        card_number=None,
    )
except ValidationError as e:
    print(e)

try:
    UserModel(
        username='waldo',
        password1='pw1',
        password2='pw2',
        card_number='1234',
    )
except ValidationError as e:
    print(e)
