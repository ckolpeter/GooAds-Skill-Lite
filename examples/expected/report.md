# GooAds Skill Lite｜離線企劃初稿

> 尚未投放、未查詢帳號或網站；所有建議須人工確認。

版本：1.0.0｜資料：synthetic｜產生方式：deterministic\_starter
狀態：PLAN_READY（僅本地結構）｜人工審查：HUMAN_REVIEW_REQUIRED

## 1. 商業資料與證據

- **brand**：範例學院
- **offer**：廣告入門課程
- **audience**：想練習廣告規劃的初學者
- **market**：台灣
- **goal**：leads
- **success\_action**：提交課程諮詢表單
- **landing\_page\_url**：https://example.com/course
- **landing\_page\_text**：合成範例：頁面介紹課程內容，設有課程諮詢表單。未提供價格、保證、開課日或真實成效。
- **currency**：TWD
- **total\_budget**：6000
- **duration\_days**：14
- **video\_duration\_seconds**：30
- **facts**
  - 項目 1
    - **id**：F1
    - **text**：課程內容包含廣告規劃練習。
    - **source**：合成教學範例，不是 AI Ads Academy 的真實課程承諾。
- **constraints**
  - 不得宣稱保證收益。
  - 未提供價格，不得補寫優惠。
- **data\_label**：synthetic

## 2. 預算算術摘要

- **currency**：TWD
- **total\_limit**：6000
- **duration\_days**：14
- **daily\_average**：428.57
- **note**：僅為總額除以天數的規劃均值，不是平台每日預算設定；不得直接四捨五入後乘回作為支出承諾。

## 3. 平台專用產出

- **intent\_groups**
  - 項目 1
    - **id**：local-intent-1
    - **intent**：需求探索
    - **keywords**
      - 項目 1
        - **text**：廣告入門課程
        - **source**：hypothesis
        - **match\_hint**：待人工選擇
        - **search\_volume**：待確認
        - **cpc**：待確認
      - 項目 2
        - **text**：廣告入門課程 介紹
        - **source**：hypothesis
        - **match\_hint**：待人工選擇
        - **search\_volume**：待確認
        - **cpc**：待確認
    - **rationale**：先確認使用者要找的是這項產品或服務，而非相似名稱。
  - 項目 2
    - **id**：local-intent-2
    - **intent**：比較評估
    - **keywords**
      - 項目 1
        - **text**：廣告入門課程 比較
        - **source**：hypothesis
        - **match\_hint**：待人工選擇
        - **search\_volume**：待確認
        - **cpc**：待確認
      - 項目 2
        - **text**：廣告入門課程 適合誰
        - **source**：hypothesis
        - **match\_hint**：待人工選擇
        - **search\_volume**：待確認
        - **cpc**：待確認
    - **rationale**：比較詞可能反映評估需求；是否有商業價值仍須實際資料確認。
  - 項目 3
    - **id**：local-intent-3
    - **intent**：行動評估
    - **keywords**
      - 項目 1
        - **text**：廣告入門課程 方案
        - **source**：hypothesis
        - **match\_hint**：待人工選擇
        - **search\_volume**：待確認
        - **cpc**：待確認
      - 項目 2
        - **text**：廣告入門課程 如何開始
        - **source**：hypothesis
        - **match\_hint**：待人工選擇
        - **search\_volume**：待確認
        - **cpc**：待確認
    - **rationale**：與可觀察的成功行動對齊；不推定實際搜尋量或購買意圖強度。
- **negative\_candidates**
  - 項目 1
    - **term**：免費
    - **reason**：僅在未提供免費方案、且確認此查詢無價值時考慮；不能直接套用。
    - **requires\_confirmation**：true
  - 項目 2
    - **term**：職缺
    - **reason**：僅在不是招募目的且查詢無關時考慮。
    - **requires\_confirmation**：true
- **rsa\_copy**
  - **headlines**
    - 了解廣告入門課程
    - 查看方案內容
    - 先比較再決定
    - 認識範例學院
    - 查看適用情境
  - **descriptions**
    - 了解廣告入門課程的內容與使用方式，確認是否符合你的需求。
    - 先查看完整方案與適用情境，再決定下一步；詳細資訊請以品牌提供內容為準。
- **test\_plan**
  - 項目 1
    - **id**：local-test-1
    - **variable**：headline\_message
    - **variants**
      - 內容導覽
      - 適用情境
    - **hold\_constant**
      - 搜尋意圖群組
      - 落地頁
      - 量測口徑
    - **decision\_rule**：先確認追蹤可用，再比較與成功行動相關的資料；不以單次點擊或固定天數宣告勝出。
    - **budget\_allocation**：待確認
- **review\_notes**
  - 關鍵字為固定規則候選，不含 Keyword Planner 或市場資料。
  - 這是 Search 企劃，不是 PMax、Shopping、Display 或 YouTube 方案。
  - 本地文字寬度檢查不是 Google 官方驗證器；emoji 等複雜 Unicode 須再確認。

## 4. 量測待辦

- **success\_action**：提交課程諮詢表單
- **tracking\_status**：NOT\_VERIFIED
- **baseline**：待確認
- **target**：待確認
- **attribution\_window**：待確認

## 5. 假設

- 這是固定規則產生的企劃起稿；訊息角度是待驗證假設，不是成效預測。
- 輸入事實由使用者提供，未經本工具外部查證；合成範例不得當作真實案例。
- 平台目標與素材規格未作 live 驗證；人工上線前須在實際帳號確認。

## 6. 檢查與待確認

- **valid**：true
- **validation\_scope**：local\_structure\_only
- **warnings**
  - 尚未驗證模型路由、廣告審核、素材授權或實際投放成效。
  - 通過僅表示本地結構檢查；商品真實性與廣告策略須人工審查。

