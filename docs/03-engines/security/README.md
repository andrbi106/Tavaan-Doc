# DOC-075 — موتور Security | امنیت عرضی (CSRF/RateLimit/Sanitizer/SSRF)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-075 |
| نوع | شاخص موتور (Engine Index) |
| وضعیت | Draft v0.0.1 |
| مسیر پوشه | `docs/03-engines/security/` |

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-075 |
| Engine ID | `tavaan.engine.security` |
| Namespace | `Tavaan\Engine\Security\` |
| مسیر | `engines/security/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `http`, `crypt`, `cache`, `config` |
| وابستگی (نرم/اختیاری) | `session`, `router` |
| Facade | `Security` → accessor `security` |
| جداول DB | — |
| LOC برآوردی | 1054 |
| مسئول | @TavaanOfficial |
| مرتبط | DOC-030 |

---

## فهرست فایل‌های ممیزی

این پوشه شامل **۱۸ فایل ممیزی عملیاتی** است (README + ۱۷ بخش).
هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| شناسه | فایل | بخش | ممیزی |
|---|---|---|---|
| [DOC-075-S01](./01-goal-scope.md) | هدف و دامنه | 📋 |
| [DOC-075-S02](./02-concepts.md) | مفاهیم و واژگان | 📋 |
| [DOC-075-S03](./03-architecture.md) | معماری داخلی | 📋 |
| [DOC-075-S04](./04-public-api.md) | API عمومی | 📋 |
| [DOC-075-S05](./05-algorithms.md) | الگوریتم‌ها و ساختار داده | 📋 |
| [DOC-075-S06](./06-config.md) | پیکربندی | 📋 |
| [DOC-075-S07](./07-contracts.md) | قراردادها (Contracts) | 📋 |
| [DOC-075-S08](./08-extensibility.md) | نقاط توسعه | 📋 |
| [DOC-075-S09](./09-security.md) | امنیت | 📋 |
| [DOC-075-S10](./10-performance.md) | کارایی | 📋 |
| [DOC-075-S11](./11-error-handling.md) | مدیریت خطا | 📋 |
| [DOC-075-S12](./12-testing.md) | تست | 📋 |
| [DOC-075-S13](./13-example.md) | مثال End-to-End | 📋 |
| [DOC-075-S14](./14-acceptance.md) | معیار پذیرش 🧪 | 📋 |
| [DOC-075-S15](./15-limitations.md) | محدودیت‌ها و کارهای آینده | 📋 |
| [DOC-075-S16](./16-references.md) | مراجع | 📋 |
| [DOC-075-S17](./17-machine-readable.yml) | بلوک ماشین‌خوان 🧠 | 📋 |


## روش استفاده

۱. برای مرور کلی، این README را بخوان.
۲. برای ممیزی بخش خاص، فایل مربوطه را باز کن.
۳. چک‌لیست ممیزی عملیاتی در هر فایل را تکمیل کن.
۴. وضعیت ممیزی را در جدول پایین هر فایل ثبت کن.

## وضعیت کلی ممیزی

| شاخص | وضعیت |
|---|---|
| کل فایل‌ها | ۱۸ |
| فایل‌های ممیزی‌شده | ۰ |
| فایل‌های با محتوای کامل | 17 |
| فایل‌های N/A | 9 |
