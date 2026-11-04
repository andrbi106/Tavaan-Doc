# DOC-069-S03 — معماری داخلی (موتور report)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-069-S03 |
| موتور | `report` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
