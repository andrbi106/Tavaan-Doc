# DOC-034 — موتور Auth | احراز هویت

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-034 |
| نوع | شاخص موتور (Engine Index) |
| وضعیت | Draft v0.0.1 |
| مسیر پوشه | `docs/03-engines/auth/` |

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-034 |
| Engine ID | `tavaan.engine.auth` |
| Namespace | `Tavaan\Engine\Auth\` |
| مسیر | `engines/auth/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `session`, `hash`, `crypt`, `event`, `database`, `cache`, `config` |
| وابستگی (نرم/اختیاری) | `http`, `orm`, `notification` |
| Facade | `Auth` → accessor `auth` |
| جداول DB | `password_resets`, `personal_access_tokens`, `user_devices`, `two_factor_secrets` |
| LOC برآوردی | 2430 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## فهرست فایل‌های ممیزی

این پوشه شامل **۱۸ فایل ممیزی عملیاتی** است (README + ۱۷ بخش).
هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| شناسه | فایل | بخش | ممیزی |
|---|---|---|---|
| [DOC-034-S01](./01-goal-scope.md) | هدف و دامنه | ✅ |
| [DOC-034-S02](./02-concepts.md) | مفاهیم و واژگان | ✅ |
| [DOC-034-S03](./03-architecture.md) | معماری داخلی | ✅ |
| [DOC-034-S04](./04-public-api.md) | API عمومی | ✅ |
| [DOC-034-S05](./05-algorithms.md) | الگوریتم‌ها و ساختار داده | ✅ |
| [DOC-034-S06](./06-config.md) | پیکربندی | ✅ |
| [DOC-034-S07](./07-contracts.md) | قراردادها (Contracts) | ✅ |
| [DOC-034-S08](./08-extensibility.md) | نقاط توسعه | ✅ |
| [DOC-034-S09](./09-security.md) | امنیت | ✅ |
| [DOC-034-S10](./10-performance.md) | کارایی | ✅ |
| [DOC-034-S11](./11-error-handling.md) | مدیریت خطا | ✅ |
| [DOC-034-S12](./12-testing.md) | تست | ✅ |
| [DOC-034-S13](./13-example.md) | مثال End-to-End | ✅ |
| [DOC-034-S14](./14-acceptance.md) | معیار پذیرش 🧪 | ✅ |
| [DOC-034-S15](./15-limitations.md) | محدودیت‌ها و کارهای آینده | ✅ |
| [DOC-034-S16](./16-references.md) | مراجع | ✅ |
| [DOC-034-S17](./17-machine-readable.yml) | بلوک ماشین‌خوان 🧠 | ✅ |


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
