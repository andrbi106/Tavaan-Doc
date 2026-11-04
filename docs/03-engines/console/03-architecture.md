# DOC-039-S03 — معماری داخلی (موتور console)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-039-S03 |
| موتور | `console` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 38 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Application` | Class | `src/Application.php` |
| `ArgvParser` | Class | `src/ArgvParser.php` |
| `Command` | Command | `src/Command.php` |
| `AboutCommand` | Command | `src/Commands/AboutCommand.php` |
| `ArchCheckCommand` | Command | `src/Commands/ArchCheckCommand.php` |
| `AutoloadCacheCommand` | Command | `src/Commands/AutoloadCacheCommand.php` |
| `BenchAllCommand` | Command | `src/Commands/BenchAllCommand.php` |
| `ConfigCacheCommand` | Command | `src/Commands/ConfigCacheCommand.php` |
| `ConfigClearCommand` | Command | `src/Commands/ConfigClearCommand.php` |
| `DoctorCommand` | Command | `src/Commands/DoctorCommand.php` |
| `DownCommand` | Command | `src/Commands/DownCommand.php` |
| `EngineValidateCommand` | Command | `src/Commands/EngineValidateCommand.php` |
| `EnvCheckCommand` | Command | `src/Commands/EnvCheckCommand.php` |
| `EnvCommand` | Command | `src/Commands/EnvCommand.php` |
| `EventListCommand` | Command | `src/Commands/EventListCommand.php` |
| `LintPhpCommand` | Command | `src/Commands/LintPhpCommand.php` |
| `ModuleDisableCommand` | Command | `src/Commands/ModuleDisableCommand.php` |
| `ModuleEnableCommand` | Command | `src/Commands/ModuleEnableCommand.php` |
| `ModuleListCommand` | Command | `src/Commands/ModuleListCommand.php` |
| `ModuleValidateCommand` | Command | `src/Commands/ModuleValidateCommand.php` |
| `OptimizeClearCommand` | Command | `src/Commands/OptimizeClearCommand.php` |
| `OptimizeCommand` | Command | `src/Commands/OptimizeCommand.php` |
| `SecurityScanCommand` | Command | `src/Commands/SecurityScanCommand.php` |
| `StyleCheckCommand` | Command | `src/Commands/StyleCheckCommand.php` |
| `TestCommand` | Command | `src/Commands/TestCommand.php` |
| `UpCommand` | Command | `src/Commands/UpCommand.php` |
| `VersionCommand` | Command | `src/Commands/VersionCommand.php` |
| `ConsoleEngine` | Engine | `src/ConsoleEngine.php` |
| `ConsoleKernel` | Class | `src/ConsoleKernel.php` |
| `ConsoleServiceProvider` | ServiceProvider | `src/ConsoleServiceProvider.php` |
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
