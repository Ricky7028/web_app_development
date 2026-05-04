# 路由與頁面設計文件 (ROUTES.md)

本文件規劃「食譜收藏夾」的 URL 路徑、對應的處理邏輯與 Jinja2 模板。

---

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| **首頁 / 每日推薦** | GET | `/` | `index.html` | 顯示每日推薦食譜與搜尋入口 |
| **搜尋/推薦結果** | GET | `/recipes` | `recipe_list.html` | 根據關鍵字或食材顯示結果列表 |
| **新增食譜頁面** | GET | `/recipes/new` | `recipe_form.html` | 顯示新增食譜的表單 |
| **執行新增** | POST | `/recipes/new` | — | 儲存食譜後重導向至詳情頁 |
| **食譜詳情** | GET | `/recipes/<id>` | `recipe_detail.html` | 顯示特定食譜內容與步驟 |
| **編輯食譜頁面** | GET | `/recipes/<id>/edit` | `recipe_form.html` | 顯示編輯表單（重複使用 form） |
| **執行更新** | POST | `/recipes/<id>/edit` | — | 更新後重導向至詳情頁 |
| **執行刪除** | POST | `/recipes/<id>/delete` | — | 刪除後重導向回首頁 |
| **食材推薦頁面** | GET | `/recommend` | `recommend.html` | 顯示食材輸入介面（可整併至首頁） |

---

## 2. 每個路由的詳細說明

### 首頁 (`/`)
- **輸入**：無。
- **處理邏輯**：
    1. 從資料庫隨機挑選一個食譜（或根據日期挑選）。
    2. 調用 `Recipe.get_random()`。
- **輸出**：渲染 `index.html`。

### 搜尋列表 (`/recipes`)
- **輸入**：URL 參數 `q` (關鍵字) 或 `ingredients` (食材列表)。
- **處理邏輯**：
    1. 若有 `q`，調用 `Recipe.search_by_title(q)`。
    2. 若有 `ingredients`，調用 `Recipe.search_by_ingredients(ingredients)`。
- **輸出**：渲染 `recipe_list.html`。

### 新增食譜 (`POST /recipes/new`)
- **輸入**：表單欄位 `title`, `ingredients`, `instructions`, `image` (可選)。
- **處理邏輯**：
    1. 驗證資料是否齊全。
    2. 調用 `Recipe.create()` 寫入資料庫。
- **輸出**：重導向至 `/recipes/<new_id>`。

### 編輯/刪除
- **處理邏輯**：檢查 `id` 是否存在，不存在則回傳 404。更新成功後重導向至詳情頁。

---

## 3. Jinja2 模板清單

所有模板皆存放在 `app/templates/` 目錄下：

1.  **`base.html`**：基礎版面（導覽列、頁尾、CSS/JS 引用）。
2.  **`index.html`**：繼承 `base.html`，顯示每日推薦。
3.  **`recipe_list.html`**：顯示搜尋或推薦結果。
4.  **`recipe_detail.html`**：食譜詳細內容與步驟。
5.  **`recipe_form.html`**：新增與編輯食譜共用的表單頁面。
6.  **`recommend.html`**：輸入食材的專用頁面。

---

## 4. 路由骨架規劃

我們將使用 Flask 的 **Blueprint (藍圖)** 來組織程式碼：
- `app/routes/main.py`：負責首頁與基礎導覽。
- `app/routes/recipe.py`：負責食譜相關的 CRUD 與推薦邏輯。
