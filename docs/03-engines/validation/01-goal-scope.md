# DOC-080-S01 — هدف و دامنه (موتور validation)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-080-S01 |
| موتور | `validation` |
| بخش | ۱ — هدف و دامنه |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۱٫۱ هدف (Why)
موتور Validation اعتبارسنجی ورودی را با rules، FormRequest، DTO validator، RuleParser، Iranian checks و message bag فراهم می‌کند و پایهٔ امنیت ورودی است.

### ۱٫۲ دامنه (What)
- ✅ شامل: Validator، RuleParser، FormRequest، DtoValidator، built-in rules، IranianChecks (melli/card/iban)، MessageBag
- ❌ خارج از دامنه: Security sanitizing (در security)، ORM data casts (در orm)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-VAL-01 | پیاده‌سازی هستهٔ موتور validation به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-VAL-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-VAL-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Validation + Respect Validation | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

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
