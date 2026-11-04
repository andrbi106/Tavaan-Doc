# تَوان | Tavaan — مستندات (Tavaan-Doc)

> مخزن مستندات فریمورک تَوان — بازنویسی با محتوای واقعی پروژه Tavaan-Demo.

این مخزن حاصل مطالعهٔ کامل مخزن مرجع `Derogaramin/Tavaan-Doc` و بازنویسی مستندات بر اساس **وضعیت واقعی** پروژه `andrbi106/Tavaan-Demo` (نسخهٔ ۰.۰.۱) است.

---

## تفاوت با مخزن مرجع

| ویژگی | مرجع (Derogaramin/Tavaan-Doc) | این مخزن (andrbi106/Tavaan-Doc) |
|---|---|---|
| منبع محتوا | طراحی تئوریک (فاز M0) | پروژهٔ واقعی Tavaan-Demo v0.0.1 |
| تعداد موتورها | ۵۳ (طراحی‌شده) | ۵۲ (پیاده‌سازی‌شده) |
| وضعیت اجرا | طراحی | اجراشونده (CLI + HTTP) |
| ADRها | ۱۶ (طراحی) | بر اساس تصمیمات واقعی |
| CLI | ۱۰۵ دستور (طراحی) | ۵ دستور (پیاده‌سازی‌شده) |
| Config | ۴۸ فایل (طراحی) | فایل‌های واقعی موجود |

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
├── 04-structure/                  ساختار واقعی Tavaan-Demo
│   ├── folder-structure.md        DOC-080
│   ├── file-conventions.md        DOC-081
│   ├── cli-reference.md           DOC-083 — ۵ دستور واقعی
│   └── config-reference.md        DOC-085
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
git clone https://github.com/andrbi106/Tavaan-Doc.git
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

## وضعیت فاز (۲۶ فاز تفکیک‌شده M0-M25)

برای جلوگیری از کد اسپاگتی و هماهنگی بهتر، فازها از ۱۰ به **۲۶** افزایش یافتند.
جزئیات کامل در `docs/08-roadmap/milestones.md`.

| فاز | نام | موتورها | وضعیت |
|---|---|---|---|
| **M0** | مستندات و معماری | — | ✅ کامل |
| **M1** | هستهٔ بنیاد | container, compat | ✅ کامل |
| **M2** | هستهٔ پیکربندی | config, pipeline, module | ✅ کامل |
| **M3** | هستهٔ رویداد | event, console, log, error | ✅ کامل |
| **M4** | هستهٔ پشتیبان | crypt, hash, filesystem, i18n, optimizer | ✅ کامل |
| **M5** | موتور والد | engine-core | ✅ کامل |
| **M6** | HTTP بنیاد | http | ⚠️ اسکلت |
| **M7** | مسیریابی | router | ⚠️ اسکلت |
| **M8** | وب پشتیبان | session, cookie, cors | ⚠️ اسکلت |
| **M9** | نما و i18n | view, jalali | ⚠️ اسکلت |
| **M10** | دیتابیس | database | ⚠️ اسکلت |
| **M11** | طرح و مهاجرت | schema, migration | ⚠️ اسکلت |
| **M12** | ORM | orm | ⚠️ اسکلت |
| **M13** | اعتبارسنجی و جستجو | validation, search | ⚠️ اسکلت |
| **M14** | کش و صف | cache, queue, schedule | ⚠️ اسکلت |
| **M15** | احراز هویت | auth | ⚠️ اسکلت |
| **M16** | RBAC و امنیت | rbac, security, audit | ⚠️ اسکلت |
| **M17** | نامه و اطلاع‌رسانی | mail, notification | ⚠️ اسکلت |
| **M18** | رسانه و HTTP-Client | media, http-client | ⚠️ اسکلت |
| **M19** | رصدپذیری و پشتیبان | observability, backup | ⚠️ اسکلت |
| **M20** | چنداجاره‌ای و پرچم | tenancy, feature-flag | ⚠️ اسکلت |
| **M21** | API و Realtime | api, realtime | ⚠️ اسکلت |
| **M22** | دامنه | workflow, report, payment | ⚠️ اسکلت |
| **M23** | ابزارسازی | scaffold, admin, plugin | ⚠️ اسکلت |
| **M24** | QA و ارتقا | test, upgrade | ⚠️ اسکلت |
| **M25** | اپلیکیشن‌ها و انتشار | Blog/Shop/ERP/... | ⬜ آینده |

**مستندات مرتبط:**
- `docs/08-roadmap/milestones.md` — جدول کامل فازها
- `docs/08-roadmap/phase-audit.md` — ممیزی فایل‌های هر فاز
- `docs/08-roadmap/phase-dependencies.md` — گراف وابستگی + قواعد هماهنگی
- `docs/08-roadmap/agent-backlog.md` — بک‌لاگ تیکت‌های ایجنت

---

## مجوز

MIT
