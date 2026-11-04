# DOC-034 — موتور Auth | احراز هویت

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-034 |
| Engine ID | `tavaan.engine.auth` |
| Namespace | `Tavaan\Engine\Auth\` |
| مسیر | `engines/auth/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `session`, `hash`, `crypt`, `event`, `database`, `cache`, `config` |
| وابستگی (نرم/اختیاری) | `http`, `orm`, `notification` |
| Facade | `Auth` → accessor `auth` |
| جداول DB | `password_resets`, `personal_access_tokens`, `user_devices`, `two_factor_secrets` |
| LOC برآوردی | 2430 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Auth احراز هویت چندگاردی (session و JWT خودنوشته)، چرخش توکن refresh با تشخیص استفاده مجدد، OTP یک‌بارمصرف، TOTP RFC 6238، ردیابی دستگاه و تأیید دومرحله‌ای را مدیریت می‌کند. این موتور پایهٔ امنیت شناسایی کاربران Tavaan را تشکیل می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: Guardهای session و JWT، refresh rotation، OTP و TOTP، ردیابی دستگاه، Password broker، Two-Factor
- ❌ خارج از دامنه: مدیریت نقش و مجوز (در rbac)، CSRF و Rate-limit عمومی (در security)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-AUTH-01 | پیاده‌سازی هستهٔ موتور auth به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-AUTH-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-AUTH-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Sanctum + Passport | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Auth\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی این موتور در `engines/auth/config/auth.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.auth.config.auth`.

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
| AC-AUTH-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-AUTH-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Sanctum + Passport | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.auth.v1
engine:
  id: tavaan.engine.auth
  namespace: Tavaan\Engine\Auth\
  path: engines/auth
  priority: P0
  phase: M4
  depends_on: [session, hash, crypt, event, database, cache, config]
  soft_depends_on: [http, orm, notification]
  facade: {name: Auth, accessor: auth}
  tables: [password_resets, personal_access_tokens, user_devices, two_factor_secrets]
  config_file: engines/auth/config/auth.php
  loc_estimate: 2430
  acceptance:
    - {id: AC-AUTH-01, test: 'php bin/tvn engines'}
    - {id: AC-AUTH-02, test: 'php bin/tvn engines --list'}
```
