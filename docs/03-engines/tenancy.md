# DOC-077 — موتور Tenancy | چنداجاره‌ای

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-077 |
| Engine ID | `tavaan.engine.tenancy` |
| Namespace | `Tavaan\Engine\Tenancy\` |
| مسیر | `engines/tenancy/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M6 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Tenant` → accessor `tenant` |
| جداول DB | — |
| LOC برآوردی | 3117 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Tenancy چندمستاجری (multi-tenant) را با tenant identification، database separation، config switching و middleware فراهم می‌کند و امکان اجرای یک کد برای چند tenant را می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: TenantManager، identification، DB separation، config switch، middleware
- ❌ خارج از دامنه: Database (در database)، Config (در config)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-TENANT-01 | پیاده‌سازی هستهٔ موتور tenancy به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-TENANT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-TENANT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| stancl/tenancy + hyn/multi-tenant | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Tenancy\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 48 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `BelongsToTenant` | Class | `src/BelongsToTenant.php` |
| `DbTenantGuardCommand` | Command | `src/Console/DbTenantGuardCommand.php` |
| `TenantCreateCommand` | Command | `src/Console/TenantCreateCommand.php` |
| `TenantDeleteCommand` | Command | `src/Console/TenantDeleteCommand.php` |
| `TenantListCommand` | Command | `src/Console/TenantListCommand.php` |
| `TenantMigrateCommand` | Command | `src/Console/TenantMigrateCommand.php` |
| `TenantQueryGuard` | Guard | `src/Console/TenantQueryGuard.php` |
| `TenantStatsCommand` | Command | `src/Console/TenantStatsCommand.php` |
| `TenantInterface` | Contract/Interface | `src/Contracts/TenantInterface.php` |
| `TenantInterfaces` | Contract/Interface | `src/Contracts/TenantInterfaces.php` |
| `TenantResolverInterface` | Contract/Interface | `src/Contracts/TenantResolverInterface.php` |
| `DatabaseTenantManager` | Manager | `src/DatabaseTenantManager.php` |
| `TenantConnected` | Class | `src/Events/TenantConnected.php` |
| `TenantCreated` | Class | `src/Events/TenantCreated.php` |
| `TenantQuotaExceeded` | Class | `src/Events/TenantQuotaExceeded.php` |
| `TenantResolved` | Class | `src/Events/TenantResolved.php` |
| `TenancyException` | Exception | `src/Exceptions/TenancyException.php` |
| `TenantNotFoundException` | Exception | `src/Exceptions/TenantNotFoundException.php` |
| `TenantNotResolvedException` | Exception | `src/Exceptions/TenantNotResolvedException.php` |
| `TenantQuotaExceededException` | Exception | `src/Exceptions/TenantQuotaExceededException.php` |
| `TenantSuspendedException` | Exception | `src/Exceptions/TenantSuspendedException.php` |
| `Tenant` | Facade | `src/Facades/Tenant.php` |
| `InMemoryTenantRepository` | Repository | `src/InMemoryTenantRepository.php` |
| `IdentifyTenantMiddleware` | Middleware | `src/Middleware/IdentifyTenantMiddleware.php` |
| `QuotaGuard` | Guard | `src/QuotaGuard.php` |
| `DefaultResolver` | Class | `src/Resolvers/DefaultResolver.php` |
| `DomainResolver` | Class | `src/Resolvers/DomainResolver.php` |
| `HeaderResolver` | Class | `src/Resolvers/HeaderResolver.php` |
| `PathResolver` | Class | `src/Resolvers/PathResolver.php` |
| `QueryResolver` | Class | `src/Resolvers/QueryResolver.php` |
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
فایل پیکربندی: `engines/tenancy/config/tenancy.php`

کلیدهای اصلی:
`strategy`, `base_domain`, `default_tenants`, `resolvers`, `resolver_config`, `header_name`, `path_segment`, `default_quota`, `orders_per_day`, `storage_mb`

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
| AC-TENANCY-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-TENANCY-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| stancl/tenancy + hyn/multi-tenant | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.tenancy.v1
engine:
  id: tavaan.engine.tenancy
  namespace: Tavaan\Engine\Tenancy\
  path: engines/tenancy
  priority: P2
  phase: M6
  depends_on: [config]
  soft_depends_on: []
  facade: {name: Tenant, accessor: tenant}
  tables: []
  config_file: engines/tenancy/config/tenancy.php
  loc_estimate: 3117
  acceptance:
    - {id: AC-TENANCY-01, test: 'php bin/tvn engines'}
    - {id: AC-TENANCY-02, test: 'php bin/tvn engines --list'}
```
