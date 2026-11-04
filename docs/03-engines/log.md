# DOC-054 — موتور Log | گزارش ساختاریافته

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-054 |
| Engine ID | `tavaan.engine.log` |
| Namespace | `Tavaan\Engine\Log\` |
| مسیر | `engines/log/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Log` → accessor `log` |
| جداول DB | — |
| LOC برآوردی | 1409 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Log زیرساخت لاگ‌نویسی را با چندین channel (File، Stderr، Syslog، Slack)، levels، formatting و rotation فراهم می‌کند و مطابق با PSR-3 عمل می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: Logger PSR-3، channels (File/Stderr/Syslog/Slack)، levels، formatter، rotation
- ❌ خارج از دامنه: Audit (در audit)، Observability (در observability)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-LOG-01 | پیاده‌سازی هستهٔ موتور log به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-LOG-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-LOG-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Monolog | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Log\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 28 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Buffer` | Class | `src/Buffer.php` |
| `FormatterInterface` | Contract/Interface | `src/Contracts/FormatterInterface.php` |
| `HandlerInterface` | Contract/Interface | `src/Contracts/HandlerInterface.php` |
| `LoggerInterface` | Contract/Interface | `src/Contracts/LoggerInterface.php` |
| `ProcessorInterface` | Contract/Interface | `src/Contracts/ProcessorInterface.php` |
| `LogException` | Exception | `src/Exceptions/LogException.php` |
| `Log` | Facade | `src/Facades/Log.php` |
| `JsonFormatter` | Class | `src/Formatters/JsonFormatter.php` |
| `LineFormatter` | Class | `src/Formatters/LineFormatter.php` |
| `ArrayHandler` | Handler | `src/Handlers/ArrayHandler.php` |
| `FileHandler` | Handler | `src/Handlers/FileHandler.php` |
| `NullHandler` | Handler | `src/Handlers/NullHandler.php` |
| `RotatingFileHandler` | Handler | `src/Handlers/RotatingFileHandler.php` |
| `StderrHandler` | Handler | `src/Handlers/StderrHandler.php` |
| `StreamHandler` | Handler | `src/Handlers/StreamHandler.php` |
| `LogEngine` | Engine | `src/LogEngine.php` |
| `LogLevel` | Class | `src/LogLevel.php` |
| `LogManager` | Manager | `src/LogManager.php` |
| `LogRecord` | Class | `src/LogRecord.php` |
| `LogServiceProvider` | ServiceProvider | `src/LogServiceProvider.php` |
| `Logger` | Class | `src/Logger.php` |
| `BacktraceProcessor` | Class | `src/Processors/BacktraceProcessor.php` |
| `EnvironmentProcessor` | Class | `src/Processors/EnvironmentProcessor.php` |
| `IdentityProcessor` | Class | `src/Processors/IdentityProcessor.php` |
| `MaskProcessor` | Class | `src/Processors/MaskProcessor.php` |
| `MemoryProcessor` | Class | `src/Processors/MemoryProcessor.php` |
| `RuntimeProcessor` | Class | `src/Processors/RuntimeProcessor.php` |
| `TraceContextProcessor` | Class | `src/Processors/TraceContextProcessor.php` |

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
فایل پیکربندی: `engines/log/config/log.php`

کلیدهای اصلی:
`level`, `default`, `handlers`, `type`, `path`, `format`, `append`, `mask_keys`, `rotation`, `enabled`, `max_files`, `max_size_mb`, `buffer`, `size`

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
| AC-LOG-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-LOG-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Monolog | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.log.v1
engine:
  id: tavaan.engine.log
  namespace: Tavaan\Engine\Log\
  path: engines/log
  priority: P0
  phase: M1
  depends_on: [config]
  soft_depends_on: []
  facade: {name: Log, accessor: log}
  tables: []
  config_file: engines/log/config/log.php
  loc_estimate: 1409
  acceptance:
    - {id: AC-LOG-01, test: 'php bin/tvn engines'}
    - {id: AC-LOG-02, test: 'php bin/tvn engines --list'}
```
