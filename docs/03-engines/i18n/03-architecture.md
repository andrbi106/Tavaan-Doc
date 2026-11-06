# DOC-052-S03 — معماری داخلی (موتور i18n)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-052-S03 |
| موتور | `i18n` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 11 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `TranslatorInterface` | Contract/Interface | `src/Contracts/TranslatorInterface.php` |
| `Lang` | Facade | `src/Facades/Lang.php` |
| `I18nEngine` | Engine | `src/I18nEngine.php` |
| `I18nServiceProvider` | ServiceProvider | `src/I18nServiceProvider.php` |
| `Jalali` | Class | `src/Jalali/Jalali.php` |
| `JalaliDate` | Class | `src/Jalali/JalaliDate.php` |
| `NumberFormatter` | Class | `src/NumberFormatter.php` |
| `PersianFormatter` | Class | `src/PersianFormatter.php` |
| `PluralRules` | Rule | `src/PluralRules.php` |
| `Translator` | Class | `src/Translator.php` |
| `helpers` | Class | `src/helpers.php` |

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
