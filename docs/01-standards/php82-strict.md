# DOC-010 — قواعد PHP 8.2+ تَوان

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-010 |
| وضعیت | Approved v0.0.1 |
| نقش | قواعد اجباری PHP 8.2/8.3/8.4 |
| پیش‌نیاز | DOC-002 |

## حداقل نسخه

🔒 **PHP ≥ ۸.۲.۰** اجباری است. کد باید روی ۸.۲/۸.۳/۸.۴ بدون `E_DEPRECATED` اجرا شود.

```php
// core/bootstrap.php
if (PHP_VERSION_ID < 80200) {
    fwrite(STDERR, 'Tavaan requires PHP >= 8.2.0. Current: ' . PHP_VERSION . PHP_EOL);
    exit(1);
}
```

## قواعد اجباری

### 🔒 declare(strict_types=1)
هر فایل PHP باید با `declare(strict_types=1);` شروع شود.
**وضعیت Tavaan-Demo:** ⚠️ ۸۳ فایل نقض دارند (بیشتر در routes/, config/).

### 🔒 readonly classes (PHP 8.2+)
کلاس‌های Value Object باید `readonly` باشند یا propertyهای `readonly` داشته باشند.

### 🔒 Enum (PHP 8.1+)
به‌جای ثابت‌های ماژیک، از `enum` استفاده شود.
```php
enum Lifetime: string {
    case Singleton = 'singleton';
    case Transient = 'transient';
}
```

### 🔒 Match expression
به‌جای `switch` برای مقایسهٔ مقداری، از `match` استفاده شود.

### 🔒 Named arguments
در فراخوانی متدهای عمومی، named arguments مجاز است.

### 🔒 Union/Intersection types
برای تایپ‌های ترکیبی استفاده شود.

## ممنوعه‌ها (Deprecated)

| ممنوعه | جایگزین |
|---|---|
| `create_function()` | closure |
| `each()` | `foreach` |
| Property پویا (PHP 8.2 deprecation) | property typed یا `#[AllowDynamicProperties]` |
| `${var}` در رشته | `{$var}` |
| `utf8_encode/decode` | `mb_convert_encoding` |

## افزونه‌های PHP مورد‌نیار

| افزونه | کاربرد | Fallback |
|---|---|---|
| pdo | دیتابیس | — (اجباری) |
| mbstring | کاراکترهای چندبایتی | — (اجباری) |
| json | JSON | — (اجباری در 8.x) |
| hash | درهم‌سازی | — (اجباری) |
| openssl | رمزنگاری | — (توصیه‌شده) |
| curl | HTTP client | stream wrapper |
| sqlite3 | SQLite | — |
| dom, xml | XML پردازش | — |
