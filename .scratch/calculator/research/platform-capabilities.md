# Возможности Windows и macOS для калькулятора-палитры

Дата исследования: 2026-09-10. Исследователь: platform_research; итог сохранён основным агентом.

Исследование основано на официальной документации. Прототипы не запускались; стек, версии ОС и числовые бюджеты производительности не выбраны. Предложения ниже требуют отдельного решения в карте.

## Вывод

Документированные средства позволяют рассматривать Tauri, Electron и отдельные нативные оболочки с общим ядром. Основная неопределённость — сквозное поведение вызова, ввода, скрытия и возврата к прежнему приложению, особенно в полноэкранных рабочих пространствах. Наличие отдельных API не доказывает этот сценарий целиком; необходим установленный прототип на обеих ОС.

## Системные ограничения и следствия для спецификации

| Область | Подтверждённые факты | Предложение для спецификации |
| --- | --- | --- |
| Глобальное сочетание | Windows `RegisterHotKey` доставляет `WM_HOTKEY`; занятое сочетание может не зарегистрироваться. `MOD_NOREPEAT` подавляет повтор. Electron также сообщает неуспех регистрации занятого сочетания; Tauri имеет официальный плагин. [Windows](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerhotkey), [Electron](https://www.electronjs.org/docs/latest/api/global-shortcut), [Tauri](https://v2.tauri.app/plugin/global-shortcut/). | Проверять результат переназначения; при конфликте сохранять рабочий способ вызова. Значение по умолчанию согласовать отдельно. |
| Раскладки и разрешения | Глобальный монитор `NSEvent` отличается от регистрации конкретного сочетания: наблюдает события и не подавляет их, а для клавиатуры требует доверия Accessibility. Electron документирует ограничение globalShortcut на macOS с раскладками, отличными от QWERTY. [Apple](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/MonitoringEvents/MonitoringEvents.html), [Electron](https://www.electronjs.org/docs/latest/tutorial/keyboard-shortcuts). | Проверять RU/EN, нужные пользовательские раскладки и фактические разрешения выбранной реализации. Не требовать мониторинг всей клавиатуры без необходимости. |
| Окно без рамки | Windows имеет стили popup-окна, AppKit — borderless/nonactivatingPanel. Tauri предоставляет управление декорациями и геометрией, Electron — `frame: false`. [Windows](https://learn.microsoft.com/en-us/windows/win32/winmsg/window-styles), [Apple](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/nonactivatingpanel), [Tauri](https://v2.tauri.app/reference/javascript/api/namespacewindow/), [Electron](https://www.electronjs.org/docs/latest/api/base-window). | Отсутствие рамки совместимо с замыслом. Отдельно проверить фокус именно поля ввода, масштабирование и доступ к управлению приложением. |
| Активация и возврат фокуса | Windows ограничивает `SetForegroundWindow`. Обработчик зарегистрированного hotkey получает обычный контекст для активации, но это не снимает системных ограничений. В macOS активация является запросом, который ОС может отклонить. [Windows API](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setforegroundwindow), [Microsoft о hotkey](https://devblogs.microsoft.com/oldnewthing/20090226-00/?p=19013), [Apple](https://developer.apple.com/documentation/appkit/passing-control-from-one-app-to-another-with-cooperative-activation). | Проверить вызов из другого приложения, отсутствие потери первых символов, скрытие и возврат в прежнее поле. Не обещать принудительный фокус в любом системном контексте. |
| Рабочие пространства | Electron документирует macOS `type: panel` для показа поверх полноэкранных приложений и на всех Spaces. `setVisibleOnAllWorkspaces` не поддерживается на Windows в Tauri и не действует там в Electron. Это ограничение показа на всех рабочих столах, а не доказательство невозможности вызова на текущем. Apple различает поведения Spaces, fullscreen и Stage Manager. [Electron panel](https://www.electronjs.org/docs/latest/api/base-window), [Electron workspaces](https://www.electronjs.org/docs/latest/api/browser-window/#winsetvisibleonallworkspacesvisible-options), [Tauri](https://v2.tauri.app/reference/javascript/api/namespacewindow/#setvisibleonallworkspaces), [Apple](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct). | Включить в прототип разные рабочие столы, Spaces, Stage Manager и fullscreen. Проверять поведение Tauri отдельно, не переносить на него гарантии Electron panel. |
| Мониторы и масштаб | Windows требует обработки смены DPI. `NSScreen` предоставляет экраны и видимые области; Electron `screen` — дисплеи, координаты и события изменений. Tauri предоставляет сведения о мониторах и геометрию окна. [Windows](https://learn.microsoft.com/en-us/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows), [Apple](https://developer.apple.com/documentation/AppKit/NSScreen), [Electron](https://www.electronjs.org/docs/latest/api/screen), [Tauri](https://v2.tauri.app/reference/javascript/api/namespacewindow/). | Неподвижность строки при истории — отдельное правило приложения. Проверить расширение в доступную сторону, прокрутку, разные масштабы и отключение монитора. |
| Буфер обмена | Оба фреймворка записывают текст. Windows `OpenClipboard` может отказать при занятом буфере; AppKit `writeObjects` также сообщает результат. [Windows](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-openclipboard), [Apple](https://developer.apple.com/documentation/appkit/nspasteboard/writeobjects(_:)), [Tauri](https://v2.tauri.app/plugin/clipboard/), [Electron](https://www.electronjs.org/docs/latest/api/clipboard). | Подтверждать копирование после успеха; согласовать поведение при ошибке. Автовставка в чужое приложение является отдельной возможностью, которой исходный запрос не требует. |
| Фон и управление | У Tauri есть System Tray, у Electron — Tray. Apple предупреждает, что статусный элемент может оказаться недоступным из-за нехватки места. [Tauri](https://v2.tauri.app/learn/system-tray/), [Electron](https://www.electronjs.org/docs/latest/api/tray), [Apple](https://developer.apple.com/documentation/appkit/nsstatusbar). | Отделить скрытие палитры от завершения процесса; предусмотреть запасной способ открыть управление через запуск приложения. |
| Автозапуск | Windows Run entries не гарантируют немедленного старта после входа. macOS `SMAppService` учитывает пользовательское одобрение. У Tauri есть autostart plugin; Electron различает регистрацию и фактическое разрешение запуска и требует проверять macOS login item в упакованной подписанной сборке после notarization. [Windows](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys), [Apple](https://developer.apple.com/documentation/servicemanagement/smappservice), [Tauri](https://v2.tauri.app/plugin/autostart/), [Electron](https://www.electronjs.org/docs/latest/api/app#appsetloginitemsettingssettings). | Показывать фактическое состояние и уважать отключение автозапуска через ОС. Согласовать значение по умолчанию. |

## Сравнение подходов

| Подход | Документированная основа | Что требуется проверить или принять |
| --- | --- | --- |
| Tauri | Rust backend, системный WebView, взаимодействие общего веб-интерфейса с нативной частью. [Архитектура Tauri](https://v2.tauri.app/concept/architecture/). | Поведение macOS panel/fullscreen может потребовать нативной доработки; проверить фокус, различия WebView и измерить ресурсы. |
| Electron | Chromium renderer и основной процесс с системными API; предусмотрен macOS panel. [Модель процессов](https://www.electronjs.org/docs/latest/tutorial/process-model), [окна](https://www.electronjs.org/docs/latest/api/base-window). | Проверить раскладки, рабочие пространства, возврат фокуса и измерить ресурсы установленной сборки. |
| Две нативные оболочки | Прямое использование перечисленных Win32/AppKit API с общим вычислительным ядром. | По архитектурной оценке, это два интерфейса и два контура поставки; нужны единые сценарии проверки поведения. Системные ограничения сохраняются. |

Архитектурная рекомендация исследователя: общее ядро отвечает за язык выражений, вычисления, переменные, результаты и диапазоны ошибок; оболочки — за окно, сочетания, фокус, буфер и жизненный цикл. Ответственность хранения и точный контракт определить в вопросе архитектуры. Это предложение, а не выбранный стек или принятое распределение ответственности.

## Установка и обновления

- Для доверенной поставки macOS вне Store предусмотрены Developer ID и notarization. [Apple Developer ID](https://developer.apple.com/developer-id/).
- Подпись Windows сама по себе не гарантирует отсутствия SmartScreen для нового файла. [Microsoft SmartScreen](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/smartscreen-reputation).
- Tauri updater проверяет отдельную подпись обновления; она не заменяет подпись приложения для ОС. Electron autoUpdater зависит от упаковки и требует подписи приложения на macOS. [Tauri updater](https://v2.tauri.app/plugin/updater/), [Electron autoUpdater](https://www.electronjs.org/docs/latest/api/auto-updater).
- Для Tauri нужно выбрать доставку WebView2 на Windows: стандартный путь установки отсутствующего runtime требует сети; документация описывает и офлайн-варианты. [Установщик Tauri](https://v2.tauri.app/distribute/windows-installer/).

Рекомендация: зафиксировать каналы поставки и обновления после выбора аудитории, требований к работе без сети и архитектуры. Цены, сроки, минимальные версии ОС и поддерживаемые процессорные архитектуры данным исследованием не утверждаются.

## Минимальная проверка будущего прототипа

1. Вызов и немедленный ввод без потери первых символов; повтор, удержание, конфликт и переназначение сочетания.
2. RU/EN, нужные не-QWERTY раскладки, IME и фактические разрешения ОС.
3. Escape, выбранное действие копирования, клик снаружи, закрывшееся исходное окно; отсутствие повторного перехвата фокуса после переключения пользователя.
4. Несколько дисплеев, разные DPI, отрицательные координаты, отключение монитора; неподвижная строка при раскрытии истории.
5. Windows desktops, macOS Spaces/Stage Manager, обычный и эксклюзивный fullscreen — с явным указанием поддержанных сценариев.
6. Сон, повторный запуск, вход в систему, запрет автозапуска через ОС, полное завершение и отсутствие дублей процесса.
7. Установленная подписанная сборка: обновление, ошибка сети/подписи, сохранение данных и восстановление сочетания.
8. Измерения холодного запуска, повторного вызова, скрытого простоя и раскрытой истории на указанном оборудовании.

Эти проверки ещё не выполнены. Результаты прототипа нужны до окончательной фиксации платформенных гарантий.
