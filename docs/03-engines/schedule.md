# DOC-072 — موتور Schedule | زمان‌بندی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-072 |
| Engine ID | `tavaan.engine.schedule` |
| Namespace | `Tavaan\Engine\Schedule\` |
| مسیر | `engines/schedule/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `console` |
| وابستگی (نرم/اختیاری) | `cache`, `queue`, `log` |
| Facade | `Schedule` → accessor `schedule` |
| جداول DB | — |
| LOC برآوردی | 960 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Schedule زمان‌بندی وظایف را با Cron expressions، intervals، withoutOverlapping، runInBackground و command-line runner فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: ScheduleManager، CronExpression، ScheduleEvent، run/list commands، overlap guard
- ❌ خارج از دامنه: Queue (در queue)، Console (در console)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-SCHED-01 | پیاده‌سازی هستهٔ موتور schedule به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-SCHED-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-SCHED-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Scheduler + cron | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Schedule\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 8 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ScheduleListCommand` | Command | `src/Console/ScheduleListCommand.php` |
| `ScheduleRunCommand` | Command | `src/Console/ScheduleRunCommand.php` |
| `CronExpression` | Class | `src/CronExpression.php` |
| `InvalidCronException` | Exception | `src/Exceptions/InvalidCronException.php` |
| `Schedule` | Facade | `src/Facades/Schedule.php` |
| `ScheduleEngine` | Engine | `src/ScheduleEngine.php` |
| `ScheduleEvent` | Class | `src/ScheduleEvent.php` |
| `schedule` | Class | `src/schedule.php` |

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
فایل پیکربندی این موتور در `engines/schedule/config/schedule.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.schedule.config.schedule`.

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
| AC-SCHEDULE-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-SCHEDULE-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Scheduler + cron | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.schedule.v1
engine:
  id: tavaan.engine.schedule
  namespace: Tavaan\Engine\Schedule\
  path: engines/schedule
  priority: P1
  phase: M5
  depends_on: [config, console]
  soft_depends_on: [cache, queue, log]
  facade: {name: Schedule, accessor: schedule}
  tables: []
  config_file: engines/schedule/config/schedule.php
  loc_estimate: 960
  acceptance:
    - {id: AC-SCHEDULE-01, test: 'php bin/tvn engines'}
    - {id: AC-SCHEDULE-02, test: 'php bin/tvn engines --list'}
```
