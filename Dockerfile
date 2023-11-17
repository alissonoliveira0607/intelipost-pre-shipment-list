# Use a imagem base do Python
FROM python:3.8-slim

# Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Criação do diretório de trabalho
WORKDIR /app

# Instalação das dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do código fonte para o contêiner
COPY . /app/

# Expor a porta utilizada pela aplicação (por padrão, o Flask usa a porta 5000)
EXPOSE 5000

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
