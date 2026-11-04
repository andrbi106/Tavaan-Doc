# DOC-002 — اصول بنیادین تَوان

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-002 |
| وضعیت | Approved v0.0.1 |
| نقش | ۱۲ اصل بنیادین و قواعد تصمیم‌گیری |
| پیش‌نیاز | DOC-001 |

## ۱۲ اصل

### P1 — Zero Dependency 🔒
هیچ پکیج Composer در `core/` و `engines/` ممنوع است. افزونه‌های PHP مجازند اما باید Fallback داشته باشند.
**وضعیت Tavaan-Demo:** ✅ کامل — هیچ composer.json، هیچ `use Psr\`

### P2 — Contract-First 🔒
Interface قبل از پیاده‌سازی.
**وضعیت:** ⚠️ جزئی — قراردادها در `core/Contracts/` موجود اما همهٔ کلاس‌ها Interface ندارند.

### P3 — Minimal Kernel
هسته = حداقل.
**وضعیت:** ✅ هسته فقط: Autoloader, Container, Application, Events, Bootstrap, Provider, Facade, Support, Contracts, Error, Exceptions, Context.

### P4 — Explicit Boundaries 🔒
مرز ماژول.
**وضعیت:** ⚠️ مرزها تعریف شده اما enforcement ناقص.

### P5 — Events over Calls
بین دامنه‌ها با رویداد.
**وضعیت:** ✅ EventDispatcher موجود.

### P6 — Fail Fast & Loud
بدون catch خالی.
**وضعیت:** ⚠️ بررسی لازم.

### P7 — Secure by Default 🔒
Auto-escape، Prepared Statement، CSRF.
**وضعیت:** ⚠️ اسکلت موجود.

### P8 — No Hidden Magic
Facade = Lazy Proxy + @mixin.
**وضعیت:** ✅ Facade پایه موجود.

### P9 — SRP + Small Surface
کلاس ≤۳۰۰ خط، متد ≤۵۰ خط.
**وضعیت:** ⚠️ بررسی لازم.

### P10 — Readable Performance
بهینه‌سازی فقط با اندازه‌گیری.
**وضعیت:** N/A v0.0.1.

### P11 — Language Forward-Compat
کد روی ۸.۲، اجرای بدون Deprecated تا ۸.۴.
**وضعیت:** ✅ اجرا روی PHP 8.3.32 بدون خطا.

### P12 — Extensibility Triad
هر موتور ۳ نقطهٔ توسعه.
**وضعیت:** ⚠️ اسکلت.

## ترتیب قطع‌کننده

```
Correctness > Security > Simplicity > Performance > Flexibility > Convenience
```

**قاعدهٔ طلایی:** تصمیم برگشت‌ناپذیر → ADR؛ تصمیم برگشت‌پذیر → سریع تصمیم بگیر.
