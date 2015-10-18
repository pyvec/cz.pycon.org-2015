import psycopg2
import psycopg2.extras
from config import db


class BaseModel:
    def __init__(self):
        self.conn = psycopg2.connect(**db)
        self.conn.autocommit = True

        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
