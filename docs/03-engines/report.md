# DOC-069 — موتور Report | گزارش‌ساز

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-069 |
| Engine ID | `tavaan.engine.report` |
| Namespace | `Tavaan\Engine\Report\` |
| مسیر | `engines/report/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M7 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | `database`, `filesystem`, `view`, `i18n`, `compat`, `http` |
| Facade | `Report` → accessor `report` |
| جداول DB | — |
| LOC برآوردی | 2121 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Report تولید گزارش‌های ساختاریافته را با datasource، renderer (PDF/Excel/CSV/HTML)، template و scheduling فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: ReportManager، datasources، renderers (PDF/Excel/CSV/HTML)، templates، scheduled reports
- ❌ خارج از دامنه: PDF rendering خارجی (در pdf skill)، Mail (در mail)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-REPORT-01 | پیاده‌سازی هستهٔ موتور report به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-REPORT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-REPORT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Nova Reports + Jasper | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Report\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 20 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Aggregator` | Class | `src/Aggregator.php` |
| `DatasetResolver` | Class | `src/DatasetResolver.php` |
| `ReportException` | Exception | `src/Exceptions/ReportException.php` |
| `CsvExporter` | Exporter | `src/Export/CsvExporter.php` |
| `HtmlExporter` | Exporter | `src/Export/HtmlExporter.php` |
| `JsonExporter` | Exporter | `src/Export/JsonExporter.php` |
| `PdfExporter` | Exporter | `src/Export/PdfExporter.php` |
| `XlsxExporter` | Exporter | `src/Export/XlsxExporter.php` |
| `XlsxWriter` | Class | `src/Export/XlsxWriter.php` |
| `Report` | Facade | `src/Facades/Report.php` |
| `Field` | Class | `src/Field.php` |
| `Filter` | Class | `src/Filter.php` |
| `Formatter` | Class | `src/Formatter.php` |
| `PivotBuilder` | Builder | `src/PivotBuilder.php` |
| `PivotConfig` | Class | `src/PivotConfig.php` |
| `ReportEngine` | Engine | `src/ReportEngine.php` |
| `ReportExporter` | Exporter | `src/ReportExporter.php` |
| `ReportResolver` | Class | `src/ReportResolver.php` |
| `ReportResult` | Value/DTO | `src/ReportResult.php` |
| `report` | Class | `src/report.php` |

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
فایل پیکربندی این موتور در `engines/report/config/report.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.report.config.report`.

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
| AC-REPORT-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-REPORT-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Nova Reports + Jasper | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.report.v1
engine:
  id: tavaan.engine.report
  namespace: Tavaan\Engine\Report\
  path: engines/report
  priority: P2
  phase: M7
  depends_on: [config]
  soft_depends_on: [database, filesystem, view, i18n, compat, http]
  facade: {name: Report, accessor: report}
  tables: []
  config_file: engines/report/config/report.php
  loc_estimate: 2121
  acceptance:
    - {id: AC-REPORT-01, test: 'php bin/tvn engines'}
    - {id: AC-REPORT-02, test: 'php bin/tvn engines --list'}
```
