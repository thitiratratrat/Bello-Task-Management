import websockets
import asyncio
import json


class Bello:
    def __init__(self):
        self.__websocket = None
        self.__uri = "ws://localhost:8765"

    async def __connect(self):
        self.__websocket = await websockets.client.connect(self.__uri)
        await self.__websocket.send(json.dumps({"action": "connected"}))

    def __handleMessage(self, message):
        response = message["response"]

        if response == "existedUsername":
            print("existed username! Fail to create account!")

        elif response == "createdAccount":
            print("account created successsfully")

        else:
            return

    def verifyPassword(self, password):
        pass

    async def signUp(self, username, password):
        await self.__websocket.send(json.dumps({"action": "signUp",
                                                "data": {
                                                    "username": username,
                                                    "password": password}
                                                }))

    async def __handleServer(self):
        async for message in self.__websocket:
            message = json.loads(message)

            self.__handleMessage(message)

    async def start(self):
        await self.__connect()

        task = asyncio.create_task(self.__handleServer())

        await task


if __name__ == '__main__':
    bello = Bello()

    asyncio.get_event_loop().run_until_complete(bello.start())
