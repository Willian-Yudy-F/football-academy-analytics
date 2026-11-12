from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DECK_PATH = ROOT / "football_academy_analytics_demo.html"


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.slide_count = 0
        self.links: list[str] = []

    def handle_starttag(
        self,
        tag: str,
        attributes: list[tuple[str, str | None]],
    ) -> None:
        attrs = dict(attributes)
        classes = (attrs.get("class") or "").split()
        if tag == "div" and "slide" in classes:
            self.slide_count += 1
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"] or "")


class DeckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = DECK_PATH.read_text(encoding="utf-8")
        cls.parser = DeckParser()
        cls.parser.feed(cls.html)

    def test_deck_contains_eight_slides(self) -> None:
        self.assertEqual(self.parser.slide_count, 8)

    def test_links_do_not_use_placeholders(self) -> None:
        self.assertNotIn("#", self.parser.links)
        self.assertNotIn("[your-handle]", self.html)

    def test_scope_is_explicit(self) -> None:
        self.assertIn("Concept Deck", self.html)
        self.assertIn("no deployed dashboard", self.html)
        self.assertIn("no real child data", self.html)

    def test_known_unverified_claims_are_absent(self) -> None:
        forbidden = [
            "Measured Impact",
            "Full source code available",
            "100% free stack",
            "near 100% in pilot",
        ]
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, self.html)

    def test_accessibility_controls_are_present(self) -> None:
        self.assertIn("Skip to presentation", self.html)
        self.assertIn("prefers-reduced-motion", self.html)
        self.assertIn("aria-expanded", self.html)
        self.assertIn("aria-hidden", self.html)


if __name__ == "__main__":
    unittest.main()
