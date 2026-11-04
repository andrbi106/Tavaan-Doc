# DOC-058-S03 — معماری داخلی (موتور module)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-058-S03 |
| موتور | `module` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 17 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `KitInstallCommand` | Command | `src/Console/KitInstallCommand.php` |
| `KitListCommand` | Command | `src/Console/KitListCommand.php` |
| `CircularModuleDependencyException` | Exception | `src/Exceptions/CircularModuleDependencyException.php` |
| `ModuleException` | Exception | `src/Exceptions/ModuleException.php` |
| `Module` | Facade | `src/Facades/Module.php` |
| `KitException` | Exception | `src/Kit/KitException.php` |
| `KitManager` | Manager | `src/Kit/KitManager.php` |
| `KitManifest` | Class | `src/Kit/KitManifest.php` |
| `Manifest` | Class | `src/Manifest.php` |
| `ManifestParser` | Class | `src/ManifestParser.php` |
| `Module` | Class | `src/Module.php` |
| `ModuleEngine` | Engine | `src/ModuleEngine.php` |
| `ModuleManager` | Manager | `src/ModuleManager.php` |
| `ModuleRegistry` | Class | `src/ModuleRegistry.php` |
| `ModuleRunner` | Class | `src/ModuleRunner.php` |
| `ModuleServiceProvider` | ServiceProvider | `src/ModuleServiceProvider.php` |
| `TopologicalSorter` | Class | `src/TopologicalSorter.php` |

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
