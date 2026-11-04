# DOC-074 — موتور Search | جست‌وجوی Full-Text

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-074 |
| Engine ID | `tavaan.engine.search` |
| Namespace | `Tavaan\Engine\Search\` |
| مسیر | `engines/search/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M3 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 4047 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Search جستجوی full-text را با drivers (PgSQL/MySQL/SQLite FTS/Meilisearch/Typesense/Native)، Searchable trait، highlight و Persian normalization فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: SearchManager، drivers (PgSQL/MySQL/SQLite/Meili/Typesense/Native)، Searchable، Highlighter، Persian normalization
- ❌ خارج از دامنه: ORM (در orm)، Database (در database)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-SEARCH-01 | پیاده‌سازی هستهٔ موتور search به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-SEARCH-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-SEARCH-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Scout + Meilisearch | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Search\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی: `engines/search/config/search.php`

کلیدهای اصلی:
`driver`, `per_page`, `highlight`, `pre_tag`, `post_tag`, `mysql`, `connection`, `min_word_length`

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
| AC-SEARCH-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-SEARCH-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Scout + Meilisearch | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.search.v1
engine:
  id: tavaan.engine.search
  namespace: Tavaan\Engine\Search\
  path: engines/search
  priority: P0
  phase: M3
  depends_on: [config]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/search/config/search.php
  loc_estimate: 4047
  acceptance:
    - {id: AC-SEARCH-01, test: 'php bin/tvn engines'}
    - {id: AC-SEARCH-02, test: 'php bin/tvn engines --list'}
```
