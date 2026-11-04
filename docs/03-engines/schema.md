# DOC-073 — موتور Schema | ساختار دیتابیس

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-073 |
| Engine ID | `tavaan.engine.schema` |
| Namespace | `Tavaan\Engine\Database\Schema\` |
| مسیر | `engines/schema/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M3 |
| وابستگی (سخت) | `database` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Schema` → accessor `schema` |
| جداول DB | — |
| LOC برآوردی | 745 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Schema ساخت و تغییر ساختار جداول پایگاه‌داده را با Blueprint، column types، indexes، foreign keys و rename/drop فراهم می‌کند و پایهٔ migration است.

### ۱٫۲ دامنه (What)
- ✅ شامل: SchemaBuilder، Blueprint، column types، indexes، foreign keys، rename/drop
- ❌ خارج از دامنه: Migration (در migration)، Database (در database)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-SCHEMA-01 | پیاده‌سازی هستهٔ موتور schema به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-SCHEMA-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-SCHEMA-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Schema + Doctrine Schema | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Database\Schema\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 6 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Blueprint` | Class | `src/Blueprint.php` |
| `ColumnDefinition` | Class | `src/ColumnDefinition.php` |
| `SchemaBuilder` | Builder | `src/SchemaBuilder.php` |
| `SchemaEngine` | Engine | `src/SchemaEngine.php` |
| `SchemaManager` | Manager | `src/SchemaManager.php` |
| `SchemaServiceProvider` | ServiceProvider | `src/SchemaServiceProvider.php` |

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
فایل پیکربندی: `engines/schema/config/schema.php`

کلیدهای اصلی:
`connection`

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
| AC-SCHEMA-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-SCHEMA-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Schema + Doctrine Schema | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.schema.v1
engine:
  id: tavaan.engine.schema
  namespace: Tavaan\Engine\Database\Schema\
  path: engines/schema
  priority: P0
  phase: M3
  depends_on: [database]
  soft_depends_on: []
  facade: {name: Schema, accessor: schema}
  tables: []
  config_file: engines/schema/config/schema.php
  loc_estimate: 745
  acceptance:
    - {id: AC-SCHEMA-01, test: 'php bin/tvn engines'}
    - {id: AC-SCHEMA-02, test: 'php bin/tvn engines --list'}
```
