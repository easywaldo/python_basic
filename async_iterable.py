import asyncio

class Reader:
    async def readline(self):
        print(".....")
        

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val

r1 = Reader()
loop = asyncio.get_event_loop()
loop.run_until_complete(r1.readline())
loop.close()    