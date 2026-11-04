# DOC-045-S03 — معماری داخلی (موتور error)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-045-S03 |
| موتور | `error` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 14 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ErrorCode` | Class | `src/ErrorCode.php` |
| `ErrorEngine` | Engine | `src/ErrorEngine.php` |
| `ErrorHandler` | Handler | `src/ErrorHandler.php` |
| `ErrorServiceProvider` | ServiceProvider | `src/ErrorServiceProvider.php` |
| `ExceptionHandler` | Exception | `src/ExceptionHandler.php` |
| `ExceptionMapper` | Exception | `src/ExceptionMapper.php` |
| `HttpException` | Exception | `src/HttpException.php` |
| `LogMasker` | Class | `src/LogMasker.php` |
| `RefCodeGenerator` | Generator | `src/RefCodeGenerator.php` |
| `RenderResult` | Value/DTO | `src/RenderResult.php` |
| `CliRenderer` | Renderer | `src/Renderers/CliRenderer.php` |
| `DebugRenderer` | Renderer | `src/Renderers/DebugRenderer.php` |
| `HtmlRenderer` | Renderer | `src/Renderers/HtmlRenderer.php` |
| `JsonRenderer` | Renderer | `src/Renderers/JsonRenderer.php` |

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
