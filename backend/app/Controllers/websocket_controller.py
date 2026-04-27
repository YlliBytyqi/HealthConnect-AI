from datetime import datetime, timezone

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.Services.websocket_service import manager

router = APIRouter(tags=["WebSockets"])


@router.websocket("/ws/notifications/{user_id}")
async def notifications_socket(websocket: WebSocket, user_id: int):
    await manager.connect_notifications(user_id, websocket)
    try:
        while True:
            incoming = await websocket.receive_text()
            await manager.push_notification(
                user_id,
                {"type": "notification_ack", "payload": incoming, "timestamp": datetime.now(timezone.utc).isoformat()},
            )
    except WebSocketDisconnect:
        manager.disconnect_notifications(user_id, websocket)


@router.websocket("/ws/chat/{room_id}")
async def chat_socket(websocket: WebSocket, room_id: str):
    await manager.connect_chat(room_id, websocket)
    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast_chat(
                room_id,
                {"room_id": room_id, "message": message, "timestamp": datetime.now(timezone.utc).isoformat()},
            )
    except WebSocketDisconnect:
        manager.disconnect_chat(room_id, websocket)
