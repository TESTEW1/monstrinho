FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia apenas o arquivo de requisitos primeiro (ajuda no cache e evita erros)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Agora copia todo o resto dos arquivos do GitHub para o container
COPY . .

# Comando para rodar o bot
CMD ["python", "bot.py"]
