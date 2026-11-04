# DOC-070 — موتور Router | مسیریاب Compiled Trie

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-070 |
| Engine ID | `tavaan.engine.router` |
| Namespace | `Tavaan\Engine\Http\Routing\` |
| مسیر | `engines/router/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `http`, `container`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Route` → accessor `router` |
| جداول DB | — |
| LOC برآوردی | 572 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Router مسیریابی HTTP را با تعریف route، group، middleware binding، parameter، named routes و resource controllers فراهم می‌کند و پایهٔ dispatching است.

### ۱٫۲ دامنه (What)
- ✅ شامل: Router، Route collection، Group/Middleware binding، Parameters، Named routes، Resource
- ❌ خارج از دامنه: HTTP kernel (در http)، CORS (در cors)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-ROUTER-01 | پیاده‌سازی هستهٔ موتور router به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-ROUTER-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-ROUTER-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Router + Symfony Routing | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Http\Routing\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 3 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Route` | Facade | `src/Facades/Route.php` |
| `Router` | Class | `src/Router.php` |
| `RouterEngine` | Engine | `src/RouterEngine.php` |

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
فایل پیکربندی این موتور در `engines/router/config/router.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.router.config.router`.

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
| AC-ROUTER-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-ROUTER-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Router + Symfony Routing | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.router.v1
engine:
  id: tavaan.engine.router
  namespace: Tavaan\Engine\Http\Routing\
  path: engines/router
  priority: P0
  phase: M2
  depends_on: [http, container, config]
  soft_depends_on: []
  facade: {name: Route, accessor: router}
  tables: []
  config_file: engines/router/config/router.php
  loc_estimate: 572
  acceptance:
    - {id: AC-ROUTER-01, test: 'php bin/tvn engines'}
    - {id: AC-ROUTER-02, test: 'php bin/tvn engines --list'}
```
