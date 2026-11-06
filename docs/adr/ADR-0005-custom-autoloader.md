# ADR-0005 — Autoloader خودنوشته

| متادیتا | مقدار |
|---|---|
| شماره | ADR-0005 |
| وضعیت | **Accepted** |
| تاریخ | 2026-11-04 |
| سطح اثر | Kernel |
| مرتبط | ADR-0004، DOC-027 |

## ۱. زمینه
Composer autoloader به `vendor/autoload.php` وابسته است. تَوان ZeroDependency است.

## ۲. تصمیم
`Tavaan\Core\Autoloading\Autoloader` با ویژگی‌های:
- نگاشت prefix → path (سبک PSR-4-like اما با کلید `namespace-map`)
- Wildcard: `engines/*/src/`
- ClassMap cache (اختیاری)
- Locked prefixes (غیرقابل override)
- Security: path traversal prevention

## ۳. گزینه‌ها
| گزینه | مزیت | عیب |
|---|---|---|
| Composer autoloader | استاندارد | نیاز به vendor |
| **Autoloader خودنوشته (انتخابی)** | صفر‌وابستگی | نگهداری |

## ۴. دلایل
- ADR-0004 (ZeroDependency)
- کنترل کامل روی بارگذاری کلاس
- امکان wildcard برای کشف موتورها

## ۵. پیامدها
### مثبت
- بدون vendor
- کشف خودکار موتورها با wildcard
- prefix locking برای امنیت

### منفی
- باید خودش维护 شود

## ۶. انطباق
- `core/Autoloading/Autoloader.php`
- `config/autoload.php` با کلید `namespace-map`
- `core/bootstrap.php` ثبت namespaceها

## ۷. اعتبارسنجی 🧪
- ✅ `php bin/tvn info` بدون vendor اجرا می‌شود
- ✅ ۵۲ موتور با wildcard کشف می‌شوند
- ✅ prefixهای قفل‌شده override نمی‌شوند
