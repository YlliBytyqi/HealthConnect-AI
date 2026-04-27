from collections import defaultdict

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.notification_connections: dict[int, list[WebSocket]] = defaultdict(list)
        self.chat_rooms: dict[str, list[WebSocket]] = defaultdict(list)

    async def connect_notifications(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.notification_connections[user_id].append(websocket)

    def disconnect_notifications(self, user_id: int, websocket: WebSocket):
        if websocket in self.notification_connections[user_id]:
            self.notification_connections[user_id].remove(websocket)

    async def push_notification(self, user_id: int, message: dict):
        for ws in self.notification_connections[user_id]:
            await ws.send_json(message)

    async def connect_chat(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        self.chat_rooms[room_id].append(websocket)

    def disconnect_chat(self, room_id: str, websocket: WebSocket):
        if websocket in self.chat_rooms[room_id]:
            self.chat_rooms[room_id].remove(websocket)

    async def broadcast_chat(self, room_id: str, message: dict):
        for ws in self.chat_rooms[room_id]:
            await ws.send_json(message)


manager = ConnectionManager()
