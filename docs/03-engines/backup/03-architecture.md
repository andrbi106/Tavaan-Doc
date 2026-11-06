# DOC-035-S03 — معماری داخلی (موتور backup)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-035-S03 |
| موتور | `backup` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 14 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `BackupEncrypter` | Class | `src/BackupEncrypter.php` |
| `BackupEngine` | Engine | `src/BackupEngine.php` |
| `BackupListCommand` | Command | `src/Console/BackupListCommand.php` |
| `BackupPruneCommand` | Command | `src/Console/BackupPruneCommand.php` |
| `BackupRestoreCommand` | Command | `src/Console/BackupRestoreCommand.php` |
| `BackupRunCommand` | Command | `src/Console/BackupRunCommand.php` |
| `BackupVerifyCommand` | Command | `src/Console/BackupVerifyCommand.php` |
| `DatabaseDumper` | Class | `src/DatabaseDumper.php` |
| `DatabaseRestorer` | Store | `src/DatabaseRestorer.php` |
| `BackupException` | Exception | `src/Exceptions/BackupException.php` |
| `Backup` | Facade | `src/Facades/Backup.php` |
| `Manifest` | Class | `src/Manifest.php` |
| `ZipReader` | Class | `src/ZipReader.php` |
| `backup` | Class | `src/backup.php` |

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
