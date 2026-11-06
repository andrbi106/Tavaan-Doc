# DOC-071-S01 — هدف و دامنه (موتور scaffold)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-071-S01 |
| موتور | `scaffold` |
| بخش | ۱ — هدف و دامنه |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۱٫۱ هدف (Why)
موتور Scaffold کدجنریتور CLI را با stubs، generators (Model/Controller/Migration/Resource/Policy/Test و…) و GeneratorManager فراهم می‌کند و شروع سریع پروژه را ممکن می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: ScaffoldEngine، GeneratorManager، Generators (Model/Controller/Migration/Test/...)، StubRenderer، Make commands
- ❌ خارج از دامنه: Admin CRUD (در admin)، Module (در module)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-SCAFFOLD-01 | پیاده‌سازی هستهٔ موتور scaffold به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-SCAFFOLD-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-SCAFFOLD-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Make + Artisan generators | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

---

## چک‌لیست ممیزی عملیاتی

- [ ] هدف (Why) در یک پاراگراف مشخص است
- [ ] دامنه (What) شامل/خارج از دامنه فهرست شده
- [ ] الزامات با FR-/NFR- ارجاع داده شده
- [ ] مقایسه با مراجع (Laravel/Symfony) انجام شده
- [ ] justification برای تغییرات ذکر شده

---

## وضعیت ممیزی

| شاخص | وضعیت |
|---|---|
| وضعیت محتوا | ✅ دارای محتوا |
| تعداد آیتم‌های چک‌لیست | 5 |
| نیاز به تکمیل | ✅ خیر |

---

## یادداشت‌های ممیزی‌کننده

> این بخش توسط ممیزی‌کننده پر می‌شود.

- **تاریخ ممیزی:** _TODO_
- **ممیزی‌کننده:** _TODO_
- **یادداشت:** _TODO_
