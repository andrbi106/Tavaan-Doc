# DOC-058 — موتور Module | کشف و مدیریت ماژول

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-058 |
| Engine ID | `tavaan.engine.module` |
| Namespace | `Tavaan\Engine\Module\` |
| مسیر | `engines/module/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | `container`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 1641 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Module زیرساخت ماژولار بودن را با registration، discovery، enable/disable و namespace isolation فراهم می‌کند و امکان تقسیم پروژه به ماژول‌های مستقل را می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: ModuleManager، discovery، enable/disable، namespace isolation، manifest
- ❌ خارج از دامنه: Plugin سیستم (در plugin)، Tenancy (در tenancy)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-MODULE-01 | پیاده‌سازی هستهٔ موتور module به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-MODULE-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-MODULE-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| nwidart/laravel-modules | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Module\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 17 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `KitInstallCommand` | Command | `src/Console/KitInstallCommand.php` |
| `KitListCommand` | Command | `src/Console/KitListCommand.php` |
| `CircularModuleDependencyException` | Exception | `src/Exceptions/CircularModuleDependencyException.php` |
| `ModuleException` | Exception | `src/Exceptions/ModuleException.php` |
| `Module` | Facade | `src/Facades/Module.php` |
| `KitException` | Exception | `src/Kit/KitException.php` |
| `KitManager` | Manager | `src/Kit/KitManager.php` |
| `KitManifest` | Class | `src/Kit/KitManifest.php` |
| `Manifest` | Class | `src/Manifest.php` |
| `ManifestParser` | Class | `src/ManifestParser.php` |
| `Module` | Class | `src/Module.php` |
| `ModuleEngine` | Engine | `src/ModuleEngine.php` |
| `ModuleManager` | Manager | `src/ModuleManager.php` |
| `ModuleRegistry` | Class | `src/ModuleRegistry.php` |
| `ModuleRunner` | Class | `src/ModuleRunner.php` |
| `ModuleServiceProvider` | ServiceProvider | `src/ModuleServiceProvider.php` |
| `TopologicalSorter` | Class | `src/TopologicalSorter.php` |

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
فایل پیکربندی: `engines/module/config/module.php`

کلیدهای اصلی:
`path`, `enabled`, `disabled`, `hmvc`, `cache`

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
| AC-MODULE-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-MODULE-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| nwidart/laravel-modules | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.module.v1
engine:
  id: tavaan.engine.module
  namespace: Tavaan\Engine\Module\
  path: engines/module
  priority: P0
  phase: M1
  depends_on: [container, config]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/module/config/module.php
  loc_estimate: 1641
  acceptance:
    - {id: AC-MODULE-01, test: 'php bin/tvn engines'}
    - {id: AC-MODULE-02, test: 'php bin/tvn engines --list'}
```
