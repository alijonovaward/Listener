from fastapi import FastAPI, Request
from datetime import datetime
import json

app = FastAPI()


# Webhook endpoint
@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
    except:
        data = await request.body()
        data = data.decode("utf-8")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {json.dumps(data, ensure_ascii=False, indent=4)}\n"

    with open("webhook_log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)

    return {"status": "success", "message": "Webhook logged."}
