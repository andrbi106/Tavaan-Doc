# DOC-057-S03 — معماری داخلی (موتور migration)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-057-S03 |
| موتور | `migration` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 8 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `MigrateCommand` | Command | `src/Console/MigrateCommand.php` |
| `MigrateFreshCommand` | Command | `src/Console/MigrateFreshCommand.php` |
| `MigrateInstallCommand` | Command | `src/Console/MigrateInstallCommand.php` |
| `MigrateRefreshCommand` | Command | `src/Console/MigrateRefreshCommand.php` |
| `MigrateRollbackCommand` | Command | `src/Console/MigrateRollbackCommand.php` |
| `MigrateStatusCommand` | Command | `src/Console/MigrateStatusCommand.php` |
| `MigrationEngine` | Engine | `src/MigrationEngine.php` |
| `migration` | Class | `src/migration.php` |

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
