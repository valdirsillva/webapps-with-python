from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy 
from models.User import db, User
import json

def index():
    session = request.get_json()
    users = session.query(User).all()
    users_json = [user.serialize() for user in users ]
    session.close()
    return Response(json.dumps(users_json))
    