from fastapi import FastAPI
from fastapi.responses import FileResponse
import edge_tts
import uuid

app = FastAPI()

VOICE = "pt-BR-AntonioNeural"

@app.post("/tts")
async def tts(data: dict):

    texto = data["texto"]

    arquivo = f"/tmp/{uuid.uuid4()}.mp3"

    communicate = edge_tts.Communicate(
        text=texto,
        voice=VOICE
    )

    await communicate.save(arquivo)

    return FileResponse(
        arquivo,
        media_type="audio/mpeg",
        filename="audio.mp3"
    )
