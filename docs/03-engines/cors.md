# DOC-042 — موتور CORS | مدیریت CORS

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-042 |
| Engine ID | `tavaan.engine.cors` |
| Namespace | `Tavaan\Engine\Http\Cors\` |
| مسیر | `engines/cors/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `http`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 213 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور CORS مدیریت سیاست‌های Cross-Origin Resource Sharing را با پیکربندی مسیر/گروه، preflight handling و هدرهای استاندارد فراهم می‌کند و امکان ارتباط امن API با کلاینت‌های تحت وب دیگر را ممکن می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: Middleware CORS، پیکربندی paths/allowed_methods/allowed_origins، preflight، هدرهای Access-Control-*
- ❌ خارج از دامنه: Rate limiting (در security)، احراز هویت (در auth)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-CORS-01 | پیاده‌سازی هستهٔ موتور cors به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-CORS-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-CORS-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| fruitcake/laravel-cors + barryvdh/laravel-cors | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Http\Cors\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 2 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `CORSEngine` | Engine | `src/CORSEngine.php` |
| `Cors` | Class | `src/Cors.php` |

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
فایل پیکربندی: `engines/cors/config/cors.php`

کلیدهای اصلی:
`allowed_origins`, `allowed_methods`, `allowed_headers`, `exposed_headers`, `supports_credentials`, `max_age`

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
| AC-CORS-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-CORS-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| fruitcake/laravel-cors + barryvdh/laravel-cors | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.cors.v1
engine:
  id: tavaan.engine.cors
  namespace: Tavaan\Engine\Http\Cors\
  path: engines/cors
  priority: P0
  phase: M2
  depends_on: [http, config]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/cors/config/cors.php
  loc_estimate: 213
  acceptance:
    - {id: AC-CORS-01, test: 'php bin/tvn engines'}
    - {id: AC-CORS-02, test: 'php bin/tvn engines --list'}
```
