# شاخص مستندات تَوان (Tavaan Docs Index)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-000 |
| وضعیت | Approved v0.0.1 |
| نقش | نقطهٔ ورود رسمی و نمای ناوبری همهٔ مستندات |
| منبع | بازنویسی از Derogaramin/Tavaan-Doc بر اساس Tavaan-Demo واقعی |

## راهنمای نمادها

| نماد | معنا |
|---|---|
| 🔒 | الزامی (MUST) — نقض = ریجکت |
| ⚠️ | توصیهٔ قوی (SHOULD) |
| 💡 | اختیاری (MAY) |
| 🧪 | دارای معیار تست/پذیرش |
| 🧠 | دارای بلوک ماشین‌خوان |

---

## جدول کامل اسناد

| DOC-ID | سند | مسیر | نوع |
|---|---|---|---|
| DOC-000 | شاخص | `docs/README.md` | فهرست |
| DOC-001 | اهداف و چشم‌انداز | `docs/00-overview/goals-vision.md` | تحلیلی |
| DOC-002 | اصول بنیادین | `docs/00-overview/principles.md` | تحلیلی |
| DOC-003 | الزامات | `docs/00-overview/requirements.md` | تحلیلی 🧪 |
| DOC-004 | شروع سریع | `docs/00-overview/quickstart.md` | راهنما 🧠 |
| DOC-010 | قواعد PHP 8.2+ | `docs/01-standards/php82-strict.md` | استاندارد 🔒 |
| DOC-011 | سبک کد | `docs/01-standards/coding-style.md` | استاندارد 🔒 |
| DOC-012 | نام‌گذاری | `docs/01-standards/naming-conventions.md` | استاندارد 🔒 |
| DOC-013 | مدیریت خطا | `docs/01-standards/error-handling.md` | استاندارد 🔒 |
| DOC-014 | کاتالوگ قراردادها | `docs/01-standards/contracts-interfaces.md` | مرجع 🔒 |
| DOC-015 | استاندارد مستندسازی | `docs/01-standards/documentation-standard.md` | استاندارد |
| DOC-016 | سیاست امنیتی | `docs/01-standards/security-policy.md` | استاندارد 🔒 |
| DOC-020 | نمای کلان معماری | `docs/02-architecture/overview.md` | معماری |
| DOC-021 | لایه‌ای + HMVC | `docs/02-architecture/layered-hmvc.md` | معماری 🔒 |
| DOC-022 | ماژولار مونولیت | `docs/02-architecture/modular-monolith.md` | معماری 🔒 |
| DOC-023 | رویداد‌محور | `docs/02-architecture/event-driven.md` | معماری 🔒 |
| DOC-025 | چرخهٔ عمر درخواست | `docs/02-architecture/request-lifecycle.md` | معماری 🔒 |
| DOC-026 | کانتینر و DI | `docs/02-architecture/container-di.md` | معماری 🔒 |
| DOC-027 | راه‌اندازی و Autoload | `docs/02-architecture/bootstrapping.md` | معماری 🔒 |
| DOC-030 | رجیستری موتورها | `docs/03-engines/README.md` | مرجع 🔒 🧠 |
| DOC-031..082 | مستند هر موتور | `docs/03-engines/*.md` | مشخصات 🔒 🧪 |
| DOC-080 | ساختار پوشه/فایل | `docs/04-structure/folder-structure.md` | مرجع 🔒 |
| DOC-081 | قرارداد فایل‌ها | `docs/04-structure/file-conventions.md` | استاندارد 🔒 |
| DOC-083 | مرجع CLI | `docs/04-structure/cli-reference.md` | مرجع 🔒 |
| DOC-085 | مرجع پیکربندی | `docs/04-structure/config-reference.md` | مرجع 🔒 |
| DOC-110 | استراتژی تست | `docs/07-quality/testing-strategy.md` | استاندارد 🔒 |
| DOC-113 | تعریف انجام‌شده | `docs/07-quality/definition-of-done.md` | استاندارد 🔒 |
| DOC-120 | نقشهٔ راه | `docs/08-roadmap/milestones.md` | برنامه |
| DOC-131 | واژه‌نامه | `docs/09-references/glossary.md` | مرجع |
| DOC-140 | شاخص ADR | `docs/adr/README.md` | تصمیم 🔒 |
| DOC-150 | قالب مستند موتور | `docs/templates/engine-spec-template.md` | قالب |
| DOC-152 | قالب ADR | `docs/templates/adr-template.md` | قالب |

---

## مسیرهای مطالعه

### ایجنت پیاده‌ساز موتور
```
DOC-010 → DOC-011 → DOC-012 → DOC-030 → <engine-doc> → DOC-110 → DOC-113
```

### ایجنت معمار
```
DOC-001 → DOC-002 → DOC-020 → DOC-021 → DOC-022 → DOC-023 → DOC-027 → ADRs
```

### بازبین کیفیت
```
DOC-010 → DOC-016 → DOC-110 → DOC-113 → audit-report
```

---

## قواعد حاکم

1. 🔒 **منبع یگانهٔ حقیقت (SSOT):** اگر کد با سند در تضاد باشد، ابتدا سند اصلاح می‌شود.
2. 🔒 **شناسه‌پذیری:** هر الزام دارای شناسه است.
3. ⚠️ **بدون ابهام:** واژه‌های «باید/نباید» با RFC 2119: MUST/SHOULD/MAY.
4. ⚠️ **قابل‌اجرا:** هر سند موتور دارای «معیار پذیرش» است.
5. 💡 **دوزبانه:** توضیحات فارسی، شناسه‌های فنی لاتین.
