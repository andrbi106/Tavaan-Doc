# DOC-048-S03 — معماری داخلی (موتور filesystem)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-048-S03 |
| موتور | `filesystem` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
