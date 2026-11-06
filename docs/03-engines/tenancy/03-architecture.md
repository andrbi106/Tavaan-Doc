# DOC-077-S03 — معماری داخلی (موتور tenancy)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-077-S03 |
| موتور | `tenancy` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
