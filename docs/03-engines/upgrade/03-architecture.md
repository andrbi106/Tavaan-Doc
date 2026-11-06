# DOC-079-S03 — معماری داخلی (موتور upgrade)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-079-S03 |
| موتور | `upgrade` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 16 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ConfigMigrator` | Class | `src/ConfigMigrator.php` |
| `UpgradeCheckCommand` | Command | `src/Console/Commands/UpgradeCheckCommand.php` |
| `UpgradeCommand` | Command | `src/Console/Commands/UpgradeCommand.php` |
| `UpgradePatchesCommand` | Command | `src/Console/Commands/UpgradePatchesCommand.php` |
| `UpgradeRollbackCommand` | Command | `src/Console/Commands/UpgradeRollbackCommand.php` |
| `UpgradeStatusCommand` | Command | `src/Console/Commands/UpgradeStatusCommand.php` |
| `UpgradeException` | Exception | `src/Exceptions/UpgradeException.php` |
| `PatchRunner` | Class | `src/PatchRunner.php` |
| `PreChecker` | Class | `src/PreChecker.php` |
| `BackupAdapter` | Class | `src/Support/BackupAdapter.php` |
| `BackupRunnerInterface` | Contract/Interface | `src/Support/BackupRunnerInterface.php` |
| `Upgrade` | Class | `src/Upgrade.php` |
| `UpgradeEngine` | Engine | `src/UpgradeEngine.php` |
| `UpgradeRepository` | Repository | `src/UpgradeRepository.php` |
| `Upgrader` | Class | `src/Upgrader.php` |
| `VersionResolver` | Class | `src/VersionResolver.php` |

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
