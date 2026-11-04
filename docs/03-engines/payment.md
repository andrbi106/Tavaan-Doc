# DOC-063 — موتور Payment | پرداخت

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-063 |
| Engine ID | `tavaan.engine.payment` |
| Namespace | `Tavaan\Engine\Payment\` |
| مسیر | `engines/payment/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M7 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | `http-client`, `database`, `migration`, `orm`, `event`, `crypt`, `http`, `console` |
| Facade | `Payment` → accessor `payment` |
| جداول DB | `tvn_payment_transactions` |
| LOC برآوردی | 2597 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Payment اتصال به درگاه‌های پرداخت ایرانی و بین‌المللی را با abstraction، transaction logging، verification و refund فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: GatewayManager، drivers (زرین‌پال/سامان/Stripe/PayPal)، Transaction logging، Verify، Refund
- ❌ خارج از دامنه: Workflow (در workflow)، Notification (در notification)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-PAY-01 | پیاده‌سازی هستهٔ موتور payment به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-PAY-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-PAY-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Cashier + shetpayment | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Payment\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 36 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `CallbackOutcome` | Class | `src/CallbackOutcome.php` |
| `PaymentListCommand` | Command | `src/Console/PaymentListCommand.php` |
| `GatewayInterface` | Contract/Interface | `src/Contracts/GatewayInterface.php` |
| `PaymentFailed` | Class | `src/Events/PaymentFailed.php` |
| `PaymentInitiated` | Class | `src/Events/PaymentInitiated.php` |
| `PaymentRefunded` | Class | `src/Events/PaymentRefunded.php` |
| `PaymentSucceeded` | Class | `src/Events/PaymentSucceeded.php` |
| `GatewayException` | Exception | `src/Exceptions/GatewayException.php` |
| `PaymentException` | Exception | `src/Exceptions/PaymentException.php` |
| `PaymentNotFoundException` | Exception | `src/Exceptions/PaymentNotFoundException.php` |
| `SignatureMismatchException` | Exception | `src/Exceptions/SignatureMismatchException.php` |
| `Payment` | Facade | `src/Facades/Payment.php` |
| `AbstractHttpGateway` | Class | `src/Gateways/AbstractHttpGateway.php` |
| `BehpardakhtGateway` | Class | `src/Gateways/BehpardakhtGateway.php` |
| `ConfigWalletStore` | Store | `src/Gateways/ConfigWalletStore.php` |
| `IdPayGateway` | Class | `src/Gateways/IdPayGateway.php` |
| `MelliGateway` | Class | `src/Gateways/MelliGateway.php` |
| `ParsianGateway` | Class | `src/Gateways/ParsianGateway.php` |
| `PayPingGateway` | Class | `src/Gateways/PayPingGateway.php` |
| `SadadGateway` | Class | `src/Gateways/SadadGateway.php` |
| `SamanGateway` | Class | `src/Gateways/SamanGateway.php` |
| `StripeGateway` | Class | `src/Gateways/StripeGateway.php` |
| `WalletGateway` | Class | `src/Gateways/WalletGateway.php` |
| `WalletStoreInterface` | Contract/Interface | `src/Gateways/WalletStoreInterface.php` |
| `ZarinPalGateway` | Class | `src/Gateways/ZarinPalGateway.php` |
| `PaymentEngine` | Engine | `src/PaymentEngine.php` |
| `PaymentResolver` | Class | `src/PaymentResolver.php` |
| `PaymentResult` | Value/DTO | `src/PaymentResult.php` |
| `PaymentStatus` | Class | `src/PaymentStatus.php` |
| `PurchaseRequest` | Class | `src/PurchaseRequest.php` |
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
فایل پیکربندی این موتور در `engines/payment/config/payment.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.payment.config.payment`.

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
| AC-PAYMENT-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-PAYMENT-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Cashier + shetpayment | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.payment.v1
engine:
  id: tavaan.engine.payment
  namespace: Tavaan\Engine\Payment\
  path: engines/payment
  priority: P2
  phase: M7
  depends_on: [config]
  soft_depends_on: [http-client, database, migration, orm, event, crypt, http, console]
  facade: {name: Payment, accessor: payment}
  tables: [tvn_payment_transactions]
  config_file: engines/payment/config/payment.php
  loc_estimate: 2597
  acceptance:
    - {id: AC-PAYMENT-01, test: 'php bin/tvn engines'}
    - {id: AC-PAYMENT-02, test: 'php bin/tvn engines --list'}
```
