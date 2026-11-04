# DOC-075-S03 — معماری داخلی (موتور security)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-075-S03 |
| موتور | `security` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 12 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Csrf` | Class | `src/Csrf.php` |
| `CsrfManager` | Manager | `src/Csrf/CsrfManager.php` |
| `SsrfException` | Exception | `src/Exceptions/SsrfException.php` |
| `Security` | Facade | `src/Facades/Security.php` |
| `CsrfVerifyMiddleware` | Middleware | `src/Middleware/CsrfVerifyMiddleware.php` |
| `ThrottleMiddleware` | Middleware | `src/Middleware/ThrottleMiddleware.php` |
| `InputNormalizer` | Class | `src/Normalize/InputNormalizer.php` |
| `RateLimiter` | Class | `src/RateLimit/RateLimiter.php` |
| `HtmlSanitizer` | Class | `src/Sanitize/HtmlSanitizer.php` |
| `Security` | Class | `src/Security.php` |
| `SecurityEngine` | Engine | `src/SecurityEngine.php` |
| `security` | Class | `src/security.php` |

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
