from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic import ValidationError


class User(BaseModel):
    id: int
    name: str = 'waldo'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user = User(**external_data)


print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())

print(user.name)

assert user.id == 123
assert user.name == 'waldo'
assert user.__fields_set__ == {'id', 'signup_ts', 'friends'}

try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())
