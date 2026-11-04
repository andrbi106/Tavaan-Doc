# DOC-080 — موتور Validation | اعتبارسنجی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-080 |
| Engine ID | `tavaan.engine.validation` |
| Namespace | `Tavaan\Engine\Validation\` |
| مسیر | `engines/validation/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M3 |
| وابستگی (سخت) | `i18n`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Validator` → accessor `validator` |
| جداول DB | — |
| LOC برآوردی | 2975 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Validation اعتبارسنجی ورودی را با rules، FormRequest، DTO validator، RuleParser، Iranian checks و message bag فراهم می‌کند و پایهٔ امنیت ورودی است.

### ۱٫۲ دامنه (What)
- ✅ شامل: Validator، RuleParser، FormRequest، DtoValidator، built-in rules، IranianChecks (melli/card/iban)، MessageBag
- ❌ خارج از دامنه: Security sanitizing (در security)، ORM data casts (در orm)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-VAL-01 | پیاده‌سازی هستهٔ موتور validation به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-VAL-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-VAL-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Validation + Respect Validation | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Validation\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی: `engines/validation/config/validation.php`

کلیدهای اصلی:
`strict`, `stop_on_first`

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
| AC-VALIDATION-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-VALIDATION-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Validation + Respect Validation | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.validation.v1
engine:
  id: tavaan.engine.validation
  namespace: Tavaan\Engine\Validation\
  path: engines/validation
  priority: P0
  phase: M3
  depends_on: [i18n, config]
  soft_depends_on: []
  facade: {name: Validator, accessor: validator}
  tables: []
  config_file: engines/validation/config/validation.php
  loc_estimate: 2975
  acceptance:
    - {id: AC-VALIDATION-01, test: 'php bin/tvn engines'}
    - {id: AC-VALIDATION-02, test: 'php bin/tvn engines --list'}
```
