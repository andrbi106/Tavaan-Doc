# DOC-048 — موتور Filesystem | سامانه فایل

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-048 |
| Engine ID | `tavaan.engine.filesystem` |
| Namespace | `Tavaan\Engine\Filesystem\` |
| مسیر | `engines/filesystem/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Storage` → accessor `filesystem` |
| جداول DB | — |
| LOC برآوردی | 2248 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Filesystem لایهٔ ذخیره‌سازی فایل را با چندین disk (Local، S3، FTP، SFTP، Flysystem) فراهم می‌کند و operations read/write/stream/list را به‌صورت یکپارچه ارائه می‌دهد.

### ۱٫۲ دامنه (What)
- ✅ شامل: DiskManager، Local/S3/FTP/SFTP drivers، Stream operations، File existence/metadata
- ❌ خارج از دامنه: Media processing (در media)، Backup (در backup)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-FS-01 | پیاده‌سازی هستهٔ موتور filesystem به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-FS-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-FS-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Filesystem + Flysystem | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Filesystem\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 19 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `AbstractFilesystem` | Class | `src/Adapters/AbstractFilesystem.php` |
| `FtpFilesystem` | Class | `src/Adapters/FtpFilesystem.php` |
| `CurlS3Transport` | Class | `src/Adapters/S3/CurlS3Transport.php` |
| `S3TransportInterface` | Contract/Interface | `src/Adapters/S3/S3TransportInterface.php` |
| `StreamS3Transport` | Class | `src/Adapters/S3/StreamS3Transport.php` |
| `S3Filesystem` | Class | `src/Adapters/S3Filesystem.php` |
| `S3Signer` | Class | `src/Adapters/S3Signer.php` |
| `StorageLinkCommand` | Command | `src/Console/StorageLinkCommand.php` |
| `FilesystemInterface` | Contract/Interface | `src/Contracts/FilesystemInterface.php` |
| `LocalFilesystem` | Class | `src/Drivers/LocalFilesystem.php` |
| `MemoryFilesystem` | Class | `src/Drivers/MemoryFilesystem.php` |
| `DiskFullException` | Exception | `src/Exceptions/DiskFullException.php` |
| `FileNotFoundException` | Exception | `src/Exceptions/FileNotFoundException.php` |
| `FilesystemException` | Exception | `src/Exceptions/FilesystemException.php` |
| `PathTraversalException` | Exception | `src/Exceptions/PathTraversalException.php` |
| `Storage` | Facade | `src/Facades/Storage.php` |
| `FilesystemEngine` | Engine | `src/FilesystemEngine.php` |
| `FilesystemManager` | Manager | `src/FilesystemManager.php` |
| `FilesystemServiceProvider` | ServiceProvider | `src/FilesystemServiceProvider.php` |

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
فایل پیکربندی: `engines/filesystem/config/filesystem.php`

کلیدهای اصلی:
`default`, `disks`, `local`, `driver`, `root`, `visibility`, `public`, `memory`, `links`

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
| AC-FILESYSTEM-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-FILESYSTEM-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Filesystem + Flysystem | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.filesystem.v1
engine:
  id: tavaan.engine.filesystem
  namespace: Tavaan\Engine\Filesystem\
  path: engines/filesystem
  priority: P1
  phase: M5
  depends_on: [config]
  soft_depends_on: []
  facade: {name: Storage, accessor: filesystem}
  tables: []
  config_file: engines/filesystem/config/filesystem.php
  loc_estimate: 2248
  acceptance:
    - {id: AC-FILESYSTEM-01, test: 'php bin/tvn engines'}
    - {id: AC-FILESYSTEM-02, test: 'php bin/tvn engines --list'}
```
