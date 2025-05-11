# Use Python 3.11 slim como base
FROM python:3.12-alpine

RUN pip install faker

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . .

# Exponha a porta
EXPOSE 8000

# Defina o comando para iniciar a aplicação
CMD ["python", "main.py"]
