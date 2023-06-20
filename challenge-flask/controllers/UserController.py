from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy 
from models.User import db, User
import json

def index():
    try:
        session = db.session()
        users = session.query(User).all()
        users_json = [user.serialize() for user in users]
        session.close()
        return Response(json.dumps(users_json))
    except Exception as e:
        session.rollback()
        return { 'err': 'Erro ao listar usuários', 'status': 400 }

def create():
    body = request.get_json()
    session = db.session()
    try:
        user = User(
            username=body['username'],
            name=body['name'],
            phone_number=body['phone_number'],
            address=body['address'],
            cpf=body['cpf']
        )
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return { 'err': 'Erro ao tentar criar o usuário', 'status': 400 }
    finally:
        session.close()        
    
def show(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return { 'err': 'Não foi possível retornar o usuário', 'status': 400 }
    finally:
        session.close()  

def update(user_id):
    session = db.session()
    try:
        body = request.get_json()
        user = session.query(User).get(user_id)
        if body and body['username']:
            user.username = body['username']
        if body and body['name']:
            user.name = body['name']
        if body and body['phone_number']:
            user.phone_number = body['phone_number']
        if body and body['address']:
            user.address = body['address']
        if body and body['cpf']:
            user.cpf = body['cpf']
        session.commit()

        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return { 'err': 'Não foi possível editar o usuário', 'status': 400 }
    finally:
        session.close()    

def delete(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        
        return { 'success': 'Usuário apagado com sucesso'}
    except Exception as e:
        session.rollback() 
        return { 'err': 'Não foi possível apagar o usuário.'}
    finally:
        session.close()

    