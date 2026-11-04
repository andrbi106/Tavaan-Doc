# DOC-044 — موتور Database | دیتابیس

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-044 |
| Engine ID | `tavaan.engine.database` |
| Namespace | `Tavaan\Engine\Database\` |
| مسیر | `engines/database/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M3 |
| وابستگی (سخت) | `config`, `event`, `log` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `DB` → accessor `db` |
| جداول DB | — |
| LOC برآوردی | 11329 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Database لایهٔ ارتباط با پایگاه‌داده را با چند درایور (MySQL، PostgreSQL، SQLite، SQLServer)، connection pooling، query builder، تراکنش و schema abstraction فراهم می‌کند و پایهٔ همه عملیات داده است.

### ۱٫۲ دامنه (What)
- ✅ شامل: ConnectionManager، QueryBuilder، MySQL/PgSQL/SQLite/SQLServer drivers، Transactions، Schema abstraction
- ❌ خارج از دامنه: ORM (در orm)، migration (در migration)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-DATABASE-01 | پیاده‌سازی هستهٔ موتور database به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-DATABASE-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-DATABASE-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Database + Doctrine DBAL | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Database\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی: `engines/database/config/database.php`

کلیدهای اصلی:
`default`, `connections`, `driver`, `database`, `host`, `port`, `username`, `password`, `charset`, `query_log`, `enabled`, `slow_threshold`, `read_write_split`

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
| AC-DATABASE-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-DATABASE-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Database + Doctrine DBAL | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.database.v1
engine:
  id: tavaan.engine.database
  namespace: Tavaan\Engine\Database\
  path: engines/database
  priority: P0
  phase: M3
  depends_on: [config, event, log]
  soft_depends_on: []
  facade: {name: DB, accessor: db}
  tables: []
  config_file: engines/database/config/database.php
  loc_estimate: 11329
  acceptance:
    - {id: AC-DATABASE-01, test: 'php bin/tvn engines'}
    - {id: AC-DATABASE-02, test: 'php bin/tvn engines --list'}
```
