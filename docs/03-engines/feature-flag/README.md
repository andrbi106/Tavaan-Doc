# DOC-047 — موتور FeatureFlag | پرچم قابلیت

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-047 |
| نوع | شاخص موتور (Engine Index) |
| وضعیت | Draft v0.0.1 |
| مسیر پوشه | `docs/03-engines/feature-flag/` |

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-047 |
| Engine ID | `tavaan.engine.feature-flag` |
| Namespace | `Tavaan\Engine\FeatureFlag\` |
| مسیر | `engines/feature-flag/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M7 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | `cache`, `database`, `rbac`, `tenancy` |
| Facade | `Feature` → accessor `feature` |
| جداول DB | — |
| LOC برآوردی | 499 |
| مسئول | @TavaanOfficial |
| مرتبط | DOC-030 |

---

## فهرست فایل‌های ممیزی

این پوشه شامل **۱۸ فایل ممیزی عملیاتی** است (README + ۱۷ بخش).
هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| شناسه | فایل | بخش | ممیزی |
|---|---|---|---|
| [DOC-047-S01](./01-goal-scope.md) | هدف و دامنه | 📋 |
| [DOC-047-S02](./02-concepts.md) | مفاهیم و واژگان | 📋 |
| [DOC-047-S03](./03-architecture.md) | معماری داخلی | 📋 |
| [DOC-047-S04](./04-public-api.md) | API عمومی | 📋 |
| [DOC-047-S05](./05-algorithms.md) | الگوریتم‌ها و ساختار داده | 📋 |
| [DOC-047-S06](./06-config.md) | پیکربندی | 📋 |
| [DOC-047-S07](./07-contracts.md) | قراردادها (Contracts) | 📋 |
| [DOC-047-S08](./08-extensibility.md) | نقاط توسعه | 📋 |
| [DOC-047-S09](./09-security.md) | امنیت | 📋 |
| [DOC-047-S10](./10-performance.md) | کارایی | 📋 |
| [DOC-047-S11](./11-error-handling.md) | مدیریت خطا | 📋 |
| [DOC-047-S12](./12-testing.md) | تست | 📋 |
| [DOC-047-S13](./13-example.md) | مثال End-to-End | 📋 |
| [DOC-047-S14](./14-acceptance.md) | معیار پذیرش 🧪 | 📋 |
| [DOC-047-S15](./15-limitations.md) | محدودیت‌ها و کارهای آینده | 📋 |
| [DOC-047-S16](./16-references.md) | مراجع | 📋 |
| [DOC-047-S17](./17-machine-readable.yml) | بلوک ماشین‌خوان 🧠 | 📋 |


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
