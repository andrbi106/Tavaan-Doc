# DOC-AUDIT — گزارش ممیزی فریمورک تَوان

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-AUDIT |
| وضعیت | Approved v1.0 |
| نقش | قالب گزارش ممیزی انطباق با مشخصات رسمی |
| تاریخ | — |

## خلاصه

این سند قالب رسمی گزارش ممیزی انطباق یک پیاده‌سازی با مشخصات فریمورک تَوان است.
برای هر پیاده‌سازی، این قالب پر شود.

- **نسخهٔ مشخصات:** v1.0.0
- **کل قوانین سخت:** ۱۰ (R1-R10)
- **کل اصول بنیادین:** ۱۲ (P1-P12)

## نتایج قوانین سخت (R1-R10)

| قانون | وضعیت | تعداد نقض | توصیه |
|---|---|---|---|
| R1 strict_types | — | — | همهٔ فایل‌ها باید `declare(strict_types=1)` داشته باشند |
| R2 بدون require دستی | — | — | فقط Autoloader هسته |
| R3 ZeroDependency | — | — | هیچ پکیج بیرونی در core/ و engines/ |
| R4 بدون property پویا | — | — | همهٔ propertyها typed یا readonly |
| R5 Contract-First | — | — | هر کلاس عمومی Interface دارد |
| R6 تکمیل موتور | — | — | Provider + Interface + Tests + Docs + Benchmark |
| R7 namespace ریشه | — | — | فقط از ریشه‌های مجاز |
| R8 مدیریت خطا | — | — | استثناهای اختصاصی با MessageId |
| R9 Prepared Statement | — | — | بدون الحاق رشته در SQL |
| R10 قبل از Merge | — | — | php -l + PHPStan + تست + Benchmark |

## نتایج اصول (P1-P12)

| اصل | وضعست | یادداشت |
|---|---|---|
| P1 Zero Dependency | — | — |
| P2 Contract-First | — | — |
| P3 Minimal Kernel | — | — |
| P4 Explicit Boundaries | — | — |
| P5 Events over Calls | — | — |
| P6 Fail Fast & Loud | — | — |
| P7 Secure by Default | — | — |
| P8 No Hidden Magic | — | — |
| P9 SRP + Small Surface | — | — |
| P10 Readable Performance | — | — |
| P11 Language Forward-Compat | — | — |
| P12 Extensibility Triad | — | — |

## تفاوت‌ها با مشخصات رسمی

| مورد | مشخصات رسمی | پیاده‌سازی | توصیه |
|---|---|---|---|

## تناقضات داخلی

| تناقض | محل | توصیه |
|---|---|---|

## توصیه‌های اولویت‌دار

۱. —
۲. —
۳. —
