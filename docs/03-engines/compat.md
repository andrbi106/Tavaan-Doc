# DOC-037 — موتور Compat | سازگاری و Polyfill

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-037 |
| Engine ID | `tavaan.engine.compat` |
| Namespace | `Tavaan\Engine\Compat\` |
| مسیر | `engines/compat/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | — |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 1398 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Compat لایهٔ سازگاری برای جبران نبود افزونه‌های PHP (ext-intl، ext-zip، ext-mbstring) را در محیط‌های محدود ارائه می‌دهد و شامل پیاده‌سازی خالص PHP برای UTF-8، Decimal، ZipWriter و MagicBytes است. این موتور قابلیت اجرای Tavaan در hostingهای اشتراکی را تضمین می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: Utf8 خالص، Decimal، ZipWriterPure، MagicBytesDetector، دستور doctor، تابع compat()
- ❌ خارج از دامنه: بهینه‌سازی عملکرد (در optimizer)، رمزنگاری (در crypt)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-COMPAT-01 | پیاده‌سازی هستهٔ موتور compat به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-COMPAT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-COMPAT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| symfony/polyfill-* | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Compat\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 14 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Compat` | Class | `src/Compat.php` |
| `CompatEngine` | Engine | `src/CompatEngine.php` |
| `CompatServiceProvider` | ServiceProvider | `src/CompatServiceProvider.php` |
| `DoctorCommand` | Command | `src/Console/DoctorCommand.php` |
| `CompatInterface` | Contract/Interface | `src/Contracts/CompatInterface.php` |
| `MagicBytesDetectorInterface` | Contract/Interface | `src/Contracts/MagicBytesDetectorInterface.php` |
| `Utf8Interface` | Contract/Interface | `src/Contracts/Utf8Interface.php` |
| `ZipWriterPureInterface` | Contract/Interface | `src/Contracts/ZipWriterPureInterface.php` |
| `Decimal` | Class | `src/Decimal.php` |
| `EngineCapabilityException` | Exception | `src/EngineCapabilityException.php` |
| `MagicBytesDetector` | Class | `src/MagicBytesDetector.php` |
| `RoundingMode` | Class | `src/RoundingMode.php` |
| `Utf8` | Class | `src/Utf8.php` |
| `ZipWriterPure` | Class | `src/ZipWriterPure.php` |

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
فایل پیکربندی: `engines/compat/config/compat.php`

کلیدهای اصلی:
`force_fallbacks`, `drivers`, `math`, `image`, `zip`, `http`, `unicode`, `mime`, `warn_on_fallback`

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
| AC-COMPAT-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-COMPAT-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| symfony/polyfill-* | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.compat.v1
engine:
  id: tavaan.engine.compat
  namespace: Tavaan\Engine\Compat\
  path: engines/compat
  priority: P0
  phase: M1
  depends_on: []
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/compat/config/compat.php
  loc_estimate: 1398
  acceptance:
    - {id: AC-COMPAT-01, test: 'php bin/tvn engines'}
    - {id: AC-COMPAT-02, test: 'php bin/tvn engines --list'}
```
