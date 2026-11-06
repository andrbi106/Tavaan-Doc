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
🔒 **الزام:** هیچ `composer.json` در core/ و engines/، هیچ `use Psr\` در کد

### P2 — Contract-First 🔒
Interface قبل از پیاده‌سازی.
🔒 **الزام:** هر کلاس عمومی باید Interface داشته باشد.

### P3 — Minimal Kernel
هسته = حداقل.
🔒 **الزام:** هسته فقط شامل: Autoloader, Container, Application, Events, Bootstrap, Provider, Facade, Support, Contracts, Error, Exceptions, Context.

### P4 — Explicit Boundaries 🔒
مرز ماژول.
🔒 **الزام:** موتورها فقط از طریق سه درگاه (Container, Events, EngineBus) ارتباط می‌گیرند.

### P5 — Events over Calls
بین دامنه‌ها با رویداد.
🔒 **الزام:** EventDispatcher برای ارتباط بین دامنه‌ها.

### P6 — Fail Fast & Loud
بدون catch خالی.
🔒 **الزام:** بدون catch خالی یا @ suppression.

### P7 — Secure by Default 🔒
Auto-escape، Prepared Statement، CSRF.
🔒 **الزام:** Auto-escape، Prepared Statement، CSRF هم‌روشن.

### P8 — No Hidden Magic
Facade = Lazy Proxy + @mixin.
🔒 **الزام:** Facade = Lazy Proxy + @mixin؛ بدون property پویا.

### P9 — SRP + Small Surface
کلاس ≤۳۰۰ خط، متد ≤۵۰ خط.
🔒 **الزام:** بدون catch خالی یا @ suppression.

### P10 — Readable Performance
بهینه‌سازی فقط با اندازه‌گیری.
🔒 **الزام:** بهینه‌سازی فقط با اندازه‌گیری.

### P11 — Language Forward-Compat
کد روی ۸.۲، اجرای بدون Deprecated تا ۸.۴.
🔒 **الزام:** کد روی 8.2، اجرای بدون Deprecated تا 8.4/9.

### P12 — Extensibility Triad
هر موتور ۳ نقطهٔ توسعه.
🔒 **الزام:** هر موتور ۳ نقطهٔ توسعه: Hook + Contract + Decorator.

## ترتیب قطع‌کننده

```
Correctness > Security > Simplicity > Performance > Flexibility > Convenience
```

**قاعدهٔ طلایی:** تصمیم برگشت‌ناپذیر → ADR؛ تصمیم برگشت‌پذیر → سریع تصمیم بگیر.
