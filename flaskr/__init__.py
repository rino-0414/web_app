from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # データベース設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0414@localhost/calendar_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # SQLAlchemyの初期化
    db.init_app(app)

    # テーブル作成
    with app.app_context():
        db.create_all()

    # ブループリントの登録
    from .main import bp
    app.register_blueprint(bp)

    return app
