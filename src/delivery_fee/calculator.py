"""Business rules for delivery fee calculation.

All monetary values are integer cents. Keeping one unit at the API boundary
avoids rounding surprises and makes the code-review scenarios easy to inspect.
"""

from dataclasses import dataclass
import math


FREE_DELIVERY_THRESHOLD_CENTS = 5_000
PRIORITY_SURCHARGE_CENTS = 250


@dataclass(frozen=True, slots=True)
class QuoteRequest:
    subtotal_cents: int
    distance_km: float
    priority: bool = False


@dataclass(frozen=True, slots=True)
class DeliveryQuote:
    fee_cents: int
    free_delivery: bool


def _validate_request(request: QuoteRequest) -> None:
    if isinstance(request.subtotal_cents, bool) or not isinstance(
        request.subtotal_cents, int
    ):
        raise TypeError("subtotal_cents must be an integer")
    if request.subtotal_cents < 0:
        raise ValueError("subtotal_cents must not be negative")
    if isinstance(request.distance_km, bool) or not isinstance(
        request.distance_km, (int, float)
    ):
        raise TypeError("distance_km must be a number")
    if not math.isfinite(request.distance_km) or request.distance_km <= 0:
        raise ValueError("distance_km must be finite and positive")
    if not isinstance(request.priority, bool):
        raise TypeError("priority must be a boolean")


def _distance_fee_cents(distance_km: float) -> int:
    if distance_km <= 3:
        return 300
    if distance_km <= 10:
        return 500
    return 800


def calculate_quote(request: QuoteRequest) -> DeliveryQuote:
    """Calculate a delivery quote using integer-cent arithmetic."""

    _validate_request(request)
    free_delivery = request.subtotal_cents >= FREE_DELIVERY_THRESHOLD_CENTS
    fee_cents = 0 if free_delivery else _distance_fee_cents(request.distance_km)
    if request.priority:
        fee_cents += PRIORITY_SURCHARGE_CENTS
    return DeliveryQuote(fee_cents=fee_cents, free_delivery=free_delivery)
