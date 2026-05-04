from datetime import datetime
from app import db

class Interaction(db.Model):
    __tablename__ = 'interactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id', ondelete='CASCADE'))
    interaction_type = db.Column(db.String(20), nullable=False) # 'view', 'search', 'like'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Interaction {self.interaction_type} for recipe {self.recipe_id}>'

    @classmethod
    def log(cls, recipe_id, interaction_type):
        """記錄使用者行為"""
        try:
            new_interaction = cls(recipe_id=recipe_id, interaction_type=interaction_type)
            db.session.add(new_interaction)
            db.session.commit()
            return new_interaction
        except Exception as e:
            db.session.rollback()
            print(f"Error logging interaction: {e}")
            return None

    @classmethod
    def get_stats(cls):
        """取得統計數據 (進階推薦用)"""
        # 這裡可以實作更複雜的查詢
        return cls.query.all()
