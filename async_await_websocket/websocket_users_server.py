import websockets
import asyncio
from websockets import ServerConnection

async def test_server(websocket: ServerConnection):
    async for message in websocket:
        response = f"Сервер получил сообщение {message}"
        await websocket.send(response)

        for _ in range(5):
            await websocket.send(f"{_+1} Сообщение пользователя: {message}")

async def main():
    serv = await websockets.serve(test_server, "localhost", 8765)
    print("Websocket server started at ws://localhost:8765")
    await serv.wait_closed()

asyncio.run(main())