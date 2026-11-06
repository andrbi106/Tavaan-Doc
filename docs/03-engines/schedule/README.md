# DOC-072 — موتور Schedule | زمان‌بندی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-072 |
| نوع | شاخص موتور (Engine Index) |
| وضعیت | Draft v0.0.1 |
| مسیر پوشه | `docs/03-engines/schedule/` |

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-072 |
| Engine ID | `tavaan.engine.schedule` |
| Namespace | `Tavaan\Engine\Schedule\` |
| مسیر | `engines/schedule/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `console` |
| وابستگی (نرم/اختیاری) | `cache`, `queue`, `log` |
| Facade | `Schedule` → accessor `schedule` |
| جداول DB | — |
| LOC برآوردی | 960 |
| مسئول | @TavaanOfficial |
| مرتبط | DOC-030 |

---

## فهرست فایل‌های ممیزی

این پوشه شامل **۱۸ فایل ممیزی عملیاتی** است (README + ۱۷ بخش).
هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| شناسه | فایل | بخش | ممیزی |
|---|---|---|---|
| [DOC-072-S01](./01-goal-scope.md) | هدف و دامنه | ✅ |
| [DOC-072-S02](./02-concepts.md) | مفاهیم و واژگان | ✅ |
| [DOC-072-S03](./03-architecture.md) | معماری داخلی | ✅ |
| [DOC-072-S04](./04-public-api.md) | API عمومی | ✅ |
| [DOC-072-S05](./05-algorithms.md) | الگوریتم‌ها و ساختار داده | ✅ |
| [DOC-072-S06](./06-config.md) | پیکربندی | ✅ |
| [DOC-072-S07](./07-contracts.md) | قراردادها (Contracts) | ✅ |
| [DOC-072-S08](./08-extensibility.md) | نقاط توسعه | ✅ |
| [DOC-072-S09](./09-security.md) | امنیت | ✅ |
| [DOC-072-S10](./10-performance.md) | کارایی | ✅ |
| [DOC-072-S11](./11-error-handling.md) | مدیریت خطا | ✅ |
| [DOC-072-S12](./12-testing.md) | تست | ✅ |
| [DOC-072-S13](./13-example.md) | مثال End-to-End | ✅ |
| [DOC-072-S14](./14-acceptance.md) | معیار پذیرش 🧪 | ✅ |
| [DOC-072-S15](./15-limitations.md) | محدودیت‌ها و کارهای آینده | ✅ |
| [DOC-072-S16](./16-references.md) | مراجع | ✅ |
| [DOC-072-S17](./17-machine-readable.yml) | بلوک ماشین‌خوان 🧠 | ✅ |


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
