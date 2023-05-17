"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi80ie4dadc9vm2g140-a.oregon-postgres.render.com",
        database="todo_4f1k",
        user="root",
        password="FILM5gDW3YRdSW17G951Qg0uEuzPA6uV")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
