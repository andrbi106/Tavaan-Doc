# DOC-067 — موتور RBAC | نقش و کنترل دسترسی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-067 |
| Engine ID | `tavaan.engine.rbac` |
| Namespace | `Tavaan\Engine\Rbac\` |
| مسیر | `engines/rbac/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `auth`, `database`, `cache`, `event`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Gate` → accessor `gate` |
| جداول DB | `tvn_permissions`, `tvn_roles`, `tvn_role_user`, `tvn_permission_role`, `tvn_delegations` |
| LOC برآوردی | 1242 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور RBAC مدیریت نقش، مجوز و سیاست دسترسی را با Role/Permission، Policy، Gate و caching فراهم می‌کند و کنترل دسترسی مبتنی بر نقش را پیاده می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: Role/Permission، Policy، Gate، caching، wildcard/owner checks
- ❌ خارج از دامنه: Auth (در auth)، Admin (در admin)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-RBAC-01 | پیاده‌سازی هستهٔ موتور rbac به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-RBAC-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-RBAC-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| spatie/laravel-permission + Laravel Gate | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Rbac\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 17 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `HasRoles` | Class | `src/Concerns/HasRoles.php` |
| `RbacSyncCommand` | Command | `src/Console/RbacSyncCommand.php` |
| `GateInterface` | Contract/Interface | `src/Contracts/GateInterface.php` |
| `ResponseInterface` | Contract/Interface | `src/Contracts/ResponseInterface.php` |
| `AuthorizationException` | Exception | `src/Exceptions/AuthorizationException.php` |
| `Gate` | Facade | `src/Facades/Gate.php` |
| `Gate` | Class | `src/Gate.php` |
| `GateResponse` | Value/DTO | `src/GateResponse.php` |
| `PermissionResolver` | Class | `src/PermissionResolver.php` |
| `PermissionSync` | Class | `src/PermissionSync.php` |
| `RBACEngine` | Engine | `src/RBACEngine.php` |
| `RoleManager` | Manager | `src/RoleManager.php` |
| `OwnershipScope` | Class | `src/Scopes/OwnershipScope.php` |
| `OrderFixture` | Class | `src/Testing/OrderFixture.php` |
| `OrderPolicyFixture` | Class | `src/Testing/OrderPolicyFixture.php` |
| `RbacTestUser` | Class | `src/Testing/RbacTestUser.php` |
| `rbac` | Class | `src/rbac.php` |

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
فایل پیکربندی این موتور در `engines/rbac/config/rbac.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.rbac.config.rbac`.

در v0.0.1 فقط ساختار اولیه پشتیبانی می‌شود.

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
| AC-RBAC-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-RBAC-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| spatie/laravel-permission + Laravel Gate | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.rbac.v1
engine:
  id: tavaan.engine.rbac
  namespace: Tavaan\Engine\Rbac\
  path: engines/rbac
  priority: P0
  phase: M4
  depends_on: [auth, database, cache, event, config]
  soft_depends_on: []
  facade: {name: Gate, accessor: gate}
  tables: [tvn_permissions, tvn_roles, tvn_role_user, tvn_permission_role, tvn_delegations]
  config_file: engines/rbac/config/rbac.php
  loc_estimate: 1242
  acceptance:
    - {id: AC-RBAC-01, test: 'php bin/tvn engines'}
    - {id: AC-RBAC-02, test: 'php bin/tvn engines --list'}
```
