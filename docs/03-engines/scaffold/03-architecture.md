# DOC-071-S03 — معماری داخلی (موتور scaffold)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-071-S03 |
| موتور | `scaffold` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 41 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `MakeCommandCommand` | Command | `src/Console/Commands/MakeCommandCommand.php` |
| `MakeControllerCommand` | Controller | `src/Console/Commands/MakeControllerCommand.php` |
| `MakeEngineCommand` | Command | `src/Console/Commands/MakeEngineCommand.php` |
| `MakeEventCommand` | Command | `src/Console/Commands/MakeEventCommand.php` |
| `MakeFactoryCommand` | Command | `src/Console/Commands/MakeFactoryCommand.php` |
| `MakeJobCommand` | Command | `src/Console/Commands/MakeJobCommand.php` |
| `MakeListenerCommand` | Command | `src/Console/Commands/MakeListenerCommand.php` |
| `MakeMiddlewareCommand` | Middleware | `src/Console/Commands/MakeMiddlewareCommand.php` |
| `MakeMigrationCommand` | Command | `src/Console/Commands/MakeMigrationCommand.php` |
| `MakeModelCommand` | Command | `src/Console/Commands/MakeModelCommand.php` |
| `MakeModuleCommand` | Command | `src/Console/Commands/MakeModuleCommand.php` |
| `MakePolicyCommand` | Command | `src/Console/Commands/MakePolicyCommand.php` |
| `MakeRequestCommand` | Command | `src/Console/Commands/MakeRequestCommand.php` |
| `MakeResourceCommand` | Command | `src/Console/Commands/MakeResourceCommand.php` |
| `MakeSeederCommand` | Command | `src/Console/Commands/MakeSeederCommand.php` |
| `MakeTestCommand` | Command | `src/Console/Commands/MakeTestCommand.php` |
| `MakeWidgetCommand` | Command | `src/Console/Commands/MakeWidgetCommand.php` |
| `GenerateCommand` | Command | `src/GenerateCommand.php` |
| `Generator` | Generator | `src/Generator.php` |
| `GeneratorManager` | Manager | `src/GeneratorManager.php` |
| `CommandGenerator` | Command | `src/Generators/CommandGenerator.php` |
| `ControllerGenerator` | Controller | `src/Generators/ControllerGenerator.php` |
| `EngineGenerator` | Generator | `src/Generators/EngineGenerator.php` |
| `EventGenerator` | Generator | `src/Generators/EventGenerator.php` |
| `FactoryGenerator` | Generator | `src/Generators/FactoryGenerator.php` |
| `JobGenerator` | Generator | `src/Generators/JobGenerator.php` |
| `ListenerGenerator` | Generator | `src/Generators/ListenerGenerator.php` |
| `MiddlewareGenerator` | Middleware | `src/Generators/MiddlewareGenerator.php` |
| `MigrationGenerator` | Generator | `src/Generators/MigrationGenerator.php` |
| `ModelGenerator` | Generator | `src/Generators/ModelGenerator.php` |
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
