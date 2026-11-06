# DOC-065-S03 — معماری داخلی (موتور plugin)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-065-S03 |
| موتور | `plugin` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 21 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `PluginDisableCommand` | Command | `src/Console/Commands/PluginDisableCommand.php` |
| `PluginEnableCommand` | Command | `src/Console/Commands/PluginEnableCommand.php` |
| `PluginInstallCommand` | Command | `src/Console/Commands/PluginInstallCommand.php` |
| `PluginListCommand` | Command | `src/Console/Commands/PluginListCommand.php` |
| `PluginScanCommand` | Command | `src/Console/Commands/PluginScanCommand.php` |
| `PluginUninstallCommand` | Command | `src/Console/Commands/PluginUninstallCommand.php` |
| `PluginUpdateCommand` | Command | `src/Console/Commands/PluginUpdateCommand.php` |
| `PluginVerifyCommand` | Command | `src/Console/Commands/PluginVerifyCommand.php` |
| `PluginException` | Exception | `src/Exceptions/PluginException.php` |
| `Plugin` | Facade | `src/Facades/Plugin.php` |
| `Hook` | Class | `src/Hook.php` |
| `Plugin` | Class | `src/Plugin.php` |
| `PluginCapabilities` | Class | `src/PluginCapabilities.php` |
| `PluginEngine` | Engine | `src/PluginEngine.php` |
| `PluginProvider` | Class | `src/PluginProvider.php` |
| `PluginSandbox` | Class | `src/PluginSandbox.php` |
| `PluginScanner` | Class | `src/PluginScanner.php` |
| `PluginVerifier` | Class | `src/PluginVerifier.php` |
| `PluginsLock` | Class | `src/PluginsLock.php` |
| `ScanReport` | Class | `src/ScanReport.php` |
| `plugin` | Class | `src/plugin.php` |

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
