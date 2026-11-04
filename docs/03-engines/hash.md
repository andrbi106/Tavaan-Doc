# DOC-049 — موتور Hash | هش رمز عبور

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-049 |
| Engine ID | `tavaan.engine.hash` |
| Namespace | `Tavaan\Engine\Hash\` |
| مسیر | `engines/hash/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Hash` → accessor `hash` |
| جداول DB | — |
| LOC برآوردی | 355 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Hash هش کردن رمز عبور را با الگوریتم‌های Bcrypt و Argon2id، تطرید (rehash) و verify فراهم می‌کند و مطابق با استانداردهای امنیتی مدرن است.

### ۱٫۲ دامنه (What)
- ✅ شامل: HashManager، BcryptHasher، Argon2idHasher، needsRehash، verify
- ❌ خارج از دامنه: JWT (در auth)، Crypt عمومی (در crypt)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-HASH-01 | پیاده‌سازی هستهٔ موتور hash به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-HASH-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-HASH-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Hash + password_hash() | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Hash\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 6 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Argon2idHasher` | Class | `src/Argon2idHasher.php` |
| `BcryptHasher` | Class | `src/BcryptHasher.php` |
| `HasherInterface` | Contract/Interface | `src/Contracts/HasherInterface.php` |
| `HashEngine` | Engine | `src/HashEngine.php` |
| `HashManager` | Manager | `src/HashManager.php` |
| `HashServiceProvider` | ServiceProvider | `src/HashServiceProvider.php` |

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
فایل پیکربندی: `engines/hash/config/hash.php`

کلیدهای اصلی:
`driver`, `argon2id`, `memory_cost`, `time_cost`, `threads`, `bcrypt`, `cost`, `rehash_on_login`

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
| AC-HASH-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-HASH-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Hash + password_hash() | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.hash.v1
engine:
  id: tavaan.engine.hash
  namespace: Tavaan\Engine\Hash\
  path: engines/hash
  priority: P0
  phase: M4
  depends_on: [config]
  soft_depends_on: []
  facade: {name: Hash, accessor: hash}
  tables: []
  config_file: engines/hash/config/hash.php
  loc_estimate: 355
  acceptance:
    - {id: AC-HASH-01, test: 'php bin/tvn engines'}
    - {id: AC-HASH-02, test: 'php bin/tvn engines --list'}
```
