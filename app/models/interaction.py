from datetime import datetime

class Interaction:
    """
    使用者互動記錄模型
    """
    def __init__(self, id=None, recipe_id=None, interaction_type=None, created_at=None):
        self.id = id
        self.recipe_id = recipe_id
        self.interaction_type = interaction_type
        self.created_at = created_at or datetime.utcnow()

    @staticmethod
    def log(db_session, recipe_id, interaction_type):
        """記錄一次互動 (瀏覽、搜尋等)"""
        # new_log = Interaction(recipe_id=recipe_id, interaction_type=interaction_type)
        # db_session.add(new_log)
        # db_session.commit()
        # return new_log
        pass

    @staticmethod
    def get_by_recipe(db_session, recipe_id):
        """取得特定食譜的所有互動紀錄"""
        # return db_session.query(Interaction).filter_by(recipe_id=recipe_id).all()
        pass
