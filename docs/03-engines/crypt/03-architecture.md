# DOC-043-S03 — معماری داخلی (موتور crypt)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-043-S03 |
| موتور | `crypt` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
