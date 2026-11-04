# DOC-033 — موتور Audit | ممیزی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-033 |
| Engine ID | `tavaan.engine.audit` |
| Namespace | `Tavaan\Engine\Audit\` |
| مسیر | `engines/audit/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `event`, `log`, `crypt`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Audit` → accessor `audit` |
| جداول DB | `tvn_audit_logs` |
| LOC برآوردی | 908 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Audit رخدادهای امنیتی و عملیاتی سیستم را به‌صورت ساختاریافته، رمزنگاری‌شده و قابل پرس‌وجو ثبت می‌کند تا accountability و traceability کامل برای تراکنش‌ها فراهم شود. این موتور برای انطباق با الزامات ممیزی و تحلیل‌های انشعابی استفاده می‌شود.

### ۱٫۲ دامنه (What)
- ✅ شامل: ثبت لاگ ممیزی در جدول tvn_audit_logs، رمزنگاری فیلدهای حساس، پرس‌وجو و فیلتر رویدادها، اتصال به event و log
- ❌ خارج از دامنه: لاگ‌های سیستم عمومی (در log)، ردیابی توزیع‌شده (در observability)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-AUDIT-01 | پیاده‌سازی هستهٔ موتور audit به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-AUDIT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-AUDIT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Auditing / spatie/laravel-activitylog | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Audit\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 12 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Audit` | Class | `src/Audit.php` |
| `AuditEngine` | Engine | `src/AuditEngine.php` |
| `AuditEvent` | Class | `src/AuditEvent.php` |
| `AuditObserver` | Class | `src/AuditObserver.php` |
| `Auditor` | Class | `src/Auditor.php` |
| `AuditExportCommand` | Command | `src/Console/AuditExportCommand.php` |
| `AuditPruneCommand` | Command | `src/Console/AuditPruneCommand.php` |
| `AuditShowCommand` | Command | `src/Console/AuditShowCommand.php` |
| `AuditVerifyCommand` | Command | `src/Console/AuditVerifyCommand.php` |
| `Audit` | Facade | `src/Facades/Audit.php` |
| `Observed` | Class | `src/Observed.php` |
| `VerifyResult` | Value/DTO | `src/VerifyResult.php` |

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
فایل پیکربندی: `engines/audit/config/audit.php`

کلیدهای اصلی:
`key`, `table`, `hash_algorithm`

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
| AC-AUDIT-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-AUDIT-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Auditing / spatie/laravel-activitylog | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.audit.v1
engine:
  id: tavaan.engine.audit
  namespace: Tavaan\Engine\Audit\
  path: engines/audit
  priority: P0
  phase: M4
  depends_on: [event, log, crypt, config]
  soft_depends_on: []
  facade: {name: Audit, accessor: audit}
  tables: [tvn_audit_logs]
  config_file: engines/audit/config/audit.php
  loc_estimate: 908
  acceptance:
    - {id: AC-AUDIT-01, test: 'php bin/tvn engines'}
    - {id: AC-AUDIT-02, test: 'php bin/tvn engines --list'}
```
