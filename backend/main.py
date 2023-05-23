from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.auth.router import auth_router
from src.student.router import student_router
from src.instructor.router import instructor_router
from src.database.db import Base, engine

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(student_router, prefix="/students", tags=["students"])
app.include_router(instructor_router, prefix="/instructors", tags=["instructors"])


# Middleware to log requests and responses
@app.middleware("http")
async def log_requests(request, call_next):
    # Log the request
    print(f"Request: {request.method} {request.url}")
    # Call the next middleware
    response = await call_next(request)
    # Log the response
    print(f"Response: {response.status_code}")
    return response
