# DOC-038 — موتور Config | پیکربندی و محیط

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-038 |
| Engine ID | `tavaan.engine.config` |
| Namespace | `Tavaan\Engine\Config\` |
| مسیر | `engines/config/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | `container` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Config` → accessor `config` |
| جداول DB | — |
| LOC برآوردی | 1314 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Config بارگذاری، ادغام، اعتبارسنجی schema و کش پیکربندی را از منابع چندگانه (فایل، env، cache) مدیریت می‌کند و Repository immutable با پشتیبانی frozen mode ارائه می‌دهد. این موتور هستهٔ پیکربندی Tavaan است.

### ۱٫۲ دامنه (What)
- ✅ شامل: ConfigLoader، EnvLoader و EnvRepository، SchemaValidator، ConfigCacher، Repository، فایل‌های کمکی
- ❌ خارج از دامنه: متغیرهای محیط (در env مستقل)، کش برنامه (در cache)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-CONFIG-01 | پیاده‌سازی هستهٔ موتور config به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-CONFIG-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-CONFIG-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Config + Symfony Config | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Config\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی: `engines/config/config/config.php`

کلیدهای اصلی:
`env_file`, `env_required`, `cache`, `enabled`, `path`, `schema`, `frozen`

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
| AC-CONFIG-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-CONFIG-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Config + Symfony Config | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.config.v1
engine:
  id: tavaan.engine.config
  namespace: Tavaan\Engine\Config\
  path: engines/config
  priority: P0
  phase: M1
  depends_on: [container]
  soft_depends_on: []
  facade: {name: Config, accessor: config}
  tables: []
  config_file: engines/config/config/config.php
  loc_estimate: 1314
  acceptance:
    - {id: AC-CONFIG-01, test: 'php bin/tvn engines'}
    - {id: AC-CONFIG-02, test: 'php bin/tvn engines --list'}
```
