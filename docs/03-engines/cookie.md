# DOC-041 — موتور Cookie | کوکی رمزنگاری‌شده

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-041 |
| Engine ID | `tavaan.engine.cookie` |
| Namespace | `Tavaan\Engine\Http\Cookie\` |
| مسیر | `engines/cookie/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `http`, `crypt` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Cookie` → accessor `cookie` |
| جداول DB | — |
| LOC برآوردی | 217 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Cookie مدیریت کوکی‌های رمزنگاری‌شده، امضاشده و HttpOnly را با پشتیبانی SameSite، Secure و expire/delete فراهم می‌کند. این موتور پایهٔ ذخیره‌سازی سمت کلاینت امن است.

### ۱٫۲ دامنه (What)
- ✅ شامل: CookieJar، Cookie رمزنگاری‌شده، SameSite/Secure، expire/delete
- ❌ خارج از دامنه: Session (در session)، CSRF (در security)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-COOKIE-01 | پیاده‌سازی هستهٔ موتور cookie به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-COOKIE-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-COOKIE-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Symfony HttpFoundation Cookie | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Http\Cookie\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 2 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Cookie` | Class | `src/Cookie.php` |
| `CookieEngine` | Engine | `src/CookieEngine.php` |

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
فایل پیکربندی این موتور در `engines/cookie/config/cookie.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.cookie.config.cookie`.

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
| AC-COOKIE-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-COOKIE-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Symfony HttpFoundation Cookie | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.cookie.v1
engine:
  id: tavaan.engine.cookie
  namespace: Tavaan\Engine\Http\Cookie\
  path: engines/cookie
  priority: P0
  phase: M2
  depends_on: [http, crypt]
  soft_depends_on: []
  facade: {name: Cookie, accessor: cookie}
  tables: []
  config_file: engines/cookie/config/cookie.php
  loc_estimate: 217
  acceptance:
    - {id: AC-COOKIE-01, test: 'php bin/tvn engines'}
    - {id: AC-COOKIE-02, test: 'php bin/tvn engines --list'}
```
