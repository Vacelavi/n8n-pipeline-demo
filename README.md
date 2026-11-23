# GitHub-стенд для практик 7.1 и 7.2

Небольшой самостоятельный Python-проект для демонстрации n8n-пайплайнов:

GitHub: <https://github.com/Vacelavi/n8n-pipeline-demo>

- практика 7.1 — ревью Pull Request по командам `/make_ai_review` и
  `/make_other_ai_review`, дедупликация и точечные review-комментарии;
- практика 7.2 — классификация новых Issues, ветка `needs-triage` и сбор
  еженедельной статистики.

Проект не требует внешних зависимостей. На основной ветке находится рабочий
сервис расчёта стоимости доставки и unit-тесты. Две демонстрационные ветки
создаются скриптом и содержат намеренные, но реалистичные дефекты для AI-review.

## Быстрый старт

```bash
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

## Публикация отдельным GitHub-репозиторием

Чтобы опубликовать собственную копию стенда, создайте пустой репозиторий и
выполните команды из корня этой папки:

```bash
git init -b main
git add .
git commit -m "Initial demo service"
git remote add origin git@github.com:Vacelavi/n8n-pipeline-demo.git
git push -u origin main
```

Затем создайте метки и две демонстрационные ветки:

```bash
./scripts/setup_labels.sh Vacelavi/n8n-pipeline-demo
./scripts/create_demo_branches.sh
```

Скрипт только создаёт локальные ветки и коммиты. После проверки отправьте их:

```bash
git push -u origin demo/promo-discounts
git push -u origin demo/bulk-quotes
```

Откройте два Pull Request в `main`:

1. `demo/promo-discounts` — проверка денежных расчётов и валидации промокода;
2. `demo/bulk-quotes` — проверка пакетной обработки и обработки ошибок.

Описание для каждого PR находится в [docs/pr-scenarios.md](docs/pr-scenarios.md).

## Проверка практики 7.1

1. Убедитесь, что GitHub Webhook в n8n подписан на `Pull requests` и
   `Issue comments`.
2. Откройте первый PR. Проверьте запуск workflow по событию
   `pull_request.opened`.
3. Напишите отдельным комментарием `/make_ai_review`.
4. Повторите `/make_ai_review`: Data Table должен запретить повторное ревью
   того же PR.
5. Во втором PR напишите `/make_other_ai_review` и убедитесь, что выбрана
   другая модель.
6. Для задания со звёздочкой проверьте, что замечания опубликованы как review
   comments на конкретных строках diff, а не одним общим сообщением.

Команды нужно писать в комментарии к PR, а не в review-комментарии к строке.
Оба события приходят через тип GitHub webhook `issue_comment`, потому что PR в
GitHub также является Issue.

## Проверка практики 7.2

1. Убедитесь, что Webhook подписан на `Issues`.
2. Создайте четыре Issue по примерам из
   [docs/issue-scenarios.md](docs/issue-scenarios.md).
3. Проверьте метки `bug`, `feature`, `task` и `needs-triage`.
4. Для неоднозначного Issue убедитесь, что комментарий не опубликован.
5. Запустите workflow статистики вручную. В репозитории уже будут Issues и PR,
   поэтому запросы GitHub API за неделю вернут непустые данные.

Формы в `.github/ISSUE_TEMPLATE` помогают создавать новые собственные примеры,
но для воспроизводимой демонстрации лучше начать с готовых текстов.

## Сброс демонстрации

- для дедупликации 7.1 откройте новый PR или удалите запись соответствующего PR
  из n8n Data Table;
- для 7.2 создайте новый Issue: событие `issues.opened` нельзя повторно вызвать
  простым переоткрытием без изменения фильтра workflow;
- старые PR и Issues лучше закрывать, а не удалять — они останутся полезны для
  недельной статистики.

## Безопасность

GitHub token и webhook secret не хранятся в проекте. Скрипт создания меток
использует установленный `gh` и его локальную авторизацию. Для n8n используйте
Credentials или переменные окружения.
