# DOC-070-S01 — هدف و دامنه (موتور router)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-070-S01 |
| موتور | `router` |
| بخش | ۱ — هدف و دامنه |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۱٫۱ هدف (Why)
موتور Router مسیریابی HTTP را با تعریف route، group، middleware binding، parameter، named routes و resource controllers فراهم می‌کند و پایهٔ dispatching است.

### ۱٫۲ دامنه (What)
- ✅ شامل: Router، Route collection، Group/Middleware binding، Parameters، Named routes، Resource
- ❌ خارج از دامنه: HTTP kernel (در http)، CORS (در cors)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-ROUTER-01 | پیاده‌سازی هستهٔ موتور router به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-ROUTER-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-ROUTER-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Router + Symfony Routing | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

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
