# 系統流程圖文件 (FLOWCHART.md)

本文件透過視覺化圖表描述「食譜收藏夾」的使用者操作路徑與系統內部的資料流動。

---

## 1. 使用者流程圖 (User Flow)

描述使用者從進入系統到完成各項核心功能的流程。

```mermaid
flowchart LR
    Start([使用者開啟首頁]) --> Home[首頁 - 每日推薦食譜]
    Home --> Choice{想要做什麼？}
    
    Choice -->|新增食譜| Add[填寫食譜表單]
    Add --> Save[儲存並跳轉至詳情頁]
    
    Choice -->|搜尋食譜| Search[輸入名稱或關鍵字]
    Search --> List[顯示搜尋結果列表]
    List --> Detail[點擊查看食譜詳情]
    
    Choice -->|食材推薦| Recom[輸入現有食材]
    Recom --> Match[系統配對適合食譜]
    Match --> List
    
    Choice -->|瀏覽紀錄| History[查看過往食譜]
    History --> Detail
```

---

## 2. 系統序列圖 (Sequence Diagram)

以「新增食譜」與「搜尋食譜」為例，描述資料如何在各元件間傳遞。

### 場景 A：新增食譜並存入資料庫
```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器
    participant Route as Flask Route
    participant Model as SQLAlchemy Model
    participant DB as SQLite

    User->>Browser: 填寫名稱、食材、步驟並點擊送出
    Browser->>Route: POST /recipes/add
    Route->>Model: 建立 Recipe 物件
    Model->>DB: INSERT INTO recipes
    DB-->>Model: 回傳成功與 ID
    Route-->>Browser: Redirect to /recipes/<id>
    Browser->>Route: GET /recipes/<id>
    Route->>Model: 查詢該 ID 食譜
    Model->>DB: SELECT * FROM recipes WHERE id=<id>
    DB-->>Model: 回傳食譜資料
    Route-->>Browser: 渲染詳情頁 HTML (Jinja2)
    Browser-->>User: 呈現新食譜頁面
```

### 場景 B：根據食材推薦食譜
```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器
    participant Route as Flask Route
    participant Model as SQLAlchemy Model
    participant DB as SQLite

    User->>Browser: 輸入「雞蛋, 番茄」
    Browser->>Route: GET /recommend?ingredients=雞蛋,番茄
    Route->>Model: 搜尋包含這些食材的食譜
    Model->>DB: SELECT * FROM recipes WHERE ingredients LIKE ...
    DB-->>Model: 回傳符合條件的清單
    Route-->>Browser: 渲染推薦結果頁面
    Browser-->>User: 呈現推薦清單
```

---

## 3. 功能清單與路徑對照表

以下為系統規劃的初步 API/路由對照表：

| 功能名稱 | URL 路徑 | HTTP 方法 | 說明 |
| :--- | :--- | :--- | :--- |
| **首頁** | `/` | GET | 顯示每日推薦與功能入口 |
| **新增食譜頁面** | `/recipes/add` | GET | 顯示新增表單 |
| **執行新增** | `/recipes/add` | POST | 接收表單資料並寫入資料庫 |
| **食譜詳情** | `/recipes/<int:id>` | GET | 顯示特定食譜內容 |
| **搜尋/推薦列表** | `/recipes` | GET | 顯示搜尋結果或依食材推薦的結果 |
| **個人化推薦** | `/recommend/personal` | GET | 根據用戶行為推薦食譜 (進階功能) |

---

## 說明

- **重導向 (Redirect)**：在執行新增 (POST) 操作後，系統會重導向至該食譜的詳情頁，以符合「Post-Redirect-Get」模式，避免使用者重新整理頁面時發生重複送出的問題。
- **資料配對**：目前設計中，推薦功能將優先使用簡單的 SQL `LIKE` 語法進行關鍵字比對。
