# DOC-076 — موتور Session | نشست

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-076 |
| نوع | شاخص موتور (Engine Index) |
| وضعیت | Draft v0.0.1 |
| مسیر پوشه | `docs/03-engines/session/` |

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-076 |
| Engine ID | `tavaan.engine.session` |
| Namespace | `Tavaan\Engine\Session\` |
| مسیر | `engines/session/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `http`, `crypt`, `config` |
| وابستگی (نرم/اختیاری) | `database`, `cache` |
| Facade | `Session` → accessor `session` |
| جداول DB | `sessions` |
| LOC برآوردی | 968 |
| مسئول | @TavaanOfficial |
| مرتبط | DOC-030 |

---

## فهرست فایل‌های ممیزی

این پوشه شامل **۱۸ فایل ممیزی عملیاتی** است (README + ۱۷ بخش).
هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| شناسه | فایل | بخش | ممیزی |
|---|---|---|---|
| [DOC-076-S01](./01-goal-scope.md) | هدف و دامنه | ✅ |
| [DOC-076-S02](./02-concepts.md) | مفاهیم و واژگان | ✅ |
| [DOC-076-S03](./03-architecture.md) | معماری داخلی | ✅ |
| [DOC-076-S04](./04-public-api.md) | API عمومی | ✅ |
| [DOC-076-S05](./05-algorithms.md) | الگوریتم‌ها و ساختار داده | ✅ |
| [DOC-076-S06](./06-config.md) | پیکربندی | ✅ |
| [DOC-076-S07](./07-contracts.md) | قراردادها (Contracts) | ✅ |
| [DOC-076-S08](./08-extensibility.md) | نقاط توسعه | ✅ |
| [DOC-076-S09](./09-security.md) | امنیت | ✅ |
| [DOC-076-S10](./10-performance.md) | کارایی | ✅ |
| [DOC-076-S11](./11-error-handling.md) | مدیریت خطا | ✅ |
| [DOC-076-S12](./12-testing.md) | تست | ✅ |
| [DOC-076-S13](./13-example.md) | مثال End-to-End | ✅ |
| [DOC-076-S14](./14-acceptance.md) | معیار پذیرش 🧪 | ✅ |
| [DOC-076-S15](./15-limitations.md) | محدودیت‌ها و کارهای آینده | ✅ |
| [DOC-076-S16](./16-references.md) | مراجع | ✅ |
| [DOC-076-S17](./17-machine-readable.yml) | بلوک ماشین‌خوان 🧠 | ✅ |


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
