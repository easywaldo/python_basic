from typing import Optional


class Hello:
    def world(self) -> int:
        return 1000
    
class World:
    pass

hello: Hello = Hello()
print(hello.world())


def foo(instance: "Hello") -> int:
    return instance.world()

print(foo(hello))


world: World = World()


class Node:
    def __init__(self, data: int, node: Optional["Node"] = None):
        self.data = data
        self.node = node
        
node2 = Node(100)
node1 = Node(27, node2)
node0 = Node(30, node1)



