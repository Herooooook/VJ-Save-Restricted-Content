import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21980964"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dafddfc1607628eb9b04d3c2fe3ff7ef")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ajaykr:Fqno6lqyw1RrV6X0@cluster0.axqy4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
