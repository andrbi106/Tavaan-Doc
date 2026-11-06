# DOC-030 — رجیستری موتورها (Engine Registry)

این سند فهرست رسمی ۵۲ موتور Tavaan است. هر موتور در `engines/<name>/` قرار دارد و مستندات کامل آن در پوشهٔ `docs/03-engines/<name>/` شامل **۱۸ فایل ممیزی عملیاتی** (README + ۱۷ بخش) است. هر فایل دارای شناسهٔ یکتای `DOC-XXX-SNN` است.

| DOC-ID | Engine | عنوان فارسی | Namespace | اولویت | فاز | وابستگی سخت | Facade |
|---|---|---|---|---|---|---|---|
| DOC-031 | [Admin](./admin/README.md) | پیشخان و CRUD Generator | `Tavaan\Engine\Admin\` | P2 | M8 | view, rbac, orm, validation, http | `Admin` |
| DOC-032 | [API](./api/README.md) | لایهٔ API | `Tavaan\Engine\Api\` | P0 | M2 | config, http | `—` |
| DOC-033 | [Audit](./audit/README.md) | ممیزی | `Tavaan\Engine\Audit\` | P0 | M4 | event, log, crypt, config | `Audit` |
| DOC-034 | [Auth](./auth/README.md) | احراز هویت | `Tavaan\Engine\Auth\` | P0 | M4 | session, hash, crypt, event, database, cache, config | `Auth` |
| DOC-035 | [Backup](./backup/README.md) | پشتیبان‌گیری | `Tavaan\Engine\Backup\` | P1 | M5 | config, filesystem | `Backup` |
| DOC-036 | [Cache](./cache/README.md) | حافظه نهان | `Tavaan\Engine\Cache\` | P1 | M5 | config, event | `Cache` |
| DOC-037 | [Compat](./compat/README.md) | سازگاری و Polyfill | `Tavaan\Engine\Compat\` | P0 | M1 | — | `—` |
| DOC-038 | [Config](./config/README.md) | پیکربندی و محیط | `Tavaan\Engine\Config\` | P0 | M1 | container | `Config` |
| DOC-039 | [Console](./console/README.md) | چارچوب CLI | `Tavaan\Engine\Console\` | P0 | M1 | container, config | `—` |
| DOC-040 | [Container](./container/README.md) | ظرف سرویس (DI) | `Tavaan\Engine\Container\` | P0 | M1 | — | `App` |
| DOC-041 | [Cookie](./cookie/README.md) | کوکی رمزنگاری‌شده | `Tavaan\Engine\Http\Cookie\` | P0 | M2 | http, crypt | `Cookie` |
| DOC-042 | [CORS](./cors/README.md) | مدیریت CORS | `Tavaan\Engine\Http\Cors\` | P0 | M2 | http, config | `—` |
| DOC-043 | [Crypt](./crypt/README.md) | رمزنگاری | `Tavaan\Engine\Crypt\` | P0 | M4 | config | `Crypt` |
| DOC-044 | [Database](./database/README.md) | دیتابیس | `Tavaan\Engine\Database\` | P0 | M3 | config, event, log | `DB` |
| DOC-045 | [Error](./error/README.md) | مدیریت خطا | `Tavaan\Engine\Error\` | P0 | M1 | config, log | `—` |
| DOC-046 | [Event](./event/README.md) | رویداد و Outbox | `Tavaan\Engine\Event\` | P0 | M1 | container, config | `Event` |
| DOC-047 | [FeatureFlag](./feature-flag/README.md) | پرچم قابلیت | `Tavaan\Engine\FeatureFlag\` | P2 | M7 | config | `Feature` |
| DOC-048 | [Filesystem](./filesystem/README.md) | سامانه فایل | `Tavaan\Engine\Filesystem\` | P1 | M5 | config | `Storage` |
| DOC-049 | [Hash](./hash/README.md) | هش رمز عبور | `Tavaan\Engine\Hash\` | P0 | M4 | config | `Hash` |
| DOC-050 | [Http](./http/README.md) | HTTP | `Tavaan\Engine\Http\` | P0 | M2 | pipeline, event, error, config | `Http` |
| DOC-051 | [HttpClient](./http-client/README.md) | کلاینت HTTP | `Tavaan\Engine\HttpClient\` | P1 | M5 | config, event | `Http` |
| DOC-052 | [I18n](./i18n/README.md) | بین‌المللی‌سازی | `Tavaan\Engine\I18n\` | P0 | M2 | config | `Lang` |
| DOC-053 | [Jalali](./jalali/README.md) | تقویم جلالی | `Tavaan\Engine\I18n\Jalali\` | P0 | M2 | i18n | `—` |
| DOC-054 | [Log](./log/README.md) | گزارش ساختاریافته | `Tavaan\Engine\Log\` | P0 | M1 | config | `Log` |
| DOC-055 | [Mail](./mail/README.md) | پست الکترونیک | `Tavaan\Engine\Mail\` | P1 | M5 | config, event | `Mail` |
| DOC-056 | [Media](./media/README.md) | آپلود و پردازش رسانه | `Tavaan\Engine\Media\` | P1 | M5 | config | `Media` |
| DOC-057 | [Migration](./migration/README.md) | مهاجرت دیتابیس | `Tavaan\Engine\Database\Migration\` | P0 | M3 | database, schema, console | `—` |
| DOC-058 | [Module](./module/README.md) | کشف و مدیریت ماژول | `Tavaan\Engine\Module\` | P0 | M1 | container, config | `—` |
| DOC-059 | [Notification](./notification/README.md) | آگاه‌سازی | `Tavaan\Engine\Notification\` | P1 | M5 | config, event | `Notification` |
| DOC-060 | [Observability](./observability/README.md) | رصدپذیری | `Tavaan\Engine\Observability\` | P1 | M5 | config, log | `Metrics` |
| DOC-061 | [Optimizer](./optimizer/README.md) | بهینه‌سازی | `Tavaan\Engine\Optimizer\` | P0 | M1 | config, console | `—` |
| DOC-062 | [ORM](./orm/README.md) | نگاشت شیء-رابطه | `Tavaan\Engine\Database\ORM\` | P0 | M3 | database, event | `—` |
| DOC-063 | [Payment](./payment/README.md) | پرداخت | `Tavaan\Engine\Payment\` | P2 | M7 | config | `Payment` |
| DOC-064 | [Pipeline](./pipeline/README.md) | خط لوله | `Tavaan\Engine\Pipeline\` | P0 | M1 | container | `—` |
| DOC-065 | [Plugin](./plugin/README.md) | افزونهٔ ثالث (sandbox + امضا) | `Tavaan\Engine\Plugin\` | P2 | M6 | module, filesystem, crypt | `Plugin` |
| DOC-066 | [Queue](./queue/README.md) | صف و Worker | `Tavaan\Engine\Queue\` | P1 | M5 | config, event | `Queue` |
| DOC-067 | [RBAC](./rbac/README.md) | نقش و کنترل دسترسی | `Tavaan\Engine\Rbac\` | P0 | M4 | auth, database, cache, event, config | `Gate` |
| DOC-068 | [Realtime](./realtime/README.md) | بلادرنگ | `Tavaan\Engine\Realtime\` | P0 | M2 | config, event, http | `—` |
| DOC-069 | [Report](./report/README.md) | گزارش‌ساز | `Tavaan\Engine\Report\` | P2 | M7 | config | `Report` |
| DOC-070 | [Router](./router/README.md) | مسیریاب Compiled Trie | `Tavaan\Engine\Http\Routing\` | P0 | M2 | http, container, config | `Route` |
| DOC-071 | [Scaffold](./scaffold/README.md) | تولید کد (make:*) | `Tavaan\Engine\Scaffold\` | P2 | M6 | console, filesystem | `—` |
| DOC-072 | [Schedule](./schedule/README.md) | زمان‌بندی | `Tavaan\Engine\Schedule\` | P1 | M5 | config, console | `Schedule` |
| DOC-073 | [Schema](./schema/README.md) | ساختار دیتابیس | `Tavaan\Engine\Database\Schema\` | P0 | M3 | database | `Schema` |
| DOC-074 | [Search](./search/README.md) | جست‌وجوی Full-Text | `Tavaan\Engine\Search\` | P0 | M3 | config | `—` |
| DOC-075 | [Security](./security/README.md) | امنیت عرضی (CSRF/RateLimit/Sanitizer/SSRF) | `Tavaan\Engine\Security\` | P0 | M4 | http, crypt, cache, config | `Security` |
| DOC-076 | [Session](./session/README.md) | نشست | `Tavaan\Engine\Session\` | P0 | M2 | http, crypt, config | `Session` |
| DOC-077 | [Tenancy](./tenancy/README.md) | چنداجاره‌ای | `Tavaan\Engine\Tenancy\` | P2 | M6 | config | `Tenant` |
| DOC-078 | [Test](./test/README.md) | چارچوب تست | `Tavaan\Testing\` | P2 | M6 | — | `—` |
| DOC-079 | [Upgrade](./upgrade/README.md) | ارتقای نسخه | `Tavaan\Engine\Upgrade\` | P2 | M8 | console, database, filesystem | `—` |
| DOC-080 | [Validation](./validation/README.md) | اعتبارسنجی | `Tavaan\Engine\Validation\` | P0 | M3 | i18n, config | `Validator` |
| DOC-081 | [View](./view/README.md) | قالب‌ساز | `Tavaan\Engine\View\` | P0 | M2 | event, i18n, config | `View` |
| DOC-082 | [Workflow](./workflow/README.md) | گردش‌کار | `Tavaan\Engine\Workflow\` | P2 | M7 | config | `Workflow` |

**مجموع:** 52 موتور | **فایل‌های نوشته‌شده:** 52

