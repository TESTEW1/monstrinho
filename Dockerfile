FROM python:3.10-slim

# Define onde as coisas vão acontecer dentro do servidor
WORKDIR /app

# Instala a biblioteca do Discord
RUN pip install discord.py

# Copia TODOS os seus arquivos (bot.py, estrelas.json, etc) para o servidor
COPY . .

# Comando para ligar o bot
CMD ["python", "bot.py"]
