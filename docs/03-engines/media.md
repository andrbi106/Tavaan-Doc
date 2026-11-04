# DOC-056 — موتور Media | آپلود و پردازش رسانه

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-056 |
| Engine ID | `tavaan.engine.media` |
| Namespace | `Tavaan\Engine\Media\` |
| مسیر | `engines/media/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Media` → accessor `media` |
| جداول DB | — |
| LOC برآوردی | 1219 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Media مدیریت فایل‌های رسانه‌ای را با آپلود، تشخیص MIME، اعتبارسنجی نوع، پردازش تصویر (resize/crop/watermark)، thumbnail و conversion فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: MediaManager، Uploader، ImageProcessor، ImageManager، MimeDetector، MimeValidator، conversions
- ❌ خارج از دامنه: Filesystem پایه (در filesystem)، Backup (در backup)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-MEDIA-01 | پیاده‌سازی هستهٔ موتور media به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-MEDIA-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-MEDIA-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Media Library + Intervention | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Media\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 13 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `InvalidFileTypeException` | Exception | `src/Exceptions/InvalidFileTypeException.php` |
| `MediaException` | Exception | `src/Exceptions/MediaException.php` |
| `Media` | Facade | `src/Facades/Media.php` |
| `Image` | Class | `src/Image.php` |
| `ImageManager` | Manager | `src/ImageManager.php` |
| `ImageProcessor` | Class | `src/ImageProcessor.php` |
| `Media` | Class | `src/Media.php` |
| `MediaEngine` | Engine | `src/MediaEngine.php` |
| `MediaManager` | Manager | `src/MediaManager.php` |
| `MediaServiceProvider` | ServiceProvider | `src/MediaServiceProvider.php` |
| `MimeDetector` | Class | `src/MimeDetector.php` |
| `MimeValidator` | Class | `src/MimeValidator.php` |
| `Uploader` | Class | `src/Uploader.php` |

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
فایل پیکربندی: `engines/media/config/media.php`

کلیدهای اصلی:
`max_size`, `allowed_extensions`, `image_driver`, `thumbnails`, `sizes`, `small`, `medium`, `large`, `webp`, `enabled`, `quality`

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
| AC-MEDIA-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-MEDIA-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Media Library + Intervention | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.media.v1
engine:
  id: tavaan.engine.media
  namespace: Tavaan\Engine\Media\
  path: engines/media
  priority: P1
  phase: M5
  depends_on: [config]
  soft_depends_on: []
  facade: {name: Media, accessor: media}
  tables: []
  config_file: engines/media/config/media.php
  loc_estimate: 1219
  acceptance:
    - {id: AC-MEDIA-01, test: 'php bin/tvn engines'}
    - {id: AC-MEDIA-02, test: 'php bin/tvn engines --list'}
```
