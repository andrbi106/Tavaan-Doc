# DOC-034-S03 — معماری داخلی (موتور auth)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-034-S03 |
| موتور | `auth` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 31 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `AuthEngine` | Engine | `src/AuthEngine.php` |
| `Authenticatable` | Class | `src/Contracts/Authenticatable.php` |
| `GuardInterface` | Contract/Interface | `src/Contracts/GuardInterface.php` |
| `StatefulGuard` | Guard | `src/Contracts/StatefulGuard.php` |
| `UserProviderInterface` | Contract/Interface | `src/Contracts/UserProviderInterface.php` |
| `DeviceManager` | Manager | `src/Devices/DeviceManager.php` |
| `AccountBannedException` | Exception | `src/Exceptions/AccountBannedException.php` |
| `AuthenticationException` | Exception | `src/Exceptions/AuthenticationException.php` |
| `ThrottledException` | Exception | `src/Exceptions/ThrottledException.php` |
| `TokenExpiredException` | Exception | `src/Exceptions/TokenExpiredException.php` |
| `TokenInvalidException` | Exception | `src/Exceptions/TokenInvalidException.php` |
| `Auth` | Facade | `src/Facades/Auth.php` |
| `GenericUser` | Class | `src/GenericUser.php` |
| `SessionGuard` | Guard | `src/Guards/SessionGuard.php` |
| `TokenGuard` | Guard | `src/Guards/TokenGuard.php` |
| `Base32` | Class | `src/Jwt/Base32.php` |
| `Base64Url` | Class | `src/Jwt/Base64Url.php` |
| `JwtEncoder` | Class | `src/Jwt/JwtEncoder.php` |
| `AuthenticateMiddleware` | Middleware | `src/Middleware/AuthenticateMiddleware.php` |
| `ArrayOtpChannel` | Class | `src/Otp/ArrayOtpChannel.php` |
| `LogOtpChannel` | Class | `src/Otp/LogOtpChannel.php` |
| `OtpChannelInterface` | Contract/Interface | `src/Otp/OtpChannelInterface.php` |
| `OtpManager` | Manager | `src/Otp/OtpManager.php` |
| `PasswordBroker` | Class | `src/Passwords/PasswordBroker.php` |
| `DatabaseUserProvider` | Class | `src/Providers/DatabaseUserProvider.php` |
| `LoginThrottle` | Class | `src/Throttle/LoginThrottle.php` |
| `TokenManager` | Manager | `src/TokenManager.php` |
| `TokenPair` | Class | `src/TokenPair.php` |
| `Totp` | Class | `src/TwoFactor/Totp.php` |
| `TwoFactorManager` | Manager | `src/TwoFactor/TwoFactorManager.php` |
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
