from flask import Flask, render_template
from flask_migrate import Migrate
from models.User import db 
from routes.user import user_bp  

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/api/v1')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(DEBUG=True, port=5000)