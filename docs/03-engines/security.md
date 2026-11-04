# DOC-075 — موتور Security | امنیت عرضی (CSRF/RateLimit/Sanitizer/SSRF)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-075 |
| Engine ID | `tavaan.engine.security` |
| Namespace | `Tavaan\Engine\Security\` |
| مسیر | `engines/security/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `http`, `crypt`, `cache`, `config` |
| وابستگی (نرم/اختیاری) | `session`, `router` |
| Facade | `Security` → accessor `security` |
| جداول DB | — |
| LOC برآوردی | 1054 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Security مجموعه‌ای از middleware و managerهای امنیتی شامل CSRF، Rate Limiting (Throttle)، HTML Sanitizer، Input Normalizer و SSRF protection را فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: CsrfManager، RateLimiter/Throttle، HtmlSanitizer، InputNormalizer، SSRF protection
- ❌ خارج از دامنه: Auth (در auth)، Crypt (در crypt)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-SEC-01 | پیاده‌سازی هستهٔ موتور security به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-SEC-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-SEC-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Security + HTML Purifier | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Security\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 12 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Csrf` | Class | `src/Csrf.php` |
| `CsrfManager` | Manager | `src/Csrf/CsrfManager.php` |
| `SsrfException` | Exception | `src/Exceptions/SsrfException.php` |
| `Security` | Facade | `src/Facades/Security.php` |
| `CsrfVerifyMiddleware` | Middleware | `src/Middleware/CsrfVerifyMiddleware.php` |
| `ThrottleMiddleware` | Middleware | `src/Middleware/ThrottleMiddleware.php` |
| `InputNormalizer` | Class | `src/Normalize/InputNormalizer.php` |
| `RateLimiter` | Class | `src/RateLimit/RateLimiter.php` |
| `HtmlSanitizer` | Class | `src/Sanitize/HtmlSanitizer.php` |
| `Security` | Class | `src/Security.php` |
| `SecurityEngine` | Engine | `src/SecurityEngine.php` |
| `security` | Class | `src/security.php` |

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
فایل پیکربندی این موتور در `engines/security/config/security.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.security.config.security`.

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
| AC-SECURITY-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-SECURITY-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Security + HTML Purifier | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.security.v1
engine:
  id: tavaan.engine.security
  namespace: Tavaan\Engine\Security\
  path: engines/security
  priority: P0
  phase: M4
  depends_on: [http, crypt, cache, config]
  soft_depends_on: [session, router]
  facade: {name: Security, accessor: security}
  tables: []
  config_file: engines/security/config/security.php
  loc_estimate: 1054
  acceptance:
    - {id: AC-SECURITY-01, test: 'php bin/tvn engines'}
    - {id: AC-SECURITY-02, test: 'php bin/tvn engines --list'}
```
