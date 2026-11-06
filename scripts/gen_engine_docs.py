#!/usr/bin/env python3
"""Generate 52 Tavaan engine documentation files."""
import json
import os
import re
from pathlib import Path

ENGINES_DIR = "/home/z/my-project/workspace/Tavaan-Demo/engines"
OUT_DIR = "/home/z/my-project/workspace/Tavaan-Doc-new/docs/03-engines"
os.makedirs(OUT_DIR, exist_ok=True)

ENGINES = [
    "admin", "api", "audit", "auth", "backup", "cache", "compat", "config",
    "console", "container", "cookie", "cors", "crypt", "database", "error",
    "event", "feature-flag", "filesystem", "hash", "http", "http-client",
    "i18n", "jalali", "log", "mail", "media", "migration", "module",
    "notification", "observability", "optimizer", "orm", "payment", "pipeline",
    "plugin", "queue", "rbac", "realtime", "report", "router", "scaffold",
    "schedule", "schema", "search", "security", "session", "tenancy", "test",
    "upgrade", "validation", "view", "workflow"
]
assert len(ENGINES) == 52

PHASE_MAP = {
    "container": "M1", "config": "M1", "event": "M1", "error": "M1",
    "log": "M1", "console": "M1", "pipeline": "M1", "compat": "M1",
    "optimizer": "M1", "module": "M1",
    "http": "M2", "router": "M2", "session": "M2", "cookie": "M2",
    "view": "M2", "api": "M2", "realtime": "M2", "cors": "M2",
    "database": "M3", "schema": "M3", "migration": "M3", "orm": "M3",
    "validation": "M3", "search": "M3", "pagination": "M3",
    "crypt": "M4", "hash": "M4", "auth": "M4", "rbac": "M4", "audit": "M4",
    "security": "M4",
    "cache": "M5", "queue": "M5", "schedule": "M5", "filesystem": "M5",
    "http-client": "M5", "mail": "M5", "notification": "M5",
    "observability": "M5", "backup": "M5", "media": "M5",
    "i18n": "M2", "jalali": "M2",
    "workflow": "M7", "report": "M7", "payment": "M7", "feature-flag": "M7",
    "scaffold": "M6", "admin": "M8", "plugin": "M6", "test": "M6",
    "upgrade": "M8", "tenancy": "M6",
}

P0 = {"container", "config", "event", "error", "log", "console", "pipeline",
      "compat", "optimizer", "module", "http", "router", "session", "cookie",
      "view", "api", "realtime", "cors", "database", "schema", "migration",
      "orm", "validation", "search", "crypt", "hash", "auth", "rbac", "audit",
      "security", "i18n", "jalali"}
P1 = {"cache", "queue", "schedule", "filesystem", "http-client", "mail",
      "notification", "observability", "backup", "media"}

def priority(name):
    if name in P0:
        return "P0"
    if name in P1:
        return "P1"
    return "P2"

META = {
    "admin": ("موتور Admin پیشخان (dashboard) و سازندهٔ CRUD اعلامی (declarative) ارائه می‌دهد که با تعریف منابع در فایل manifest، فرم‌ها، جداول، نماهای نمایش و نمودارهای SVG را به‌صورت خودکار با پشتیبانی RTL و تم ظاهری تولید می‌کند. این موتور امکان ساخت پنل‌های مدیریتی یکپارچه فارسی را بدون نیاز به کدنویسی تکراری فراهم می‌کند.", "ساخت منابع CRUD اعلامی، منوی پویا با فیلتر دسترسی، ویجت و نمودار داشبورد، ۲۷ نوع فیلد، sanitizer برای richtext، jalali_date دوطرفه", "مدیریت نقش‌ها (در موتور rbac)، احراز هویت (در موتور auth)", "ADMIN", "Filament/Laravel Nova"),
    "api": ("موتور API لایهٔ ساخت و تبدیل پاسخ‌های JSON را برای APIهای نسخه‌دار فراهم می‌کند و شامل JsonResource با شرط‌های when/whenLoaded، صفحه‌بندی، Idempotency-Key، Throttle و سازندهٔ OpenAPI 3.1 خودنوشته است. این موتور استانداردهای مدرن API (RFC 9457، Deprecation/Sunset) را پیاده می‌کند.", "JsonResource، نسخه‌بندی API (URL/Header/Query)، Idempotency-Key، Throttle نام‌دار، OpenAPI 3.1 generator، صفحه‌بندی", "احراز هویت API (در auth)، مسیریابی پایه (در router)", "API", "Laravel API Resources + Spatie"),
    "audit": ("موتور Audit رخدادهای امنیتی و عملیاتی سیستم را به‌صورت ساختاریافته، رمزنگاری‌شده و قابل پرس‌وجو ثبت می‌کند تا accountability و traceability کامل برای تراکنش‌ها فراهم شود. این موتور برای انطباق با الزامات ممیزی و تحلیل‌های انشعابی استفاده می‌شود.", "ثبت لاگ ممیزی در جدول tvn_audit_logs، رمزنگاری فیلدهای حساس، پرس‌وجو و فیلتر رویدادها، اتصال به event و log", "لاگ‌های سیستم عمومی (در log)، ردیابی توزیع‌شده (در observability)", "AUDIT", "Laravel Auditing / spatie/laravel-activitylog"),
    "auth": ("موتور Auth احراز هویت چندگاردی (session و JWT خودنوشته)، چرخش توکن refresh با تشخیص استفاده مجدد، OTP یک‌بارمصرف، TOTP RFC 6238، ردیابی دستگاه و تأیید دومرحله‌ای را مدیریت می‌کند. این موتور پایهٔ امنیت شناسایی کاربران Tavaan را تشکیل می‌دهد.", "Guardهای session و JWT، refresh rotation، OTP و TOTP، ردیابی دستگاه، Password broker، Two-Factor", "مدیریت نقش و مجوز (در rbac)، CSRF و Rate-limit عمومی (در security)", "AUTH", "Laravel Sanctum + Passport"),
    "backup": ("موتور Backup پشتیبان‌گیری از پایگاه‌داده و فایل‌ها را با dump خالص PHP (بدون mysqldump)، ZIP خودنوشته (ZipWriterPure)، رمزنگاری AES-256-GCM با کلید جدا از APP_KEY، verify و restore در حالت نگهداری فراهم می‌کند. retention و prune خودکار نیز پشتیبانی می‌شود.", "DB dump خالص PHP، ZIP خالص، رمزنگاری AES-256-GCM، verify، restore، retention/prune، دستورات کنسول backup:*", "ذخیره‌سازی اشیاء (در filesystem)، صف بندی وظایف (در queue)", "BACKUP", "spatie/laravel-backup"),
    "cache": ("موتور Cache لایهٔ caching یکپارچه با چندین store (Array، File، Database، Redis، Memcached، APCu)، tagged cache، قفل‌های توزیع‌شده (Locks) و دستورات مدیریت را فراهم می‌کند. این موتور با مدیریت یکپارچه Repository به‌عنوان facade عمل می‌کند.", "Storeهای Array/File/Database/Redis/Memcached/APCu، TaggedCache، Locks، دستور cache:clear", "صف (در queue)، session (در session)", "CACHE", "Laravel Cache + Symfony Cache"),
    "compat": ("موتور Compat لایهٔ سازگاری برای جبران نبود افزونه‌های PHP (ext-intl، ext-zip، ext-mbstring) را در محیط‌های محدود ارائه می‌دهد و شامل پیاده‌سازی خالص PHP برای UTF-8، Decimal، ZipWriter و MagicBytes است. این موتور قابلیت اجرای Tavaan در hostingهای اشتراکی را تضمین می‌کند.", "Utf8 خالص، Decimal، ZipWriterPure، MagicBytesDetector، دستور doctor، تابع compat()", "بهینه‌سازی عملکرد (در optimizer)، رمزنگاری (در crypt)", "COMPAT", "symfony/polyfill-*"),
    "config": ("موتور Config بارگذاری، ادغام، اعتبارسنجی schema و کش پیکربندی را از منابع چندگانه (فایل، env، cache) مدیریت می‌کند و Repository immutable با پشتیبانی frozen mode ارائه می‌دهد. این موتور هستهٔ پیکربندی Tavaan است.", "ConfigLoader، EnvLoader و EnvRepository، SchemaValidator، ConfigCacher، Repository، فایل‌های کمکی", "متغیرهای محیط (در env مستقل)، کش برنامه (در cache)", "CONFIG", "Laravel Config + Symfony Config"),
    "console": ("موتور Console زیرساخت CLI را با تعریف دستورات، آرگومان‌ها، گزینه‌ها، رنگ‌آمیزی ANSI و خروجی جدولی فراهم می‌کند و پایهٔ اجرای همه دستورات `php bin/tvn` را تشکیل می‌دهد.", "Command registry، Argument/Option parsing، ANSI output، Table renderer، Schedule integration", "زمان‌بندی (در schedule)، تست‌های CLI (در test)", "CONSOLE", "Symfony Console"),
    "container": ("موتور Container هستهٔ DI Container با auto-wiring، bindingهای contextual، scoping، lazy proxies، reflection cache و مدیریت وابستگی‌های حلقوی است. این موتور ستون فقرات Tavaan است و همه سرویس‌ها از آن resolve می‌شوند.", "Auto-wiring، Contextual bindings، Scope/Lifetime، LazyProxy، ReflectionCache، ContainerStats، Binding resolution", "رویدادها (در event)، پیکربندی (در config)", "CONTAINER", "Laravel Container + PSR-11"),
    "cookie": ("موتور Cookie مدیریت کوکی‌های رمزنگاری‌شده، امضاشده و HttpOnly را با پشتیبانی SameSite، Secure و expire/delete فراهم می‌کند. این موتور پایهٔ ذخیره‌سازی سمت کلاینت امن است.", "CookieJar، Cookie رمزنگاری‌شده، SameSite/Secure، expire/delete", "Session (در session)، CSRF (در security)", "COOKIE", "Symfony HttpFoundation Cookie"),
    "cors": ("موتور CORS مدیریت سیاست‌های Cross-Origin Resource Sharing را با پیکربندی مسیر/گروه، preflight handling و هدرهای استاندارد فراهم می‌کند و امکان ارتباط امن API با کلاینت‌های تحت وب دیگر را ممکن می‌سازد.", "Middleware CORS، پیکربندی paths/allowed_methods/allowed_origins، preflight، هدرهای Access-Control-*", "Rate limiting (در security)، احراز هویت (در auth)", "CORS", "fruitcake/laravel-cors + barryvdh/laravel-cors"),
    "crypt": ("موتور Crypt رمزنگاری متقارن (AES-256-GCM/CBC) با مدیریت کلید، رمزنگاری رشته/فایل، signing و MAC را فراهم می‌کند و پایهٔ امنیت داده‌های حساس در Tavaan است.", "Encrypter AES-256-GCM، Key management، String/File encryption، Signing/MAC", "Hashing password (در hash)، JWT signing (در auth)", "CRYPT", "Laravel Crypt + defuse/php-encryption"),
    "database": ("موتور Database لایهٔ ارتباط با پایگاه‌داده را با چند درایور (MySQL، PostgreSQL، SQLite، SQLServer)، connection pooling، query builder، تراکنش و schema abstraction فراهم می‌کند و پایهٔ همه عملیات داده است.", "ConnectionManager، QueryBuilder، MySQL/PgSQL/SQLite/SQLServer drivers، Transactions، Schema abstraction", "ORM (در orm)، migration (در migration)", "DATABASE", "Laravel Database + Doctrine DBAL"),
    "error": ("موتور Error مدیریت یکپارچه استثناها را با mapping کد خطا، rendererهای CLI/JSON/HTML/Debug، ref-code generation، log masking و توزیع به لاگر فراهم می‌کند و تجربهٔ دیباگ و گزارش خطای ساختاریافته ارائه می‌دهد.", "ExceptionHandler، ExceptionMapper، Renderers (CLI/JSON/HTML/Debug)، RefCodeGenerator، LogMasker، ErrorCode", "لاگ (در log)، HTTP (در http)", "ERROR", "Laravel Exceptions + Boo boo"),
    "event": ("موتور Event زیرساخت pub/sub داخلی را با Dispatcher، Listener registration، queued listeners و wildcards فراهم می‌کند و ارتباط loosely-coupled بین موتورها را ممکن می‌سازد.", "EventDispatcher، Listener registration، Queued listeners، Wildcard listeners", "Queue (در queue)، Realtime (در realtime)", "EVENT", "Laravel Events + Symfony EventDispatcher"),
    "feature-flag": ("موتور Feature-Flag پرچم‌های ویژگی را با پشتیبانی کاربر/درصد/جلسه/محدوده زمانی، ذخیره‌سازی در DB/Config/Memory و ارزیابی یکپارچه فراهم می‌کند و rollout تدریجی و A/B testing را ممکن می‌سازد.", "FlagManager، strategies (user/percentage/time/session)، stores (DB/Config/Memory)، Evaluation API", "تست‌های A/B (در test)، گزارش‌گیری (در report)", "FF", "LaunchDarkly / Unleash / flagr"),
    "filesystem": ("موتور Filesystem لایهٔ ذخیره‌سازی فایل را با چندین disk (Local، S3، FTP، SFTP، Flysystem) فراهم می‌کند و operations read/write/stream/list را به‌صورت یکپارچه ارائه می‌دهد.", "DiskManager، Local/S3/FTP/SFTP drivers، Stream operations، File existence/metadata", "Media processing (در media)، Backup (در backup)", "FS", "Laravel Filesystem + Flysystem"),
    "hash": ("موتور Hash هش کردن رمز عبور را با الگوریتم‌های Bcrypt و Argon2id، تطرید (rehash) و verify فراهم می‌کند و مطابق با استانداردهای امنیتی مدرن است.", "HashManager، BcryptHasher، Argon2idHasher، needsRehash، verify", "JWT (در auth)، Crypt عمومی (در crypt)", "HASH", "Laravel Hash + password_hash()"),
    "http": ("موتور HTTP هستهٔ پردازش درخواست/پاسخ را با Request/Response objects، middleware stack، cookie، session integration و send/stream فراهم می‌کند و پایهٔ همه ورودی‌های وب است.", "Request/Response، Middleware pipeline، Cookie integration، Stream responses، Header manipulation", "Router (در router)، View (در view)", "HTTP", "Symfony HttpFoundation + Nyholm PSR-7"),
    "http-client": ("موتور HTTP-Client کلاینت HTTP خالص PHP را با pool، retry، timeout، mock و middleware chain فراهم می‌کند و امکان ارسال درخواست‌های امن به سرویس‌های خارجی را می‌دهد.", "Client، Pool، Retry/Middleware، Mock، Response objects", "Realtime websocket (در realtime)، Mail transport (در mail)", "HTTPCLIENT", "Laravel HTTP Client + Guzzle"),
    "i18n": ("موتور i18n ترجمه، pluralization، format اعداد/تاریخ فارسی و بارگذاری lang files را فراهم می‌کند و پشتیبانی کامل RTL و فارسی‌سازی پیام‌ها را تضمین می‌کند.", "Translator، PluralRules، PersianFormatter، NumberFormatter، Jalali date integration، helpers", "تقویم جلالی پایه (در jalali)، Validation messages (در validation)", "I18N", "Laravel Lang + Symfony Translation"),
    "jalali": ("موتور Jalali تبدیل و محاسبهٔ تاریخ شمسی را با کلاس JalaliDate، JalaliConverter و Clock فراهم می‌کند و نمایش دوطرفهٔ جلالی/میلادی را در همه‌جا یکپارچه می‌سازد.", "JalaliDate، JalaliConverter، Clock، conversion دوطرفه", "i18n (در i18n)، فرمت اعداد (در i18n)", "JALALI", "jenssegers/date + morilog/jalali"),
    "log": ("موتور Log زیرساخت لاگ‌نویسی را با چندین channel (File، Stderr، Syslog، Slack)، levels، formatting و rotation فراهم می‌کند و مطابق با PSR-3 عمل می‌کند.", "Logger PSR-3، channels (File/Stderr/Syslog/Slack)، levels، formatter، rotation", "Audit (در audit)، Observability (در observability)", "LOG", "Monolog"),
    "mail": ("موتور Mail ارسال ایمیل را با چند transport (SMTP، Sendmail، Log، Array)، Mailable objects، Markdown، queue و templating فراهم می‌کند.", "Mailer، transports (SMTP/Sendmail/Log/Array)، Mailable، Markdown، queued mail", "Notification (در notification)، Queue (در queue)", "MAIL", "Laravel Mail + Symfony Mailer"),
    "media": ("موتور Media مدیریت فایل‌های رسانه‌ای را با آپلود، تشخیص MIME، اعتبارسنجی نوع، پردازش تصویر (resize/crop/watermark)، thumbnail و conversion فراهم می‌کند.", "MediaManager، Uploader، ImageProcessor، ImageManager، MimeDetector، MimeValidator، conversions", "Filesystem پایه (در filesystem)، Backup (در backup)", "MEDIA", "Laravel Media Library + Intervention"),
    "migration": ("موتور Migration نسخه‌بندی schema پایگاه‌داده را با up/down، transactions، schema builder و status reporting فراهم می‌کند و پایهٔ schema versioning است.", "Migration runner، Schema builder، up/down، transactions، status", "Schema (در schema)، Database (در database)", "MIGRATION", "Laravel Migrations + Phinx"),
    "module": ("موتور Module زیرساخت ماژولار بودن را با registration، discovery، enable/disable و namespace isolation فراهم می‌کند و امکان تقسیم پروژه به ماژول‌های مستقل را می‌دهد.", "ModuleManager، discovery، enable/disable، namespace isolation، manifest", "Plugin سیستم (در plugin)، Tenancy (در tenancy)", "MODULE", "nwidart/laravel-modules"),
    "notification": ("موتور Notification ارسال اعلان‌های چندکاناله (Mail، SMS، Database، Broadcast، Webhook) را با queued dispatch و on-demand فراهم می‌کند.", "NotificationDispatcher، channels (Mail/SMS/Database/Broadcast/Webhook)، Queued، on-demand", "Mail (در mail)، Realtime (در realtime)", "NOTIF", "Laravel Notifications"),
    "observability": ("موتور Observability ردیابی توزیع‌شده (Tracing با OTLP/Jaeger)، metrics (Prometheus)، Health checks و DebugBar را یکپارچه فراهم می‌کند و دید کامل بر عملکرد سیستم می‌دهد.", "Tracer/TraceManager (OTLP/Jaeger)، Metrics (Prometheus)، Health checks، DebugBar، Span exporters", "Log (در log)، Audit (در audit)", "OBS", "OpenTelemetry + Prometheus + Laravel Telescope"),
    "optimizer": ("موتور Optimizer بهینه‌سازی عملکرد برنامه را با cache route/config/event/view، precompilation، opcache و benchmarking فراهم می‌کند و راهکارهایی برای payload کوچک‌تر و سریع‌تر ارائه می‌دهد.", "Route/Config/Event/View cache، precompilation، opcache advisory، OptimizerResult", "Compiler view (در view)، Cache (در cache)", "OPT", "Laravel optimize + opcache"),
    "orm": ("موتور ORM نگاشت اشیاء به داده را با Model، Collection، Repository، Observer، Cast و Scope فراهم می‌کند و الگوی Active Record/Repository را یکپارچه پشتیبانی می‌کند.", "Model، Collection، Repository، Observer، Cast، Scope، relationships", "Database پایه (در database)، Migration (در migration)", "ORM", "Laravel Eloquent + Doctrine ORM"),
    "payment": ("موتور Payment اتصال به درگاه‌های پرداخت ایرانی و بین‌المللی را با abstraction، transaction logging، verification و refund فراهم می‌کند.", "GatewayManager، drivers (زرین‌پال/سامان/Stripe/PayPal)، Transaction logging، Verify، Refund", "Workflow (در workflow)، Notification (در notification)", "PAY", "Laravel Cashier + shetpayment"),
    "pipeline": ("موتور Pipeline اجرای زنجیره‌ای middleware/pipe را با contracts استاندارد، مدیریت عمق و exception handling فراهم می‌کند و در HTTP و job processing استفاده می‌شود.", "Pipeline، MiddlewareInterface، max depth guard، exception handling", "HTTP (در http)، Queue (در queue)", "PIPE", "Laravel Pipeline + League Pipeline"),
    "plugin": ("موتور Plugin سیستم افزونه‌پذیری را با discovery، install/uninstall، hook system و isolation فراهم می‌کند و توسعهٔ third-party را ممکن می‌سازد.", "PluginManager، discovery، hooks، install/uninstall، namespace isolation", "Module (در module)، Tenancy (در tenancy)", "PLUGIN", "WordPress Plugin System + Composer Plugins"),
    "queue": ("موتور Queue صف‌بندی وظایف را با چندین connection (Database، Redis، Sync، Null)، Worker، retry، delay و failed-job management فراهم می‌کند.", "QueueManager، connections (DB/Redis/Sync/Null)، Worker، Retry/Delay، Failed jobs", "Schedule (در schedule)، Event (در event)", "QUEUE", "Laravel Queue + Symfony Messenger"),
    "rbac": ("موتور RBAC مدیریت نقش، مجوز و سیاست دسترسی را با Role/Permission، Policy، Gate و caching فراهم می‌کند و کنترل دسترسی مبتنی بر نقش را پیاده می‌کند.", "Role/Permission، Policy، Gate، caching، wildcard/owner checks", "Auth (در auth)، Admin (در admin)", "RBAC", "spatie/laravel-permission + Laravel Gate"),
    "realtime": ("موتور Realtime ارتباطات bidirectional را با WebSocket server، broadcasting، presence channel و push integration فراهم می‌کند و قابلیت‌های chat/live dashboard را ممکن می‌سازد.", "WebSocket server، Broadcasting، Presence channels، Push adapters", "Notification (در notification)، Queue (در queue)", "RT", "Laravel Echo + Soketi + Reverb"),
    "report": ("موتور Report تولید گزارش‌های ساختاریافته را با datasource، renderer (PDF/Excel/CSV/HTML)، template و scheduling فراهم می‌کند.", "ReportManager، datasources، renderers (PDF/Excel/CSV/HTML)، templates، scheduled reports", "PDF rendering خارجی (در pdf skill)، Mail (در mail)", "REPORT", "Laravel Nova Reports + Jasper"),
    "router": ("موتور Router مسیریابی HTTP را با تعریف route، group، middleware binding، parameter، named routes و resource controllers فراهم می‌کند و پایهٔ dispatching است.", "Router، Route collection، Group/Middleware binding، Parameters، Named routes، Resource", "HTTP kernel (در http)، CORS (در cors)", "ROUTER", "Laravel Router + Symfony Routing"),
    "scaffold": ("موتور Scaffold کدجنریتور CLI را با stubs، generators (Model/Controller/Migration/Resource/Policy/Test و…) و GeneratorManager فراهم می‌کند و شروع سریع پروژه را ممکن می‌سازد.", "ScaffoldEngine، GeneratorManager، Generators (Model/Controller/Migration/Test/...)، StubRenderer، Make commands", "Admin CRUD (در admin)، Module (در module)", "SCAFFOLD", "Laravel Make + Artisan generators"),
    "schedule": ("موتور Schedule زمان‌بندی وظایف را با Cron expressions، intervals، withoutOverlapping، runInBackground و command-line runner فراهم می‌کند.", "ScheduleManager، CronExpression، ScheduleEvent، run/list commands، overlap guard", "Queue (در queue)، Console (در console)", "SCHED", "Laravel Scheduler + cron"),
    "schema": ("موتور Schema ساخت و تغییر ساختار جداول پایگاه‌داده را با Blueprint، column types، indexes، foreign keys و rename/drop فراهم می‌کند و پایهٔ migration است.", "SchemaBuilder، Blueprint، column types، indexes، foreign keys، rename/drop", "Migration (در migration)، Database (در database)", "SCHEMA", "Laravel Schema + Doctrine Schema"),
    "search": ("موتور Search جستجوی full-text را با drivers (PgSQL/MySQL/SQLite FTS/Meilisearch/Typesense/Native)، Searchable trait، highlight و Persian normalization فراهم می‌کند.", "SearchManager، drivers (PgSQL/MySQL/SQLite/Meili/Typesense/Native)، Searchable، Highlighter، Persian normalization", "ORM (در orm)، Database (در database)", "SEARCH", "Laravel Scout + Meilisearch"),
    "security": ("موتور Security مجموعه‌ای از middleware و managerهای امنیتی شامل CSRF، Rate Limiting (Throttle)، HTML Sanitizer، Input Normalizer و SSRF protection را فراهم می‌کند.", "CsrfManager، RateLimiter/Throttle، HtmlSanitizer، InputNormalizer، SSRF protection", "Auth (در auth)، Crypt (در crypt)", "SEC", "Laravel Security + HTML Purifier"),
    "session": ("موتور Session مدیریت نشست کاربر را با چند handler (File، Database، Cache، Cookie، Array)، flash data، CSRF token و middleware integration فراهم می‌کند.", "SessionManager، handlers (File/DB/Cache/Cookie/Array)، flash data، CSRF token، middleware", "Auth (در auth)، Cookie (در cookie)", "SESSION", "Laravel Session + Symfony Session"),
    "tenancy": ("موتور Tenancy چندمستاجری (multi-tenant) را با tenant identification، database separation، config switching و middleware فراهم می‌کند و امکان اجرای یک کد برای چند tenant را می‌دهد.", "TenantManager، identification، DB separation، config switch، middleware", "Database (در database)، Config (در config)", "TENANT", "stancl/tenancy + hyn/multi-tenant"),
    "test": ("موتور Test فریم‌ورک آزمون خودنوشته را با TestCase، Assertion، Mock، Factory، RefreshDatabase، Coverage و MakesHttpRequests فراهم می‌کند و امکان نوشتن unit/feature test را می‌دهد.", "TestCase، TestRunner، Assertions، Mock، Factory، RefreshDatabase، Coverage، Http test traits", "Scaffold test gen (در scaffold)، Console runner (در console)", "TEST", "PHPUnit + Pest"),
    "upgrade": ("موتور Upgrade فرآیند ارتقای نسخه‌های Tavaan را با version diff، migration steps، changelog parsing و rollback فراهم می‌کند و انتقال بین نسخه‌ها را امن می‌سازد.", "Upgrader، version diff، migration steps، changelog، rollback", "Migration (در migration)، Module (در module)", "UPGRADE", "Laravel Upgrade Guide + Rector"),
    "validation": ("موتور Validation اعتبارسنجی ورودی را با rules، FormRequest، DTO validator، RuleParser، Iranian checks و message bag فراهم می‌کند و پایهٔ امنیت ورودی است.", "Validator، RuleParser، FormRequest، DtoValidator، built-in rules، IranianChecks (melli/card/iban)، MessageBag", "Security sanitizing (در security)، ORM data casts (در orm)", "VAL", "Laravel Validation + Respect Validation"),
    "view": ("موتور View موتور قالب‌سازی را با TemplateCompiler، DirectiveRegistry، ViewFinder، ComponentAttributeBag، Escaper، SafeString و caching فراهم می‌کند و پایهٔ رندر UI است.", "ViewFactory، TemplateCompiler، DirectiveRegistry، ViewFinder، ComponentAttributeBag، Escaper، SafeString، View cache", "Admin views (در admin)، i18n در قالب (در i18n)", "VIEW", "Laravel Blade + Latte + Twig"),
    "workflow": ("موتور Workflow مدیریت فرآیندهای کسب‌وکار را با state machine، activity، trigger، transition و persistence فراهم می‌کند و اتوماسیون فرآیندهای طولانی را ممکن می‌سازد.", "WorkflowManager، state machine، activities، triggers، transitions، persistence", "Queue (در queue)، Schedule (در schedule)", "WF", "Laravel Workflow + Symfony Workflow"),
}


def get_class_role(filename, classname):
    name = classname.lower()
    fpath = filename.lower()
    if "/facades/" in fpath:
        return "Facade"
    if name.endswith("engine"):
        return "Engine"
    if "serviceprovider" in name:
        return "ServiceProvider"
    if "manager" in name:
        return "Manager"
    if "middleware" in name:
        return "Middleware"
    if "controller" in name:
        return "Controller"
    if "command" in name:
        return "Command"
    if "exception" in name:
        return "Exception"
    if "contract" in name or "interface" in name:
        return "Contract/Interface"
    if "handler" in name:
        return "Handler"
    if "store" in name:
        return "Store"
    if "driver" in name:
        return "Driver"
    if "generator" in name:
        return "Generator"
    if "guard" in name:
        return "Guard"
    if "rule" in name:
        return "Rule"
    if "renderer" in name:
        return "Renderer"
    if "exporter" in name:
        return "Exporter"
    if "factory" in name:
        return "Factory"
    if "mock" in name:
        return "Mock"
    if "model" in name:
        return "Model"
    if "collection" in name:
        return "Collection"
    if "repository" in name:
        return "Repository"
    if "builder" in name:
        return "Builder"
    if "result" in name or "response" in name or "metric" in name:
        return "Value/DTO"
    return "Class"


def render_doc(idx, name, engine_data, src_files, loc_count, config_keys_str=""):
    doc_id = f"DOC-{31 + idx:03d}"
    UPPER = name.upper().replace("-", "_")
    meta = META.get(name, (
        f"موتور {name} مسئولیت حوزهٔ {engine_data.get('title_fa', name)} را بر عهده دارد و در بستر Tavaan به‌عنوان موتور مستقل قابل بارگذاری عمل می‌کند.",
        "ارائهٔ قابلیت‌های هستهٔ حوزه بر اساس engine.json",
        "خارج از دامنهٔ این موتور",
        UPPER, "Industry Standard"
    ))
    why, in_scope, out_scope, area, reference = meta

    requires_engines = engine_data.get("requires", {}).get("engines", [])
    soft_requires = engine_data.get("soft_requires", {}).get("engines", [])
    facade = engine_data.get("facade")
    tables = engine_data.get("tables", [])
    phase = PHASE_MAP.get(name, "M8")
    prio = priority(name)

    class_rows = []
    for f in src_files:
        basename = os.path.basename(f).replace(".php", "")
        role = get_class_role(f, basename)
        # path relative to src/ (e.g. Contracts/Authenticatable.php)
        rel_path = f
        if rel_path.startswith("src/"):
            rel_path = rel_path[4:]
        class_rows.append(f"| `{basename}` | {role} | `src/{rel_path}` |")
    if len(class_rows) > 30:
        class_rows = class_rows[:30]
        class_rows.append("| _(و دیگر کلاس‌ها)_ | — | — |")
    class_table = "\n".join(class_rows) if class_rows else "| _(خالی)_ | — | — |"

    hard_deps = ", ".join(f"`{e}`" for e in requires_engines) if requires_engines else "—"
    soft_deps = ", ".join(f"`{e}`" for e in soft_requires) if soft_requires else "—"

    if facade and isinstance(facade, dict) and facade.get("name"):
        facade_str = f"`{facade['name']}` → accessor `{facade.get('accessor', '')}`"
        f_name = facade.get('name', '')
        f_acc = facade.get('accessor', '')
    else:
        facade_str = "— (بدون Facade)"
        f_name = ""
        f_acc = ""

    tables_str = ", ".join(f"`{t}`" for t in tables) if tables else "—"
    class_count = len(src_files)
    engine_name = engine_data.get('name', name)
    title_fa = engine_data.get('title_fa', name)
    engine_id = engine_data.get('id', '')
    ns = engine_data.get('namespace', '')

    doc = f"""# {doc_id} — موتور {engine_name} | {title_fa}

| متادیتا | مقدار |
|---|---|
| DOC-ID | {doc_id} |
| Engine ID | `{engine_id}` |
| Namespace | `{ns}` |
| مسیر | `engines/{name}/` |
| وضعیت | Draft v0.0.1 |
| اولویت | {prio} |
| فاز ساخت | {phase} |
| وابستگی (سخت) | {hard_deps} |
| وابستگی (نرم/اختیاری) | {soft_deps} |
| Facade | {facade_str} |
| جداول DB | {tables_str} |
| LOC برآوردی | {loc_count} |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
{why}

### ۱٫۲ دامنه (What)
- ✅ شامل: {in_scope}
- ❌ خارج از دامنه: {out_scope}

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-{area}-01 | پیاده‌سازی هستهٔ موتور {name} به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-{area}-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-{area}-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| {reference} | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `{ns}`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع {class_count} فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
{class_table}

### ۳٫۲ دیاگرام وابستگی داخلی
N/A: در نسخهٔ ۱.۰ با دیاگرام PlantUML.

### ۳٫۳ الگوهای طراحی
- Service Provider + Facade (الگوی Laravel-like)
- Manager/Driver برای چند-درایوری (در صورت وجود)
- Contract → Implementation separation

---

## ۴. API عمومی
N/A: پیاده‌سازی v0.0.1 — API در نسخه‌های بعدی مستند می‌شود.

## ۵. الگوریتم‌ها
N/A: v0.0.1 — الگوریتم‌ها در نسخهٔ ۱.۰ مستند می‌شوند.

## ۶. پیکربندی
"""
    if config_keys_str:
        doc += config_keys_str
    else:
        doc += f"فایل پیکربندی این موتور در `engines/{name}/config/{name}.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.{name}.config.{name}`.\n\nدر v0.0.1 فقط ساختار اولیه پشتیبانی می‌شود.\n"

    doc += f"""
## ۷. قراردادها
N/A: قراردادها در نسخه‌های بعدی به `core/Contracts/` منتقل می‌شوند.

## ۸. نقاط توسعه
N/A: v0.0.1

## ۹. امنیت
N/A: در نسخهٔ ۱.۰ با چک‌لیست کامل.

## ۱۰. کارایی
N/A: بنچمارک در نسخهٔ ۱.۰.

## ۱۱. مدیریت خطا
N/A: کلاس‌های استثنا در نسخه‌های بعدی.

## ۱۲. تست
N/A: موتور test در v0.0.1 وجود دارد اما آزمون‌ها هنوز نوشته نشده‌اند.

## ۱۳. مثال End-to-End
N/A: در نسخهٔ ۱.۰.

## ۱۴. معیار پذیرش 🧪
| ID | معیار | تست |
|---|---|---|
| AC-{UPPER}-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-{UPPER}-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| {reference} | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.{name}.v1
engine:
  id: {engine_id}
  namespace: {ns}
  path: engines/{name}
  priority: {prio}
  phase: {phase}
  depends_on: [{", ".join(requires_engines)}]
  soft_depends_on: [{", ".join(soft_requires)}]
  facade: {{name: {f_name}, accessor: {f_acc}}}
  tables: [{", ".join(tables)}]
  config_file: engines/{name}/config/{name}.php
  loc_estimate: {loc_count}
  acceptance:
    - {{id: AC-{UPPER}-01, test: 'php bin/tvn engines'}}
    - {{id: AC-{UPPER}-02, test: 'php bin/tvn engines --list'}}
```
"""
    return doc


def main():
    readme_rows = []
    files_written = 0
    errors = []

    for idx, name in enumerate(ENGINES):
        engine_path = os.path.join(ENGINES_DIR, name)
        json_path = os.path.join(engine_path, "engine.json")
        src_dir = os.path.join(engine_path, "src")

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                engine_data = json.load(f)
        except Exception as e:
            errors.append(f"{name}: cannot read engine.json: {e}")
            continue

        src_files = []
        if os.path.isdir(src_dir):
            for root, dirs, files in os.walk(src_dir):
                for f in files:
                    if f.endswith(".php"):
                        rel = os.path.relpath(os.path.join(root, f), engine_path)
                        src_files.append(rel)
            src_files.sort()

        loc = 0
        for sf in src_files:
            full_path = os.path.join(engine_path, sf)
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                    loc += sum(1 for _ in fp)
            except Exception:
                pass

        config_keys_str = ""
        config_file = os.path.join(engine_path, "config", f"{name}.php")
        if os.path.isfile(config_file):
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    content = f.read()
                if "return [" in content:
                    keys = re.findall(r"^\s*['\"]([a-zA-Z0-9_\-]+)['\"]\s*=>", content, re.MULTILINE)
                    if keys:
                        seen = []
                        for k in keys:
                            if k not in seen:
                                seen.append(k)
                        keys_str = ", ".join(f"`{k}`" for k in seen[:20])
                        config_keys_str = (
                            f"فایل پیکربندی: `engines/{name}/config/{name}.php`\n\n"
                            f"کلیدهای اصلی:\n{keys_str}\n"
                        )
            except Exception:
                pass

        doc_content = render_doc(idx, name, engine_data, src_files, loc, config_keys_str)

        out_file = os.path.join(OUT_DIR, f"{name}.md")
        try:
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(doc_content)
            files_written += 1
        except Exception as e:
            errors.append(f"{name}: cannot write doc: {e}")

        readme_rows.append((idx, name, engine_data))

    # Build README (DOC-030)
    readme = "# DOC-030 — رجیستری موتورها (Engine Registry)\n\n"
    readme += "این سند فهرست رسمی ۵۲ موتور Tavaan است. هر موتور در `engines/<name>/` قرار دارد و مستندات کامل آن در `docs/03-engines/<name>.md`.\n\n"
    readme += "| DOC-ID | Engine | عنوان فارسی | Namespace | اولویت | فاز | وابستگی سخت | Facade |\n"
    readme += "|---|---|---|---|---|---|---|---|\n"
    for idx, name, data in readme_rows:
        doc_id = f"DOC-{31 + idx:03d}"
        title_fa = data.get("title_fa", "")
        ns = data.get("namespace", "")
        prio = priority(name)
        phase = PHASE_MAP.get(name, "M8")
        req_eng = data.get("requires", {}).get("engines", [])
        hard = ", ".join(req_eng) if req_eng else "—"
        facade = data.get("facade")
        facade_name = facade.get("name", "—") if isinstance(facade, dict) else "—"
        readme += f"| {doc_id} | [{data.get('name', name)}](./{name}.md) | {title_fa} | `{ns}` | {prio} | {phase} | {hard} | `{facade_name}` |\n"

    readme += f"\n**مجموع:** {len(ENGINES)} موتور | **فایل‌های نوشته‌شده:** {files_written}\n\n"
    if errors:
        readme += "## خطاها\n\n"
        for e in errors:
            readme += f"- {e}\n"

    readme_path = os.path.join(OUT_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"Summary: {files_written} docs written + 1 README")
    if errors:
        print("Errors:")
        for e in errors:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
