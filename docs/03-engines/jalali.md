# DOC-053 — موتور Jalali | تقویم جلالی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-053 |
| Engine ID | `tavaan.engine.jalali` |
| Namespace | `Tavaan\Engine\I18n\Jalali\` |
| مسیر | `engines/jalali/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `i18n` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 535 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Jalali تبدیل و محاسبهٔ تاریخ شمسی را با کلاس JalaliDate، JalaliConverter و Clock فراهم می‌کند و نمایش دوطرفهٔ جلالی/میلادی را در همه‌جا یکپارچه می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: JalaliDate، JalaliConverter، Clock، conversion دوطرفه
- ❌ خارج از دامنه: i18n (در i18n)، فرمت اعداد (در i18n)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-JALALI-01 | پیاده‌سازی هستهٔ موتور jalali به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-JALALI-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-JALALI-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| jenssegers/date + morilog/jalali | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\I18n\Jalali\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 6 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Clock` | Class | `src/Clock.php` |
| `Jalali` | Class | `src/Jalali.php` |
| `JalaliConverter` | Class | `src/JalaliConverter.php` |
| `JalaliDate` | Class | `src/JalaliDate.php` |
| `JalaliEngine` | Engine | `src/JalaliEngine.php` |
| `JalaliServiceProvider` | ServiceProvider | `src/JalaliServiceProvider.php` |

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
فایل پیکربندی: `engines/jalali/config/jalali.php`

کلیدهای اصلی:
`default`, `first_day_of_week`, `show_weekdays`, `persian_digits`

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
| AC-JALALI-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-JALALI-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| jenssegers/date + morilog/jalali | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.jalali.v1
engine:
  id: tavaan.engine.jalali
  namespace: Tavaan\Engine\I18n\Jalali\
  path: engines/jalali
  priority: P0
  phase: M2
  depends_on: [i18n]
  soft_depends_on: []
  facade: {name: , accessor: }
  tables: []
  config_file: engines/jalali/config/jalali.php
  loc_estimate: 535
  acceptance:
    - {id: AC-JALALI-01, test: 'php bin/tvn engines'}
    - {id: AC-JALALI-02, test: 'php bin/tvn engines --list'}
```
