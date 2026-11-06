# DOC-060 — موتور Observability | رصدپذیری

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-060 |
| نوع | شاخص موتور (Engine Index) |
| وضعیت | Draft v0.0.1 |
| مسیر پوشه | `docs/03-engines/observability/` |

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-060 |
| Engine ID | `tavaan.engine.observability` |
| Namespace | `Tavaan\Engine\Observability\` |
| مسیر | `engines/observability/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `log` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Metrics` → accessor `metrics` |
| جداول DB | — |
| LOC برآوردی | 3452 |
| مسئول | @TavaanOfficial |
| مرتبط | DOC-030 |

---

## فهرست فایل‌های ممیزی

این پوشه شامل **۱۸ فایل ممیزی عملیاتی** است (README + ۱۷ بخش).
هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| شناسه | فایل | بخش | ممیزی |
|---|---|---|---|
| [DOC-060-S01](./01-goal-scope.md) | هدف و دامنه | ✅ |
| [DOC-060-S02](./02-concepts.md) | مفاهیم و واژگان | ✅ |
| [DOC-060-S03](./03-architecture.md) | معماری داخلی | ✅ |
| [DOC-060-S04](./04-public-api.md) | API عمومی | ✅ |
| [DOC-060-S05](./05-algorithms.md) | الگوریتم‌ها و ساختار داده | ✅ |
| [DOC-060-S06](./06-config.md) | پیکربندی | ✅ |
| [DOC-060-S07](./07-contracts.md) | قراردادها (Contracts) | ✅ |
| [DOC-060-S08](./08-extensibility.md) | نقاط توسعه | ✅ |
| [DOC-060-S09](./09-security.md) | امنیت | ✅ |
| [DOC-060-S10](./10-performance.md) | کارایی | ✅ |
| [DOC-060-S11](./11-error-handling.md) | مدیریت خطا | ✅ |
| [DOC-060-S12](./12-testing.md) | تست | ✅ |
| [DOC-060-S13](./13-example.md) | مثال End-to-End | ✅ |
| [DOC-060-S14](./14-acceptance.md) | معیار پذیرش 🧪 | ✅ |
| [DOC-060-S15](./15-limitations.md) | محدودیت‌ها و کارهای آینده | ✅ |
| [DOC-060-S16](./16-references.md) | مراجع | ✅ |
| [DOC-060-S17](./17-machine-readable.yml) | بلوک ماشین‌خوان 🧠 | ✅ |


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
