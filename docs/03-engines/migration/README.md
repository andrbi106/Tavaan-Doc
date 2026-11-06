# DOC-057 — موتور Migration | مهاجرت دیتابیس

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-057 |
| نوع | شاخص موتور (Engine Index) |
| وضعیت | Draft v0.0.1 |
| مسیر پوشه | `docs/03-engines/migration/` |

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-057 |
| Engine ID | `tavaan.engine.migration` |
| Namespace | `Tavaan\Engine\Database\Migration\` |
| مسیر | `engines/migration/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M3 |
| وابستگی (سخت) | `database`, `schema`, `console` |
| وابستگی (نرم/اختیاری) | — |
| Facade | — (بدون Facade) |
| جداول DB | `tvn_migrations` |
| LOC برآوردی | 445 |
| مسئول | @TavaanOfficial |
| مرتبط | DOC-030 |

---

## فهرست فایل‌های ممیزی

این پوشه شامل **۱۸ فایل ممیزی عملیاتی** است (README + ۱۷ بخش).
هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| شناسه | فایل | بخش | ممیزی |
|---|---|---|---|
| [DOC-057-S01](./01-goal-scope.md) | هدف و دامنه | ✅ |
| [DOC-057-S02](./02-concepts.md) | مفاهیم و واژگان | ✅ |
| [DOC-057-S03](./03-architecture.md) | معماری داخلی | ✅ |
| [DOC-057-S04](./04-public-api.md) | API عمومی | ✅ |
| [DOC-057-S05](./05-algorithms.md) | الگوریتم‌ها و ساختار داده | ✅ |
| [DOC-057-S06](./06-config.md) | پیکربندی | ✅ |
| [DOC-057-S07](./07-contracts.md) | قراردادها (Contracts) | ✅ |
| [DOC-057-S08](./08-extensibility.md) | نقاط توسعه | ✅ |
| [DOC-057-S09](./09-security.md) | امنیت | ✅ |
| [DOC-057-S10](./10-performance.md) | کارایی | ✅ |
| [DOC-057-S11](./11-error-handling.md) | مدیریت خطا | ✅ |
| [DOC-057-S12](./12-testing.md) | تست | ✅ |
| [DOC-057-S13](./13-example.md) | مثال End-to-End | ✅ |
| [DOC-057-S14](./14-acceptance.md) | معیار پذیرش 🧪 | ✅ |
| [DOC-057-S15](./15-limitations.md) | محدودیت‌ها و کارهای آینده | ✅ |
| [DOC-057-S16](./16-references.md) | مراجع | ✅ |
| [DOC-057-S17](./17-machine-readable.yml) | بلوک ماشین‌خوان 🧠 | ✅ |


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
