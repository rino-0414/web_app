from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # アプリの設定や初期化コードをここに追加
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # データベース設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0414@localhost/calendar_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # SQLAlchemyの初期化
    db.init_app(app)

    # テーブル作成
    with app.app_context():
        db.create_all()

    # ブループリントの登録
    from . import main
    app.register_blueprint(main.bp)

    return app

app = create_app()
