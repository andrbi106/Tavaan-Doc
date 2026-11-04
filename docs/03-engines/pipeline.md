# DOC-064 — موتور Pipeline | خط لوله

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-064 |
| Engine ID | `tavaan.engine.pipeline` |
| Namespace | `Tavaan\Engine\Pipeline\` |
| مسیر | `engines/pipeline/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | `container` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 410 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Pipeline اجرای زنجیره‌ای middleware/pipe را با contracts استاندارد، مدیریت عمق و exception handling فراهم می‌کند و در HTTP و job processing استفاده می‌شود.

### ۱٫۲ دامنه (What)
- ✅ شامل: Pipeline، MiddlewareInterface، max depth guard، exception handling
- ❌ خارج از دامنه: HTTP (در http)، Queue (در queue)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-PIPE-01 | پیاده‌سازی هستهٔ موتور pipeline به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-PIPE-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-PIPE-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Pipeline + League Pipeline | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Pipeline\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 8 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `MiddlewareInterface` | Middleware | `src/Contracts/MiddlewareInterface.php` |
| `PipelineInterface` | Contract/Interface | `src/Contracts/PipelineInterface.php` |
| `PipelineException` | Exception | `src/Exceptions/PipelineException.php` |
| `PipelineMaxDepthException` | Exception | `src/Exceptions/PipelineMaxDepthException.php` |
| `PipelinePipeNotFoundException` | Exception | `src/Exceptions/PipelinePipeNotFoundException.php` |
| `Pipeline` | Class | `src/Pipeline.php` |
| `PipelineEngine` | Engine | `src/PipelineEngine.php` |
| `PipelineServiceProvider` | ServiceProvider | `src/PipelineServiceProvider.php` |

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
فایل پیکربندی: `engines/pipeline/config/pipeline.php`

کلیدهای اصلی:
`method`, `terminate_method`

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
| AC-PIPELINE-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-PIPELINE-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Pipeline + League Pipeline | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.pipeline.v1
engine:
  id: tavaan.engine.pipeline
  namespace: Tavaan\Engine\Pipeline\
  path: engines/pipeline
  priority: P0
  phase: M1
  depends_on: [container]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/pipeline/config/pipeline.php
  loc_estimate: 410
  acceptance:
    - {id: AC-PIPELINE-01, test: 'php bin/tvn engines'}
    - {id: AC-PIPELINE-02, test: 'php bin/tvn engines --list'}
```
