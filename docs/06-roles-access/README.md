# بخش ۰۶ — نقش‌ها و دسترسی (Roles & Access)

این بخش مشخصات کنترل دسترسی مبتنی بر نقش (RBAC) و وظایف هر نقش در
فریمورک تَوان را تعریف می‌کند. این اسناد **مشخصات قانونی (Canonical Specs)** هستند و
تَوان را به‌عنوان یک چارچوب مستقل توصیف می‌کنند — نه پیاده‌سازی خاص.

## راهنمای نمادها

| نماد | معنا |
|---|---|
| 🔒 | الزامی (MUST) — نقض = ریجکت |
| ⚠️ | توصیهٔ قوی (SHOULD) |
| 💡 | اختیاری (MAY) |
| 🧪 | دارای معیار تست/پذیرش |
| 🧠 | دارای بلوک ماشین‌خوان |

---

## فهرست اسناد بخش

| DOC-ID | عنوان | مسیر | نوع |
|---|---|---|---|
| DOC-100 | ماتریس نقش‌ها و سطوح دسترسی | `06-roles-access/roles-matrix.md` | مرجع 🔒 |
| DOC-101 | کاتالوگ مجوزها | `06-roles-access/permission-catalog.md` | مرجع 🔒 🧠 |
| DOC-102 | وظایف و گردش‌کار نقش‌ها | `06-roles-access/duties-workflow.md` | مشخصات 🧪 |

---

## مرور کلی

### DOC-100 — ماتریس نقش‌ها
دو لایهٔ نقش در تَوان:
- **نقش‌های سطح سیستم** (super-admin, admin, developer, auditor, support) برای
  مدیریت خودِ پلتفرم.
- **نقش‌های سطح کسب‌وکار** (customer, shop-manager, editor, accountant, …) برای
  عملیات دامنه‌ای به تفکیک کاربرد (DOC-091..098).

مفاهیم کلیدی: سلسله‌مراتب نقش (حداکثر عمق ۵)، سطوح داده
(Own/Team/Department/Tenant/Global)، تفویض موقت با انقضا، و اصول SoD، Four-Eyes،
Least Privilege، Deny-by-Default.

### DOC-101 — کاتالوگ مجوزها
قالب کلید: `<module>.<resource>[.<sub-resource>].<action>`.
اکشن‌های استاندارد: `view`, `view-any`, `create`, `update`, `delete`, `restore`,
`force-delete`, `export`, `import`, `manage`. و Wildcard (`*`) فقط برای super-admin.

این کاتالوگ **ساختار ماشین‌خوان** دارد و هر ماژول مجوزهایش را در `module.json` →
`permissions.items` اعلام می‌کند. دستور `tvn rbac:sync` آن‌ها را با دیتابیس همگام
می‌سازد و `tvn rbac:check` یکپارچگی را بررسی می‌کند.

### DOC-102 — وظایف و گردش‌کار
تفاوت **مجوز** (می‌تواند) با **وظیفه** (باید):
- هر وظیفه دارای SLA، Escalation، و زنجیرهٔ تأیید چندسطحی است.
- گردش‌کارهای تصویب با آستانهٔ مبلغ/درصد قابل تنظیم (`config/approvals.php`).
- ماتریس RACI برای فرایندهای کلیدی (Responsible/Accountable/Consulted/Informed).
- تفویض موقت با انقضای خودکار و ثبت در Audit.

---

## وابستگی‌ها

| سند | پیش‌نیاز |
|---|---|
| DOC-100 | DOC-057 (RBAC engine)، DOC-016 (Security) |
| DOC-101 | DOC-100، DOC-057، DOC-022 (Module Manifest) |
| DOC-102 | DOC-100، DOC-071 (Workflow engine)، DOC-057 |

## مسیر مطالعه

```
DOC-057 (RBAC engine) → DOC-100 (Roles) → DOC-101 (Permissions)
                                          → DOC-102 (Duties & Workflow)
```

## قواعد حاکم 🔒

1. **Deny by Default** — هیچ دسترسی بدون مجوز صریح نیست.
2. **Least Privilege** — حداقل مجوز لازم برای هر نقش.
3. **Separation of Duties (SoD)** — تفکیک author/approver/auditor.
4. **Four-Eyes** — تغییرات حساس با تأیید دوم.
5. **Time-Bound** — نقش‌های حساس موقت با انقضا.
6. **Auditable** — همهٔ تغییرات دسترسی در Audit Log ثبت می‌شوند.
7. **Reviewable** — بازبینی دوره‌ای دسترسی‌ها با `tvn rbac:review`.
