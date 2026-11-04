# DOC-032 — موتور API | لایهٔ API

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-032 |
| Engine ID | `tavaan.engine.api` |
| Namespace | `Tavaan\Engine\Api\` |
| مسیر | `engines/api/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `config`, `http` |
| وابستگی (نرم/اختیاری) | `validation`, `orm`, `cache`, `router` |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 1517 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور API لایهٔ ساخت و تبدیل پاسخ‌های JSON را برای APIهای نسخه‌دار فراهم می‌کند و شامل JsonResource با شرط‌های when/whenLoaded، صفحه‌بندی، Idempotency-Key، Throttle و سازندهٔ OpenAPI 3.1 خودنوشته است. این موتور استانداردهای مدرن API (RFC 9457، Deprecation/Sunset) را پیاده می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: JsonResource، نسخه‌بندی API (URL/Header/Query)، Idempotency-Key، Throttle نام‌دار، OpenAPI 3.1 generator، صفحه‌بندی
- ❌ خارج از دامنه: احراز هویت API (در auth)، مسیریابی پایه (در router)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-API-01 | پیاده‌سازی هستهٔ موتور api به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-API-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-API-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel API Resources + Spatie | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Api\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 18 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `APIEngine` | Engine | `src/APIEngine.php` |
| `ApiResolver` | Class | `src/ApiResolver.php` |
| `Api` | Class | `src/Attributes/Api.php` |
| `ApiParam` | Class | `src/Attributes/ApiParam.php` |
| `ApiResponse` | Value/DTO | `src/Attributes/ApiResponse.php` |
| `ApiDocsCommand` | Command | `src/Console/ApiDocsCommand.php` |
| `ApiException` | Exception | `src/Exceptions/ApiException.php` |
| `JsonResource` | Class | `src/JsonResource.php` |
| `ApiVersionMiddleware` | Middleware | `src/Middleware/ApiVersionMiddleware.php` |
| `IdempotencyMiddleware` | Middleware | `src/Middleware/IdempotencyMiddleware.php` |
| `ThrottleMiddleware` | Middleware | `src/Middleware/ThrottleMiddleware.php` |
| `OpenApiGenerator` | Generator | `src/OpenApi/OpenApiGenerator.php` |
| `Yaml` | Class | `src/OpenApi/Yaml.php` |
| `AnonymousResourceCollection` | Collection | `src/Resources/AnonymousResourceCollection.php` |
| `MergeValue` | Class | `src/Resources/MergeValue.php` |
| `MissingValue` | Class | `src/Resources/MissingValue.php` |
| `ResourceCollection` | Collection | `src/Resources/ResourceCollection.php` |
| `api` | Class | `src/api.php` |

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
فایل پیکربندی این موتور در `engines/api/config/api.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.api.config.api`.

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
| AC-API-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-API-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel API Resources + Spatie | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.api.v1
engine:
  id: tavaan.engine.api
  namespace: Tavaan\Engine\Api\
  path: engines/api
  priority: P0
  phase: M2
  depends_on: [config, http]
  soft_depends_on: [validation, orm, cache, router]
  facade: {name: , accessor: }
  tables: []
  config_file: engines/api/config/api.php
  loc_estimate: 1517
  acceptance:
    - {id: AC-API-01, test: 'php bin/tvn engines'}
    - {id: AC-API-02, test: 'php bin/tvn engines --list'}
```
