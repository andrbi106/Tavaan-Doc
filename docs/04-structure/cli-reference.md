# DOC-083 — مرجع CLI تَوان

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-083 |
| وضعیت | Approved v0.0.1 |
| نقش | مرجع کامل دستورات CLI پیاده‌سازی‌شده |
| پیش‌نیاز | DOC-030 |

## وضعیت پیاده‌سازی

تَوان در نسخهٔ ۰.۰.۱ **۵ دستور CLI** پیاده‌سازی کرده است (مرجع: ۱۰۵ دستور در ۱۶ دسته).

## دستورات

### info
```bash
php bin/tvn info
```
نمایش اطلاعات سیستم: نسخه، PHP، مسیر، تعداد موتورها.

### version
```bash
php bin/tvn version
```
نمایش نسخهٔ فریمورک.

### engines
```bash
php bin/tvn engines
```
لیست ۵۲ موتور با شناسه، نسخه، عنوان، وضعیت پیکربندی.

### config
```bash
php bin/tvn config
```
نمایش پیکربندی موتورها (کلیدهای هر موتور).

### serve
```bash
php bin/tvn serve [--host=127.0.0.1] [--port=8000]
```
اجرای سرور توسعه (`php -S`).

## کدهای خروج

| کد | معنا |
|---|---|
| 0 | موفقیت |
| 1 | شکست |
| 2 | نامعتبر |

## گزینه‌های سراسری

(در نسخهٔ ۰.۰.۱ پیاده‌سازی نشده — برای نسخهٔ ۱.۰)

## دستورات آینده (طراحی‌شده در مرجع)

| دسته | تعداد | مثال |
|---|---|---|
| Info & Health | ۵ | about, doctor, health:check |
| Serve | ۵ | down, up, maintenance |
| Optimize | ۱۰ | config:cache, route:cache |
| Database | ۱۱ | migrate, db:seed |
| Scaffold | ۱۷ | make:module, make:engine |
| Module | ۱۰ | module:list, module:install |
| Queue | ۱۲ | queue:work, outbox:relay |
| Security | ۶ | key:generate, security:scan |
| RBAC | ۱۰ | rbac:sync, audit:verify |
| Quality | ۷ | test, bench:all, arch:check |
| ... | | |
| **مجموع** | **۱۰۵** | |
