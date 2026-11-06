# تَوان | Tavaan — مرجع پیاده‌سازی فریمورک

> **مرجع رسمی پیاده‌سازی فریمورک تَوان (Tavaan)** — 
> نقشهٔ کامل معماری، استانداردها و مشخصات فنی برای 
> ایجنت‌های هوش مصنوعی و توسعه‌دهندگان انسانی.

این مخزن **مرجع پیاده‌سازی فریمورک تَوان** است. همهٔ فازها **برنامه‌ریزی‌شده** هستند و باید توسط ایجنت‌ها و جامعه پیاده‌سازی شوند.

---

## 🎯 هدف

پیاده‌سازی کامل فریمورک تَوان از صفر تا انتشار نسخهٔ ۱.۰.۰ — با ۴۵ فاز گام‌به‌گام.

---

## 👥 مخاطبان

| مخاطب | چه می‌کند | کجا |
|---|---|---|
| 🤖 **ایجنت هوش مصنوعی** | پیاده‌سازی موتورها و ماژول‌ها از مشخصات | `docs/03-engines/`, `docs/10-modules/` |
| 👨‍💻 **توسعه‌دهنده** | پیاده‌سازی، بازبینی، توسعه | همهٔ مستندات |
| 📚 **نویسنده کتاب** | نگارش کتاب آموزشی از مستندات | `docs/00-learn/`, `docs/examples/` |
| 🧒 **مبتدی / نوجوان** | یادگیری مفاهیم | `docs/00-learn/`, `docs/examples/` |

---

## 📖 شروع مطالعه

| شما کی هستید؟ | از کجا شروع کنید |
|---|---|
| نوجوان یا مبتدی | `docs/00-learn/for-beginners.md` |
| نویسنده کتاب | `docs/00-learn/preface.md` → `docs/00-learn/chapter-map.md` |
| ایجنت پیاده‌ساز | `docs/08-roadmap/agent-backlog.md` → `docs/03-engines/` |
| معمار | `docs/02-architecture/overview.md` → ADRها |

---

## هویت فریمورک

| ویژگی | مقدار |
|---|---|
| نام | تَوان / Tavaan |
| پروفایل رسمی | [TavaanOfficial](https://github.com/TavaanOfficial) |
| مخزن مستندات | [TavaanOfficial/Tavaan-Doc](https://github.com/TavaanOfficial/Tavaan-Doc) |
| شعار | صفر وابستگی، بی‌نهایت امکان / Zero Dependency. Infinite Capability. |
| نسخهٔ مشخصات | v1.0.0 |
| حداقل PHP | 8.2.0 |
| سیاست وابستگی | صفر وابستگی بیرونی (Zero External Dependency) |
| معماری‌ها | layered, hmvc, modular-monolith, event-driven, hexagonal |
| تعداد موتورها | ۵۲ (برنامه‌ریزی‌شده) |
| ADRها | ۱۶ (ADR-0001 تا ADR-0016) |
| CLI | ۱۰۵ دستور (مشخصات کامل) |
| Config | ۴۸ فایل پیکربندی + ۱۱۱ کلید ENV |

---

## نقشهٔ مستندات

```
docs/
├── README.md                      DOC-000 — شاخص ناوبری
├── manifest.json                  🧠 فهرست ماشین‌خوان
├── 00-overview/                   اهداف، اصول، الزامات، شروع سریع
│   ├── goals-vision.md            DOC-001
│   ├── principles.md              DOC-002
│   ├── requirements.md            DOC-003
│   └── quickstart.md              DOC-004
├── 01-standards/
│   ├── php82-strict.md            DOC-010
│   ├── coding-style.md            DOC-011
│   ├── naming-conventions.md      DOC-012
│   ├── error-handling.md          DOC-013
│   ├── contracts-interfaces.md    DOC-014
│   ├── documentation-standard.md  DOC-015
│   └── security-policy.md         DOC-016
├── 02-architecture/               معماری بر اساس پیاده‌سازی واقعی
│   ├── overview.md                DOC-020
│   ├── layered-hmvc.md            DOC-021
│   ├── modular-monolith.md        DOC-022
│   ├── event-driven.md            DOC-023
│   ├── request-lifecycle.md       DOC-025
│   ├── container-di.md            DOC-026
│   └── bootstrapping.md           DOC-027
├── 03-engines/                    ۵۲ موتور واقعی
│   ├── README.md                  DOC-030 — رجیستری
│   └── <name>.md                  DOC-031..082 — هر موتور
├── 04-structure/                  ساختار رسمی فریمورک
│   ├── folder-structure.md        DOC-083
│   ├── file-conventions.md        DOC-084
│   ├── cli-reference.md           DOC-085 — ۵ دستور واقعی
│   └── config-reference.md        DOC-086
├── 05-applications/               N/A v0.0.1
├── 06-roles-access/               N/A v0.0.1
├── 07-quality/
│   ├── testing-strategy.md        DOC-110
│   ├── definition-of-done.md      DOC-113
│   └── audit-report.md            گزارش ممیزی واقعی
├── 08-roadmap/
│   └── milestones.md              DOC-120 — وضعیت واقعی M0/M1
├── 09-references/
│   └── glossary.md                DOC-131
├── adr/                           ADRهای واقعی
│   ├── README.md                  DOC-140
│   ├── ADR-0004-zero-dependency.md
│   └── ADR-0005-custom-autoloader.md
├── schemas/                       JSON Schemaها
│   └── project.v1.json
└── templates/
    ├── engine-spec-template.md   DOC-150
    └── adr-template.md            DOC-152
skills/tavaan-doc-writer/          Skill اختصاصی (از مخزن مرجع)
tools/scripts/
├── verify_docs.py
└── audit_tavaan.py
```

---

## شروع سریع

```bash
git clone https://github.com/TavaanOfficial/Tavaan-Doc.git
cd Tavaan-Doc

# مطالعهٔ ترتیب اجباری:
# 1. docs/00-overview/goals-vision.md
# 2. docs/00-overview/quickstart.md
# 3. docs/01-standards/php82-strict.md
# 4. docs/02-architecture/overview.md
# 5. docs/03-engines/README.md
```

---

## قواعد طلایی (Hard Rules)

```
R1  هر فایل PHP با declare(strict_types=1); شروع می‌شود.
R2  هیچ require/include دستی در کد کاربردی؛ فقط Autoloader هسته.
R3  هیچ پکیج خارجی در core/ و engines/ ممنوع است (ZeroDependency).
R4  هیچ Property پویا.
R5  هر خروجی عمومی باید Interface داشته باشد.
R6  هر موتور: Provider + Interface + Tests + Docs + Benchmark.
R7  نام namespace فقط از ریشهٔ ثبت‌شده.
R8  خطاها استثنا هستند با کد عددی و MessageId.
R9  هیچ کوئری با الحاق رشته.
R10 قبل از Merge: php -l + PHPStan + تست‌ها + Benchmark.
```

---

## وضعیت فاز (۴۵ فاز، M0-M44، نسخه 0.0.0 تا 1.0.0)

فازها بر اساس **لایه‌بندی موتورها** در `DEPENDENCIES.md` طراحی شده‌اند.
هر لایه با نسخه همسو است: L0→0.0.x, L1→0.1.x, ..., Release→1.0.0.
قواعد نسخه‌گذاری در `docs/08-roadmap/version-progression.md`.

| فاز | لایه | نسخه | موتورها | وضعیت مشخصات |
|---|---|---|---|---|
| **M0** | — | 0.0.0 | مستندات | 📋 برنامه‌ریزی‌شده |
| **M1-M2** | L0 | 0.0.1-0.0.2 | container, compat, test | 📋 برنامه‌ریزی‌شده |
| **M3** | L1 | 0.1.1 | config, pipeline | 📋 برنامه‌ریزی‌شده |
| **M4-M10** | L2 | 0.2.1-0.2.7 | event, crypt, hash, filesystem, i18n, log, cache, console, module, ... | 📋 برنامه‌ریزی‌شده |
| **M11-M17** | L3 | 0.3.1-0.3.7 | database, error, http, view, validation, jalali, queue, mail, ... | 📋 برنامه‌ریزی‌شده |
| **M18-M25** | L4 | 0.4.1-0.4.8 | orm, schema, migration, cookie, cors, session, router, ... | 📋 برنامه‌ریزی‌شده |
| **M26-M29** | L5 | 0.5.1-0.5.4 | auth, rbac, security, realtime | 📋 برنامه‌ریزی‌شده |
| **M30-M32** | L6 | 0.6.1-0.6.3 | api, workflow, admin | 📋 برنامه‌ریزی‌شده |
| **M33-M35** | App | 0.7.1-0.7.3 | Blog, News-Portal, Forum | 📋 برنامه‌ریزی‌شده |
| **M36-M38** | App | 0.8.1-0.8.3 | Shop (۲ فاز), LMS | 📋 برنامه‌ریزی‌شده |
| **M39-M43** | App | 0.9.1-0.9.5 | CRM, ERP (۲ فاز), BPMS (۲ فاز) | 📋 برنامه‌ریزی‌شده |
| **M44** | Release | 1.0.0 | انتشار فریمورک | 📋 هدف نهایی |

**نسخهٔ مشخصات:** v1.0.0 (مشخصات کامل فریمورک — پیاده‌سازی توسط جامعه)

**مستندات مرتبط:**
- `docs/08-roadmap/version-progression.md` — قواعد نسخه‌گذاری و همسویی با لایه‌ها
- `docs/08-roadmap/milestones.md` — جدول کامل ۴۵ فاز
- `docs/08-roadmap/phase-audit.md` — ممیزی فایل‌های هر فاز بر اساس لایه
- `docs/08-roadmap/phase-dependencies.md` — گراف وابستگی + قواعد هماهنگی
- `docs/08-roadmap/agent-backlog.md` — بک‌لاگ تیکت‌های ایجنت

---

## مجوز

MIT
