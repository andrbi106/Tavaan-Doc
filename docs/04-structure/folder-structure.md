# DOC-080 — ساختار پوشه/فایل تَوان

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-080 |
| وضعیت | Approved v0.0.1 |
| نقش | ساختار واقعی Tavaan-Demo |
| پیش‌نیاز | DOC-021 |

## ساختار واقعی Tavaan-Demo

```
Tavaan-Demo/
├── bin/
│   └── tvn                        # CLI entry point
├── public/
│   └── index.php                  # HTTP entry point
├── bootstrap.php                  # bootstrap اپلیکیشن
├── tavaan.json                    # manifest پروژه
├── .env.example                   # نمونهٔ تنظیمات محیطی
├── DEPENDENCIES.md                # نمودار وابستگی موتورها
├── TROUBLESHOOTING.md             # مستندات رفع اشکال
├── README.md
├── core/                          # Tavaan\Core\ — هسته
│   ├── bootstrap.php              # نقطهٔ ورود هسته
│   ├── Application/               # Application, ApplicationBuilder, RuntimeMode
│   ├── Autoloading/               # Autoloader, AutoloaderRegistry
│   ├── Bootstrap/                 # ۷ بوت‌استرپر
│   ├── Container/                 # Container, Binding, Lifetime
│   ├── Context/                   # RequestStack, TraceContext, IdentityContext
│   ├── Contracts/                 # Container, Events, Support
│   ├── Error/                     # ErrorHandler, LogMasker
│   ├── Events/                    # Event, EventDispatcher
│   ├── Exceptions/                # TavaanException + Core exceptions
│   ├── Facade/                    # Facade + Facades/
│   ├── Provider/                  # ServiceProvider پایه
│   └── Support/                   # Arr, Str, helpers, PathGuard, Ulid, Clock
├── engine-core/                   # Tavaan\EngineCore\
│   ├── Engine.php                 # کلاس پایه
│   ├── EngineBus.php              # درگاه ۳
│   ├── EngineRegistry.php         # boot توپولوژیک
│   ├── EngineLoader.php           # کشف
│   ├── EngineManifest.php
│   ├── EngineContext.php
│   └── Contracts/                 # EngineInterface, EngineBusInterface, ...
├── engines/                       # ۵۲ موتور فرزند
│   └── <name>/                    # هر موتور:
│       ├── engine.json            # manifest
│       ├── src/                   # ServiceProvider, Engine, ...
│       ├── config/<name>.php      # پیکربندی
│       ├── lang/{fa,en}/          # ترجمه
│       ├── tests/                 # آزمون‌ها
│       ├── README.md, ROADMAP.md, TICKET.md
│       └── migrations/ (در صورت وجود)
├── config/
│   ├── app.php                    # پیکربندی اپلیکیشن
│   ├── autoload.php               # نگاشت namespaceها (namespace-map)
│   ├── engine.php                 # (خودکار تولید می‌شود)
│   └── providers.php              # Service Providerها
├── app/
│   └── src/Controllers/           # کنترلرهای اپلیکیشن
├── routes/
│   ├── web.php
│   ├── api.php
│   └── console.php
├── resources/
│   └── lang/{fa,en}/              # ترجمهٔ هسته
├── storage/
│   ├── logs/
│   ├── cache/
│   └── app/
└── docs/skills/tavaan-doc-writer/ # Skill اختصاصی
```

## تفاوت با ساختار مرجع

| مورد | مرجع | Tavaan-Demo |
|---|---|---|
| `modules/` | HMVC modules | ❌ موجود نیست |
| `kits/` | Application kits | ❌ |
| `plugins/` | Third-party | ❌ |
| `database/` | migrations/seeders | ❌ (در engines/<name>/migrations/) |
| `tests/` | مرکزی | ❌ (در engines/<name>/tests/) |
| `deploy/` | Docker/Nginx | ❌ |
| `tools/` | PHPStan/CS-Fixer | ❌ |
| `examples/` | نمونه‌ها | ❌ |

## مجوزهای storage

- `storage/` = 0775
- `storage/logs/`, `storage/cache/` = قابل‌نوشتن
