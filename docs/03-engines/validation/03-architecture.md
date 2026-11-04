# DOC-080-S03 — معماری داخلی (موتور validation)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-080-S03 |
| موتور | `validation` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 24 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `ValidatesAttributes` | Class | `src/Concerns/ValidatesAttributes.php` |
| `RuleInterface` | Contract/Interface | `src/Contracts/RuleInterface.php` |
| `ValidatorInterface` | Contract/Interface | `src/Contracts/ValidatorInterface.php` |
| `DtoValidator` | Class | `src/DtoValidator.php` |
| `ValidationException` | Exception | `src/Exceptions/ValidationException.php` |
| `Validator` | Facade | `src/Facades/Validator.php` |
| `FormRequest` | Class | `src/FormRequest.php` |
| `MessageBag` | Class | `src/MessageBag.php` |
| `ParsedRule` | Rule | `src/ParsedRule.php` |
| `RuleParser` | Rule | `src/RuleParser.php` |
| `BuiltInRules` | Rule | `src/Rules/BuiltInRules.php` |
| `ExistsRule` | Rule | `src/Rules/ExistsRule.php` |
| `InRule` | Rule | `src/Rules/InRule.php` |
| `MaxLength` | Class | `src/Rules/MaxLength.php` |
| `Rule` | Rule | `src/Rules/Rule.php` |
| `UniqueRule` | Rule | `src/Rules/UniqueRule.php` |
| `ValidationAttribute` | Class | `src/Rules/ValidationAttribute.php` |
| `IranianChecks` | Class | `src/Support/IranianChecks.php` |
| `CreateUserDto` | Class | `src/Testing/CreateUserDto.php` |
| `StoreOrderFormRequest` | Store | `src/Testing/StoreOrderFormRequest.php` |
| `ValidationEngine` | Engine | `src/ValidationEngine.php` |
| `ValidationServiceProvider` | ServiceProvider | `src/ValidationServiceProvider.php` |
| `Validator` | Class | `src/Validator.php` |
| `ValidatorFactory` | Factory | `src/ValidatorFactory.php` |

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
