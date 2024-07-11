FROM python:3.11.9

COPY . .

RUN poetry add fastapi, uvicorn, sqlalchemy, aiosqlite

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]