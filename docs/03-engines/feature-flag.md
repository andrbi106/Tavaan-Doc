# DOC-047 — موتور FeatureFlag | پرچم قابلیت

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-047 |
| Engine ID | `tavaan.engine.feature-flag` |
| Namespace | `Tavaan\Engine\FeatureFlag\` |
| مسیر | `engines/feature-flag/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M7 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | `cache`, `database`, `rbac`, `tenancy` |
| Facade | `Feature` → accessor `feature` |
| جداول DB | — |
| LOC برآوردی | 499 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Feature-Flag پرچم‌های ویژگی را با پشتیبانی کاربر/درصد/جلسه/محدوده زمانی، ذخیره‌سازی در DB/Config/Memory و ارزیابی یکپارچه فراهم می‌کند و rollout تدریجی و A/B testing را ممکن می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: FlagManager، strategies (user/percentage/time/session)، stores (DB/Config/Memory)، Evaluation API
- ❌ خارج از دامنه: تست‌های A/B (در test)، گزارش‌گیری (در report)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-FF-01 | پیاده‌سازی هستهٔ موتور feature-flag به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-FF-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-FF-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| LaunchDarkly / Unleash / flagr | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\FeatureFlag\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 7 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Feature` | Facade | `src/Facades/Feature.php` |
| `FeatureEvaluator` | Class | `src/FeatureEvaluator.php` |
| `FeatureFlagEngine` | Engine | `src/FeatureFlagEngine.php` |
| `FeatureFlagResolver` | Class | `src/FeatureFlagResolver.php` |
| `FeatureManager` | Manager | `src/FeatureManager.php` |
| `ScopedFeature` | Class | `src/ScopedFeature.php` |
| `feature_flag` | Class | `src/feature_flag.php` |

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
فایل پیکربندی این موتور در `engines/feature-flag/config/feature-flag.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.feature-flag.config.feature-flag`.

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
| AC-FEATURE_FLAG-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-FEATURE_FLAG-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| LaunchDarkly / Unleash / flagr | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.feature-flag.v1
engine:
  id: tavaan.engine.feature-flag
  namespace: Tavaan\Engine\FeatureFlag\
  path: engines/feature-flag
  priority: P2
  phase: M7
  depends_on: [config]
  soft_depends_on: [cache, database, rbac, tenancy]
  facade: {name: Feature, accessor: feature}
  tables: []
  config_file: engines/feature-flag/config/feature-flag.php
  loc_estimate: 499
  acceptance:
    - {id: AC-FEATURE_FLAG-01, test: 'php bin/tvn engines'}
    - {id: AC-FEATURE_FLAG-02, test: 'php bin/tvn engines --list'}
```
