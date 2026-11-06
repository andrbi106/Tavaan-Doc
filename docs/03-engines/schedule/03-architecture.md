# DOC-072-S03 — معماری داخلی (موتور schedule)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-072-S03 |
| موتور | `schedule` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 8 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ScheduleListCommand` | Command | `src/Console/ScheduleListCommand.php` |
| `ScheduleRunCommand` | Command | `src/Console/ScheduleRunCommand.php` |
| `CronExpression` | Class | `src/CronExpression.php` |
| `InvalidCronException` | Exception | `src/Exceptions/InvalidCronException.php` |
| `Schedule` | Facade | `src/Facades/Schedule.php` |
| `ScheduleEngine` | Engine | `src/ScheduleEngine.php` |
| `ScheduleEvent` | Class | `src/ScheduleEvent.php` |
| `schedule` | Class | `src/schedule.php` |

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
