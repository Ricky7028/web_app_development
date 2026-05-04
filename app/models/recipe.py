from datetime import datetime
# 假設 db 從 app 的初始化檔案中導入
# from app import db 

class Recipe:
    """
    食譜模型 (純 Python 類別範例，若使用 SQLAlchemy 則繼承 db.Model)
    """
    def __init__(self, id=None, title=None, ingredients=None, instructions=None, image_path=None, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_path = image_path
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    @staticmethod
    def get_all(db_session):
        """取得所有食譜"""
        # return db_session.query(Recipe).all()
        pass

    @staticmethod
    def get_by_id(db_session, recipe_id):
        """根據 ID 取得單一食譜"""
        # return db_session.query(Recipe).filter_by(id=recipe_id).first()
        pass

    @staticmethod
    def create(db_session, data):
        """建立新食譜"""
        # new_recipe = Recipe(**data)
        # db_session.add(new_recipe)
        # db_session.commit()
        # return new_recipe
        pass

    @staticmethod
    def update(db_session, recipe_id, data):
        """更新食譜內容"""
        # recipe = Recipe.get_by_id(db_session, recipe_id)
        # if recipe:
        #     for key, value in data.items():
        #         setattr(recipe, key, value)
        #     recipe.updated_at = datetime.utcnow()
        #     db_session.commit()
        # return recipe
        pass

    @staticmethod
    def delete(db_session, recipe_id):
        """刪除食譜"""
        # recipe = Recipe.get_by_id(db_session, recipe_id)
        # if recipe:
        #     db_session.delete(recipe)
        #     db_session.commit()
        #     return True
        # return False
        pass
