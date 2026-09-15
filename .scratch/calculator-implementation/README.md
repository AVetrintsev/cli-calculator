# Задачи реализации калькулятора

Созданы **57 отдельных карточек** по [согласованному плану](breakdown.md): 114 критериев приёмки, все 72 пользовательских сценария SPEC и технические требования архитектуры/поставки.

## С чего начать

Сейчас доступна только [01 — Согласование всех прототипов с пользователем](issues/01-approve-all-prototypes.md). Нужно собрать и показать полный актуальный комплект, внести замечания и получить явное согласование пользователя. Разрешение создать карточки не закрывает эту задачу.

После её завершения доступна задача 02, затем независимо 03 и 07. Для дальнейшего выбора работы используйте поле **Blocked by**: начать можно только задачу, все блокирующие карточки которой завершены. Статус `ready-for-agent` означает, что карточка подготовлена для работы; он не снимает блокирующие связи или внешние условия.

Каждая карточка хранит собственное текущее состояние. Этот реестр содержит ссылки и зависимости; начальные 57 карточек имеют незавершённые критерии.

## Нормативные материалы

- [Полная спецификация](../../SPEC.md), [подробные продуктовые правила](../calculator/spec.md) и [глоссарий](../../CONTEXT.md).
- [Архитектура](../calculator/architecture/proposal.md), [матрица приёмки](../calculator/distribution/acceptance.md) и [поставка](../calculator/distribution/delivery.md).
- [Общие правила исполнения](breakdown.md#как-читать-план) и [внешние условия](breakdown.md#внешние-условия-выполнения): доступ к реальным ОС, IME/дикторам, устройствам и сертификатам.
- [Уточнение масштаба результата](breakdown.md#уточнение-уже-принятого-правила): актуальный показ для floor(1234mm) — 1000mm.

## Карточки

### Согласование прототипов

| Задача | Блокируют |
| --- | --- |
| [01 — Согласование всех прототипов с пользователем](issues/01-approve-all-prototypes.md) | Нет |

### Первый рабочий путь и история

| Задача | Блокируют |
| --- | --- |
| [02 — Первый расчёт в Windows](issues/02-first-windows-calculation.md) | [01](issues/01-approve-all-prototypes.md) |
| [03 — Первый расчёт в macOS](issues/03-first-macos-calculation.md) | [02](issues/02-first-windows-calculation.md) |
| [04 — Глобальный вызов и возврат к работе](issues/04-global-invocation-and-focus.md) | [03](issues/03-first-macos-calculation.md) |
| [05 — Сохранение быстрого ввода между запусками](issues/05-persist-quick-draft.md) | [04](issues/04-global-invocation-and-focus.md) |
| [06 — Предел расчёта и восстановление после аварии](issues/06-compute-deadline-and-recovery.md) | [03](issues/03-first-macos-calculation.md) |
| [07 — Точные числа и компактный ответ](issues/07-exact-numbers-and-display.md) | [02](issues/02-first-windows-calculation.md) |
| [08 — Копирование ответа и обычное редактирование](issues/08-copy-and-native-editing.md) | [03](issues/03-first-macos-calculation.md), [07](issues/07-exact-numbers-and-display.md) |
| [09 — Подтверждение расчёта без потери данных](issues/09-confirmation-and-history.md) | [05](issues/05-persist-quick-draft.md), [06](issues/06-compute-deadline-and-recovery.md), [08](issues/08-copy-and-native-editing.md) |
| [10 — Навигация по истории у неподвижного ввода](issues/10-history-navigation.md) | [09](issues/09-confirmation-and-history.md) |
| [11 — Поиск и удаление истории](issues/11-history-search-and-deletion.md) | [10](issues/10-history-navigation.md) |

### Язык, редактор, календарь и финансы

| Задача | Блокируют |
| --- | --- |
| [12 — Математическая запись и справка приоритетов](issues/12-math-expressions-and-precedence.md) | [07](issues/07-exact-numbers-and-display.md) |
| [13 — Тригонометрия и логарифмы](issues/13-trigonometry-and-logarithms.md) | [12](issues/12-math-expressions-and-precedence.md) |
| [14 — Условия и логические значения](issues/14-conditions-and-booleans.md) | [08](issues/08-copy-and-native-editing.md), [12](issues/12-math-expressions-and-precedence.md) |
| [15 — Процентные значения](issues/15-percentage-values.md) | [08](issues/08-copy-and-native-editing.md), [12](issues/12-math-expressions-and-precedence.md) |
| [16 — Системы счисления и преобразования](issues/16-number-base-conversion.md) | [08](issues/08-copy-and-native-editing.md), [12](issues/12-math-expressions-and-precedence.md) |
| [17 — Измерения и явный перевод единиц](issues/17-units-and-explicit-conversion.md) | [08](issues/08-copy-and-native-editing.md), [12](issues/12-math-expressions-and-precedence.md) |
| [18 — Типовые операции и масштаб результата](issues/18-typed-operations-and-result-scale.md) | [13](issues/13-trigonometry-and-logarithms.md), [15](issues/15-percentage-values.md), [17](issues/17-units-and-explicit-conversion.md) |
| [19 — Контекстные единицы и все варианты ответа](issues/19-contextual-units-and-alternatives.md) | [06](issues/06-compute-deadline-and-recovery.md), [18](issues/18-typed-operations-and-result-scale.md) |
| [20 — Выбор и подтверждение нескольких ответов](issues/20-select-and-confirm-results.md) | [09](issues/09-confirmation-and-history.md), [19](issues/19-contextual-units-and-alternatives.md) |
| [21 — Подсветка, надстрочные единицы и Undo](issues/21-editor-highlighting-and-unit-powers.md) | [17](issues/17-units-and-explicit-conversion.md) |
| [22 — Контекстные подсказки с описаниями](issues/22-contextual-completion.md) | [16](issues/16-number-base-conversion.md), [19](issues/19-contextual-units-and-alternatives.md), [21](issues/21-editor-highlighting-and-unit-powers.md) |
| [23 — Даты, время и фиксированные длительности](issues/23-dates-times-and-durations.md) | [14](issues/14-conditions-and-booleans.md), [17](issues/17-units-and-explicit-conversion.md) |
| [24 — Календарные месяцы и фиксированные смещения](issues/24-calendar-intervals-and-offsets.md) | [23](issues/23-dates-times-and-durations.md) |
| [25 — Динамические часы и сохранённый снимок](issues/25-dynamic-clock-snapshots.md) | [09](issues/09-confirmation-and-history.md), [24](issues/24-calendar-intervals-and-offsets.md) |
| [26 — Кредитные расчёты](issues/26-loan-calculations.md) | [13](issues/13-trigonometry-and-logarithms.md), [15](issues/15-percentage-values.md) |
| [27 — Накопления и сложные проценты](issues/27-savings-and-compound-interest.md) | [26](issues/26-loan-calculations.md) |
| [28 — Прибыль, ROI и окупаемость](issues/28-profit-roi-and-payback.md) | [15](issues/15-percentage-values.md) |

### Листы, определения и шаблоны

| Задача | Блокируют |
| --- | --- |
| [29 — Многострочный лист с автосохранением](issues/29-autosaved-calculation-sheets.md) | [05](issues/05-persist-quick-draft.md), [21](issues/21-editor-highlighting-and-unit-powers.md) |
| [30 — Локальные переменные и пересчёт зависимостей](issues/30-sheet-variables-and-dependencies.md) | [06](issues/06-compute-deadline-and-recovery.md), [29](issues/29-autosaved-calculation-sheets.md) |
| [31 — Ответы и история внутри листа](issues/31-sheet-results-and-history.md) | [10](issues/10-history-navigation.md), [20](issues/20-select-and-confirm-results.md), [30](issues/30-sheet-variables-and-dependencies.md) |
| [32 — Публикация пользовательских констант](issues/32-publish-user-constants.md) | [22](issues/22-contextual-completion.md), [25](issues/25-dynamic-clock-snapshots.md), [31](issues/31-sheet-results-and-history.md) |
| [33 — Пользовательские функции с аргументами](issues/33-user-functions-with-arguments.md) | [32](issues/32-publish-user-constants.md) |
| [34 — Многострочные пользовательские функции](issues/34-multiline-user-functions.md) | [33](issues/33-user-functions-with-arguments.md) |
| [35 — Каталог и управление сохранёнными объектами](issues/35-catalog-and-object-management.md) | [32](issues/32-publish-user-constants.md) |
| [36 — Шаблоны с параметрами](issues/36-parameterized-templates.md) | [33](issues/33-user-functions-with-arguments.md), [35](issues/35-catalog-and-object-management.md) |
| [37 — Переименование и удаление определений](issues/37-definition-rename-and-deletion.md) | [34](issues/34-multiline-user-functions.md), [36](issues/36-parameterized-templates.md) |

### Данные и настройки

| Задача | Блокируют |
| --- | --- |
| [38 — Полные локальные резервные снимки](issues/38-local-backup-snapshots.md) | [05](issues/05-persist-quick-draft.md) |
| [39 — Предпросмотр и восстановление резервной копии](issues/39-backup-preview-and-restore.md) | [11](issues/11-history-search-and-deletion.md), [36](issues/36-parameterized-templates.md), [38](issues/38-local-backup-snapshots.md) |
| [40 — Миграции, новый формат и повреждённая база](issues/40-storage-migration-and-recovery.md) | [39](issues/39-backup-preview-and-restore.md) |
| [41 — Полный и выборочный экспорт](issues/41-full-and-selective-export.md) | [37](issues/37-definition-rename-and-deletion.md) |
| [42 — Импорт с предпросмотром конфликтов](issues/42-import-preview-and-conflicts.md) | [38](issues/38-local-backup-snapshots.md), [41](issues/41-full-and-selective-export.md) |
| [43 — Темы и калибровка масштаба](issues/43-themes-and-scale-calibration.md) | [05](issues/05-persist-quick-draft.md) |
| [44 — Смена языка и локальных обозначений](issues/44-language-and-notation-switching.md) | [37](issues/37-definition-rename-and-deletion.md) |
| [45 — Сочетания, автозапуск и системный значок](issues/45-shortcuts-autostart-and-system-icon.md) | [05](issues/05-persist-quick-draft.md) |

### Нативные проверки, поставка и приёмка

| Задача | Блокируют |
| --- | --- |
| [46 — Настоящий ввод и экраны Windows](issues/46-windows-input-and-displays.md) | [37](issues/37-definition-rename-and-deletion.md), [43](issues/43-themes-and-scale-calibration.md), [45](issues/45-shortcuts-autostart-and-system-icon.md) |
| [47 — Настоящий ввод и рабочие пространства macOS](issues/47-macos-input-and-spaces.md) | [37](issues/37-definition-rename-and-deletion.md), [43](issues/43-themes-and-scale-calibration.md), [45](issues/45-shortcuts-autostart-and-system-icon.md) |
| [48 — Клавиатура и средства доступности](issues/48-keyboard-and-accessibility.md) | [40](issues/40-storage-migration-and-recovery.md), [42](issues/42-import-preview-and-conflicts.md), [44](issues/44-language-and-notation-switching.md), [46](issues/46-windows-input-and-displays.md), [47](issues/47-macos-input-and-spaces.md) |
| [49 — Подписанная установка Windows](issues/49-signed-windows-installation.md) | [45](issues/45-shortcuts-autostart-and-system-icon.md) |
| [50 — Подписанная установка macOS](issues/50-signed-macos-installation.md) | [45](issues/45-shortcuts-autostart-and-system-icon.md) |
| [51 — Обновление Windows после сохранения](issues/51-windows-update-and-save-barrier.md) | [40](issues/40-storage-migration-and-recovery.md), [49](issues/49-signed-windows-installation.md) |
| [52 — Обновление macOS через Sparkle](issues/52-macos-sparkle-updates.md) | [50](issues/50-signed-macos-installation.md), [51](issues/51-windows-update-and-save-barrier.md) |
| [53 — Сохранность данных на NTFS и APFS](issues/53-ntfs-apfs-data-durability.md) | [42](issues/42-import-preview-and-conflicts.md), [52](issues/52-macos-sparkle-updates.md) |
| [54 — Скорость ответа, вызова и запуска](issues/54-interactive-latency-and-startup.md) | [27](issues/27-savings-and-compound-interest.md), [28](issues/28-profit-roi-and-payback.md), [44](issues/44-language-and-notation-switching.md), [49](issues/49-signed-windows-installation.md), [50](issues/50-signed-macos-installation.md) |
| [55 — Большая история, библиотека и лист](issues/55-large-history-and-sheet-performance.md) | [11](issues/11-history-search-and-deletion.md), [42](issues/42-import-preview-and-conflicts.md), [44](issues/44-language-and-notation-switching.md), [49](issues/49-signed-windows-installation.md), [50](issues/50-signed-macos-installation.md) |
| [56 — Память, скрытый простой и дорогие расчёты](issues/56-memory-idle-and-expensive-calculations.md) | [46](issues/46-windows-input-and-displays.md), [47](issues/47-macos-input-and-spaces.md), [54](issues/54-interactive-latency-and-startup.md), [55](issues/55-large-history-and-sheet-performance.md) |
| [57 — Полная приёмка выпуска](issues/57-complete-release-acceptance.md) | [48](issues/48-keyboard-and-accessibility.md), [53](issues/53-ntfs-apfs-data-durability.md), [56](issues/56-memory-idle-and-expensive-calculations.md) |
