from typing import List
from pydantic import BaseModel, ValidationError, validator


class ParentModel(BaseModel):
    names: List[str]


class ChildModel(ParentModel):
    @validator('names', each_item=True)
    def check_names_not_empty(cls, v):
        assert v != '', 'Empty string are not allowed.'
        return v


try:
    child = ChildModel(names=['Alice', 'Bob', 'Eve', ''])
except ValidationError as e:
    print(e)
else:
    print('No ValidationError caught.')


class ChildModel2(ParentModel):
    @validator('names')
    def check_names_not_empty(cls, v):
        for name in v:
            assert name != '', 'Empty strings are not allowed.'
        return v


try:
    child = ChildModel2(names=['Alice', 'Waldo', 'Eve', 'Bob', ''])
except ValidationError as e:
    print(e)
    """
    1 validation error for ChildModel2
    names
        Empty strings are not allowed. (type=assertion_error)
    """
