# DOC-066 — موتور Queue | صف و Worker

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-066 |
| Engine ID | `tavaan.engine.queue` |
| Namespace | `Tavaan\Engine\Queue\` |
| مسیر | `engines/queue/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `event` |
| وابستگی (نرم/اختیاری) | `database`, `cache`, `log` |
| Facade | `Queue` → accessor `queue` |
| جداول DB | `tvn_jobs`, `tvn_failed_jobs`, `tvn_job_batches` |
| LOC برآوردی | 4555 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Queue صف‌بندی وظایف را با چندین connection (Database، Redis، Sync، Null)، Worker، retry، delay و failed-job management فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: QueueManager، connections (DB/Redis/Sync/Null)، Worker، Retry/Delay، Failed jobs
- ❌ خارج از دامنه: Schedule (در schedule)، Event (در event)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-QUEUE-01 | پیاده‌سازی هستهٔ موتور queue به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-QUEUE-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-QUEUE-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Queue + Symfony Messenger | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Queue\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 53 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ArrayBatchRepository` | Repository | `src/Batch/ArrayBatchRepository.php` |
| `Batch` | Class | `src/Batch/Batch.php` |
| `DatabaseBatchRepository` | Repository | `src/Batch/DatabaseBatchRepository.php` |
| `PendingBatch` | Class | `src/Batch/PendingBatch.php` |
| `PendingChain` | Class | `src/Batch/PendingChain.php` |
| `QueueFailedCommand` | Command | `src/Console/QueueFailedCommand.php` |
| `QueueFlushCommand` | Command | `src/Console/QueueFlushCommand.php` |
| `QueueListenCommand` | Command | `src/Console/QueueListenCommand.php` |
| `QueueMonitorCommand` | Command | `src/Console/QueueMonitorCommand.php` |
| `QueuePruneFailedCommand` | Command | `src/Console/QueuePruneFailedCommand.php` |
| `QueueRestartCommand` | Command | `src/Console/QueueRestartCommand.php` |
| `QueueRetryCommand` | Command | `src/Console/QueueRetryCommand.php` |
| `QueueWorkCommand` | Command | `src/Console/QueueWorkCommand.php` |
| `BatchRepositoryInterface` | Contract/Interface | `src/Contracts/BatchRepositoryInterface.php` |
| `FailedJobProviderInterface` | Contract/Interface | `src/Contracts/FailedJobProviderInterface.php` |
| `JobInterface` | Contract/Interface | `src/Contracts/JobInterface.php` |
| `QueueInterface` | Contract/Interface | `src/Contracts/QueueInterface.php` |
| `ShouldQueue` | Class | `src/Contracts/ShouldQueue.php` |
| `JobFailed` | Class | `src/Events/JobFailed.php` |
| `JobProcessed` | Class | `src/Events/JobProcessed.php` |
| `JobProcessing` | Class | `src/Events/JobProcessing.php` |
| `JobQueued` | Class | `src/Events/JobQueued.php` |
| `JobReleased` | Class | `src/Events/JobReleased.php` |
| `WorkerStopping` | Class | `src/Events/WorkerStopping.php` |
| `JobTimedOutException` | Exception | `src/Exceptions/JobTimedOutException.php` |
| `MaxAttemptsExceededException` | Exception | `src/Exceptions/MaxAttemptsExceededException.php` |
| `QueueException` | Exception | `src/Exceptions/QueueException.php` |
| `UnsafeJobException` | Exception | `src/Exceptions/UnsafeJobException.php` |
| `Queue` | Facade | `src/Facades/Queue.php` |
| `DatabaseFailedJobProvider` | Class | `src/Failed/DatabaseFailedJobProvider.php` |
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
فایل پیکربندی این موتور در `engines/queue/config/queue.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.queue.config.queue`.

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
| AC-QUEUE-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-QUEUE-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Queue + Symfony Messenger | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.queue.v1
engine:
  id: tavaan.engine.queue
  namespace: Tavaan\Engine\Queue\
  path: engines/queue
  priority: P1
  phase: M5
  depends_on: [config, event]
  soft_depends_on: [database, cache, log]
  facade: {name: Queue, accessor: queue}
  tables: [tvn_jobs, tvn_failed_jobs, tvn_job_batches]
  config_file: engines/queue/config/queue.php
  loc_estimate: 4555
  acceptance:
    - {id: AC-QUEUE-01, test: 'php bin/tvn engines'}
    - {id: AC-QUEUE-02, test: 'php bin/tvn engines --list'}
```
