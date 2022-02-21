from enum import Enum


class TestEnumType(Enum):
    TEST_MODE = (1000, "TEST MODE")

    def __init__(self, code: int, message: str):
        self.code: int = code
        self.message: str = message

    @property
    def response(self) -> dict:
        return {"code": self.code, "message": self.message}

    def __str__(self) -> str:
        return f'test enum values spec: code=>{self.code}, '
        'message=>{self.message}'


myEnum = TestEnumType.TEST_MODE
print(myEnum.response)
print(str(myEnum))
