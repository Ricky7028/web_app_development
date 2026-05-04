from flask import Blueprint, render_template, request, redirect, url_for

recipe_bp = Blueprint('recipe', __name__)

@recipe_bp.route('/recipes')
def list_recipes():
    """
    食譜列表：搜尋結果或食材配對結果。
    1. 接收 q (關鍵字) 或 ingredients (食材列表) 參數。
    2. 呼叫 Recipe Model 進行查詢。
    3. 渲染 recipe_list.html。
    """
    pass

@recipe_bp.route('/recipes/new', methods=['GET', 'POST'])
def add_recipe():
    """
    新增食譜：
    - GET: 顯示新增表單 (recipe_form.html)。
    - POST: 接收表單資料，儲存至資料庫，重導向至詳情頁。
    """
    pass

@recipe_bp.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    """
    食譜詳情：
    1. 根據 ID 取得食譜。
    2. 記錄使用者瀏覽行為 (Interaction)。
    3. 渲染 recipe_detail.html。
    """
    pass

@recipe_bp.route('/recipes/<int:recipe_id>/edit', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """
    編輯食譜：
    - GET: 顯示帶有原有資料的表單 (recipe_form.html)。
    - POST: 更新資料庫，重導向至詳情頁。
    """
    pass

@recipe_bp.route('/recipes/<int:recipe_id>/delete', methods=['POST'])
def delete_recipe(recipe_id):
    """
    刪除食譜：
    1. 刪除指定 ID 的食譜。
    2. 重導向回首頁或列表頁。
    """
    pass
