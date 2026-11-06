# DOC-078-S03 — معماری داخلی (موتور test)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-078-S03 |
| موتور | `test` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 28 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `AssertionFailed` | Class | `src/AssertionFailed.php` |
| `CoverageReporter` | Class | `src/Coverage/CoverageReporter.php` |
| `Faker` | Class | `src/Database/Faker.php` |
| `RefreshDatabase` | Class | `src/Database/RefreshDatabase.php` |
| `AssertionFailedException` | Exception | `src/Exceptions/AssertionFailedException.php` |
| `TestIncompleteException` | Exception | `src/Exceptions/TestIncompleteException.php` |
| `Factory` | Factory | `src/Factory.php` |
| `Group` | Class | `src/Group.php` |
| `MakesHttpRequests` | Class | `src/Http/MakesHttpRequests.php` |
| `TestResponse` | Value/DTO | `src/Http/TestResponse.php` |
| `Expectation` | Class | `src/Mock/Expectation.php` |
| `Mock` | Mock | `src/Mock/Mock.php` |
| `MockBuilder` | Mock | `src/Mock/MockBuilder.php` |
| `MockHandler` | Handler | `src/Mock/MockHandler.php` |
| `MockProxy` | Mock | `src/Mock/MockProxy.php` |
| `ProxyGenerator` | Generator | `src/Mock/ProxyGenerator.php` |
| `TestCase` | Class | `src/TestCase.php` |
| `TestClassDescriptor` | Class | `src/TestClassDescriptor.php` |
| `TestCommand` | Command | `src/TestCommand.php` |
| `TestEngine` | Engine | `src/TestEngine.php` |
| `TestFailure` | Class | `src/TestFailure.php` |
| `TestMethodDescriptor` | Class | `src/TestMethodDescriptor.php` |
| `TestResult` | Value/DTO | `src/TestResult.php` |
| `TestRunner` | Class | `src/TestRunner.php` |
| `TestServiceProvider` | ServiceProvider | `src/TestServiceProvider.php` |
| `TestSkipped` | Class | `src/TestSkipped.php` |
| `TestSuite` | Class | `src/TestSuite.php` |
| `TestSuiteResult` | Value/DTO | `src/TestSuiteResult.php` |

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
