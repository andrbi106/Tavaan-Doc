# DOC-067 — موتور RBAC | نقش و کنترل دسترسی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-067 |
| نوع | شاخص موتور (Engine Index) |
| وضعیت | Draft v0.0.1 |
| مسیر پوشه | `docs/03-engines/rbac/` |

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-067 |
| Engine ID | `tavaan.engine.rbac` |
| Namespace | `Tavaan\Engine\Rbac\` |
| مسیر | `engines/rbac/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M4 |
| وابستگی (سخت) | `auth`, `database`, `cache`, `event`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Gate` → accessor `gate` |
| جداول DB | `tvn_permissions`, `tvn_roles`, `tvn_role_user`, `tvn_permission_role`, `tvn_delegations` |
| LOC برآوردی | 1242 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## فهرست فایل‌های ممیزی

این پوشه شامل **۱۸ فایل ممیزی عملیاتی** است (README + ۱۷ بخش).
هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| شناسه | فایل | بخش | ممیزی |
|---|---|---|---|
| [DOC-067-S01](./01-goal-scope.md) | هدف و دامنه | ✅ |
| [DOC-067-S02](./02-concepts.md) | مفاهیم و واژگان | ✅ |
| [DOC-067-S03](./03-architecture.md) | معماری داخلی | ✅ |
| [DOC-067-S04](./04-public-api.md) | API عمومی | ✅ |
| [DOC-067-S05](./05-algorithms.md) | الگوریتم‌ها و ساختار داده | ✅ |
| [DOC-067-S06](./06-config.md) | پیکربندی | ✅ |
| [DOC-067-S07](./07-contracts.md) | قراردادها (Contracts) | ✅ |
| [DOC-067-S08](./08-extensibility.md) | نقاط توسعه | ✅ |
| [DOC-067-S09](./09-security.md) | امنیت | ✅ |
| [DOC-067-S10](./10-performance.md) | کارایی | ✅ |
| [DOC-067-S11](./11-error-handling.md) | مدیریت خطا | ✅ |
| [DOC-067-S12](./12-testing.md) | تست | ✅ |
| [DOC-067-S13](./13-example.md) | مثال End-to-End | ✅ |
| [DOC-067-S14](./14-acceptance.md) | معیار پذیرش 🧪 | ✅ |
| [DOC-067-S15](./15-limitations.md) | محدودیت‌ها و کارهای آینده | ✅ |
| [DOC-067-S16](./16-references.md) | مراجع | ✅ |
| [DOC-067-S17](./17-machine-readable.yml) | بلوک ماشین‌خوان 🧠 | ✅ |


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
