# Готовые Issue для проверки классификатора

Создавайте Issues по одному и дожидайтесь завершения n8n workflow. Не добавляйте
метки вручную: метка — проверяемый результат сценария.

## 1. Bug

**Title**

```text
Priority surcharge is charged twice for a free-delivery order
```

**Body**

```text
Version: 0.1.0

Steps to reproduce:
1. Request a quote with subtotal_cents=5000, distance_km=2 and priority=true.
2. Confirm the quote.

Expected: the fee is 250 cents (only the priority surcharge).
Actual: the API returns 500 cents. The customer is charged twice.
```

Ожидаемая метка: `bug`.

## 2. Feature

**Title**

```text
Support scheduled delivery time slots
```

**Body**

```text
Customers need to choose a two-hour delivery window while requesting a quote.
The quote should return the selected slot and an additional slot fee. Same-day
and next-day slots are enough for the first version.

Acceptance criteria:
- available slots can be requested before creating a quote;
- a valid slot can be attached to a quote;
- an unavailable slot produces a clear validation error.
```

Ожидаемая метка: `feature`.

## 3. Task

**Title**

```text
Document the integer-cent convention
```

**Body**

```text
Add a short architecture note explaining why every public monetary field uses
integer cents. Link it from the README and include one correct and one incorrect
request example. No runtime behaviour should change.
```

Ожидаемая метка: `task`.

## 4. Unknown / needs-triage

**Title**

```text
Delivery pricing follow-up
```

**Body**

```text
We should revisit this after the next planning meeting. There may be something
to change around delivery pricing, but the expected outcome and affected users
are not known yet.
```

Ожидаемая метка: `needs-triage`, комментариев от workflow быть не должно.

> Точный confidence зависит от модели. Если модель уверенно присваивает тип
> этому примеру, сократите body до `Needs discussion after planning`.
