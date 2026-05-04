import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # 基本設定
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL', f"sqlite:///{os.path.join(app.instance_path, 'database.db')}"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # 確保 instance 資料夾存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 初始化資料庫
    db.init_app(app)

    # 註冊藍圖 (Blueprints)
    from app.routes.main import main_bp
    from app.routes.recipe import recipe_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(recipe_bp)

    return app
