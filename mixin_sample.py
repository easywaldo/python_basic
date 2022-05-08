class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))
class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "easywaldo"
t.feature = "python"
t.age = "forthy two"
t.dump()


print(Thing.mro())