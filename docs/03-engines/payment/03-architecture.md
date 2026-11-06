# DOC-063-S03 — معماری داخلی (موتور payment)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-063-S03 |
| موتور | `payment` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
