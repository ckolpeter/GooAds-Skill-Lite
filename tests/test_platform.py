from __future__ import annotations
import sys, unittest, copy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import core, platform_rules


class GoogleTests(unittest.TestCase):
    def copy(self):
        return {"headlines": ["了解課程", "查看內容", "適用情境"], "descriptions": ["查看完整內容。", "先了解再決定。"]}

    def test_valid_copy(self):
        self.assertTrue(core.rsa_check(self.copy())["valid"])

    def test_cjk_limit(self):
        self.assertEqual(core.google_width("學" * 15), 30)
        p = self.copy(); p["headlines"][0] = "學" * 16
        self.assertFalse(core.rsa_check(p)["valid"])

    def test_ascii_limit(self):
        p = self.copy(); p["headlines"][0] = "x" * 31
        self.assertFalse(core.rsa_check(p)["valid"])

    def test_description_limit(self):
        p = self.copy(); p["descriptions"][0] = "字" * 46
        self.assertFalse(core.rsa_check(p)["valid"])

    def test_minimum_count(self):
        p = self.copy(); p["headlines"].pop()
        self.assertFalse(core.rsa_check(p)["valid"])

    def test_maximum_count(self):
        p = self.copy(); p["headlines"] = [f"標題{i}" for i in range(16)]
        self.assertFalse(core.rsa_check(p)["valid"])

    def test_duplicate_copy(self):
        p = self.copy(); p["headlines"][1] = p["headlines"][0]
        self.assertFalse(core.rsa_check(p)["valid"])

    def test_unicode_warning(self):
        p = self.copy(); p["headlines"][0] += "\U0001f600"
        self.assertTrue(core.rsa_check(p)["warnings"])

    def test_long_product_name_not_truncated(self):
        p = core.make_plan({"offer": "超長商品名稱" * 20}, platform_rules.build)
        self.assertTrue(core.validate_plan(p, platform_rules.validate)["valid"])
        self.assertEqual(p["input"]["offer"], "超長商品名稱" * 20)
        self.assertIn("此方案", p["deliverables"]["rsa_copy"]["headlines"][0])

    def test_no_fabricated_metrics(self):
        p = core.make_plan({"offer": "課程"}, platform_rules.build)
        k = p["deliverables"]["intent_groups"][0]["keywords"][0]
        self.assertIsNone(k["search_volume"])
        k["search_volume"] = 999
        with self.assertRaises(core.InputError):
            core.validate_plan(p, platform_rules.validate)

    def test_negative_confirmation_required(self):
        p = core.make_plan({"offer": "課程"}, platform_rules.build)
        p["deliverables"]["negative_candidates"][0]["requires_confirmation"] = False
        with self.assertRaises(core.InputError):
            core.validate_plan(p, platform_rules.validate)

    def test_duplicate_intent_ids(self):
        p = core.make_plan({"offer": "課程"}, platform_rules.build)
        p["deliverables"]["intent_groups"][1]["id"] = p["deliverables"]["intent_groups"][0]["id"]
        with self.assertRaises(core.InputError):
            core.validate_plan(p, platform_rules.validate)
