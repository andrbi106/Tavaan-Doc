# DOC-044-S03 — معماری داخلی (موتور database)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-044-S03 |
| موتور | `database` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 93 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Connection` | Class | `src/Connection.php` |
| `ConnectionManager` | Manager | `src/ConnectionManager.php` |
| `MySqlConnection` | Class | `src/Connections/MySqlConnection.php` |
| `PostgresConnection` | Class | `src/Connections/PostgresConnection.php` |
| `SqliteConnection` | Class | `src/Connections/SqliteConnection.php` |
| `ConnectionInterface` | Contract/Interface | `src/Contracts/ConnectionInterface.php` |
| `GrammarInterface` | Contract/Interface | `src/Contracts/GrammarInterface.php` |
| `MigrationInterface` | Contract/Interface | `src/Contracts/MigrationInterface.php` |
| `PaginatorInterface` | Contract/Interface | `src/Contracts/PaginatorInterface.php` |
| `QueryBuilderInterface` | Contract/Interface | `src/Contracts/QueryBuilderInterface.php` |
| `SchemaBuilderInterface` | Contract/Interface | `src/Contracts/SchemaBuilderInterface.php` |
| `TransactionManagerInterface` | Manager | `src/Contracts/TransactionManagerInterface.php` |
| `DatabaseEngine` | Engine | `src/DatabaseEngine.php` |
| `DatabaseServiceProvider` | ServiceProvider | `src/DatabaseServiceProvider.php` |
| `ConnectionException` | Exception | `src/Exceptions/ConnectionException.php` |
| `DatabaseException` | Exception | `src/Exceptions/DatabaseException.php` |
| `DeadlockException` | Exception | `src/Exceptions/DeadlockException.php` |
| `MixedBindingException` | Exception | `src/Exceptions/MixedBindingException.php` |
| `QueryException` | Exception | `src/Exceptions/QueryException.php` |
| `RecordNotFoundException` | Exception | `src/Exceptions/RecordNotFoundException.php` |
| `UnsafeQueryException` | Exception | `src/Exceptions/UnsafeQueryException.php` |
| `Expression` | Class | `src/Expression.php` |
| `DB` | Facade | `src/Facades/DB.php` |
| `Schema` | Facade | `src/Facades/Schema.php` |
| `Grammar` | Class | `src/Grammars/Grammar.php` |
| `MySqlGrammar` | Class | `src/Grammars/MySqlGrammar.php` |
| `PostgresGrammar` | Class | `src/Grammars/PostgresGrammar.php` |
| `SqliteGrammar` | Class | `src/Grammars/SqliteGrammar.php` |
| `MigrationException` | Exception | `src/Migration/Exceptions/MigrationException.php` |
| `MigrationLockedException` | Exception | `src/Migration/Exceptions/MigrationLockedException.php` |
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
