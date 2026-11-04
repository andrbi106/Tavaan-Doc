# DOC-076 — موتور Session | نشست

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-076 |
| Engine ID | `tavaan.engine.session` |
| Namespace | `Tavaan\Engine\Session\` |
| مسیر | `engines/session/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `http`, `crypt`, `config` |
| وابستگی (نرم/اختیاری) | `database`, `cache` |
| Facade | `Session` → accessor `session` |
| جداول DB | `sessions` |
| LOC برآوردی | 968 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Session مدیریت نشست کاربر را با چند handler (File، Database، Cache، Cookie، Array)، flash data، CSRF token و middleware integration فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: SessionManager، handlers (File/DB/Cache/Cookie/Array)، flash data، CSRF token، middleware
- ❌ خارج از دامنه: Auth (در auth)، Cookie (در cookie)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-SESSION-01 | پیاده‌سازی هستهٔ موتور session به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-SESSION-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-SESSION-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Session + Symfony Session | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Session\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 12 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ArrayHandler` | Handler | `src/Handlers/ArrayHandler.php` |
| `CacheHandler` | Handler | `src/Handlers/CacheHandler.php` |
| `CookieHandler` | Handler | `src/Handlers/CookieHandler.php` |
| `DatabaseHandler` | Handler | `src/Handlers/DatabaseHandler.php` |
| `FileHandler` | Handler | `src/Handlers/FileHandler.php` |
| `CsrfVerifyMiddleware` | Middleware | `src/Middleware/CsrfVerifyMiddleware.php` |
| `ShareErrorsFromSessionMiddleware` | Middleware | `src/Middleware/ShareErrorsFromSessionMiddleware.php` |
| `StartSessionMiddleware` | Middleware | `src/Middleware/StartSessionMiddleware.php` |
| `SessionEngine` | Engine | `src/SessionEngine.php` |
| `SessionHandlerInterface` | Contract/Interface | `src/SessionHandlerInterface.php` |
| `SessionManager` | Manager | `src/SessionManager.php` |
| `session` | Class | `src/session.php` |

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
فایل پیکربندی این موتور در `engines/session/config/session.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.session.config.session`.

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
| AC-SESSION-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-SESSION-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Session + Symfony Session | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.session.v1
engine:
  id: tavaan.engine.session
  namespace: Tavaan\Engine\Session\
  path: engines/session
  priority: P0
  phase: M2
  depends_on: [http, crypt, config]
  soft_depends_on: [database, cache]
  facade: {name: Session, accessor: session}
  tables: [sessions]
  config_file: engines/session/config/session.php
  loc_estimate: 968
  acceptance:
    - {id: AC-SESSION-01, test: 'php bin/tvn engines'}
    - {id: AC-SESSION-02, test: 'php bin/tvn engines --list'}
```
