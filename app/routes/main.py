from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    首頁：顯示每日推薦食譜。
    1. 從資料庫隨機取得一個食譜。
    2. 渲染 index.html 模板。
    """
    pass

@main_bp.route('/recommend')
def recommend():
    """
    食材推薦頁面：讓使用者輸入現有食材。
    1. 渲染 recommend.html 模板。
    """
    pass
