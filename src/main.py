from fastapi import FastAPI
import uvicorn
from tasks import router as tasks_router

app = FastAPI()
app.include_router(tasks_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
