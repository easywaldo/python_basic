from enum import Enum


class Skill(Enum):
    HTML = ("HTML", "hypertext markup language")
    CSS = ("CSS", "cascading style sheets")
    JS = ("JS", "javascript")

    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

    @classmethod
    def get_most_popular(cls):
        return cls.JS

    def lower_title(self):
        return self.title.lower()


print(Skill.HTML.value)
print(Skill.HTML.description)
print(Skill.HTML.title)
print(Skill.get_most_popular())
print(Skill.CSS.lower_title())
