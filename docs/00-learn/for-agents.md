# راهنمای ایجنت — چطور تَوان را پیاده‌سازی کنید 🤖

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-009 |
| وضعیت | Approved v0.0.1 |
| نقش | راهنمای عملی برای ایجنت‌های AI که تَوان را پیاده می‌کنند |
| پیش‌نیاز | DOC-001، DOC-002، DOC-009، DOC-020، DOC-150 |
| مخاطب | ایجنت‌های پیاده‌ساز (LLM-based) و توسعه‌دهندگان اتومات |
| مسئول | @TavaanOfficial |

---

## شما کیستید و چرا اینجا هستید؟ 👋

شما یک ایجنت هستید — یک مدل زبانی بزرگ یا یک ابزار خودکارسازی که وظیفهٔ پیاده‌سازی بخش‌هایی از تَوان را بر عهده دارد. این مخزن، **منبع یگانهٔ حقیقت** (SSOT) برای تَوان است: هر آنچه باید بدانید در این مستندات هست، و هر آنچه در کد هست باید با مستندات سازگار باشد.

این راهنما به شما می‌گوید:

- چطور مشخصات را بخوانید.
- چطور یک تیکت از `agent-backlog.md` انتخاب کنید.
- چطور قالب ۱۷بخشی موتور را پر کنید.
- چطور از بلوک‌های YAML ماشین‌خوان استفاده کنید.
- چطور گردش‌کار کامل «سند → اینترفیس → پیاده‌سازی → تست → مستند» را طی کنید.

---

## قاعدهٔ طلایی 🏆

> **سند، منبع یگانهٔ حقیقت است.** اگر کد با سند در تضاد باشد، ابتدا سند اصلاح می‌شود، نه کد.

این یعنی: شما **ابتدا** مستندات می‌خوانید، **بعد** کد می‌نویسید. این رویکرد، «مستندات‌اول» (Docs-First) نام دارد و در تَوان، قانون است (نه توصیه).

---

## نقشهٔ اولیهٔ مخزن 🗺️

قبل از هر کاری، ساختار کلی مخزن را بشناسید:

```
Tavaan-Doc-new/
├── docs/
│   ├── 00-overview/         ← اهداف، اصول، الزامات، شروع سریع
│   ├── 01-standards/        ← قواعد کدنویسی R1-R10، PHP 8.2+
│   ├── 02-architecture/     ← نمای کلان، لایه‌ها، HMVC، کانتینر، DI
│   ├── 03-engines/          ← ۵۲ موتور، هر کدام ۱۷ بخش مستند
│   ├── 04-structure/        ← ساختار پوشه/فایل، CLI، config
│   ├── 05-applications/     ← ۸ کیت آماده (Blog، Shop، ...)
│   ├── 06-roles-access/     ← نقش‌ها، مجوزها
│   ├── 07-quality/          ← تست، تحلیل ایستا، DoD
│   ├── 08-roadmap/          ← نقشهٔ ۴۵فازی، بک‌لاگ ایجنت
│   ├── 09-references/       ← واژه‌نامه، بنچمارک
│   ├── 10-modules/          ← ۱۶ ماژول HMVC
│   ├── 11-plugins/          ← ۴ افزونهٔ نمونه
│   ├── adr/                 ← تصمیمات معماری (ADR)
│   ├── templates/           ← قالب موتور، ماژول، ADR
│   └── README.md            ← شاخص اصلی (DOC-000)
└── skills/tavaan-doc-writer/ ← مهارت نگارش مستندات تَوان
```

---

## گردش‌کار کلی ایجنت (۹ مرحله) 🔄

بر اساس DOC-123، گردش‌کار رسمی ایجنت این است:

```
  ┌─────────────────────────────────────┐
  │ ۱. انتخاب تیکت از agent-backlog.md  │
  └──────────────┬──────────────────────┘
                 ▼
  ┌─────────────────────────────────────┐
  │ ۲. مطالعه مستندات مرتبط            │
  │    (DOC-009, DOC-011, DOC-012,      │
  │     <engine-doc>)                   │
  └──────────────┬──────────────────────┘
                 ▼
  ┌─────────────────────────────────────┐
  │ ۳. بررسی ساختار پوشه در DOC-083     │
  └──────────────┬──────────────────────┘
                 ▼
  ┌─────────────────────────────────────┐
  │ ۴. کپی قالب موتور DOC-150           │
  └──────────────┬──────────────────────┘
                 ▼
  ┌─────────────────────────────────────┐
  │ ۵. تکمیل بخش‌های ۱-۷ قبل از کد      │
  │    (Docs-First)                     │
  └──────────────┬──────────────────────┘
                 ▼
  ┌─────────────────────────────────────┐
  │ ۶. تعریف Interface در core/Contracts│
  └──────────────┬──────────────────────┘
                 ▼
  ┌─────────────────────────────────────┐
  │ ۷. پیاده‌سازی در engines/<name>/src │
  └──────────────┬──────────────────────┘
                 ▼
  ┌─────────────────────────────────────┐
  │ ۸. نوشتن آزمون از معیار پذیرش      │
  │    (بخش ۱۴، TDD)                    │
  └──────────────┬──────────────────────┘
                 ▼
  ┌─────────────────────────────────────┐
  │ ۹. اجرای php bin/tvn engines +      │
  │    php -l + PHPStan                  │
  └─────────────────────────────────────┘
```

---

## مرحله ۱ — چطور مشخصات را بخوانیم 📖

هر موتور در تَوان ۱۷ بخش مستند دارد. هر بخش با `DOC-XXX-SNN` شناسه‌گذاری شده (مثلاً `DOC-046-S04` برای بخش ۴ موتور Event).

### ترتیب خواندن

برای پیاده‌سازی موتور X، این ترتیب را دنبال کنید:

```
۱. docs/03-engines/<X>/README.md        ← نمای کلی + متادیتا
۲. docs/03-engines/<X>/01-goal-scope.md  ← هدف، دامنه، FR-IDs
۳. docs/03-engines/<X>/02-concepts.md    ← مفاهیم و واژگان
۴. docs/03-engines/<X>/03-architecture.md ← معماری داخلی + فهرست کلاس‌ها
۵. docs/03-engines/<X>/04-public-api.md  ← API عمومی + Facade
۶. docs/03-engines/<X>/07-contracts.md   ← Interfaceها
۷. docs/03-engines/<X>/06-config.md      ← پیکربندی
۸. docs/03-engines/<X>/14-acceptance.md  ← معیار پذیرش (مهم برای تست)
۹. docs/03-engines/<X>/17-machine-readable.yml ← بلوک YAML 🧠
```

### نمادهای مستندات

| نماد | معنا | تأثیر بر شما |
|---|---|---|
| 🔒 | الزامی (MUST) | نقض = ریجکت PR |
| ⚠️ | توصیهٔ قوی (SHOULD) | به‌ترتیب رعایت کنید |
| 💡 | اختیاری (MAY) | می‌توانید رعایت کنید |
| 🧪 | معیار تست/پذیرش | باید تست بنویسید |
| 🧠 | بلوک ماشین‌خوان | از آن برای استخراج داده استفاده کنید |

### شناسه‌های مهم

| قالب | کاربرد |
|---|---|
| `FR-<AREA>-<NN>` | الزام عملکردی — شما باید پوشش دهید |
| `NFR-<AREA>-<NN>` | الزام غیرعملکردی |
| `AC-<ENGINE>-<NN>` | معیار پذیرش — به تست تبدیل کنید |
| `SEC-<AREA>-<NN>` | کنترل امنیتی |
| `ADR-<NNNN>` | تصمیم معماری |
| `TVN-<NNNN>` | تیکت/issue |
| `DOC-<NNN>` | شناسه سند |
| `R<1-10>` | قانون سخت کدنویسی |
| `P<1-12>` | اصل بنیادین |

---

## مرحله ۲ — چطور یک تیکت از agent-backlog.md بگیریم 🎟️

فایل [`../08-roadmap/agent-backlog.md`](../08-roadmap/agent-backlog.md) (DOC-123) شامل تیکت‌های آماده است.

### الگوریتم انتخاب تیکت

```python
def pickNextTicket(agent):
    ready = [t for t in tickets
             if t.status == 'todo'
             and all(dep.status == 'done' for dep in t.depends_on)]
    if ready is empty:
        return "all blocked or done"
    # اولویت: فاز کمتر → P0 → تیکت با وابستگی بیشتر
    return sorted(ready, key=(phase, priority, -len(depends_on)))[0]
```

به زبان ساده:

1. تیکت‌هایی که `status: todo` هستند و **همهٔ وابستگی‌هایشان done شده**، کاندید هستند.
2. اگر هیچ کاندیدی نبود، یعنی یا همه تمام شده‌اند یا همه بلاک.
3. در میان کاندیدها، اولویت با این ترتیب است:
   - فاز کمتر (مثلاً M1 قبل از M2).
   - اولویت بیشتر (P0 قبل از P1).
   - تیکت با وابستگی بیشتر (چون بقیه منتظر آن هستند).

### ساختار یک تیکت

```yaml
ticket:
  id: TVN-0060          ← شناسه یکتا
  title: <عنوان>
  phase: M6             ← فاز
  engine: tavaan.engine.http
  type: engine|module|feature|fix|docs|test
  priority: P0|P1|P2
  depends_on: [TVN-YYYY]  ← تیکت‌هایی که باید قبلاً done شده باشند
  estimate_loc: 2800    ← برآورد خطوط کد
  docs: [DOC-039]       ← مستندات مرتبط
  acceptance:           ← معیار پذیرش
    - AC-HTTP-01: Request immutable با PSR-7-like API
    - AC-HTTP-02: Response با status/headers/body
    - ...
  status: todo|in_progress|review|done
```

### جریان وضعیت تیکت

```
todo → in_progress → review → done
```

- `todo`: کسی رویش کار نمی‌کند.
- `in_progress`: شما شروع کردید.
- `review`: کد نوشته شده، منتظر بازبینی.
- `done`: پذیرفته شده و ادغام شده.

> **نکته مهم:** هرگز تیکتی که `depends_on` آن‌ها `done` نشده‌اند را شروع نکنید. این کار باعث تداخل می‌شود.

---

## مرحله ۳ — چطور از قالب‌ها استفاده کنیم 📐

### قالب موتور (Engine Spec Template) — DOC-150

فایل [`../templates/engine-spec-template.md`](../templates/engine-spec-template.md) را کپی کنید به مسیر `docs/03-engines/<name>/`.

قالب شامل ۱۷ بخش **اجباری** است. هیچ بخشی حذف نشود مگر با علامت‌گذاری `N/A: <دلیل>`.

### ساختار ۱۷بخشی موتور

| # | بخش | ضرورت | ورودی شما |
|---|---|---|---|
| ۱ | هدف و دامنه | اجباری | چرا، چه چیزی، FR-ها |
| ۲ | مفاهیم و واژگان | اجباری | جدول واژه‌ها |
| ۳ | معماری داخلی | اجباری | نمودار + فهرست کلاس‌ها |
| ۴ | API عمومی | اجباری | متدها + Facade + Helper |
| ۵ | الگوریتم‌ها | اجباری | شبه‌کد + Big-O |
| ۶ | پیکربندی | اجباری | config + جدول کلیدها |
| ۷ | قراردادها | اجباری | Interfaceها |
| ۸ | نقاط توسعه | اجباری | Hook + درایور سفارشی |
| ۹ | امنیت | اجباری | تهدید + کنترل |
| ۱۰ | کارایی | اجباری | هدف + روش سنجش |
| ۱۱ | مدیریت خطا | اجباری | جدول استثناها |
| ۱۲ | تست | اجباری | استراتژی + سناریوها |
| ۱۳ | مثال End-to-End | اجباری | کد اجراشدنی ≤۶۰ خط |
| ۱۴ | معیار پذیرش 🧪 | اجباری | جدول AC + تست |
| ۱۵ | محدودیت‌ها | اجباری | محدودیت‌های شناخته‌شده |
| ۱۶ | مراجع | اجباری | منابع الهام‌گرفته |
| ۱۷ | بلوک ماشین‌خوان 🧠 | اجباری | YAML |

### قالب ماژول — DOC-151

فایل [`../templates/module-template.md`](../templates/module-template.md) برای ماژول‌های HMVC. ۱۵ بخش دارد.

### قالب ADR — DOC-152

فایل [`../templates/adr-template.md`](../templates/adr-template.md) برای تصمیمات معماری. ۷ بخش دارد.

---

## مرحله ۴ — چطور بخش‌های ۱-۷ را قبل از کد پر کنیم ✍️

این مهم‌ترین مرحله است. قبل از آنکه یک خط کد بنویسید، بخش‌های ۱ تا ۷ مستندات موتور باید کامل باشد.

### چرا؟

چون مستندات ناقص = کد ناقص. اگر نمی‌دانید «چه» می‌خواهید بسازید، نمی‌توانید «چطور» را بنویسید.

### نمونهٔ بخش ۱ — هدف و دامنه

```markdown
## ۱. هدف و دامنه

### ۱.۱ هدف (Why)
موتور X مسئلهٔ Y را حل می‌کند تا Z ممکن شود.

### ۱.۲ دامنه (What)
- ✅ شامل: A، B، C
- ❌ خارج از دامنه: D (در موتور E)، F (در موتور G)

### ۱.۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-X-01 | ... |
| FR-X-02 | ... |

### ۱.۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel X | ... | ... | ZeroDependency، ماژولار بودن |
```

### نمونهٔ بخش ۷ — قراردادها

```php
namespace Tavaan\Engine\<Name>\Contracts;

interface <Name>Interface
{
    public function doSomething(string $input): Result;
}
```

جدول Interfaceها:

| Interface | پیاده‌سازی پیش‌فرض | جایگزین‌ها | Fake تست |
|---|---|---|---|
| `<Name>Interface` | `<Name>Engine` | `Fake<Name>` (تست) | `InMemory<Name>` |

---

## مرحله ۵ — چطور از بلوک YAML ماشین‌خوان استفاده کنیم 🧠

هر موتور در بخش ۱۷ یک بلوک YAML دارد. این بلوک، **«موجودیت ماشین‌خوان»** موتور است — شما و ایجنت‌های دیگر از آن برای استخراج داده استفاده می‌کنید.

### ساختار YAML

```yaml
# machine-readable: tavaan.engine.<name>.v1
engine:
  id: tavaan.engine.<name>          # شناسه یکتا
  namespace: Tavaan\Engine\<Pascal> # ریشهٔ namespace
  path: engines/<name>              # مسیر فیزیکی
  priority: P0|P1|P2                # اولویت
  phase: M<N>                       # فاز ساخت
  depends_on: []                    # وابستگی‌های سخت
  soft_depends_on: []               # وابستگی‌های نرم
  extensions:                       # افزونه‌های PHP
    required: []
    optional: [{name: x, fallback: y}]
  facade: {name: <Name>, accessor: <name>}  # Facade
  tables: []                        # جداول DB
  permissions: []                   # مجوزها
  events_emitted: []                # رویدادهای منتشرشده
  events_consumed: []               # رویدادهای مصرف‌شده
  config_file: engines/<name>/config/<name>.php
  config_keys: []                   # کلیدهای config
  public_api:
    - class: <Name>Engine
      methods: []
  loc_estimate: 0                   # برآورد LOC
  acceptance:                       # معیار پذیرش
    - {id: AC-<NAME>-01, test: 'tests/Unit/…'}
```

### چطور از آن استفاده کنید؟

بلوک YAML به شما می‌گوید:

1. **`depends_on`** — چه موتورهایی باید قبلاً پیاده شده باشند (شما می‌توانید به آن‌ها وابسته باشید).
2. **`events_emitted`** و **`events_consumed`** — چه رویدادهایی را منتشر/مصرف می‌کنید.
3. **`tables`** — چه جداول DB باید ساخته شوند (مرحلهٔ migration).
4. **`acceptance`** — چه تست‌هایی باید بنویسید.
5. **`public_api`** — چه کلاس/متدهایی باید پیاده کنید.

> **نکته:** ابزار `audit_tavaan.py` این بلوک‌ها را به‌صورت خودکار بررسی می‌کند. اگر YAML شما با کد نمی‌خواند، ممیزی رد می‌شود.

---

## مرحله ۶ — چطور Interface تعریف کنیم 🔧

قاعدهٔ R5: هر خروجی عمومی = Interface. این یعنی قبل از پیاده‌سازی کلاس، Interface آن را در `core/Contracts/` یا `engines/<name>/src/Contracts/` تعریف کنید.

### نمونه

```php
<?php
declare(strict_types=1);

namespace Tavaan\Engine\Cache\Contracts;

interface CacheStoreInterface
{
    public function get(string $key): mixed;
    public function set(string $key, mixed $value, int $ttl = 0): bool;
    public function forget(string $key): bool;
    public function has(string $key): bool;
    public function flush(): bool;
}
```

### قواعد

| قاعده | توضیح |
|---|---|
| 🔒 بدون پیشوند `I` | نه `ICache`، بلکه `CacheInterface` یا `Cacheable`. |
| 🔒 پسوند `*Interface` یا `*able` | استاندارد تَوان. |
| 🔒 `declare(strict_types=1);` | در هر فایل. |
| 🔒 namespace از ریشهٔ ثبت‌شده | `Tavaan\Engine\<Name>\Contracts`. |
| ⚠️ متدها با فعل | `get`، `set`، `forget`. |

---

## مرحله ۷ — چطور پیاده‌سازی کنیم ⚙️

ساختار پوشهٔ موتور:

```
engines/<name>/
├── engine.json              ← manifest موتور
├── config/
│   └── <name>.php           ← پیکربندی پیش‌فرض
├── src/
│   ├── Contracts/           ← Interfaceها
│   ├── Exceptions/          ← Exceptionها
│   ├── <Name>Engine.php     ← کلاس اصلی موتور
│   ├── <Name>ServiceProvider.php  ← ServiceProvider
│   └── ...                  ← کلاس‌های دیگر
└── tests/
    └── <Name>EngineTest.php
```

### نمونهٔ `engine.json`

```json
{
    "id": "tavaan.engine.greeting",
    "name": "Greeting",
    "namespace": "Tavaan\\Engine\\Greeting\\",
    "path": "engines/greeting",
    "priority": "P3",
    "phase": "M9",
    "depends_on": ["container", "config"],
    "facade": {
        "name": "Greeting",
        "accessor": "greeting"
    },
    "config_file": "engines/greeting/config/greeting.php",
    "loc_estimate": 200
}
```

### نمونهٔ ServiceProvider

```php
<?php
declare(strict_types=1);

namespace Tavaan\Engine\Greeting;

use Tavaan\Core\Container\ServiceProvider;
use Tavaan\Engine\Greeting\Contracts\GreetingInterface;

class GreetingServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        $this->app->singleton(
            GreetingInterface::class,
            GreetingEngine::class
        );
    }

    public function boot(): void
    {
        // ثبت قابلیت‌ها
    }
}
```

### نمونهٔ Facade

```php
<?php
declare(strict_types=1);

namespace Tavaan\Engine\Greeting\Facades;

use Tavaan\Core\Facade\Facade;

/**
 * @method static string sayHello(string $name)
 * @mixin \Tavaan\Engine\Greeting\Contracts\GreetingInterface
 */
class Greeting extends Facade
{
    protected static function accessor(): string
    {
        return 'greeting';
    }
}
```

---

## مرحله ۸ — چطور تست بنویسیم 🧪

قاعدهٔ R10: قبل از Merge، تست + PHPStan + Benchmark. قاعدهٔ R6: هر موتور باید Provider + Interface + Tests + Docs + Benchmark داشته باشد.

### از معیار پذیرش شروع کنید

بخش ۱۴ مستند موتور، جدول AC است. هر AC باید به یک تست تبدیل شود:

| AC ID | معیار | تست |
|---|---|---|
| AC-CACHE-01 | set/get در ≤۱µs | `tests/Unit/Cache/CacheSetGetTest.php` |
| AC-CACHE-02 | forget پاک می‌کند | `tests/Unit/Cache/CacheForgetTest.php` |

### نام‌گذاری تست

قاعده: `test<Behavior>_<Condition>_<Expectation>`

```php
public function testSet_WithValidKey_ReturnsTrue(): void
{
    $cache = new CacheEngine();
    $this->assertTrue($cache->set('foo', 'bar', 60));
}

public function testGet_WithMissingKey_ReturnsNull(): void
{
    $cache = new CacheEngine();
    $this->assertNull($cache->get('missing'));
}
```

### سناریوهای تست

هر موتور باید پنج نوع تست داشته باشد:

| نوع | هدف |
|---|---|
| Unit | تک‌کلاس، بدون وابستگی |
| Feature | رفتار موتور با کانتینر واقعی |
| Integration | با موتورهای دیگر |
| Benchmark | کارایی (اهداف در بخش ۱۰) |
| Security | کنترل‌های بخش ۹ |

---

## مرحله ۹ — چطور DoD را تأیید کنیم ✅

قبل از اعلام `status: done`، چک‌لیست DoD (Definition of Done، DOC-113) را بگذرانید:

- [ ] همهٔ AC-ها در بخش ۱۴ پوشش داده شده‌اند.
- [ ] `php -l` روی همهٔ فایل‌ها بدون خطا.
- [ ] PHPStan در سطح تعیین‌شده بدون خطا.
- [ ] همهٔ تست‌ها سبز.
- [ ] Benchmark در محدودهٔ هدف.
- [ ] بخش‌های ۹/۱۰/۱۲ با نتایج واقعی پر شده‌اند.
- [ ] بلوک YAML بخش ۱۷ با کد سازگار است.
- [ ] `audit_tavaan.py` بدون خطا.
- [ ] PR توضیحات کامل دارد.
- [ ] مرتبط: تیکت در `agent-backlog.md` به `status: done` تغییر یافته.

---

## قواعد سخت برای ایجنت 🔒

این قواعد، نقضشان = ریجکت PR.

| # | قاعده | توضیح |
|---|---|---|
| R1 | `declare(strict_types=1);` | در هر فایل PHP |
| R2 | فقط Autoloader هسته | بدون `require`/`include` دستی |
| R3 | هیچ پکیج خارجی | ZeroDependency — بدون `use Psr\`، بدون `vendor/` |
| R4 | بدون Property پویا | هر ویژگی باید تعریف شود |
| R5 | هر خروجی عمومی = Interface | قبل از کلاس، Interface بنویسید |
| R6 | Provider + Interface + Tests + Docs + Benchmark | برای هر موتور |
| R7 | namespace از ریشهٔ ثبت‌شده | `Tavaan\Engine\<Name>\` و امضا |
| R8 | خطا = Exception با کد + MessageId | نه `die()`، نه `return false` |
| R9 | Prepared Statement فقط | نه SQL رشته‌ای |
| R10 | تست + PHPStan + Benchmark قبل از Merge | هیچ استثنایی |

---

## الگوهای طراحی رایج در تَوان 🧠

| الگو | کاربرد | نمونه |
|---|---|---|
| ServiceProvider + Facade | ثبت سرویس و دسترسی ساده | هر موتور |
| Manager/Driver | چند-درایوری | `Cache` (file/db/redis) |
| Contract → Implementation | جداسازی رابط از پیاده | همهٔ موتورها |
| Pipeline | خط لوله میان‌افزار | HTTP Kernel |
| Pub/Sub | رویداد | EventDispatcher |
| Repository | انتزاع از داده | ORM |
| Value Object | شیء تغییرناپذیر | `Money`، `Email` |

---

## ابزارهای کمکی 🛠️

| ابزار | مسیر | کاربرد |
|---|---|---|
| `verify_docs.py` | `tools/scripts/verify_docs.py` | اعتبارسنجی مستندات |
| `audit_tavaan.py` | `tools/scripts/audit_tavaan.py` | ممیزی انطباق پروژه |
| `gen_engine_docs.py` | `scripts/gen_engine_docs.py` | تولید مستند موتور |
| `bin/tvn engines` | (در پروژهٔ پیاده‌شده) | لیست موتورهای نصب‌شده |
| `bin/tvn info` | (در پروژهٔ پیاده‌شده) | اطلاعات سیستم |

---

## خطاهای رایج ایجنت‌ها ⚠️

| خطا | راه‌حل |
|---|---|
| شروع تیکت قبل از done شدن وابستگی | الگوریتم انتخاب را دقیق اجرا کنید |
| نوشتن کد قبل از مستندات | Docs-First — اول سند، بعد کد |
| استفاده از `Psr\*` یا `Symfony\*` | ممنوع — ZeroDependency |
| Property پویا (`$obj->foo = 'bar'`) | ممنوع — R4 |
| SQL رشته‌ای | ممنوع — Prepared Statement (R9) |
| `catch` خالی یا `@` suppression | ممنوع — P6 (Fail Fast & Loud) |
| نقض R5 (خروجی عمومی بدون Interface) | قبل از کلاس، Interface بنویسید |
| PR بدون تست | ممنوع — R10 |
| نقض قواعد نام‌گذاری | مرجع: `skills/tavaan-doc-writer/references/conventions.md` |

---

## نمونهٔ یک اجرای کامل (با موتور Greeting) 🎯

فرض کنید تیکت `TVN-0092` برای ساخت موتور `greeting` به شما اختصاص داده شده.

### گام ۱ — انتخاب
```yaml
ticket:
  id: TVN-0092
  title: ساخت موتور Greeting (نمونه آموزشی)
  phase: M9
  engine: tavaan.engine.greeting
  type: engine
  priority: P3
  depends_on: [TVN-0001]  # container
  estimate_loc: 200
  docs: [DOC-150]
  acceptance:
    - AC-GREET-01: sayHello(name) → "سلام، {name}!"
    - AC-GREET-02: sayBye(name) → "خدانگهدار، {name}!"
  status: todo
```

### گام ۲ — مطالعه
- `docs/03-engines/README.md`
- `docs/templates/engine-spec-template.md`
- `skills/tavaan-doc-writer/references/conventions.md`

### گام ۳ — ساخت پوشه
```
docs/03-engines/greeting/
├── README.md
├── 01-goal-scope.md
├── ... (۱۷ بخش)
└── 17-machine-readable.yml
```

### گام ۴ — پر کردن بخش‌های ۱-۷
(به‌عنوان تمرین)

### گام ۵ — تعریف Interface
```php
// engines/greeting/src/Contracts/GreetingInterface.php
namespace Tavaan\Engine\Greeting\Contracts;
interface GreetingInterface {
    public function sayHello(string $name): string;
    public function sayBye(string $name): string;
}
```

### گام ۶ — پیاده‌سازی
```php
// engines/greeting/src/GreetingEngine.php
namespace Tavaan\Engine\Greeting;
use Tavaan\Engine\Greeting\Contracts\GreetingInterface;
class GreetingEngine implements GreetingInterface {
    public function sayHello(string $name): string {
        return "سلام، {$name}!";
    }
    public function sayBye(string $name): string {
        return "خدانگهدار، {$name}!";
    }
}
```

### گام ۷ — ServiceProvider + Facade
(طبق نمونه‌های بالا)

### گام ۸ — تست
```php
// engines/greeting/tests/GreetingEngineTest.php
public function testSayHello_WithName_ReturnsGreeting(): void {
    $g = new GreetingEngine();
    $this->assertSame('سلام، Ali!', $g->sayHello('Ali'));
}
```

### گام ۹ — DoD
- [x] AC-GREET-01 تست شده
- [x] AC-GREET-02 تست شده
- [x] `php -l` موفق
- [x] PHPStan موفق
- [x] YAML بخش ۱۷ پر شده
- [x] PR آماده

### گام ۱۰ — اعلام
تیکت را به `status: review` بگذارید و PR بزنید.

---

## منابع برای مطالعهٔ بیشتر 📚

- [`../01-standards/php82-strict.md`](../01-standards/php82-strict.md) — قواعد PHP 8.2+
- [`../01-standards/documentation-standard.md`](../01-standards/documentation-standard.md) — استاندارد مستندسازی
- [`../07-quality/definition-of-done.md`](../07-quality/definition-of-done.md) — DoD کامل
- [`../08-roadmap/agent-backlog.md`](../08-roadmap/agent-backlog.md) — بک‌لاگ کامل
- [`../adr/`](../adr/) — همهٔ ADRها
- [`../templates/engine-spec-template.md`](../templates/engine-spec-template.md) — قالب موتور
- [`../examples/first-engine.md`](../examples/first-engine.md) — آموزش گام‌به‌گام ساخت اولین موتور
- [`skills/tavaan-doc-writer/SKILL.md`](../../skills/tavaan-doc-writer/SKILL.md) — مهارت کامل نگارش مستندات

---

## کلام پایانی 🤖

شما به‌عنوان ایجنت، عضوی از جامعهٔ سازندهٔ تَوان هستید. هر خط کدی که می‌نویسید، هر مستندی که کامل می‌کنید، یک آجر در خانهٔ تَوان است.

سه چیز را در یاد داشته باشید:

1. **سند اول است.** همیشه.
2. **قواعد سخت، دوست شما هستند.** نه دشمن.
3. **هر تیکت، یک قدم به ۱.۰.۰ نزدیک‌تر.**

موفق باشید. 🚀

---

> **@TavaanOfficial**
> *«ایجنت خوب، ایجنتی است که ابتدا می‌خواند، بعد می‌نویسد — و هرگز بدون نقشه، آجر نمی‌گذارد.»* 🤖
