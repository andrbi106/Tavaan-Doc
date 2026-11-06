# DOC-076-S03 — معماری داخلی (موتور session)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-076-S03 |
| موتور | `session` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 12 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ArrayHandler` | Handler | `src/Handlers/ArrayHandler.php` |
| `CacheHandler` | Handler | `src/Handlers/CacheHandler.php` |
| `CookieHandler` | Handler | `src/Handlers/CookieHandler.php` |
| `DatabaseHandler` | Handler | `src/Handlers/DatabaseHandler.php` |
| `FileHandler` | Handler | `src/Handlers/FileHandler.php` |
| `CsrfVerifyMiddleware` | Middleware | `src/Middleware/CsrfVerifyMiddleware.php` |
| `ShareErrorsFromSessionMiddleware` | Middleware | `src/Middleware/ShareErrorsFromSessionMiddleware.php` |
| `StartSessionMiddleware` | Middleware | `src/Middleware/StartSessionMiddleware.php` |
| `SessionEngine` | Engine | `src/SessionEngine.php` |
| `SessionHandlerInterface` | Contract/Interface | `src/SessionHandlerInterface.php` |
| `SessionManager` | Manager | `src/SessionManager.php` |
| `session` | Class | `src/session.php` |

### ۳٫۲ دیاگرام وابستگی داخلی
N/A: در نسخهٔ ۱.۰ با دیاگرام PlantUML.

### ۳٫۳ الگوهای طراحی
- Service Provider + Facade (الگوی Laravel-like)
- Manager/Driver برای چند-درایوری (در صورت وجود)
- Contract → Implementation separation

---

---

## چک‌لیست ممیزی عملیاتی

- [ ] نمودار اجزا (ASCII/Mermaid) موجود است
- [ ] فهرست کلاس‌ها با نوع/مسئولیت موجود است
- [ ] نمودار توالی جریان اصلی موجود است
- [ ] نمودار وضعیت (در صورت State Machine) موجود است
- [ ] الگوهای طراحی ذکر شده

---

## وضعیت ممیزی

| شاخص | وضعیت |
|---|---|
| وضعیت محتوا | ✅ دارای محتوا |
| تعداد آیتم‌های چک‌لیست | 5 |
| نیاز به تکمیل | ✅ خیر |

---

## یادداشت‌های ممیزی‌کننده

> این بخش توسط ممیزی‌کننده پر می‌شود.

- **تاریخ ممیزی:** _TODO_
- **ممیزی‌کننده:** _TODO_
- **یادداشت:** _TODO_
