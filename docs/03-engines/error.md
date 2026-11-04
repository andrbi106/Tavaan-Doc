# DOC-045 — موتور Error | مدیریت خطا

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-045 |
| Engine ID | `tavaan.engine.error` |
| Namespace | `Tavaan\Engine\Error\` |
| مسیر | `engines/error/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | `config`, `log` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 992 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Error مدیریت یکپارچه استثناها را با mapping کد خطا، rendererهای CLI/JSON/HTML/Debug، ref-code generation، log masking و توزیع به لاگر فراهم می‌کند و تجربهٔ دیباگ و گزارش خطای ساختاریافته ارائه می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: ExceptionHandler، ExceptionMapper، Renderers (CLI/JSON/HTML/Debug)، RefCodeGenerator، LogMasker، ErrorCode
- ❌ خارج از دامنه: لاگ (در log)، HTTP (در http)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-ERROR-01 | پیاده‌سازی هستهٔ موتور error به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-ERROR-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-ERROR-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Exceptions + Boo boo | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Error\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 14 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ErrorCode` | Class | `src/ErrorCode.php` |
| `ErrorEngine` | Engine | `src/ErrorEngine.php` |
| `ErrorHandler` | Handler | `src/ErrorHandler.php` |
| `ErrorServiceProvider` | ServiceProvider | `src/ErrorServiceProvider.php` |
| `ExceptionHandler` | Exception | `src/ExceptionHandler.php` |
| `ExceptionMapper` | Exception | `src/ExceptionMapper.php` |
| `HttpException` | Exception | `src/HttpException.php` |
| `LogMasker` | Class | `src/LogMasker.php` |
| `RefCodeGenerator` | Generator | `src/RefCodeGenerator.php` |
| `RenderResult` | Value/DTO | `src/RenderResult.php` |
| `CliRenderer` | Renderer | `src/Renderers/CliRenderer.php` |
| `DebugRenderer` | Renderer | `src/Renderers/DebugRenderer.php` |
| `HtmlRenderer` | Renderer | `src/Renderers/HtmlRenderer.php` |
| `JsonRenderer` | Renderer | `src/Renderers/JsonRenderer.php` |

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
فایل پیکربندی: `engines/error/config/error.php`

کلیدهای اصلی:
`debug`, `auto_register`, `strict_deprecated`, `show_trace`, `sensitive_keys`

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
| AC-ERROR-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-ERROR-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Exceptions + Boo boo | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.error.v1
engine:
  id: tavaan.engine.error
  namespace: Tavaan\Engine\Error\
  path: engines/error
  priority: P0
  phase: M1
  depends_on: [config, log]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/error/config/error.php
  loc_estimate: 992
  acceptance:
    - {id: AC-ERROR-01, test: 'php bin/tvn engines'}
    - {id: AC-ERROR-02, test: 'php bin/tvn engines --list'}
```
