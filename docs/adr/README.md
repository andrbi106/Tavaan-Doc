# DOC-140 — شاخص تصمیم‌های معماری (ADR)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-140 |
| وضعیت | Approved v0.0.1 |
| نقش | فهرست ADRهای تَوان |
| پیش‌نیاز | DOC-020 |

## قواعد ADR 🔒

1. شمارهٔ ترتیبی هرگز تغییر نمی‌کند
2. ADR پذیرفته‌شده تغییر نمی‌کند (اصلاح با ADR جدید)
3. هر ADR باید به اصل ارجاع دهد
4. وضعیت: Proposed → Accepted → Deprecated/Superseded

## فهرست ADRهای پذیرفته‌شده

| شماره | عنوان | وضعیت | فایل |
|---|---|---|---|
| ADR-0004 | صفر وابستگی در هسته | Accepted | `ADR-0004-zero-dependency.md` |
| ADR-0005 | Autoloader خودنوشته | Accepted | `ADR-0005-custom-autoloader.md` |

## ADRهای مرجع (طراحی‌شده، هنوز پیاده‌سازی نشده)

| شماره | عنوان | وضعیت در دمو |
|---|---|---|
| ADR-0001 | معماری ترکیبی | ⚠️ اسکلت |
| ADR-0002 | مدل مجوزدهی | N/A |
| ADR-0003 | حداقل PHP 8.2 | ✅ پیاده‌سازی |
| ADR-0006 | ULID کلید اصلی | ⬜ |
| ADR-0007 | ORM دوگانه | ⬜ |
| ADR-0008 | View .tv.php | ⬜ |
| ADR-0009 | Outbox | ⬜ |
| ADR-0010 | Multi-Tenancy | ⬜ |
| ADR-0011 | Fiber Context | ⬜ |
| ADR-0012 | تقویم جلالی | ⬜ (موتور jalali موجود) |
| ADR-0013 | Money VO | ⬜ |
| ADR-0014 | صفر vendor runtime | ✅ پیاده‌سازی |
| ADR-0015 | API Versioning | ⬜ |
| ADR-0016 | Lazy Proxy | ⬜ |
