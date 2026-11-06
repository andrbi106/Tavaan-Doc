# DOC-067-S03 — معماری داخلی (موتور rbac)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-067-S03 |
| موتور | `rbac` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
