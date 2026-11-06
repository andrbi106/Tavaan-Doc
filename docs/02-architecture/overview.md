# DOC-020 — نمای کلان معماری تَوان

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-020 |
| وضعیت | Approved v0.0.1 |
| نقش | ترکیب معماری‌ها و نمودار کلان |
| پیش‌نیاز | DOC-002 |

## ترکیب معماری‌ها

تَوان ۵ الگوی معماری را ترکیب می‌کند:

```
Layered (لایه‌ای)
   ↑
HMVC (سلسله‌مراتبی)
   ↑
Modular Monolith (مونولیت ماژولار) ← پیش‌فرض
   ↑
Event-Driven (رویداد‌محور)
   ↑
Hexagonal (شش‌ضلعی) ← آمادگی مایکروسرویس
```

## نمودار C4 — Level 1 (Context)

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   کاربر     │────→│   تَوان     │────→│  پایگاه     │
│  (Browser)  │     │  (PHP 8.2+) │     │  داده       │
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                    ┌──────┴──────┐
                    │  ۵۲ موتور   │
                    │  خودنوشته   │
                    └─────────────┘
```

## نمودار Level 2 (Container)

```
tavaan/
├── bin/tvn              ← CLI Entry Point
├── public/index.php     ← HTTP Entry Point
├── core/                ← هسته (Tavaan\Core\)
│   ├── Autoloader       ← صفر‌وابستگی
│   ├── Container        ← DI (درگاه ۱)
│   ├── Events           ← Pub/Sub (درگاه ۲)
│   └── Application      ← چرخهٔ عمر
├── engine-core/         ← والد موتورها (EngineBus = درگاه ۳)
├── engines/             ← ۵۲ موتور فرزند
├── config/              ← پیکربندی
└── storage/             ← logs, cache
```

## سه درگاه ارتباط بین موتورها

| درگاه | الگو | کاربرد | پیاده‌سازی |
|---|---|---|---|
| **Container** | pull-based DI | `$this->make(CacheInterface::class)` | `core/Container/Container.php` |
| **Events** | pub/sub | `$this->dispatch('user.registered', $data)` | `core/Events/EventDispatcher.php` |
| **EngineBus** | point-to-point RPC | `$this->call('auth', 'issue-token', $input)` | `engine-core/EngineBus.php` |

## چرخهٔ بوت

```
bin/tvn یا public/index.php
    ↓
require bootstrap.php
    ↓
core/bootstrap.php
    ├── ثابت‌ها (TVN_BASE_PATH, TVN_VERSION)
    ├── بررسی PHP ≥ 8.2
    ├── Autoloader (PSR-4-like + wildcard)
    ├── config/autoload.php (namespace-map)
    └── ثبت در Registry
    ↓
bootstrap.php (ریشه)
    ├── اصلاح مسیر EngineCore
    ├── بارگذاری .env
    └── کشف پیکربندی موتورها
    ↓
ApplicationBuilder::create()->boot()
```

## تصمیمات کلیدی

- **ZeroDependency** (ADR-0004): هیچ پکیج بیرونی
- **Autoloader خودنوشته** (ADR-0005): بدون `vendor/autoload.php`
- **صفر vendor در runtime** (ADR-0014): فقط در dev
