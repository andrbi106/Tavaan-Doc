# DOC-061 — موتور Optimizer | بهینه‌سازی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-061 |
| Engine ID | `tavaan.engine.optimizer` |
| Namespace | `Tavaan\Engine\Optimizer\` |
| مسیر | `engines/optimizer/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | `config`, `console` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 397 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Optimizer بهینه‌سازی عملکرد برنامه را با cache route/config/event/view، precompilation، opcache و benchmarking فراهم می‌کند و راهکارهایی برای payload کوچک‌تر و سریع‌تر ارائه می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: Route/Config/Event/View cache، precompilation، opcache advisory، OptimizerResult
- ❌ خارج از دامنه: Compiler view (در view)، Cache (در cache)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-OPT-01 | پیاده‌سازی هستهٔ موتور optimizer به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-OPT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-OPT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel optimize + opcache | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Optimizer\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 3 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Optimizer` | Class | `src/Optimizer.php` |
| `OptimizerEngine` | Engine | `src/OptimizerEngine.php` |
| `OptimizerResult` | Value/DTO | `src/OptimizerResult.php` |

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
فایل پیکربندی: `engines/optimizer/config/optimizer.php`

کلیدهای اصلی:
`cache_dir`

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
| AC-OPTIMIZER-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-OPTIMIZER-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel optimize + opcache | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.optimizer.v1
engine:
  id: tavaan.engine.optimizer
  namespace: Tavaan\Engine\Optimizer\
  path: engines/optimizer
  priority: P0
  phase: M1
  depends_on: [config, console]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/optimizer/config/optimizer.php
  loc_estimate: 397
  acceptance:
    - {id: AC-OPTIMIZER-01, test: 'php bin/tvn engines'}
    - {id: AC-OPTIMIZER-02, test: 'php bin/tvn engines --list'}
```
