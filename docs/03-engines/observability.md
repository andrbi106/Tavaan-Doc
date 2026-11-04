# DOC-060 — موتور Observability | رصدپذیری

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-060 |
| Engine ID | `tavaan.engine.observability` |
| Namespace | `Tavaan\Engine\Observability\` |
| مسیر | `engines/observability/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `log` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Metrics` → accessor `metrics` |
| جداول DB | — |
| LOC برآوردی | 3452 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Observability ردیابی توزیع‌شده (Tracing با OTLP/Jaeger)، metrics (Prometheus)، Health checks و DebugBar را یکپارچه فراهم می‌کند و دید کامل بر عملکرد سیستم می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: Tracer/TraceManager (OTLP/Jaeger)، Metrics (Prometheus)، Health checks، DebugBar، Span exporters
- ❌ خارج از دامنه: Log (در log)، Audit (در audit)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-OBS-01 | پیاده‌سازی هستهٔ موتور observability به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-OBS-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-OBS-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| OpenTelemetry + Prometheus + Laravel Telescope | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Observability\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی: `engines/observability/config/observability.php`

کلیدهای اصلی:
`metrics`, `enabled`, `prefix`, `tracing`, `sample_rate`, `health`

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
| AC-OBSERVABILITY-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-OBSERVABILITY-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| OpenTelemetry + Prometheus + Laravel Telescope | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.observability.v1
engine:
  id: tavaan.engine.observability
  namespace: Tavaan\Engine\Observability\
  path: engines/observability
  priority: P1
  phase: M5
  depends_on: [config, log]
  soft_depends_on: []
  facade: {name: Metrics, accessor: metrics}
  tables: []
  config_file: engines/observability/config/observability.php
  loc_estimate: 3452
  acceptance:
    - {id: AC-OBSERVABILITY-01, test: 'php bin/tvn engines'}
    - {id: AC-OBSERVABILITY-02, test: 'php bin/tvn engines --list'}
```
