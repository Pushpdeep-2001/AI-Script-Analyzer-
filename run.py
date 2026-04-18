import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

PORT=os.getenv("PORT")
HOST=os.getenv("HOST")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
