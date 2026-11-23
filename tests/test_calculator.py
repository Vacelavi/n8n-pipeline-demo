import math
import sys
from pathlib import Path
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from delivery_fee import QuoteRequest, calculate_quote  # noqa: E402


class CalculateQuoteTests(unittest.TestCase):
    def test_uses_distance_tiers(self) -> None:
        cases = ((1, 300), (3, 300), (3.1, 500), (10, 500), (11, 800))
        for distance_km, expected_fee in cases:
            with self.subTest(distance_km=distance_km):
                quote = calculate_quote(QuoteRequest(1_000, distance_km))
                self.assertEqual(expected_fee, quote.fee_cents)

    def test_free_delivery_still_charges_priority_surcharge(self) -> None:
        quote = calculate_quote(QuoteRequest(5_000, 2, priority=True))
        self.assertTrue(quote.free_delivery)
        self.assertEqual(250, quote.fee_cents)

    def test_rejects_invalid_subtotal(self) -> None:
        for subtotal in (-1, True, 10.5):
            with self.subTest(subtotal=subtotal):
                with self.assertRaises((TypeError, ValueError)):
                    calculate_quote(QuoteRequest(subtotal, 2))  # type: ignore[arg-type]

    def test_rejects_invalid_distance(self) -> None:
        for distance in (0, -1, math.inf, math.nan, True, "2"):
            with self.subTest(distance=distance):
                with self.assertRaises((TypeError, ValueError)):
                    calculate_quote(QuoteRequest(1_000, distance))  # type: ignore[arg-type]

    def test_applies_save10_promotion(self) -> None:
        quote = calculate_quote(QuoteRequest(1_000, 2, promo_code="SAVE10"))
        self.assertEqual(290, quote.fee_cents)



if __name__ == "__main__":
    unittest.main()
