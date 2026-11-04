# DOC-035 — موتور Backup | پشتیبان‌گیری

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-035 |
| Engine ID | `tavaan.engine.backup` |
| Namespace | `Tavaan\Engine\Backup\` |
| مسیر | `engines/backup/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `filesystem` |
| وابستگی (نرم/اختیاری) | `database`, `crypt`, `cache`, `compat` |
| Facade | `Backup` → accessor `backup` |
| جداول DB | — |
| LOC برآوردی | 1388 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Backup پشتیبان‌گیری از پایگاه‌داده و فایل‌ها را با dump خالص PHP (بدون mysqldump)، ZIP خودنوشته (ZipWriterPure)، رمزنگاری AES-256-GCM با کلید جدا از APP_KEY، verify و restore در حالت نگهداری فراهم می‌کند. retention و prune خودکار نیز پشتیبانی می‌شود.

### ۱٫۲ دامنه (What)
- ✅ شامل: DB dump خالص PHP، ZIP خالص، رمزنگاری AES-256-GCM، verify، restore، retention/prune، دستورات کنسول backup:*
- ❌ خارج از دامنه: ذخیره‌سازی اشیاء (در filesystem)، صف بندی وظایف (در queue)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-BACKUP-01 | پیاده‌سازی هستهٔ موتور backup به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-BACKUP-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-BACKUP-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| spatie/laravel-backup | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Backup\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی این موتور در `engines/backup/config/backup.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.backup.config.backup`.

در v0.0.1 فقط ساختار اولیه پشتیبانی می‌شود.

## ۷. قراردادها
N/A: قراردادها در نسخه‌های بعدی به `core/Contracts/` منتقل می‌شوند.

## ۸. نقاط توسعه
N/A: v0.0.1

## ۹. امنیت
N/A: در نسخهٔ ۱.۰ با چک‌لیست کامل.

## ۱۰. کارایی
N/A: بنچمارک در نسخهٔ ۱.۰.

## ۱۱. مدیریت خطا
N/A: کلاس‌های استثنا در نسخه‌های بعدی.

## ۱۲. تست
N/A: موتور test در v0.0.1 وجود دارد اما آزمون‌ها هنوز نوشته نشده‌اند.

## ۱۳. مثال End-to-End
N/A: در نسخهٔ ۱.۰.

## ۱۴. معیار پذیرش 🧪
| ID | معیار | تست |
|---|---|---|
| AC-BACKUP-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-BACKUP-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| spatie/laravel-backup | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.backup.v1
engine:
  id: tavaan.engine.backup
  namespace: Tavaan\Engine\Backup\
  path: engines/backup
  priority: P1
  phase: M5
  depends_on: [config, filesystem]
  soft_depends_on: [database, crypt, cache, compat]
  facade: {name: Backup, accessor: backup}
  tables: []
  config_file: engines/backup/config/backup.php
  loc_estimate: 1388
  acceptance:
    - {id: AC-BACKUP-01, test: 'php bin/tvn engines'}
    - {id: AC-BACKUP-02, test: 'php bin/tvn engines --list'}
```
