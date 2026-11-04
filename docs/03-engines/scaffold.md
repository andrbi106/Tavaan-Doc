# DOC-071 — موتور Scaffold | تولید کد (make:*)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-071 |
| Engine ID | `tavaan.engine.scaffold` |
| Namespace | `Tavaan\Engine\Scaffold\` |
| مسیر | `engines/scaffold/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M6 |
| وابستگی (سخت) | `console`, `filesystem` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 2092 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Scaffold کدجنریتور CLI را با stubs، generators (Model/Controller/Migration/Resource/Policy/Test و…) و GeneratorManager فراهم می‌کند و شروع سریع پروژه را ممکن می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: ScaffoldEngine، GeneratorManager، Generators (Model/Controller/Migration/Test/...)، StubRenderer، Make commands
- ❌ خارج از دامنه: Admin CRUD (در admin)، Module (در module)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-SCAFFOLD-01 | پیاده‌سازی هستهٔ موتور scaffold به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-SCAFFOLD-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-SCAFFOLD-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Make + Artisan generators | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Scaffold\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 41 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `MakeCommandCommand` | Command | `src/Console/Commands/MakeCommandCommand.php` |
| `MakeControllerCommand` | Controller | `src/Console/Commands/MakeControllerCommand.php` |
| `MakeEngineCommand` | Command | `src/Console/Commands/MakeEngineCommand.php` |
| `MakeEventCommand` | Command | `src/Console/Commands/MakeEventCommand.php` |
| `MakeFactoryCommand` | Command | `src/Console/Commands/MakeFactoryCommand.php` |
| `MakeJobCommand` | Command | `src/Console/Commands/MakeJobCommand.php` |
| `MakeListenerCommand` | Command | `src/Console/Commands/MakeListenerCommand.php` |
| `MakeMiddlewareCommand` | Middleware | `src/Console/Commands/MakeMiddlewareCommand.php` |
| `MakeMigrationCommand` | Command | `src/Console/Commands/MakeMigrationCommand.php` |
| `MakeModelCommand` | Command | `src/Console/Commands/MakeModelCommand.php` |
| `MakeModuleCommand` | Command | `src/Console/Commands/MakeModuleCommand.php` |
| `MakePolicyCommand` | Command | `src/Console/Commands/MakePolicyCommand.php` |
| `MakeRequestCommand` | Command | `src/Console/Commands/MakeRequestCommand.php` |
| `MakeResourceCommand` | Command | `src/Console/Commands/MakeResourceCommand.php` |
| `MakeSeederCommand` | Command | `src/Console/Commands/MakeSeederCommand.php` |
| `MakeTestCommand` | Command | `src/Console/Commands/MakeTestCommand.php` |
| `MakeWidgetCommand` | Command | `src/Console/Commands/MakeWidgetCommand.php` |
| `GenerateCommand` | Command | `src/GenerateCommand.php` |
| `Generator` | Generator | `src/Generator.php` |
| `GeneratorManager` | Manager | `src/GeneratorManager.php` |
| `CommandGenerator` | Command | `src/Generators/CommandGenerator.php` |
| `ControllerGenerator` | Controller | `src/Generators/ControllerGenerator.php` |
| `EngineGenerator` | Generator | `src/Generators/EngineGenerator.php` |
| `EventGenerator` | Generator | `src/Generators/EventGenerator.php` |
| `FactoryGenerator` | Generator | `src/Generators/FactoryGenerator.php` |
| `JobGenerator` | Generator | `src/Generators/JobGenerator.php` |
| `ListenerGenerator` | Generator | `src/Generators/ListenerGenerator.php` |
| `MiddlewareGenerator` | Middleware | `src/Generators/MiddlewareGenerator.php` |
| `MigrationGenerator` | Generator | `src/Generators/MigrationGenerator.php` |
| `ModelGenerator` | Generator | `src/Generators/ModelGenerator.php` |
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
فایل پیکربندی این موتور در `engines/scaffold/config/scaffold.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.scaffold.config.scaffold`.

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
| AC-SCAFFOLD-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-SCAFFOLD-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Make + Artisan generators | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.scaffold.v1
engine:
  id: tavaan.engine.scaffold
  namespace: Tavaan\Engine\Scaffold\
  path: engines/scaffold
  priority: P2
  phase: M6
  depends_on: [console, filesystem]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/scaffold/config/scaffold.php
  loc_estimate: 2092
  acceptance:
    - {id: AC-SCAFFOLD-01, test: 'php bin/tvn engines'}
    - {id: AC-SCAFFOLD-02, test: 'php bin/tvn engines --list'}
```
