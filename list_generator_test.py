import abc
from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass
class ListViewModel:
    title: str
    description: str


class ListGenerator(abc.ABC):

    title: str
    description: str

    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

    @property
    @abc.abstractmethod
    def list_id(self) -> str:
        raise NotImplementedError("Not implemendted error")

    def generate(self) -> ListViewModel:
        return ListViewModel(
            title=self.title,
            description=self.description
        )
    
    @classmethod
    def get_name(cls):
        return cls.__name__

    @classmethod
    def get_list(
        cls,
    ) -> List[int]:
        return None


class FirstTestListGenerator(ListGenerator):
    list_id = "first_list"

    def __init__(self, title, description) -> None:
        super().__init__(title, description)

    @staticmethod
    def is_available(is_member) -> bool:
        return is_member

    @classmethod
    def get_list(
        cls,
    ) -> List[int]:
        return [
            x for x in range(10)
        ]
    

class SecondTestListGenerator(ListGenerator):
    list_id = "second_list"

    def __init__(self, title, description) -> None:
        super().__init__(title, description)

    @staticmethod
    def is_available(is_member) -> bool:
        return is_member

    @classmethod
    def get_list(
        cls,
    ) -> List[int]:
        return [
            x + 10 for x in range(10)
        ]


class TestAttrEnum(Enum):
    __attributes__ = ()

    def __new__(cls, *args, **kwargs):
        value = args[0]
        obj = value.__class__.__new__(cls, args[0])
        obj._value_ = value

        attributes = args[1:]
        if len(cls.__attributes__) != len(attributes):
            raise ValueError("not match arguments with attribues")

        for attr, value in zip(cls.__attributes__, attributes):
            setattr(obj, attr, value)

        return obj


class TestListType(int, TestAttrEnum):
    __attributes__ = (
        'list_generator',
        'list_name',
    )

    BRAVO_GROUP = (
        1,
        FirstTestListGenerator,
        FirstTestListGenerator.get_name(),
    )
    DELTA_GROUP = (
        2,
        SecondTestListGenerator,
        SecondTestListGenerator.get_name(),
    )


class TestListSelector(object):
    TARGET_LIST = [
        TestListType.BRAVO_GROUP,
        TestListType.DELTA_GROUP,
    ]


for list_type in TestListSelector.TARGET_LIST:
    generator = list_type.list_generator
    if generator.is_available(True):
        print(f'hello {generator.get_name()}')
    print(generator.get_list())


result: ListViewModel = FirstTestListGenerator(title="test easywaldo", description="this job is test").generate()
print(result)


print(TestListType.__attributes__)