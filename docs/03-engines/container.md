# DOC-040 — موتور Container | ظرف سرویس (DI)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-040 |
| Engine ID | `tavaan.engine.container` |
| Namespace | `Tavaan\Engine\Container\` |
| مسیر | `engines/container/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | — |
| وابستگی (نرم/اختیاری) | — |
| Facade | `App` → accessor `app` |
| جداول DB | — |
| LOC برآوردی | 1577 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Container هستهٔ DI Container با auto-wiring، bindingهای contextual، scoping، lazy proxies، reflection cache و مدیریت وابستگی‌های حلقوی است. این موتور ستون فقرات Tavaan است و همه سرویس‌ها از آن resolve می‌شوند.

### ۱٫۲ دامنه (What)
- ✅ شامل: Auto-wiring، Contextual bindings، Scope/Lifetime، LazyProxy، ReflectionCache، ContainerStats، Binding resolution
- ❌ خارج از دامنه: رویدادها (در event)، پیکربندی (در config)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-CONTAINER-01 | پیاده‌سازی هستهٔ موتور container به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-CONTAINER-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-CONTAINER-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Container + PSR-11 | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Container\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 20 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Binding` | Class | `src/Binding.php` |
| `ContainerGraphCommand` | Command | `src/Console/ContainerGraphCommand.php` |
| `ConstructorSignature` | Class | `src/ConstructorSignature.php` |
| `Container` | Class | `src/Container.php` |
| `ContainerEngine` | Engine | `src/ContainerEngine.php` |
| `ContainerServiceProvider` | ServiceProvider | `src/ContainerServiceProvider.php` |
| `ContainerStats` | Class | `src/ContainerStats.php` |
| `ContextualBindingBuilder` | Builder | `src/ContextualBindingBuilder.php` |
| `ContainerInterface` | Contract/Interface | `src/Contracts/ContainerInterface.php` |
| `AmbiguousUnionException` | Exception | `src/Exceptions/AmbiguousUnionException.php` |
| `BindingResolutionException` | Exception | `src/Exceptions/BindingResolutionException.php` |
| `CircularDependencyException` | Exception | `src/Exceptions/CircularDependencyException.php` |
| `NotInstantiableException` | Exception | `src/Exceptions/NotInstantiableException.php` |
| `ScopeNotActiveException` | Exception | `src/Exceptions/ScopeNotActiveException.php` |
| `UntypedParameterException` | Exception | `src/Exceptions/UntypedParameterException.php` |
| `LazyProxy` | Class | `src/LazyProxy.php` |
| `Lifetime` | Class | `src/Lifetime.php` |
| `ParameterSignature` | Class | `src/ParameterSignature.php` |
| `ReflectionCache` | Class | `src/ReflectionCache.php` |
| `ScopeManager` | Manager | `src/ScopeManager.php` |

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
فایل پیکربندی: `engines/container/config/container.php`

کلیدهای اصلی:
`reflection_cache`, `enabled`, `max_depth`, `strict`, `auto_build`

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
| AC-CONTAINER-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-CONTAINER-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Container + PSR-11 | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.container.v1
engine:
  id: tavaan.engine.container
  namespace: Tavaan\Engine\Container\
  path: engines/container
  priority: P0
  phase: M1
  depends_on: []
  soft_depends_on: []
  facade: {name: App, accessor: app}
  tables: []
  config_file: engines/container/config/container.php
  loc_estimate: 1577
  acceptance:
    - {id: AC-CONTAINER-01, test: 'php bin/tvn engines'}
    - {id: AC-CONTAINER-02, test: 'php bin/tvn engines --list'}
```
