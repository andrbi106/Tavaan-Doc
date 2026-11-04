# DOC-043 — موتور Crypt | رمزنگاری

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-043 |
| Engine ID | `tavaan.engine.crypt` |
| Namespace | `Tavaan\Engine\Crypt\` |
| مسیر | `engines/crypt/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Crypt` → accessor `encrypter` |
| جداول DB | — |
| LOC برآوردی | 905 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Crypt رمزنگاری متقارن (AES-256-GCM/CBC) با مدیریت کلید، رمزنگاری رشته/فایل، signing و MAC را فراهم می‌کند و پایهٔ امنیت داده‌های حساس در Tavaan است.

### ۱٫۲ دامنه (What)
- ✅ شامل: Encrypter AES-256-GCM، Key management، String/File encryption، Signing/MAC
- ❌ خارج از دامنه: Hashing password (در hash)، JWT signing (در auth)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-CRYPT-01 | پیاده‌سازی هستهٔ موتور crypt به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-CRYPT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-CRYPT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Crypt + defuse/php-encryption | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Crypt\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 15 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `BlindIndex` | Class | `src/BlindIndex.php` |
| `KeyGenerateCommand` | Command | `src/Console/KeyGenerateCommand.php` |
| `EncrypterInterface` | Contract/Interface | `src/Contracts/EncrypterInterface.php` |
| `HasherInterface` | Contract/Interface | `src/Contracts/HasherInterface.php` |
| `Crypt` | Class | `src/Crypt.php` |
| `CryptEngine` | Engine | `src/CryptEngine.php` |
| `CryptServiceProvider` | ServiceProvider | `src/CryptServiceProvider.php` |
| `Encrypter` | Class | `src/Encrypter.php` |
| `DecryptException` | Exception | `src/Exceptions/DecryptException.php` |
| `EncryptionException` | Exception | `src/Exceptions/EncryptionException.php` |
| `KeyMissingException` | Exception | `src/Exceptions/KeyMissingException.php` |
| `Crypt` | Facade | `src/Facades/Crypt.php` |
| `Hash` | Facade | `src/Facades/Hash.php` |
| `KeyRing` | Class | `src/KeyRing.php` |
| `Signer` | Class | `src/Signer.php` |

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
فایل پیکربندی: `engines/crypt/config/crypt.php`

کلیدهای اصلی:
`key`, `key_version`, `cipher`, `previous_keys`

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
| AC-CRYPT-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-CRYPT-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Crypt + defuse/php-encryption | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.crypt.v1
engine:
  id: tavaan.engine.crypt
  namespace: Tavaan\Engine\Crypt\
  path: engines/crypt
  priority: P0
  phase: M4
  depends_on: [config]
  soft_depends_on: []
  facade: {name: Crypt, accessor: encrypter}
  tables: []
  config_file: engines/crypt/config/crypt.php
  loc_estimate: 905
  acceptance:
    - {id: AC-CRYPT-01, test: 'php bin/tvn engines'}
    - {id: AC-CRYPT-02, test: 'php bin/tvn engines --list'}
```
