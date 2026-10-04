"""Google Search planning only; no keyword volume or account access."""
from core import google_width, rsa_check


def build(brief: dict) -> dict:
    offer = brief["offer"]
    label = offer if google_width(offer) <= 20 else "此方案"
    brand = brief["brand"]
    brand_line = f"認識{brand}" if brand and google_width(brand) <= 24 else "進一步了解方案"
    headlines = list(dict.fromkeys([f"了解{label}", "查看方案內容", "先比較再決定", brand_line, "查看適用情境"]))
    groups = []
    for i, (intent, suffixes, rationale) in enumerate([
        ("需求探索", ["", "介紹"], "先確認使用者要找的是這項產品或服務，而非相似名稱。"),
        ("比較評估", ["比較", "適合誰"], "比較詞可能反映評估需求；是否有商業價值仍須實際資料確認。"),
        ("行動評估", ["方案", "如何開始"], "與可觀察的成功行動對齊；不推定實際搜尋量或購買意圖強度。"),
    ], 1):
        groups.append({"id": f"local-intent-{i}", "intent": intent,
                       "keywords": [{"text": (offer + " " + s).strip(), "source": "hypothesis",
                                     "match_hint": "待人工選擇", "search_volume": None, "cpc": None} for s in suffixes],
                       "rationale": rationale})
    return {
        "intent_groups": groups,
        "negative_candidates": [
            {"term": "免費", "reason": "僅在未提供免費方案、且確認此查詢無價值時考慮；不能直接套用。", "requires_confirmation": True},
            {"term": "職缺", "reason": "僅在不是招募目的且查詢無關時考慮。", "requires_confirmation": True},
        ],
        "rsa_copy": {"headlines": headlines, "descriptions": [
            f"了解{label}的內容與使用方式，確認是否符合你的需求。",
            "先查看完整方案與適用情境，再決定下一步；詳細資訊請以品牌提供內容為準。",
        ]},
        "test_plan": [{"id": "local-test-1", "variable": "headline_message",
                       "variants": ["內容導覽", "適用情境"], "hold_constant": ["搜尋意圖群組", "落地頁", "量測口徑"],
                       "decision_rule": "先確認追蹤可用，再比較與成功行動相關的資料；不以單次點擊或固定天數宣告勝出。",
                       "budget_allocation": None}],
        "review_notes": ["關鍵字為固定規則候選，不含 Keyword Planner 或市場資料。",
                         "這是 Search 企劃，不是 PMax、Shopping、Display 或 YouTube 方案。",
                         "本地文字寬度檢查不是 Google 官方驗證器；emoji 等複雜 Unicode 須再確認。"],
    }


def validate(value: dict, brief: dict) -> list[str]:
    errors = rsa_check(value["rsa_copy"])["errors"]
    ids = [group["id"] for group in value["intent_groups"]]
    if len(ids) != len(set(ids)):
        errors.append("intent_groups: duplicate local IDs")
    for group in value["intent_groups"]:
        terms = [item["text"].strip().casefold() for item in group["keywords"]]
        if len(terms) != len(set(terms)):
            errors.append("intent_groups: duplicate terms within a group")
    return errors
