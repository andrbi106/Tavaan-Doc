# DOC-124 — خلاصهٔ فازهای بنیاد (M0-M5) ✅

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-124 |
| وضعیت | Approved v0.0.1 |
| نقش | خلاصهٔ تفصیلی فازهای تکمیل‌شده |
| پیش‌نیاز | DOC-120 |

## فاز M0 — مستندات و معماری ✅

### هدف
ایجاد مستندات کامل به‌عنوان «نقشهٔ راه کدنویسی» که یک تیم یا ایجنت بتواند بدون ابهام پیاده‌سازی کند.

### خروجی‌ها
- ۷۳ سند Markdown
- ۵۳ سند موتور (۱۷بخشی)
- ۲ ADR
- manifest.json ماشین‌خوان
- Skill tavaan-doc-writer
- ۲ اسکریپت اعتبارسنج

### معیار پذیرش 🧪
- ✅ `verify_docs.py` بدون خطا
- ✅ همهٔ DOC-ID یکتا
- ✅ manifest.json معتبر

---

## فاز M1 — هستهٔ بنیاد ✅

### هدف
ایجاد دی‌آی کانتینر (درگاه ۱) و موتور سازگاری (Fallback).

### موتورها

#### container
- **Engine ID:** `tavaan.engine.container`
- **Namespace:** `Tavaan\Engine\Container`
- **LOC:** 1,577 (۲۰ فایل)
- **وابستگی:** هیچ
- **Facade:** `Container` → `container`
- **نقش:** DI Container با reflection-based auto-resolution
- **API کلیدی:**
  - `bind($abstract, $concrete, $shared)`
  - `singleton($abstract, $concrete)`
  - `make($abstract, $params)`
  - `call($callback, $params)`
  - `instance($abstract, $instance)`
  - `alias($abstract, $alias)`
  - `bound($abstract)`
  - `get($id)` / `has($id)` (ReadableContainerInterface)

#### compat
- **Engine ID:** `tavaan.engine.compat`
- **LOC:** 1,398 (۱۴ فایل)
- **نقش:** Polyfill و Fallback برای افزونه‌های PHP
- **مثال:** `ext-intl` نبود → پیاده‌سازی بومی PluralRules

### معیار پذیرش 🧪
- ✅ AC-M1-01: `php bin/tvn info` بدون وابستگی بوت می‌شود
- ✅ AC-M1-02: bind/make/singleton کار می‌کند
- ✅ AC-M1-03: resolve خودکار با Reflection

---

## فاز M2 — هستهٔ پیکربندی ✅

### هدف
پیکربندی، خط لوله میان‌افزار، و رجیستری ماژول.

### موتورها

#### config
- **LOC:** 1,314 (۲۰ فایل)
- **وابستگی:** container
- **نقش:** بارگذاری config از فایل‌ها + .env + ENV

#### pipeline
- **LOC:** 410 (۸ فایل)
- **وابستگی:** container
- **نقش:** خط لوله میان‌افزار (Request → Middleware[] → Response)

#### module
- **LOC:** 1,641 (۱۷ فایل)
- **وابستگی:** container, config
- **نقش:** رجیستری و کشف ماژول‌های HMVC

---

## فاز M3 — هستهٔ رویداد ✅

### هدف
سیستم رویداد (درگاه ۲)، چارچوب CLI، گزارش‌گیری، و مدیریت خطا.

### موتورها

#### event
- **LOC:** 1,222 (۱۵ فایل)
- **وابستگی:** container, config
- **نقش:** Pub/Sub Event Dispatcher
- **API:** `dispatch($event, $data)`, `listen($event, $listener)`

#### console
- **LOC:** 3,559 (۳۸ فایل)
- **وابستگی:** container, config
- **نقش:** چارچوب CLI با ۵ دستور فعال
- **دستورات:** `info`, `version`, `engines`, `config`, `serve`

#### log
- **LOC:** 1,409 (۲۸ فایل)
- **وابستگی:** config
- **نقش:** گزارش‌گیری چندسطحی (debug/info/warning/error)

#### error
- **LOC:** 992 (۱۴ فایل)
- **وابستگی:** config, log
- **نقش:** تبدیل خطا به استثنا + ماسک دادهٔ حساس

---

## فاز M4 — هستهٔ پشتیبان ✅

### هدف
رمزنگاری، درهم‌سازی، سامانه فایل، بین‌المللی‌سازی، و بهینه‌ساز.

### موتورها

#### crypt
- **LOC:** 905 (۱۵ فایل)
- **نقش:** رمزنگاری متقارن (AES-256-GCM)

#### hash
- **LOC:** 355 (۶ فایل)
- **نقش:** درهم‌سازی رمز عبور (bcrypt/argon2)

#### filesystem
- **LOC:** 2,248 (۱۹ فایل)
- **نقش:** سامانه فایل با درایور (local/ftp/s3)

#### i18n
- **LOC:** 1,227 (۱۱ فایل)
- **نقش:** ترجمه + جمع‌بندی + RTL

#### optimizer
- **LOC:** 397 (۳ فایل)
- **نقش:** cache config/route/view/event/autoload

---

## فاز M5 — موتور والد ✅

### هدف
کلاس پایه موتورها + EngineBus (درگاه ۳) + رجیستری با boot توپولوژیک.

### فایل‌ها (در engine-core/)

| فایل | نقش |
|---|---|
| `Engine.php` | کلاس پایه همهٔ موتورها |
| `EngineBus.php` | درگاه ۳: point-to-point RPC |
| `EngineRegistry.php` | boot توپولوژیک (مرتب‌سازی بر اساس وابستگی) |
| `EngineLoader.php` | کشف موتورها از filesystem |
| `EngineManifest.php` | ارزش‌شیء manifest |
| `EngineContext.php` | زمینهٔ اجرای موتور |
| `Contracts/EngineInterface.php` | قرارداد پایه |
| `Contracts/EngineBusInterface.php` | قرارداد درگاه ۳ |
| `Contracts/EngineRegistryInterface.php` | قرارداد رجیستری |
| `Contracts/EngineManifestInterface.php` | قرارداد manifest |

- **مجموع LOC:** 1,565

### API کلیدی EngineBus
```php
$result = $engineBus->call('auth', 'issue-token', ['user_id' => 42]);
```

### معیار پذیرش 🧪
- ✅ AC-M5-01: `php bin/tvn engines` همهٔ ۵۲ موتور را فهرست می‌کند
- ✅ AC-M5-02: boot توپولوژیک وابستگی‌ها را حل می‌کند
- ✅ AC-M5-03: EngineBus فراخوانی بین موتورها کار می‌کند
