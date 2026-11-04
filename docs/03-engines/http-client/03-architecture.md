# DOC-051-S03 — معماری داخلی (موتور http-client)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-051-S03 |
| موتور | `http-client` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 21 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `CircuitBreaker` | Class | `src/CircuitBreaker.php` |
| `CircuitOpenException` | Exception | `src/Exceptions/CircuitOpenException.php` |
| `ConnectionException` | Exception | `src/Exceptions/ConnectionException.php` |
| `HttpClientException` | Exception | `src/Exceptions/HttpClientException.php` |
| `RequestException` | Exception | `src/Exceptions/RequestException.php` |
| `Factory` | Factory | `src/Factory.php` |
| `HttpClient` | Class | `src/HttpClient.php` |
| `HttpClientEngine` | Engine | `src/HttpClientEngine.php` |
| `HttpClientServiceProvider` | ServiceProvider | `src/HttpClientServiceProvider.php` |
| `PendingRequest` | Class | `src/PendingRequest.php` |
| `Pool` | Class | `src/Pool.php` |
| `Request` | Class | `src/Request.php` |
| `Response` | Value/DTO | `src/Response.php` |
| `RetryHandler` | Handler | `src/RetryHandler.php` |
| `InternalSsrfGuard` | Guard | `src/Ssrf/InternalSsrfGuard.php` |
| `SecuritySsrfAdapter` | Class | `src/Ssrf/SecuritySsrfAdapter.php` |
| `SsrfCheckerInterface` | Contract/Interface | `src/Ssrf/SsrfCheckerInterface.php` |
| `CurlTransport` | Class | `src/Transport/CurlTransport.php` |
| `HttpTransportInterface` | Contract/Interface | `src/Transport/HttpTransportInterface.php` |
| `StreamTransport` | Class | `src/Transport/StreamTransport.php` |
| `TransportResponse` | Value/DTO | `src/Transport/TransportResponse.php` |

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
