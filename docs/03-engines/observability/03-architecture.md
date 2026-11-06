# DOC-060-S03 — معماری داخلی (موتور observability)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-060-S03 |
| موتور | `observability` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 36 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `MetricsInterface` | Contract/Interface | `src/Contracts/MetricsInterface.php` |
| `SpanExporterInterface` | Contract/Interface | `src/Contracts/SpanExporterInterface.php` |
| `SpanInterface` | Contract/Interface | `src/Contracts/SpanInterface.php` |
| `StatusCode` | Class | `src/Contracts/StatusCode.php` |
| `DebugBar` | Class | `src/DebugBar/DebugBar.php` |
| `DebugBarMiddleware` | Middleware | `src/DebugBar/DebugBarMiddleware.php` |
| `Stopwatch` | Class | `src/DebugBar/Stopwatch.php` |
| `ObservabilityException` | Exception | `src/Exceptions/ObservabilityException.php` |
| `Metrics` | Facade | `src/Facades/Metrics.php` |
| `Trace` | Facade | `src/Facades/Trace.php` |
| `Health` | Class | `src/Health.php` |
| `CheckResult` | Value/DTO | `src/Health/CheckResult.php` |
| `Down` | Class | `src/Health/Down.php` |
| `HealthManager` | Manager | `src/Health/HealthManager.php` |
| `Up` | Class | `src/Health/Up.php` |
| `MetricsMiddleware` | Middleware | `src/Http/MetricsMiddleware.php` |
| `Metrics` | Value/DTO | `src/Metrics.php` |
| `Metric` | Value/DTO | `src/Metrics/Metric.php` |
| `MetricsRegistry` | Value/DTO | `src/Metrics/MetricsRegistry.php` |
| `PrometheusFormatter` | Class | `src/Metrics/PrometheusFormatter.php` |
| `Summary` | Class | `src/Metrics/Summary.php` |
| `Types` | Class | `src/Metrics/Types.php` |
| `MetricsManager` | Manager | `src/MetricsManager.php` |
| `ObservabilityEngine` | Engine | `src/ObservabilityEngine.php` |
| `ObservabilityServiceProvider` | ServiceProvider | `src/ObservabilityServiceProvider.php` |
| `Span` | Class | `src/Span.php` |
| `TraceManager` | Manager | `src/TraceManager.php` |
| `Tracer` | Class | `src/Tracer.php` |
| `ArrayExporter` | Exporter | `src/Tracing/Exporters/ArrayExporter.php` |
| `JaegerUdpExporter` | Exporter | `src/Tracing/Exporters/JaegerUdpExporter.php` |
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
