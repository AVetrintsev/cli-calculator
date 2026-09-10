# Единицы измерения и эталонные преобразования

Дата проверки: 2026-09-10. Исследователь: unit_standards. Область: определения и коэффициенты; стек, библиотеки и локальные алиасы не исследовались.

Ниже приведены **кандидаты для обсуждения, а не утверждённый каталог продукта**. Контекст уже согласован: указанные группы величин, составные единицы, действительные числа, до 30 значащих цифр; обычный вывод до 10 дробных знаков с исключением для очень малых ненулевых значений; латинский набор обозначений и ровно одна активная локализация по языку интерфейса.

## Основание и точность

Текущая [SI Brochure BIPM, 9-е издание, версия 4.01 (2026)](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0) — основной источник SI. Её таблица 8 теперь называется «Non-SI units»; старую формулировку о принятии этих единиц для использования с SI не переносим как текущую классификацию.

**«Точно» здесь означает точность определения единицы**, а не точность измерения и не обещание бесконечной вычислительной точности. В SP 811 точные коэффициенты выделены жирным, остальные округлены: например, 3.785412 L для US gallon и 0.4535924 kg для pound — сокращённые табличные значения. Они недостаточны как исходные константы при рабочей точности 30 цифр. [NIST, Appendix B, B.2](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors), [таблица B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8).

Вывод исследования: для определений ниже достаточно точных конечных десятичных дробей, целых степеней и рациональных отношений; градусы/радианы требуют π. Округлённый вывод нельзя использовать как новый коэффициент. Численный контракт округления и внутреннее представление этим отчётом не выбираются.

## Длина, площадь, объём и масса

Во всех строках равенства точные; значения квадратов и кубов получены возведением точного линейного коэффициента в соответствующую степень.

| Величина / кандидат | Определение или коэффициент | Первичный источник |
| --- | --- | --- |
| Длина SI | m; десятичные кратные и дольные, например nm, µm, mm, cm, km | [BIPM, §3, табл. 7](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0) |
| Inch, international foot, yard, international mile | 1 in = 0.0254 m; 1 ft = 12 in = 0.3048 m; 1 yd = 3 ft = 0.9144 m; 1 mi = 5280 ft = 1609.344 m | [NIST, B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8), [B.6](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors) |
| Площадь | m²; 1 ha = 10000 m²; 1 in² = 0.00064516 m²; 1 ft² = 0.09290304 m²; 1 acre на international foot = 4046.8564224 m² | [BIPM, табл. 8](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0), [NIST, B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8), [NIST, современные эквиваленты](https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors) |
| Объём SI и литр | m³; 1 L = 1 dm³ = 0.001 m³; 1 mL = 1 cm³ = 0.000001 m³ | [NIST, SI Units — Volume](https://www.nist.gov/pml/owm/si-units-volume) |
| Кубические альтернативы | 1 in³ = 0.000016387064 m³; 1 ft³ = 0.028316846592 m³ | Вычислено из [точных определений длины NIST, B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8) |
| US liquid gallon | 1 gallon = 231 in³ = 3.785411784 L | [NIST HB 44 (2026), Appendix C, C-15–C-16, C-25](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c) |
| Imperial gallon | 1 gallon = 4.54609 L | [NIST, B.8, G](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8) |
| Масса SI и tonne | 1 g = 0.001 kg; 1 mg = 0.000001 kg; 1 tonne = 1 t = 1000 kg | [NIST HB 44 (2026), C-17–C-19](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c) |
| Pound / ounce avoirdupois | 1 lb = 0.45359237 kg; 1 oz = lb/16 = 0.028349523125 kg | [NIST HB 44 (2026), C-17](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c) |
| Short ton / long ton | 1 short ton = 2000 lb = 907.18474 kg; 1 long ton = 2240 lb = 1016.0469088 kg | [NIST HB 44 (2026), C-17](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c) |

US customary и British Imperial — разные системы. Для pint/quart существуют также US liquid и US dry; у ounce есть разновидности массы и отдельная fluid ounce объёма. Эти названия нельзя считать однозначными без квалификатора системы. [NIST, U.S. Metrication FAQs](https://www.nist.gov/pml/owm/faqs/us-metrication-faqs). Исторический U.S. survey foot = (1200/3937) m точно; он отличается от international foot. NIST ограничивает его дальнейшее применение историческими данными после 2022 года; различие распространяется на соответствующие acre и mile. [NIST, B.6](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors), [актуальная таблица](https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors).

## Приставки и составные единицы

Приставка входит в обозначение единицы целиком: (cm)² = (10⁻² m)² = 10⁻⁴ m², (cm)³ = 10⁻⁶ m³; соответственно km² = 10⁶ m². Для массы приставки присоединяются к g, а не к kg: mg = 10⁻⁶ kg. Составные приставки стандартом не образуются. Регистр значим: m — milli, M — mega, k — kilo. [NIST, §6.2](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-6-rules-and-style-conventions-printing-and-using).

Для min, h и d приставки SI не применяются. [NIST, §6.2.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-6-rules-and-style-conventions-printing-and-using).

Литр допускает два символа, l и L; такое исключение не означает нечувствительность других обозначений к регистру. Диапазон приставок SI сейчас 10⁻³⁰…10³⁰; набор поддерживаемых продуктом приставок ещё нужно выбрать. [BIPM, §3, табл. 8](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0).

Следствие для проверки составных единиц: масштабы перемножаются, делятся и возводятся в степень вместе с единицами. Например, (km/h)/(m/s) = 1000/3600 = 5/18 точно. Это не распространяется автоматически на температурные значения со смещённым нулём. Требование не складывать несовместимые размерности уже принято пользователем.

## Информация и регистр

Для рассматриваемых единиц информации 1 B = 8 bit. Десятичные и двоичные множители точны и различны:

| Десятичная единица | Байтов | Двоичная единица | Байтов |
| --- | ---: | --- | ---: |
| kB | 1000 | KiB | 1024 = 2¹⁰ |
| MB | 1000000 | MiB | 1048576 = 2²⁰ |
| GB | 1000000000 | GiB | 1073741824 = 2³⁰ |

Источники таблицы: [IEC, Units and symbols](https://styleguide.iec.ch/?docs=iec/typographic/units-and-symbols), [NIST, Binary prefixes](https://physics.nist.gov/cuu/Units/binary.html). Те же приставки применяются к bit: kbit = 1000 bit, Kibit = 1024 bit. В этих источниках bit и B различаются; kB и KiB не взаимозаменяемы. Для дополнительных написаний вроде b, KB, kb стандартные примеры сами по себе не задают правила пользовательского парсера.

Актуальная редакция стандарта — [IEC 80000-13:2025](https://webstore.iec.ch/en/publication/87379), заменившая редакцию 2008 года. Проверены публичная карточка стандарта и открытые таблицы IEC/NIST; полный платный текст не изучался.

## Длительности и календарь

1 min = 60 s, 1 h = 3600 s, 1 d = 86400 s — точные единицы длительности. [BIPM, табл. 8](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0).

У календарного года 365 или 366 дней; средний григорианский год за 400-летний цикл равен 365.2425 дня. Месяцы следуют календарю, а не одному постоянному коэффициенту. [USNO, Leap Years](https://aa.usno.navy.mil/faq/leap_years), [USNO, Calendars](https://aa.usno.navy.mil/faq/calendars). Юлианский год как астрономическая единица — ровно 365.25 d, то есть 31557600 s; это отдельное соглашение. [USNO, IAU resolutions, с. 8, п. 1](https://aa.usno.navy.mil/downloads/Circular_163.pdf).

Вывод: перевод календарных месяцев/лет в секунды требует календаря и исходной даты либо явно названной условной длительности. При расчёте между моментами времени дополнительно важны шкала времени и часовой пояс: календарные сутки нельзя безоговорочно отождествлять с фиксированной d; UTC использует корректировки leap second. [USNO, Leap Second](https://maia.usno.navy.mil/information/what-is-a-leap-second). Поддержка календарной арифметики этим исследованием не утверждается.

## Температурные значения и разности

Для числовых показаний шкал c, f, k:

| Объект | Точное преобразование |
| --- | --- |
| Значение Celsius → Kelvin | k = c + 273.15 |
| Значение Celsius → Fahrenheit | f = (9/5)c + 32 |
| Значение Fahrenheit → Kelvin | k = (5/9)(f − 32) + 273.15 |
| Разность / интервал | Δk = Δc; Δf = (9/5)Δc; Δc = (5/9)Δf |

Все константы в формулах точные; 5/9 — точное рациональное отношение, его конечная десятичная запись будет приближением. Обозначения шкал: °C, °F, K. [NIST, SI Units — Temperature, Temperature Conversion (Exact)](https://www.nist.gov/pml/owm/si-units-temperature).

Следствие: разность показаний 30 °C и 20 °C равна интервалу 10 K, а значение 10 °C соответствует 283.15 K. Поэтому обычное умножение на коэффициент не описывает все температурные операции. Сложение двух показаний, прибавление интервала и использование °C/°F в произведениях требуют отдельных правил языка; стандартные формулы перевода эти правила не выбирают.

## Углы

1° = π/180 rad точно; 180° = π rad; прямой угол = π/2 rad. В SI радиан имеет размерность один, однако BIPM отдельно отмечает, что угол не тождествен произвольному отношению длин. [BIPM, табл. 4, примечание b; табл. 8](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0).

Вывод: математическое равенство через π точное, конечные десятичные градусно-радианные коэффициенты приближённые. Поведение углов как аргументов функций и при взаимодействии с безразмерными числами должно быть явно задано продуктом.

## 15 эталонных примеров

Это математические эталоны, **не утверждение синтаксиса или наличия единиц**. Десятичная точка служит единой записью коэффициентов. Знак = означает точное равенство, ≈ — показ до 10 дробных знаков; выбранный продуктом режим округления здесь не фиксируется.

| № | Проверка | Эталон | Основание |
| ---: | --- | --- | --- |
| 1 | Inch и foot | 12 in = 1 ft = 0.3048 m | [NIST, B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8) |
| 2 | Mile | 1 mi = 1.609344 km | [NIST, современные эквиваленты](https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors) |
| 3 | Квадрат приставки | 1 km² = 1000000 m²; 1 cm² = 0.0001 m² | Вычислено по [NIST, §6.2.3](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-6-rules-and-style-conventions-printing-and-using) |
| 4 | Литр и куб приставки | 1 L = 1000 cm³; 1 cm³ = 0.000001 m³ | [NIST, Volume](https://www.nist.gov/pml/owm/si-units-volume) |
| 5 | Два gallon | US liquid: 3.785411784 L; Imperial: 4.54609 L на один gallon | [NIST HB 44, C-16](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c), [NIST, B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8) |
| 6 | Ounce / pound | 16 oz avoirdupois = 1 lb = 453.59237 g | [NIST HB 44, C-17](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c) |
| 7 | Три «тонны» | tonne: 1000 kg; short ton: 907.18474 kg; long ton: 1016.0469088 kg | [NIST HB 44, C-17](https://www.nist.gov/document/2026-nist-handbook-44-appendix-c) |
| 8 | Составная скорость | 90 km/h = 25 m/s | Вычислено из точных определений выше |
| 9 | Фиксированная длительность | 1.5 d = 36 h = 129600 s | Вычислено из точных определений выше |
| 10 | Bit / byte | 1 kB = 8000 bit; 1 KiB = 8192 bit | Вычислено по [NIST, Binary prefixes](https://physics.nist.gov/cuu/Units/binary.html) |
| 11 | MB / MiB / GiB | 1 MiB = 1.048576 MB; 1 GiB = 1.073741824 GB | Вычислено по [IEC, Units and symbols](https://styleguide.iec.ch/?docs=iec/typographic/units-and-symbols) |
| 12 | Температурное значение | 32 °F = 0 °C = 273.15 K | [NIST, Temperature](https://www.nist.gov/pml/owm/si-units-temperature) |
| 13 | Температурный интервал | Δ18 °F = Δ10 °C = 10 K; величина Δ обозначает интервал | [NIST, Temperature](https://www.nist.gov/pml/owm/si-units-temperature) |
| 14 | Градусы / радианы | 180° = π rad ≈ 3.1415926536 rad | Вычислено из определения выше |
| 15 | Очень малое ненулевое значение | 1 nm = 0.000000000001 km = 10⁻¹² km; вывод 0 km потерял бы значение | Вычислено по [NIST, §6.2](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-6-rules-and-style-conventions-printing-and-using) |

## Решения, оставшиеся пользователю

1. Конкретный каталог единиц и пределы приставок; нужны ли acre, исторический survey foot, troy, US dry и другие специальные разновидности.
2. Допустимость неквалифицированных gallon, pint, ounce, ton; способ выбора системы без скрытой зависимости от языка интерфейса. Коэффициент физической единицы не определяется локализацией её названия.
3. Дополнительные написания и регистр входных обозначений: b/bit/B, KB/kB, формы для °C/°F и степеней. Нормативные символы выше служат материалом для решения; локальные алиасы здесь не выбраны.
4. Только фиксированные длительности или также календарные месяцы/годы; при втором варианте — исходная дата, календарь, конец месяца, часовой пояс и шкала времени.
5. Как выражать температурный интервал и отличать его от показания; разрешённые сложение, вычитание, умножение, деление и степени для температурных величин.
6. Сохраняется ли семантика угла при составных операциях, и где допустима безразмерная величина вместо угла.
7. Правила округления внутри 30 значащих цифр и представления очень малых результатов; точное определение коэффициента и округление экрана должны проверяться отдельно.

Проверка: все приведённые URL открыты как первичные источники; рассмотрены актуальные BIPM 4.01, HB 44 (2026) и публичные материалы IEC 80000-13:2025. Эталоны и производные коэффициенты проверены арифметически отдельно от приложения. Реализация калькулятора и её тесты в рамках исследования не менялись.
