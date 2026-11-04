# DOC-074-S01 — هدف و دامنه (موتور search)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-074-S01 |
| موتور | `search` |
| بخش | ۱ — هدف و دامنه |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

### ۱٫۱ هدف (Why)
موتور Search جستجوی full-text را با drivers (PgSQL/MySQL/SQLite FTS/Meilisearch/Typesense/Native)، Searchable trait، highlight و Persian normalization فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: SearchManager، drivers (PgSQL/MySQL/SQLite/Meili/Typesense/Native)، Searchable، Highlighter، Persian normalization
- ❌ خارج از دامنه: ORM (در orm)، Database (در database)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-SEARCH-01 | پیاده‌سازی هستهٔ موتور search به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-SEARCH-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-SEARCH-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Scout + Meilisearch | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

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
