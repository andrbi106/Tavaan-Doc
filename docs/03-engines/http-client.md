# DOC-051 — موتور HttpClient | کلاینت HTTP

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-051 |
| Engine ID | `tavaan.engine.http-client` |
| Namespace | `Tavaan\Engine\HttpClient\` |
| مسیر | `engines/http-client/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `event` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Http` → accessor `http` |
| جداول DB | — |
| LOC برآوردی | 1807 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور HTTP-Client کلاینت HTTP خالص PHP را با pool، retry، timeout، mock و middleware chain فراهم می‌کند و امکان ارسال درخواست‌های امن به سرویس‌های خارجی را می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: Client، Pool، Retry/Middleware، Mock، Response objects
- ❌ خارج از دامنه: Realtime websocket (در realtime)، Mail transport (در mail)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-HTTPCLIENT-01 | پیاده‌سازی هستهٔ موتور http-client به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-HTTPCLIENT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-HTTPCLIENT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel HTTP Client + Guzzle | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\HttpClient\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی: `engines/http-client/config/http-client.php`

کلیدهای اصلی:
`timeout`, `default_headers`, `retry`, `verify_tls`

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
| AC-HTTP_CLIENT-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-HTTP_CLIENT-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel HTTP Client + Guzzle | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.http-client.v1
engine:
  id: tavaan.engine.http-client
  namespace: Tavaan\Engine\HttpClient\
  path: engines/http-client
  priority: P1
  phase: M5
  depends_on: [config, event]
  soft_depends_on: []
  facade: {name: Http, accessor: http}
  tables: []
  config_file: engines/http-client/config/http-client.php
  loc_estimate: 1807
  acceptance:
    - {id: AC-HTTP_CLIENT-01, test: 'php bin/tvn engines'}
    - {id: AC-HTTP_CLIENT-02, test: 'php bin/tvn engines --list'}
```
