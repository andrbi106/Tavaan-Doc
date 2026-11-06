# DOC-038-S03 — معماری داخلی (موتور config)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-038-S03 |
| موتور | `config` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 20 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ConfigCacher` | Class | `src/ConfigCacher.php` |
| `ConfigEngine` | Engine | `src/ConfigEngine.php` |
| `ConfigLoader` | Class | `src/ConfigLoader.php` |
| `ConfigServiceProvider` | ServiceProvider | `src/ConfigServiceProvider.php` |
| `ConfigCacheCommand` | Command | `src/Console/ConfigCacheCommand.php` |
| `ConfigCacheInterface` | Contract/Interface | `src/Contracts/ConfigCacheInterface.php` |
| `EnvRepositoryInterface` | Contract/Interface | `src/Contracts/EnvRepositoryInterface.php` |
| `RepositoryInterface` | Contract/Interface | `src/Contracts/RepositoryInterface.php` |
| `EnvLoader` | Class | `src/EnvLoader.php` |
| `EnvRepository` | Repository | `src/EnvRepository.php` |
| `ConfigException` | Exception | `src/Exceptions/ConfigException.php` |
| `ConfigFrozenException` | Exception | `src/Exceptions/ConfigFrozenException.php` |
| `ConfigNotCacheableException` | Exception | `src/Exceptions/ConfigNotCacheableException.php` |
| `EnvParseException` | Exception | `src/Exceptions/EnvParseException.php` |
| `MissingConfigKeyException` | Exception | `src/Exceptions/MissingConfigKeyException.php` |
| `SchemaValidationException` | Exception | `src/Exceptions/SchemaValidationException.php` |
| `Config` | Facade | `src/Facades/Config.php` |
| `Repository` | Repository | `src/Repository.php` |
| `SchemaValidator` | Class | `src/SchemaValidator.php` |
| `helpers` | Class | `src/helpers.php` |

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
