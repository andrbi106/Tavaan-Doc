# DOC-039 — موتور Console | چارچوب CLI

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-039 |
| Engine ID | `tavaan.engine.console` |
| Namespace | `Tavaan\Engine\Console\` |
| مسیر | `engines/console/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | `container`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 3559 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Console زیرساخت CLI را با تعریف دستورات، آرگومان‌ها، گزینه‌ها، رنگ‌آمیزی ANSI و خروجی جدولی فراهم می‌کند و پایهٔ اجرای همه دستورات `php bin/tvn` را تشکیل می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: Command registry، Argument/Option parsing، ANSI output، Table renderer، Schedule integration
- ❌ خارج از دامنه: زمان‌بندی (در schedule)، تست‌های CLI (در test)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-CONSOLE-01 | پیاده‌سازی هستهٔ موتور console به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-CONSOLE-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-CONSOLE-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Symfony Console | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Console\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 38 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Application` | Class | `src/Application.php` |
| `ArgvParser` | Class | `src/ArgvParser.php` |
| `Command` | Command | `src/Command.php` |
| `AboutCommand` | Command | `src/Commands/AboutCommand.php` |
| `ArchCheckCommand` | Command | `src/Commands/ArchCheckCommand.php` |
| `AutoloadCacheCommand` | Command | `src/Commands/AutoloadCacheCommand.php` |
| `BenchAllCommand` | Command | `src/Commands/BenchAllCommand.php` |
| `ConfigCacheCommand` | Command | `src/Commands/ConfigCacheCommand.php` |
| `ConfigClearCommand` | Command | `src/Commands/ConfigClearCommand.php` |
| `DoctorCommand` | Command | `src/Commands/DoctorCommand.php` |
| `DownCommand` | Command | `src/Commands/DownCommand.php` |
| `EngineValidateCommand` | Command | `src/Commands/EngineValidateCommand.php` |
| `EnvCheckCommand` | Command | `src/Commands/EnvCheckCommand.php` |
| `EnvCommand` | Command | `src/Commands/EnvCommand.php` |
| `EventListCommand` | Command | `src/Commands/EventListCommand.php` |
| `LintPhpCommand` | Command | `src/Commands/LintPhpCommand.php` |
| `ModuleDisableCommand` | Command | `src/Commands/ModuleDisableCommand.php` |
| `ModuleEnableCommand` | Command | `src/Commands/ModuleEnableCommand.php` |
| `ModuleListCommand` | Command | `src/Commands/ModuleListCommand.php` |
| `ModuleValidateCommand` | Command | `src/Commands/ModuleValidateCommand.php` |
| `OptimizeClearCommand` | Command | `src/Commands/OptimizeClearCommand.php` |
| `OptimizeCommand` | Command | `src/Commands/OptimizeCommand.php` |
| `SecurityScanCommand` | Command | `src/Commands/SecurityScanCommand.php` |
| `StyleCheckCommand` | Command | `src/Commands/StyleCheckCommand.php` |
| `TestCommand` | Command | `src/Commands/TestCommand.php` |
| `UpCommand` | Command | `src/Commands/UpCommand.php` |
| `VersionCommand` | Command | `src/Commands/VersionCommand.php` |
| `ConsoleEngine` | Engine | `src/ConsoleEngine.php` |
| `ConsoleKernel` | Class | `src/ConsoleKernel.php` |
| `ConsoleServiceProvider` | ServiceProvider | `src/ConsoleServiceProvider.php` |
| _(و دیگر کلاس‌ها)_ | — | — |

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
فایل پیکربندی: `engines/console/config/console.php`

کلیدهای اصلی:
`paths`, `colors`, `verbose`

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
| AC-CONSOLE-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-CONSOLE-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Symfony Console | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.console.v1
engine:
  id: tavaan.engine.console
  namespace: Tavaan\Engine\Console\
  path: engines/console
  priority: P0
  phase: M1
  depends_on: [container, config]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/console/config/console.php
  loc_estimate: 3559
  acceptance:
    - {id: AC-CONSOLE-01, test: 'php bin/tvn engines'}
    - {id: AC-CONSOLE-02, test: 'php bin/tvn engines --list'}
```
