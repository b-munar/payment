from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv

load_dotenv()

def url_postgresql_for_create_engine(username, host, database, password, port):
    url = URL.create(
        drivername="postgresql",
        username=username,
        host=host,
        database=database,
        password=password,
        port=port
    )
    print(url) 
    return url

def engine(username=os.getenv("PAYMENT_DB_USER"),
       host=os.getenv("PAYMENT_DB_HOST"),
       database=os.getenv("PAYMENT_DB_NAME"),
       password=os.getenv("PAYMENT_DB_PASSWORD"),
       port=os.getenv("PAYMENT_DB_PORT")
       ):
    
    engine = create_engine(
        url_postgresql_for_create_engine(username, host, database, password, port)
    )
    
    return engine