# DOC-081 — موتور View | قالب‌ساز

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-081 |
| Engine ID | `tavaan.engine.view` |
| Namespace | `Tavaan\Engine\View\` |
| مسیر | `engines/view/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `event`, `i18n`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `View` → accessor `view` |
| جداول DB | — |
| LOC برآوردی | 897 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور View موتور قالب‌سازی را با TemplateCompiler، DirectiveRegistry، ViewFinder، ComponentAttributeBag، Escaper، SafeString و caching فراهم می‌کند و پایهٔ رندر UI است.

### ۱٫۲ دامنه (What)
- ✅ شامل: ViewFactory، TemplateCompiler، DirectiveRegistry، ViewFinder، ComponentAttributeBag، Escaper، SafeString، View cache
- ❌ خارج از دامنه: Admin views (در admin)، i18n در قالب (در i18n)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-VIEW-01 | پیاده‌سازی هستهٔ موتور view به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-VIEW-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-VIEW-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Blade + Latte + Twig | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\View\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 14 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ComponentAttributeBag` | Class | `src/ComponentAttributeBag.php` |
| `ViewCacheCommand` | Command | `src/Console/ViewCacheCommand.php` |
| `ViewClearCommand` | Command | `src/Console/ViewClearCommand.php` |
| `DirectiveRegistry` | Class | `src/DirectiveRegistry.php` |
| `Escaper` | Class | `src/Escaper.php` |
| `ViewException` | Exception | `src/Exceptions/ViewException.php` |
| `View` | Facade | `src/Facades/View.php` |
| `SafeString` | Class | `src/SafeString.php` |
| `TemplateCompiler` | Class | `src/TemplateCompiler.php` |
| `View` | Class | `src/View.php` |
| `ViewEngine` | Engine | `src/ViewEngine.php` |
| `ViewFactory` | Factory | `src/ViewFactory.php` |
| `ViewFinder` | Class | `src/ViewFinder.php` |
| `ViewServiceProvider` | ServiceProvider | `src/ViewServiceProvider.php` |

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
فایل پیکربندی: `engines/view/config/view.php`

کلیدهای اصلی:
`path`, `compiled`, `extension`

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
| AC-VIEW-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-VIEW-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Blade + Latte + Twig | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.view.v1
engine:
  id: tavaan.engine.view
  namespace: Tavaan\Engine\View\
  path: engines/view
  priority: P0
  phase: M2
  depends_on: [event, i18n, config]
  soft_depends_on: []
  facade: {name: View, accessor: view}
  tables: []
  config_file: engines/view/config/view.php
  loc_estimate: 897
  acceptance:
    - {id: AC-VIEW-01, test: 'php bin/tvn engines'}
    - {id: AC-VIEW-02, test: 'php bin/tvn engines --list'}
```
