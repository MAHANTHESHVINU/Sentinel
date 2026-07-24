from fastapi import FastAPI

app = FastAPI(
    title="Sentinel API",
    version="0.1.0",
    description="Enterprise AI Agent Governance Platform"
)


@app.get("/")
def root():
    return {
        "name": "Sentinel API",
        "version": "0.1.0",
        "status": "healthy"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
