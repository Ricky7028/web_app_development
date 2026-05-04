from app import create_app, db
from app.models.recipe import Recipe
from app.models.interaction import Interaction

app = create_app()
with app.app_context():
    print("正在建立資料庫表...")
    db.create_all()
    print("資料庫初始化成功！")
