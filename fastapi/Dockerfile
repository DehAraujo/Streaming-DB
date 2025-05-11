FROM python:3.11-bullseye

WORKDIR /app
RUN apt-get update && apt-get upgrade -y
# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpq-dev \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Instala dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte
COPY . .

# Exponha a porta padrão
EXPOSE 8000

# Suba a aplicação FastAPI usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
