from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # アプリの設定や初期化コードをここに追加
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ブループリントの登録
    from . import main
    app.register_blueprint(main.bp)

    return app

app = create_app()
