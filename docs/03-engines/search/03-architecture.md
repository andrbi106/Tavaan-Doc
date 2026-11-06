# DOC-074-S03 — معماری داخلی (موتور search)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-074-S03 |
| موتور | `search` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 21 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `SearchReindexCommand` | Command | `src/Console/SearchReindexCommand.php` |
| `IndexInterface` | Contract/Interface | `src/Contracts/IndexInterface.php` |
| `SearchDriverInterface` | Contract/Interface | `src/Contracts/SearchDriverInterface.php` |
| `SearchManagerInterface` | Manager | `src/Contracts/SearchManagerInterface.php` |
| `MeilisearchDriver` | Driver | `src/Drivers/MeilisearchDriver.php` |
| `MySqlDriver` | Driver | `src/Drivers/MySqlDriver.php` |
| `NativeDriver` | Driver | `src/Drivers/NativeDriver.php` |
| `NativeIndex` | Class | `src/Drivers/NativeIndex.php` |
| `PgSqlDriver` | Driver | `src/Drivers/PgSqlDriver.php` |
| `SqliteFtsDriver` | Driver | `src/Drivers/SqliteFtsDriver.php` |
| `TypesenseDriver` | Driver | `src/Drivers/TypesenseDriver.php` |
| `SearchException` | Exception | `src/Exceptions/SearchException.php` |
| `Search` | Facade | `src/Facades/Search.php` |
| `Highlighter` | Class | `src/Highlighter.php` |
| `Persian` | Class | `src/Persian.php` |
| `SearchEngine` | Engine | `src/SearchEngine.php` |
| `SearchManager` | Manager | `src/SearchManager.php` |
| `SearchResolver` | Class | `src/SearchResolver.php` |
| `SearchResult` | Value/DTO | `src/SearchResult.php` |
| `SearchServiceProvider` | ServiceProvider | `src/SearchServiceProvider.php` |
| `Searchable` | Class | `src/Searchable.php` |

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
