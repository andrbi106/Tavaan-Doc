# DOC-081-S03 — معماری داخلی (موتور view)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-081-S03 |
| موتور | `view` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 14 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ComponentAttributeBag` | Class | `src/ComponentAttributeBag.php` |
| `ViewCacheCommand` | Command | `src/Console/ViewCacheCommand.php` |
| `ViewClearCommand` | Command | `src/Console/ViewClearCommand.php` |
| `DirectiveRegistry` | Class | `src/DirectiveRegistry.php` |
| `Escaper` | Class | `src/Escaper.php` |
| `ViewException` | Exception | `src/Exceptions/ViewException.php` |
| `View` | Facade | `src/Facades/View.php` |
| `SafeString` | Class | `src/SafeString.php` |
| `TemplateCompiler` | Class | `src/TemplateCompiler.php` |
| `View` | Class | `src/View.php` |
| `ViewEngine` | Engine | `src/ViewEngine.php` |
| `ViewFactory` | Factory | `src/ViewFactory.php` |
| `ViewFinder` | Class | `src/ViewFinder.php` |
| `ViewServiceProvider` | ServiceProvider | `src/ViewServiceProvider.php` |

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
