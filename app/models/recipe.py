from datetime import datetime
from app import db

class Recipe(db.Model):
    __tablename__ = 'recipes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Recipe {self.title}>'

    @classmethod
    def create(cls, data):
        """新增一筆食譜"""
        try:
            new_recipe = cls(**data)
            db.session.add(new_recipe)
            db.session.commit()
            return new_recipe
        except Exception as e:
            db.session.rollback()
            print(f"Error creating recipe: {e}")
            return None

    @classmethod
    def get_all(cls):
        """取得所有食譜"""
        return cls.query.all()

    @classmethod
    def get_by_id(cls, recipe_id):
        """根據 ID 取得單筆食譜"""
        return cls.query.get(recipe_id)

    @classmethod
    def update(cls, recipe_id, data):
        """更新食譜記錄"""
        try:
            recipe = cls.get_by_id(recipe_id)
            if recipe:
                for key, value in data.items():
                    if hasattr(recipe, key):
                        setattr(recipe, key, value)
                db.session.commit()
                return recipe
            return None
        except Exception as e:
            db.session.rollback()
            print(f"Error updating recipe: {e}")
            return None

    @classmethod
    def delete(cls, recipe_id):
        """刪除食譜"""
        try:
            recipe = cls.get_by_id(recipe_id)
            if recipe:
                db.session.delete(recipe)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting recipe: {e}")
            return False

    @classmethod
    def search(cls, query):
        """關鍵字搜尋 (標題或食材)"""
        return cls.query.filter(
            (cls.title.like(f'%{query}%')) | 
            (cls.ingredients.like(f'%{query}%'))
        ).all()

    @classmethod
    def get_random(cls):
        """隨機取得一筆食譜 (每日推薦用)"""
        import random
        recipes = cls.get_all()
        return random.choice(recipes) if recipes else None
