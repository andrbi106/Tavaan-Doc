# DOC-078 — موتور Test | چارچوب تست

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-078 |
| Engine ID | `tavaan.engine.test` |
| Namespace | `Tavaan\Testing\` |
| مسیر | `engines/test/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M6 |
| وابستگی (سخت) | — |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 3635 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Test فریم‌ورک آزمون خودنوشته را با TestCase، Assertion، Mock، Factory، RefreshDatabase، Coverage و MakesHttpRequests فراهم می‌کند و امکان نوشتن unit/feature test را می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: TestCase، TestRunner، Assertions، Mock، Factory، RefreshDatabase، Coverage، Http test traits
- ❌ خارج از دامنه: Scaffold test gen (در scaffold)، Console runner (در console)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-TEST-01 | پیاده‌سازی هستهٔ موتور test به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-TEST-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-TEST-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| PHPUnit + Pest | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Testing\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

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

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
فایل پیکربندی: `engines/test/config/test.php`

کلیدهای اصلی:
`mode`, `verbose`, `stop_on_failure`, `paths`, `unit`, `feature`, `integration`

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
| AC-TEST-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-TEST-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| PHPUnit + Pest | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.test.v1
engine:
  id: tavaan.engine.test
  namespace: Tavaan\Testing\
  path: engines/test
  priority: P2
  phase: M6
  depends_on: []
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/test/config/test.php
  loc_estimate: 3635
  acceptance:
    - {id: AC-TEST-01, test: 'php bin/tvn engines'}
    - {id: AC-TEST-02, test: 'php bin/tvn engines --list'}
```
