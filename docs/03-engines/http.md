# DOC-050 — موتور Http | HTTP

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-050 |
| Engine ID | `tavaan.engine.http` |
| Namespace | `Tavaan\Engine\Http\` |
| مسیر | `engines/http/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `pipeline`, `event`, `error`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Http` → accessor `http` |
| جداول DB | — |
| LOC برآوردی | 5726 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور HTTP هستهٔ پردازش درخواست/پاسخ را با Request/Response objects، middleware stack، cookie، session integration و send/stream فراهم می‌کند و پایهٔ همه ورودی‌های وب است.

### ۱٫۲ دامنه (What)
- ✅ شامل: Request/Response، Middleware pipeline، Cookie integration، Stream responses، Header manipulation
- ❌ خارج از دامنه: Router (در router)، View (در view)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-HTTP-01 | پیاده‌سازی هستهٔ موتور http به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-HTTP-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-HTTP-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Symfony HttpFoundation + Nyholm PSR-7 | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Http\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 65 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `RouteCacheCommand` | Command | `src/Console/RouteCacheCommand.php` |
| `RouteClearCommand` | Command | `src/Console/RouteClearCommand.php` |
| `RouteListCommand` | Command | `src/Console/RouteListCommand.php` |
| `RouteMatchCommand` | Command | `src/Console/RouteMatchCommand.php` |
| `ServeCommand` | Command | `src/Console/ServeCommand.php` |
| `CookieInterface` | Contract/Interface | `src/Contracts/CookieInterface.php` |
| `KernelInterface` | Contract/Interface | `src/Contracts/KernelInterface.php` |
| `MiddlewareInterface` | Middleware | `src/Contracts/MiddlewareInterface.php` |
| `RequestInterface` | Contract/Interface | `src/Contracts/RequestInterface.php` |
| `ResponseInterface` | Contract/Interface | `src/Contracts/ResponseInterface.php` |
| `TerminableMiddleware` | Middleware | `src/Contracts/TerminableMiddleware.php` |
| `UploadedFileInterface` | Contract/Interface | `src/Contracts/UploadedFileInterface.php` |
| `UriInterface` | Contract/Interface | `src/Contracts/UriInterface.php` |
| `Cookie` | Class | `src/Cookie/Cookie.php` |
| `CookieJar` | Class | `src/Cookie/CookieJar.php` |
| `EncryptCookiesMiddleware` | Middleware | `src/Cookie/EncryptCookiesMiddleware.php` |
| `CorsMiddleware` | Middleware | `src/Cors/CorsMiddleware.php` |
| `BadRequestException` | Exception | `src/Exceptions/BadRequestException.php` |
| `CsrfTokenMismatchException` | Exception | `src/Exceptions/CsrfTokenMismatchException.php` |
| `ForbiddenException` | Exception | `src/Exceptions/ForbiddenException.php` |
| `HeaderInjectionException` | Exception | `src/Exceptions/HeaderInjectionException.php` |
| `HttpException` | Exception | `src/Exceptions/HttpException.php` |
| `MethodNotAllowedException` | Exception | `src/Exceptions/MethodNotAllowedException.php` |
| `PayloadTooLargeException` | Exception | `src/Exceptions/PayloadTooLargeException.php` |
| `RouteNotFoundException` | Exception | `src/Exceptions/RouteNotFoundException.php` |
| `ServerErrorException` | Exception | `src/Exceptions/ServerErrorException.php` |
| `TooManyRequestsException` | Exception | `src/Exceptions/TooManyRequestsException.php` |
| `UnauthorizedException` | Exception | `src/Exceptions/UnauthorizedException.php` |
| `UnprocessableEntityException` | Exception | `src/Exceptions/UnprocessableEntityException.php` |
| `Cookie` | Facade | `src/Facades/Cookie.php` |
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
فایل پیکربندی: `engines/http/config/http.php`

کلیدهای اصلی:
`trusted_proxies`, `trusted_headers`, `middleware`, `compress`

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
| AC-HTTP-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-HTTP-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Symfony HttpFoundation + Nyholm PSR-7 | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.http.v1
engine:
  id: tavaan.engine.http
  namespace: Tavaan\Engine\Http\
  path: engines/http
  priority: P0
  phase: M2
  depends_on: [pipeline, event, error, config]
  soft_depends_on: []
  facade: {name: Http, accessor: http}
  tables: []
  config_file: engines/http/config/http.php
  loc_estimate: 5726
  acceptance:
    - {id: AC-HTTP-01, test: 'php bin/tvn engines'}
    - {id: AC-HTTP-02, test: 'php bin/tvn engines --list'}
```
