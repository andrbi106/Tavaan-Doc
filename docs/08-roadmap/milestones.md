# DOC-120 — نقشهٔ راه تَوان

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-120 |
| وضعیت | Approved v0.0.1 |
| نقش | فازها و وضعیت واقعی |
| پیش‌نیاز | DOC-030 |

## وضعیت فازهای واقعی Tavaan-Demo

| فاز | نام | موتورها | وضعیت | خروجی |
|---|---|---|---|---|
| M0 | تحلیل و معماری | — | ✅ کامل | مستندات (این مخزن) |
| M1 | هستهٔ صفر‌وابستگی | 8 | ✅ کامل | بوت، CLI، Autoloader، Container، Events |
| M2 | وب | 8 | ⬜ اسکلت | کلاس‌ها موجود، پیاده‌سازی ناقص |
| M3 | داده | 6 | ⬜ اسکلت | database/orm/migration اسکلت |
| M4 | امنیت | 6 | ⬜ اسکلت | auth/rbac/crypt اسکلت |
| M5 | زیرساخت | 9 | ⬜ اسکلت | queue/cache/mail اسکلت |
| M6 | سرویس | 7 | ⬜ اسکلت | api/observability اسکلت |
| M7 | دامنه | 3 | ⬜ اسکلت | workflow/payment اسکلت |
| M8 | ابزار | 5 | ⬜ اسکلت | scaffold/admin/plugin اسکلت |
| M9 | اپلیکیشن | — | ⬜ | — |

## فاز M1 — هسته (تکمیل‌شده ✅)

| خروجی | وضعیت |
|---|---|
| Autoloader خودنوشته | ✅ `core/Autoloading/Autoloader.php` |
| DI Container | ✅ `core/Container/Container.php` |
| Event Dispatcher | ✅ `core/Events/EventDispatcher.php` |
| Application lifecycle | ✅ `core/Application/Application.php` |
| CLI entry point | ✅ `bin/tvn` (۵ دستور) |
| HTTP entry point | ✅ `public/index.php` |
| Config + Env | ✅ `config/`, `.env` |
| ServiceProvider پایه | ✅ `core/Provider/ServiceProvider.php` |
| Facade پایه | ✅ `core/Facade/Facade.php` |
| Engine-Core (والد) | ✅ `engine-core/` |
| ۵۲ موتور (اسکلت) | ✅ `engines/` |

## فازهای بعدی (برنامه)

### M2 — وب (۲-۳ هفته)
- پیاده‌سازی کامل HTTP Kernel
- Router با Compiled Trie
- Session/Cookie
- View Engine با `.tv.php`
- i18n + Jalali

### M3 — داده (۳-۴ هفته)
- Connection Manager
- Query Builder
- ORM (Active Record + Repository)
- Migration

### M4 — امنیت (۲-۳ هفته)
- Crypt/Hash
- Auth (Session + JWT)
- RBAC
- Audit

### M5-M9
توسعهٔ تدریجی موتورهای باقی‌مانده.
