# DOC-037-S03 — معماری داخلی (موتور compat)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-037-S03 |
| موتور | `compat` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 14 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Compat` | Class | `src/Compat.php` |
| `CompatEngine` | Engine | `src/CompatEngine.php` |
| `CompatServiceProvider` | ServiceProvider | `src/CompatServiceProvider.php` |
| `DoctorCommand` | Command | `src/Console/DoctorCommand.php` |
| `CompatInterface` | Contract/Interface | `src/Contracts/CompatInterface.php` |
| `MagicBytesDetectorInterface` | Contract/Interface | `src/Contracts/MagicBytesDetectorInterface.php` |
| `Utf8Interface` | Contract/Interface | `src/Contracts/Utf8Interface.php` |
| `ZipWriterPureInterface` | Contract/Interface | `src/Contracts/ZipWriterPureInterface.php` |
| `Decimal` | Class | `src/Decimal.php` |
| `EngineCapabilityException` | Exception | `src/EngineCapabilityException.php` |
| `MagicBytesDetector` | Class | `src/MagicBytesDetector.php` |
| `RoundingMode` | Class | `src/RoundingMode.php` |
| `Utf8` | Class | `src/Utf8.php` |
| `ZipWriterPure` | Class | `src/ZipWriterPure.php` |

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
