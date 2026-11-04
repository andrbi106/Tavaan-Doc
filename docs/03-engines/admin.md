# DOC-031 — موتور Admin | پیشخان و CRUD Generator

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-031 |
| Engine ID | `tavaan.engine.admin` |
| Namespace | `Tavaan\Engine\Admin\` |
| مسیر | `engines/admin/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M8 |
| وابستگی (سخت) | `view`, `rbac`, `orm`, `validation`, `http` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Admin` → accessor `admin` |
| جداول DB | — |
| LOC برآوردی | 2323 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Admin پیشخان (dashboard) و سازندهٔ CRUD اعلامی (declarative) ارائه می‌دهد که با تعریف منابع در فایل manifest، فرم‌ها، جداول، نماهای نمایش و نمودارهای SVG را به‌صورت خودکار با پشتیبانی RTL و تم ظاهری تولید می‌کند. این موتور امکان ساخت پنل‌های مدیریتی یکپارچه فارسی را بدون نیاز به کدنویسی تکراری فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: ساخت منابع CRUD اعلامی، منوی پویا با فیلتر دسترسی، ویجت و نمودار داشبورد، ۲۷ نوع فیلد، sanitizer برای richtext، jalali_date دوطرفه
- ❌ خارج از دامنه: مدیریت نقش‌ها (در موتور rbac)، احراز هویت (در موتور auth)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-ADMIN-01 | پیاده‌سازی هستهٔ موتور admin به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-ADMIN-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-ADMIN-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Filament/Laravel Nova | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Admin\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 16 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Action` | Class | `src/Action.php` |
| `AdminEngine` | Engine | `src/AdminEngine.php` |
| `Dashboard` | Class | `src/Dashboard/Dashboard.php` |
| `Admin` | Facade | `src/Facades/Admin.php` |
| `Form` | Class | `src/Form.php` |
| `Field` | Class | `src/Form/Field.php` |
| `Repeater` | Class | `src/Form/Repeater.php` |
| `AdminController` | Controller | `src/Http/AdminController.php` |
| `DashboardController` | Controller | `src/Http/DashboardController.php` |
| `Menu` | Class | `src/Menu/Menu.php` |
| `MenuItem` | Class | `src/Menu/MenuItem.php` |
| `Resource` | Class | `src/Resource.php` |
| `Show` | Class | `src/Show.php` |
| `ChartRenderer` | Renderer | `src/Support/ChartRenderer.php` |
| `ValueTransformer` | Class | `src/Support/ValueTransformer.php` |
| `admin` | Class | `src/admin.php` |

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
فایل پیکربندی این موتور در `engines/admin/config/admin.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.admin.config.admin`.

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
| AC-ADMIN-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-ADMIN-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Filament/Laravel Nova | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.admin.v1
engine:
  id: tavaan.engine.admin
  namespace: Tavaan\Engine\Admin\
  path: engines/admin
  priority: P2
  phase: M8
  depends_on: [view, rbac, orm, validation, http]
  soft_depends_on: []
  facade: {name: Admin, accessor: admin}
  tables: []
  config_file: engines/admin/config/admin.php
  loc_estimate: 2323
  acceptance:
    - {id: AC-ADMIN-01, test: 'php bin/tvn engines'}
    - {id: AC-ADMIN-02, test: 'php bin/tvn engines --list'}
```
