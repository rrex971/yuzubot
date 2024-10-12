import uvicorn
import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def get_code(code: str, state: int):
    print(code, state)
    asyncio.run_coroutine_threadsafe(userAuthenticate(bot, auth, code, state, c, db), loop)
    html_content=open('static/success.html')
    return HTMLResponse(content=html_content.read())

def run_server(loop1, auth1, bot1, userauth, cur, dab):
    global loop, auth, bot, userAuthenticate, c, db
    loop=loop1
    auth=auth1
    bot=bot1
    c = cur
    db = dab

    userAuthenticate=userauth
    config = uvicorn.Config(app, host="localhost", port=1727)
    server = uvicorn.Server(config)
    server.run()

if __name__ == "__main__":
    run_server()