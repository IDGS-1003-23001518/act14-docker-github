from fastapi import FastAPI

app = FastAPI(title="Act 14 Docker en GitHub", version="1.0.0")


@app.get("/")
def read_root():
    return {"mensaje": "API publicada desde GitHub Container Registry", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "ok"}