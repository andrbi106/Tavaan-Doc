# DOC-054-S03 — معماری داخلی (موتور log)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-054-S03 |
| موتور | `log` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
