class Hello:
    def world(self) -> int:
        return 1000
    
class World:
    pass

hello: Hello = Hello()
print(hello.world())


def foo(instance: Hello) -> int:
    return instance.world()

print(foo(hello))


world: World = World()
print(foo(world))