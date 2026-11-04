# DOC-066-S03 — معماری داخلی (موتور queue)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-066-S03 |
| موتور | `queue` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
