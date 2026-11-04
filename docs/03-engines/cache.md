# DOC-036 — موتور Cache | حافظه نهان

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-036 |
| Engine ID | `tavaan.engine.cache` |
| Namespace | `Tavaan\Engine\Cache\` |
| مسیر | `engines/cache/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `event` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Cache` → accessor `cache` |
| جداول DB | — |
| LOC برآوردی | 1608 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Cache لایهٔ caching یکپارچه با چندین store (Array، File، Database، Redis، Memcached، APCu)، tagged cache، قفل‌های توزیع‌شده (Locks) و دستورات مدیریت را فراهم می‌کند. این موتور با مدیریت یکپارچه Repository به‌عنوان facade عمل می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: Storeهای Array/File/Database/Redis/Memcached/APCu، TaggedCache، Locks، دستور cache:clear
- ❌ خارج از دامنه: صف (در queue)، session (در session)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-CACHE-01 | پیاده‌سازی هستهٔ موتور cache به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-CACHE-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-CACHE-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Cache + Symfony Cache | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Cache\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 19 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `CacheEngine` | Engine | `src/CacheEngine.php` |
| `CacheManager` | Manager | `src/CacheManager.php` |
| `CacheRepository` | Repository | `src/CacheRepository.php` |
| `CacheServiceProvider` | ServiceProvider | `src/CacheServiceProvider.php` |
| `CacheClearCommand` | Command | `src/Console/CacheClearCommand.php` |
| `LockInterface` | Contract/Interface | `src/Contracts/LockInterface.php` |
| `LockProviderInterface` | Contract/Interface | `src/Contracts/LockProviderInterface.php` |
| `RepositoryInterface` | Contract/Interface | `src/Contracts/RepositoryInterface.php` |
| `StoreInterface` | Contract/Interface | `src/Contracts/StoreInterface.php` |
| `LockTimeoutException` | Exception | `src/Exceptions/LockTimeoutException.php` |
| `Cache` | Facade | `src/Facades/Cache.php` |
| `CacheLock` | Class | `src/Locks/CacheLock.php` |
| `ApcuStore` | Store | `src/Stores/ApcuStore.php` |
| `ArrayStore` | Store | `src/Stores/ArrayStore.php` |
| `DatabaseStore` | Store | `src/Stores/DatabaseStore.php` |
| `FileStore` | Store | `src/Stores/FileStore.php` |
| `MemcachedStore` | Store | `src/Stores/MemcachedStore.php` |
| `RedisStore` | Store | `src/Stores/RedisStore.php` |
| `TaggedCache` | Class | `src/TaggedCache.php` |

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
فایل پیکربندی: `engines/cache/config/cache.php`

کلیدهای اصلی:
`default`, `prefix`, `default_ttl`, `file_dir`, `tags`, `stampede_protection`, `enabled`, `lock_ttl`, `serve_stale`, `lock`

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
| AC-CACHE-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-CACHE-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Cache + Symfony Cache | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.cache.v1
engine:
  id: tavaan.engine.cache
  namespace: Tavaan\Engine\Cache\
  path: engines/cache
  priority: P1
  phase: M5
  depends_on: [config, event]
  soft_depends_on: []
  facade: {name: Cache, accessor: cache}
  tables: []
  config_file: engines/cache/config/cache.php
  loc_estimate: 1608
  acceptance:
    - {id: AC-CACHE-01, test: 'php bin/tvn engines'}
    - {id: AC-CACHE-02, test: 'php bin/tvn engines --list'}
```
