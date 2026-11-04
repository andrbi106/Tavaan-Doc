# DOC-040-S03 — معماری داخلی (موتور container)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-040-S03 |
| موتور | `container` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 20 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Binding` | Class | `src/Binding.php` |
| `ContainerGraphCommand` | Command | `src/Console/ContainerGraphCommand.php` |
| `ConstructorSignature` | Class | `src/ConstructorSignature.php` |
| `Container` | Class | `src/Container.php` |
| `ContainerEngine` | Engine | `src/ContainerEngine.php` |
| `ContainerServiceProvider` | ServiceProvider | `src/ContainerServiceProvider.php` |
| `ContainerStats` | Class | `src/ContainerStats.php` |
| `ContextualBindingBuilder` | Builder | `src/ContextualBindingBuilder.php` |
| `ContainerInterface` | Contract/Interface | `src/Contracts/ContainerInterface.php` |
| `AmbiguousUnionException` | Exception | `src/Exceptions/AmbiguousUnionException.php` |
| `BindingResolutionException` | Exception | `src/Exceptions/BindingResolutionException.php` |
| `CircularDependencyException` | Exception | `src/Exceptions/CircularDependencyException.php` |
| `NotInstantiableException` | Exception | `src/Exceptions/NotInstantiableException.php` |
| `ScopeNotActiveException` | Exception | `src/Exceptions/ScopeNotActiveException.php` |
| `UntypedParameterException` | Exception | `src/Exceptions/UntypedParameterException.php` |
| `LazyProxy` | Class | `src/LazyProxy.php` |
| `Lifetime` | Class | `src/Lifetime.php` |
| `ParameterSignature` | Class | `src/ParameterSignature.php` |
| `ReflectionCache` | Class | `src/ReflectionCache.php` |
| `ScopeManager` | Manager | `src/ScopeManager.php` |

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
