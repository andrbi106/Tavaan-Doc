# DOC-125 — خلاصهٔ فازهای اجرایی (M6-M25) ⚠️

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-125 |
| وضعیت | Approved v0.0.1 |
| نقش | خلاصهٔ فازهای در حال اجرا / آینده |
| پیش‌نیاز | DOC-120, DOC-124 |

## گروه وب (M6-M9) ⚠️

### M6 — HTTP بنیاد
**موتور:** `http` (۵,۷۲۶ LOC، ۶۵ فایل)
**وابستگی:** M5 (pipeline, event, error, config)

**خروجی‌های مورد انتظار:**
- `Request` immutable (method, uri, headers, body)
- `Response` (status, headers, body)
- `Kernel` با middleware pipeline
- Server adapters (PHP built-in, FPM, Swoole, FrankenPHP)

**معیار پذیرش 🧪:**
- AC-HTTP-01: Request immutable
- AC-HTTP-02: Response با status/headers/body
- AC-HTTP-03: Kernel با middleware pipeline
- AC-HTTP-04: `php bin/tvn serve` کار می‌کند ✅

### M7 — مسیریابی
**موتور:** `router` (۵۷۲ LOC، ۳ فایل)
**وابستگی:** M6

**خروجی‌های مورد انتظار:**
- Compiled Trie با match ≤۵µs روی ۱۰۰۰ روت
- پشتیبانی از `{param}`, `{param?}`, `{param:[0-9]+}`
- گروه‌بندی روت‌ها
- نام‌گذاری روت‌ها
- cache کامپایل

### M8 — وب پشتیبان
**موتورها:** session (۹۶۸), cookie (۲۱۷), cors (۲۱۳)
**وابستگی:** M6, M4

**خروجی‌های مورد انتظار:**
- Session: start/destroy/regenerate، driver file/database/redis
- Cookie: رمزنگاری‌شده، HttpOnly + Secure + SameSite
- CORS: preflight handling، configurable origins

### M9 — نما و i18n
**موتورها:** view (۸۹۷), jalali (۵۳۵)
**وابستگی:** M4

**خروجی‌های مورد انتظار:**
- View: `{{ }}` escape، `{!! !!}` raw، `@directive`، layout، component
- Jalali: تبدیل میلادی↔جلالی، ۱۰۰۰۰ Test Vector، فرمت‌بندی فارسی

---

## گروه داده (M10-M13) ⚠️

### M10 — دیتابیس
**موتور:** `database` (۱۱,۳۲۹ LOC، ۹۳ فایل) — **بزرگ‌ترین موتور**
**وابستگی:** M3

**خروجی‌های مورد انتظار:**
- ConnectionManager چنددرایور (MySQL/Postgres/SQLite)
- QueryBuilder با prepared statement
- Grammar (MySQL/Postgres/SQLite)
- Transaction با Savepoint
- N+1 detection
- Read/Write Splitting

### M11 — طرح و مهاجرت
**موتورها:** schema (۷۴۵), migration (۴۴۵)
**وابستگی:** M10, M3

### M12 — ORM
**موتور:** `orm` (۹۶۳ LOC)
**وابستگی:** M10

**خروجی‌های مورد انتظار:**
- Active Record (find/save/delete)
- Repository pattern
- relations (hasOne/hasMany/belongsTo/belongsToMany)
- eager loading
- casts و mutators
- soft delete

### M13 — اعتبارسنجی و جستجو
**موتورها:** validation (۲,۹۷۵), search (۴,۰۴۷)
**وابستگی:** M4

---

## گروه امنیت (M14-M16) ⚠️

### M14 — کش و صف
**موتورها:** cache (۱,۶۰۸), queue (۴,۵۵۵), schedule (۹۶۰)
**وابستگی:** M3

**خروجی‌های مورد انتظار:**
- Cache: ۶ درایور (array/file/redis/memcached/apcu/database)
- Queue: At-Least-Once delivery، retry، DLQ
- Schedule: cron-like، expression parsing

### M15 — احراز هویت
**موتور:** `auth` (۲,۴۲۹ LOC)
**وابستگی:** M8 (session), M4 (hash, crypt), M10 (database), M14 (cache)

**خروجی‌های مورد انتظار:**
- SessionGuard
- TokenGuard/JWT (algorithm pinning، refresh rotation)
- OTP/2FA (RFC 6238 TOTP)
- Device tracking

### M16 — RBAC و امنیت
**موتورها:** rbac (۱,۲۴۲), security (۱,۰۵۴), audit (۹۰۸)
**وابستگی:** M15, M10, M14

---

## گروه زیرساخت (M17-M19) ⚠️

### M17 — نامه و اطلاع‌رسانی
**موتورها:** mail (۱,۷۱۶), notification (۲,۰۰۳)
**وابستگی:** M3

### M18 — رسانه و HTTP-Client
**موتورها:** media (۱,۲۱۹), http-client (۱,۸۰۷)
**وابستگی:** M4

### M19 — رصدپذیری و پشتیبان
**موتورها:** observability (۳,۴۵۲), backup (۱,۳۸۸)
**وابستگی:** M3, M4

---

## گروه سرویس (M20-M22) ⚠️

### M20 — چنداجاره‌ای و پرچم
**موتورها:** tenancy (۳,۱۱۷), feature-flag (۴۹۹)
**وابستگی:** M4

### M21 — API و Realtime
**موتورها:** api (۱,۵۱۷), realtime (۲,۰۲۷)
**وابستگی:** M6, M3

### M22 — دامنه
**موتورها:** workflow (۲,۶۸۸), report (۲,۱۲۱), payment (۲,۵۹۷)
**وابستگی:** M3, M10

---

## گروه ابزار (M23-M24) ⚠️

### M23 — ابزارسازی
**موتورها:** scaffold (۲,۰۹۲), admin (۲,۳۲۳), plugin (۱,۸۳۸)
**وابستگی:** M3, M4, M9, M12, M16

### M24 — QA و ارتقا
**موتورها:** test (۳,۶۳۵), upgrade (۱,۴۰۸)
**وابستگی:** M3, M10, M4

---

## گروه اپلیکیشن (M25) ⬜

### اپلیکیشن‌های هدف
- **پایه:** Blog, Shop, Forum, LMS, News-Portal
- **حرفه‌ای:** ERP, BPMS, CRM

### معیار پذیرش نهایی 🧪
- AC-1: نصب آفلاین + `tvn serve` + صفحهٔ خوش‌آمدگویی
- AC-2: `tvn test` سبز با ≥۹۵٪ پوشش هسته
- AC-3: `tvn bench:all` همهٔ اهداف NFR-PERF پاس
- AC-4: `tvn arch:check` + `tvn security:scan` صفر خطا
- AC-5: Blog + Shop قابل نصب با سناریوی End-to-End
- AC-6: ماژول Shop به سرویس مستقل تبدیل می‌شود با فقط تغییر `deploy/`
