# DOC-032-S03 — معماری داخلی (موتور api)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-032-S03 |
| موتور | `api` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 18 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `APIEngine` | Engine | `src/APIEngine.php` |
| `ApiResolver` | Class | `src/ApiResolver.php` |
| `Api` | Class | `src/Attributes/Api.php` |
| `ApiParam` | Class | `src/Attributes/ApiParam.php` |
| `ApiResponse` | Value/DTO | `src/Attributes/ApiResponse.php` |
| `ApiDocsCommand` | Command | `src/Console/ApiDocsCommand.php` |
| `ApiException` | Exception | `src/Exceptions/ApiException.php` |
| `JsonResource` | Class | `src/JsonResource.php` |
| `ApiVersionMiddleware` | Middleware | `src/Middleware/ApiVersionMiddleware.php` |
| `IdempotencyMiddleware` | Middleware | `src/Middleware/IdempotencyMiddleware.php` |
| `ThrottleMiddleware` | Middleware | `src/Middleware/ThrottleMiddleware.php` |
| `OpenApiGenerator` | Generator | `src/OpenApi/OpenApiGenerator.php` |
| `Yaml` | Class | `src/OpenApi/Yaml.php` |
| `AnonymousResourceCollection` | Collection | `src/Resources/AnonymousResourceCollection.php` |
| `MergeValue` | Class | `src/Resources/MergeValue.php` |
| `MissingValue` | Class | `src/Resources/MissingValue.php` |
| `ResourceCollection` | Collection | `src/Resources/ResourceCollection.php` |
| `api` | Class | `src/api.php` |

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
