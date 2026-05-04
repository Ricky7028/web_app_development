from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.recipe import Recipe
from app.models.interaction import Interaction

recipe_bp = Blueprint('recipe', __name__)

@recipe_bp.route('/recipes')
def list_recipes():
    """
    食譜列表：搜尋結果或食材配對結果。
    """
    query = request.args.get('q', '')
    ingredients = request.args.get('ingredients', '')
    
    if query:
        recipes = Recipe.search(query)
    elif ingredients:
        # 簡單起見，食材推薦也使用相同的 search 邏輯
        recipes = Recipe.search(ingredients)
    else:
        recipes = Recipe.get_all()
        
    return render_template('recipe_list.html', recipes=recipes, query=query or ingredients)

@recipe_bp.route('/recipes/new', methods=['GET', 'POST'])
def add_recipe():
    """
    新增食譜
    """
    if request.method == 'POST':
        title = request.form.get('title')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        image_path = request.form.get('image_path')

        # 基本驗證
        if not title or not ingredients or not instructions:
            flash('請填寫所有必填欄位！', 'danger')
            return render_template('recipe_form.html', action="新增")

        recipe_data = {
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions,
            'image_path': image_path
        }
        
        new_recipe = Recipe.create(recipe_data)
        if new_recipe:
            flash('食譜已成功新增！', 'success')
            return redirect(url_for('recipe.recipe_detail', recipe_id=new_recipe.id))
        else:
            flash('新增失敗，請稍後再試。', 'danger')

    return render_template('recipe_form.html', action="新增")

@recipe_bp.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    """
    食譜詳情
    """
    recipe = Recipe.get_by_id(recipe_id)
    if not recipe:
        flash('找不到該食譜！', 'warning')
        return redirect(url_for('recipe.list_recipes'))
    
    # 記錄瀏覽行為
    Interaction.log(recipe_id, 'view')
    
    return render_template('recipe_detail.html', recipe=recipe)

@recipe_bp.route('/recipes/<int:recipe_id>/edit', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """
    編輯食譜
    """
    recipe = Recipe.get_by_id(recipe_id)
    if not recipe:
        flash('找不到該食譜！', 'warning')
        return redirect(url_for('recipe.list_recipes'))

    if request.method == 'POST':
        title = request.form.get('title')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        image_path = request.form.get('image_path')

        if not title or not ingredients or not instructions:
            flash('請填寫所有必填欄位！', 'danger')
            return render_template('recipe_form.html', recipe=recipe, action="編輯")

        update_data = {
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions,
            'image_path': image_path
        }
        
        if Recipe.update(recipe_id, update_data):
            flash('食譜已成功更新！', 'success')
            return redirect(url_for('recipe.recipe_detail', recipe_id=recipe_id))
        else:
            flash('更新失敗。', 'danger')

    return render_template('recipe_form.html', recipe=recipe, action="編輯")

@recipe_bp.route('/recipes/<int:recipe_id>/delete', methods=['POST'])
def delete_recipe(recipe_id):
    """
    刪除食譜
    """
    if Recipe.delete(recipe_id):
        flash('食譜已刪除。', 'info')
    else:
        flash('刪除失敗。', 'danger')
    return redirect(url_for('recipe.list_recipes'))
