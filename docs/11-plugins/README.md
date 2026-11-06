# DOC-180 — رجیستری افزونه‌ها (Plugin Registry)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-180 |
| نوع | شاخص (Index) |
| وضعیت | Draft v0.0.1 |

---

این سند فهرست رسمی افزونه‌های Tavaan است. هر افزونه پوشه‌ای با فایل‌های ممیزی عملیاتی است.
افزونه‌ها پلاگین‌های ثالث هستند که در `plugins/` نصب می‌شوند و از قاعدهٔ ZeroDependency **معاف** هستند.

| DOC-ID | افزونه | عنوان فارسی | نوع | فروشنده |
|---|---|---|---|---|
| DOC-181 | [ExampleAnalytics](./example-analytics/README.md) 🔌 | تحلیل نمونه | feature | tavaan.example |
| DOC-182 | [ExamplePaymentGateway](./example-payment-gateway/README.md) 🔌 | درگاه پرداخت نمونه | payment | tavaan.example |
| DOC-183 | [ExampleTheme](./example-theme/README.md) 🔌 | پوسته نمونه | theme | tavaan.example |
| DOC-184 | [ExampleSEO](./example-seo/README.md) 🔌 | سئو نمونه | feature | tavaan.example |

## قواعد افزونه‌ها 🔒

۱. هر افزونه باید `plugin.json` معتبر داشته باشد.
۲. امضای دیجیتال الزامی است (در صورت فعال بودن).
۳. Sandbox ایزوله برای بارگذاری.
۴. vendor افزونه باید در `allowed_plugin_vendors` باشد.
۵. قابلیت‌ها (capabilities) در زمان اجرا enforce می‌شوند.
