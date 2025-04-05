FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Definir o comando para rodar a aplicação
CMD ["python", "main.py"]
