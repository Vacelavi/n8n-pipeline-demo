# Сценарии Pull Request для AI-review

## PR 1: promotional discounts

- Head: `demo/promo-discounts`
- Base: `main`
- Title: `Add promotional discounts to delivery quotes`

Body:

```text
Adds SAVE10 and HALFOFF promotion codes to quote calculation. Promotion values
are configured in one mapping so new campaigns can be added without changing
the calculation flow.

Please pay special attention to monetary units, input normalization and the
interaction between a promotion and free delivery.
```

Подсказка для проверки результата AI-review: в diff намеренно смешаны доллары и
центы, неизвестный код молча принимается, а тест закрепляет ошибочное поведение.
Не добавляйте эту подсказку в PR — модель должна найти проблемы самостоятельно.

## PR 2: bulk quotes

- Head: `demo/bulk-quotes`
- Base: `main`
- Title: `Add bulk delivery quote calculation`

Body:

```text
Adds a helper for calculating many quotes in a single call. A malformed item
must not prevent valid items in the same batch from being processed.

Please review the error handling, return contract and behaviour with arbitrary
iterables.
```

Подсказка для проверки результата AI-review: реализация проглатывает все типы
исключений, теряет связь результата с исходным элементом и может скрыть
программные ошибки. Тесты проверяют лишь happy path.
