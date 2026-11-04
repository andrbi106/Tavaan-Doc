# DOC-065 — موتور Plugin | افزونهٔ ثالث (sandbox + امضا)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-065 |
| Engine ID | `tavaan.engine.plugin` |
| Namespace | `Tavaan\Engine\Plugin\` |
| مسیر | `engines/plugin/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M6 |
| وابستگی (سخت) | `module`, `filesystem`, `crypt` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Plugin` → accessor `plugins` |
| جداول DB | — |
| LOC برآوردی | 1838 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Plugin سیستم افزونه‌پذیری را با discovery، install/uninstall، hook system و isolation فراهم می‌کند و توسعهٔ third-party را ممکن می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: PluginManager، discovery، hooks، install/uninstall، namespace isolation
- ❌ خارج از دامنه: Module (در module)، Tenancy (در tenancy)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-PLUGIN-01 | پیاده‌سازی هستهٔ موتور plugin به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-PLUGIN-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-PLUGIN-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| WordPress Plugin System + Composer Plugins | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Plugin\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی این موتور در `engines/plugin/config/plugin.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.plugin.config.plugin`.

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
| AC-PLUGIN-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-PLUGIN-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| WordPress Plugin System + Composer Plugins | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.plugin.v1
engine:
  id: tavaan.engine.plugin
  namespace: Tavaan\Engine\Plugin\
  path: engines/plugin
  priority: P2
  phase: M6
  depends_on: [module, filesystem, crypt]
  soft_depends_on: []
  facade: {name: Plugin, accessor: plugins}
  tables: []
  config_file: engines/plugin/config/plugin.php
  loc_estimate: 1838
  acceptance:
    - {id: AC-PLUGIN-01, test: 'php bin/tvn engines'}
    - {id: AC-PLUGIN-02, test: 'php bin/tvn engines --list'}
```
