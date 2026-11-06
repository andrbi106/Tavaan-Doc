# DOC-004 — راهنمای شروع سریع تَوان 🚀

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-004 |
| وضعیت | Approved v0.0.1 |
| نقش | راهنمای عملی شروع |
| پیش‌نیاز | DOC-001, DOC-010 |



---

## 📚 خلاصهٔ ساده (برای انسان)

> **این سند چه می‌گوید؟**
> چگونه تَوان را نصب و اجرا کنید — در ۳ گام ساده.
>
> **تشبیه:** مثل خرید کتاب دستور پخت — اول کتاب را می‌خری، بعد مواد را آماده می‌کنی، بعد شروع به آشپزی می‌کنی.
>
> **برای کی؟** تازه‌کارها — این اولین سندی است که باید بخوانید.

---

## 🔧 مشخصات فنی

## پیش‌نیازها

- PHP ≥ ۸.۲ (تَوان با PHP 8.3.32 تست شده)
- هیچ پکیج‌منیجری نیاز نیست (ZeroDependency)

## نصب و اجرا

```bash
# ۱) کلون
# پس از نصب فریمورک تَوان:
cd tavaan-project

# ۲) فایل محیطی
cp .env.example .env

# ۲) اجرای سرور توسعه
php bin/tvn serve

# مرورگر: http://127.0.0.1:8000
```

## دستورات CLI

```bash
php bin/tvn info       # اطلاعات سیستم
php bin/tvn version    # نسخهٔ فریمورک
php bin/tvn engines    # لیست ۵۲ موتور
php bin/tvn config     # پیکربندی موتورها
php bin/tvn serve      # سرور توسعه
```

## Endpointهای HTTP

| مسیر | توضیحات |
|---|---|
| `GET /` | صفحهٔ خوش‌آمدگویی |
| `GET /api` | وضعیت سیستم (JSON) |
| `GET /engines` | جدول موتورها |
| `GET /info` | phpinfo() |

## ساختار پروژه

```
tavaan-project/
├── bin/tvn              # CLI entry point
├── public/index.php     # HTTP entry point
├── bootstrap.php        # bootstrap اپلیکیشن
├── core/                # هستهٔ صفر‌وابستگی
├── engine-core/         # والد موتورها
├── engines/             # ۵۲ موتور فرزند
├── config/              # پیکربندی
├── routes/              # مسیرها
├── resources/           # views, lang
├── storage/             # logs, cache
└── tavaan.json          # manifest پروژه
```

## ده فرمان کدنویسی (R1-R10)

```
R1  declare(strict_types=1); در هر فایل
R2  فقط Autoloader هسته (без require دستی)
R3  هیچ پکیج خارجی (ZeroDependency)
R4  بدون Property پویا
R5  هر خروجی عمومی = Interface
R6  هر موتور: Provider + Interface + Tests + Docs + Benchmark
R7  namespace از ریشهٔ ثبت‌شده
R8  خطا = استثنا با کد و MessageId
R9  Prepared Statement فقط
R10 php -l + PHPStan + تست + Benchmark قبل از Merge
```

## عیب‌یابی

| مشکل | راه‌حل |
|---|---|
| `PHP not found` | نصب PHP 8.2+ یا استفاده از باینری استاتیک |
| خطای Autoloader | بررسی `TVN_BASE_PATH` در `bootstrap.php` |
| 404 در `/` | اجرای `php bin/tvn serve` از ریشهٔ پروژه |
