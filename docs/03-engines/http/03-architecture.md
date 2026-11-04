# DOC-050-S03 — معماری داخلی (موتور http)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-050-S03 |
| موتور | `http` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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

---

## چک‌لیست ممیزی عملیاتی

- [ ] نمودار اجزا (ASCII/Mermaid) موجود است
- [ ] فهرست کلاس‌ها با نوع/مسئولیت موجود است
- [ ] نمودار توالی جریان اصلی موجود است
- [ ] نمودار وضعیت (در صورت State Machine) موجود است
- [ ] الگوهای طراحی ذکر شده

---

## وضعیت ممیزی

| شاخص | وضعیت |
|---|---|
| وضعیت محتوا | ✅ دارای محتوا |
| تعداد آیتم‌های چک‌لیست | 5 |
| نیاز به تکمیل | ✅ خیر |

---

## یادداشت‌های ممیزی‌کننده

> این بخش توسط ممیزی‌کننده پر می‌شود.

- **تاریخ ممیزی:** _TODO_
- **ممیزی‌کننده:** _TODO_
- **یادداشت:** _TODO_
