# DOC-057 — موتور Migration | مهاجرت دیتابیس

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-057 |
| Engine ID | `tavaan.engine.migration` |
| Namespace | `Tavaan\Engine\Database\Migration\` |
| مسیر | `engines/migration/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M3 |
| وابستگی (سخت) | `database`, `schema`, `console` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | `tvn_migrations` |
| LOC برآوردی | 445 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Migration نسخه‌بندی schema پایگاه‌داده را با up/down، transactions، schema builder و status reporting فراهم می‌کند و پایهٔ schema versioning است.

### ۱٫۲ دامنه (What)
- ✅ شامل: Migration runner، Schema builder، up/down، transactions، status
- ❌ خارج از دامنه: Schema (در schema)، Database (در database)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-MIGRATION-01 | پیاده‌سازی هستهٔ موتور migration به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-MIGRATION-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-MIGRATION-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Migrations + Phinx | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Database\Migration\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی این موتور در `engines/migration/config/migration.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.migration.config.migration`.

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
| AC-MIGRATION-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-MIGRATION-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Migrations + Phinx | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.migration.v1
engine:
  id: tavaan.engine.migration
  namespace: Tavaan\Engine\Database\Migration\
  path: engines/migration
  priority: P0
  phase: M3
  depends_on: [database, schema, console]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: [tvn_migrations]
  config_file: engines/migration/config/migration.php
  loc_estimate: 445
  acceptance:
    - {id: AC-MIGRATION-01, test: 'php bin/tvn engines'}
    - {id: AC-MIGRATION-02, test: 'php bin/tvn engines --list'}
```
