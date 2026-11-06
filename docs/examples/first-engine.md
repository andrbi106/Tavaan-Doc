# ساخت اولین موتور تَوان — موتور Greeting ⚙️

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-E02 |
| وضعیت | Approved v0.0.1 |
| نقش | آموزش گام‌به‌گام ساخت یک موتور تَوان از صفر |
| سطح | ⭐⭐ متوسط |
| مدت | ~۱ ساعت |
| پیش‌نیاز | تکمیل [`hello-world.md`](./hello-world.md) |
| مخاطب | مبتدی پیشرفته / توسعه‌دهنده میانه / ایجنت |
| مسئول | @TavaanOfficial |

---

## هدف 🎯

در پایان این آموزش، شما خواهید داشت:

- یک موتور تَوان به‌نام `greeting` که قابل نصب و استفاده است.
- فایل `engine.json` (manifest موتور).
- یک ServiceProvider.
- یک Engine Class.
- یک Facade.
- فایل پیکربندی.
- یک تست.
- یک مسیر که از موتور استفاده می‌کند.

«موتور Greeting» ساده است — یک کلاس که `sayHello(name)` و `sayBye(name)` دارد — اما تمام الگوهای یک موتور واقعی تَوان را نشان می‌دهد.

> **تمثیل:** این آموزش، مثل ساختن یک اتاق کوچک در خانهٔ تَوان است. اتاق کوچک است، اما همهٔ مراحل ساختن (نقشه، آجر، گچ، رنگ، مبلمان) را طی می‌کند.

---

## پیش‌نیازها ✅

| چی | توضیح |
|---|---|
| تَوان نصب و اجرا | [`hello-world.md`](./hello-world.md) را تکمیل کرده باشید |
| PHP ≥ ۸.۲ | `php -v` |
| آشنایی با کلاس و Interface | [`../00-learn/glossary-simple.md`](../00-learn/glossary-simple.md) |
| آشنایی با namespace | در PHP، `namespace Tavaan\...` |

---

## ساختار موتور تَوان 📁

هر موتور تَوان این ساختار را دارد:

```
engines/<name>/
├── engine.json              ← manifest موتور
├── config/
│   └── <name>.php           ← پیکربندی پیش‌فرض
├── src/
│   ├── Contracts/           ← Interfaceها
│   ├── Exceptions/          ← Exceptionها
│   ├── Facades/             ← Facadeها
│   ├── <Name>Engine.php     ← کلاس اصلی
│   └── <Name>ServiceProvider.php  ← ServiceProvider
└── tests/
    └── <Name>EngineTest.php
```

ما برای موتور `greeting` این ساختار را می‌سازیم:

```
engines/greeting/
├── engine.json
├── config/greeting.php
├── src/
│   ├── Contracts/GreetingInterface.php
│   ├── Facades/Greeting.php
│   ├── GreetingEngine.php
│   └── GreetingServiceProvider.php
└── tests/GreetingEngineTest.php
```

---

## مرحله ۱ — ساخت پوشه‌ها 📂

در ریشهٔ پروژهٔ تَوان:

```bash
mkdir -p engines/greeting/config
mkdir -p engines/greeting/src/Contracts
mkdir -p engines/greeting/src/Facades
mkdir -p engines/greeting/tests
```

---

## مرحله ۲ — ساخت `engine.json` 📋

فایل `engines/greeting/engine.json` را با این محتوا بسازید:

```json
{
    "id": "tavaan.engine.greeting",
    "name": "Greeting",
    "description": "موتور نمونه برای آموزش ساخت موتور تَوان",
    "namespace": "Tavaan\\Engine\\Greeting\\",
    "path": "engines/greeting",
    "priority": "P3",
    "phase": "M9",
    "depends_on": ["container", "config"],
    "soft_depends_on": [],
    "facade": {
        "name": "Greeting",
        "accessor": "greeting"
    },
    "config_file": "engines/greeting/config/greeting.php",
    "loc_estimate": 200,
    "status": "draft",
    "owner": "@TavaanOfficial"
}
```

### توضیح فیلدها

| فیلد | معنا |
|---|---|
| `id` | شناسه یکتای موتور — `tavaan.engine.<name>` |
| `name` | نام کلاس موتور (PascalCase) |
| `namespace` | ریشهٔ namespace موتور |
| `path` | مسیر فیزیکی پوشه |
| `priority` | P0 (بحرانی) تا P3 (آموزشی) |
| `phase` | فاز ساخت در نقشهٔ راه |
| `depends_on` | موتورهایی که این به آن‌ها وابسته است |
| `facade` | نام و accessor فاساد |
| `config_file` | مسیر فایل پیکربندی |

> **تمثیل:** `engine.json` مثل کارت ملی موتور است — شناسنامهٔ رسمی.

---

## مرحله ۳ — ساخت Interface (قرارداد) 📜

قاعدهٔ R5 تَوان: **هر خروجی عمومی = Interface**. قبل از کلاس اصلی، Interface آن را می‌سازیم.

فایل `engines/greeting/src/Contracts/GreetingInterface.php`:

```php
<?php
declare(strict_types=1);

namespace Tavaan\Engine\Greeting\Contracts;

/**
 * قرارداد موتور Greeting.
 *
 * هر کلاسی که این Interface را پیاده‌سازی کند،
 * یک موتور Greeting معتبر است.
 */
interface GreetingInterface
{
    /**
     * سلام کردن به یک نام.
     *
     * @param  string $name نام گیرنده سلام
     * @return string پیام سلام
     */
    public function sayHello(string $name): string;

    /**
     * خداحافظی از یک نام.
     *
     * @param  string $name نام گیرنده خداحافظی
     * @return string پیام خداحافظی
     */
    public function sayBye(string $name): string;
}
```

### چرا Interface؟

تصور کنید شما صاحب یک رستوران هستید و به آشپز می‌گویید: «من به تو می‌گویم `sayHello`، تو هم باید `sayHello` داشته باشی». این «قرارداد» است — شما نمی‌گویید چطور، فقط می‌گویید «باید داشته باشی».

اگر روزی خواستید موتور `greeting` را با یک موتور دیگر (مثلاً `FancyGreeting`) جایگزین کنید، فقط کافیست Interface همان باشد.

---

## مرحله ۴ — ساخت کلاس اصلی (Engine) ⚙️

فایل `engines/greeting/src/GreetingEngine.php`:

```php
<?php
declare(strict_types=1);

namespace Tavaan\Engine\Greeting;

use Tavaan\Engine\Greeting\Contracts\GreetingInterface;

/**
 * پیاده‌سازی پیش‌فرض موتور Greeting.
 *
 * این کلاس، قرارداد GreetingInterface را پیاده‌سازی می‌کند
 * و پیام‌های سلام و خداحافظی فارسی تولید می‌کند.
 */
class GreetingEngine implements GreetingInterface
{
    /**
     * @param array<string,string> $config پیکربندی موتور
     */
    public function __construct(
        private readonly array $config = []
    ) {}

    public function sayHello(string $name): string
    {
        $prefix = $this->config['hello_prefix'] ?? 'سلام';
        return "{$prefix}، {$name}! 👋";
    }

    public function sayBye(string $name): string
    {
        $prefix = $this->config['bye_prefix'] ?? 'خدانگهدار';
        return "{$prefix}، {$name}! 👋";
    }
}
```

### نکات کد

| ویژگی | توضیح |
|---|---|
| `declare(strict_types=1);` | R1 — در هر فایل |
| `implements GreetingInterface` | R5 — قرارداد قبل از پیاده‌سازی |
| `readonly` property | R4 — بدون property پویا |
| نوع بازگشتی `string` | تایپ اجباری |
| پیکربندی در سازنده | DI — تزریق از بیرون |

---

## مرحله ۵ — ساخت ServiceProvider 🏪

ServiceProvider کلاسی است که موتور را در کانتینر ثبت می‌کند — مثل افتتاح یک مغازه.

فایل `engines/greeting/src/GreetingServiceProvider.php`:

```php
<?php
declare(strict_types=1);

namespace Tavaan\Engine\Greeting;

use Tavaan\Core\Container\ServiceProvider;
use Tavaan\Core\Config\ConfigInterface;
use Tavaan\Engine\Greeting\Contracts\GreetingInterface;

/**
 * ServiceProvider موتور Greeting.
 *
 * این کلاس:
 * ۱) قرارداد GreetingInterface را در کانتینر ثبت می‌کند.
 * ۲) پیکربندی موتور را بارگذاری می‌کند.
 */
class GreetingServiceProvider extends ServiceProvider
{
    /**
     * ثبت سرویس‌ها در کانتینر.
     * در این مرحله، فقط «ثبت» انجام می‌شود — نه اجرا.
     */
    public function register(): void
    {
        $this->app->singleton(GreetingInterface::class, function () {
            // گرفتن پیکربندی موتور
            $config = $this->app->make(ConfigInterface::class);
            $greetingConfig = $config->get('greeting', []);

            // ساخت موتور با پیکربندی
            return new GreetingEngine($greetingConfig);
        });

        // ثبت accessor برای Facade
        $this->app->alias(GreetingInterface::class, 'greeting');
    }

    /**
     * راه‌اندازی موتور پس از ثبت همهٔ سرویس‌ها.
     * اینجا می‌توان شنوندگان رویداد ثبت کرد.
     */
    public function boot(): void
    {
        // موتور Greeting رویدادی ندارد — اینجا خالی است.
    }
}
```

### دو متد مهم ServiceProvider

| متد | کار | ترتیب |
|---|---|---|
| `register()` | ثبت سرویس در کانتینر | اول |
| `boot()` | اجرای کد پس از ثبت همه | بعد از همه |

> **تمثیل:** `register()` مثل نصب تابلو مغازه است. `boot()` مثل روز افتتاح — حالا که همه چیز نصب شده، می‌توان باز کرد.

---

## مرحله ۶ — ساخت Facade 🎮

Facade یک «رابط ساده» برای دسترسی به موتور از طریق کانتینر است.

فایل `engines/greeting/src/Facades/Greeting.php`:

```php
<?php
declare(strict_types=1);

namespace Tavaan\Engine\Greeting\Facades;

use Tavaan\Core\Facade\Facade;

/**
 * Facade موتور Greeting.
 *
 * @method static string sayHello(string $name)
 * @method static string sayBye(string $name)
 * @mixin \Tavaan\Engine\Greeting\Contracts\GreetingInterface
 */
class Greeting extends Facade
{
    /**
     * نام accessor در کانتینر.
     */
    protected static function accessor(): string
    {
        return 'greeting';
    }
}
```

### چرا Facade؟

بدون Facade:
```php
$greeting = $container->make(GreetingInterface::class);
echo $greeting->sayHello('Ali');
```

با Facade:
```php
echo Greeting::sayHello('Ali');
```

> **تمثیل:** Facade مثل کنترل تلویزیون است — به‌جای آنکه بروید پشت تلویزیون و دکمه‌ها را فشار دهید، از یک کنترل از راه دور استفاده می‌کنید.

---

## مرحله ۷ — فایل پیکربندی ⚙️

فایل `engines/greeting/config/greeting.php`:

```php
<?php
declare(strict_types=1);

// پیکربندی پیش‌فرض موتور Greeting

return [
    // پیشوند پیام سلام
    'hello_prefix' => 'سلام',

    // پیشوند پیام خداحافظی
    'bye_prefix' => 'خدانگهدار',

    // فعال‌سازی لاگ
    'log_enabled' => true,
];
```

این فایل به‌طور خودکار توسط `GreetingServiceProvider` بارگذاری می‌شود (در `register()`).

---

## مرحله ۸ — ثبت موتور در پروژه 📋

حالا باید به تَوان بگوییم که این موتور را بارگذاری کند.

در فایل `config/autoload.php` (یا فایل کشف موتورها در پروژهٔ شما)، این مورد را اضافه کنید:

```php
<?php
declare(strict_types=1);

return [
    // ... موتورهای دیگر ...

    'Tavaan\\Engine\\Greeting\\' => __DIR__ . '/../engines/greeting/src/',
];
```

در فایل `config/engines.php` (یا manifest پروژه):

```php
<?php
declare(strict_types=1);

return [
    // ... موتورهای دیگر ...

    'greeting' => [
        'id' => 'tavaan.engine.greeting',
        'provider' => \Tavaan\Engine\Greeting\GreetingServiceProvider::class,
        'enabled' => true,
    ],
];
```

---

## مرحله ۹ — تست موتور 🧪

قاعدهٔ R6 و R10: هر موتور باید تست داشته باشد. قبل از Merge، تست باید سبز.

فایل `engines/greeting/tests/GreetingEngineTest.php`:

```php
<?php
declare(strict_types=1);

namespace Tavaan\Engine\Greeting\Tests;

use PHPUnit\Framework\TestCase;
use Tavaan\Engine\Greeting\GreetingEngine;

/**
 * تست موتور Greeting.
 */
class GreetingEngineTest extends TestCase
{
    private GreetingEngine $engine;

    protected function setUp(): void
    {
        $this->engine = new GreetingEngine([
            'hello_prefix' => 'سلام',
            'bye_prefix' => 'خدانگهدار',
        ]);
    }

    public function testSayHello_WithName_ReturnsGreeting(): void
    {
        $result = $this->engine->sayHello('Ali');
        $this->assertSame('سلام، Ali! 👋', $result);
    }

    public function testSayHello_WithPersianName_ReturnsGreeting(): void
    {
        $result = $this->engine->sayHello('مريم');
        $this->assertSame('سلام، مریم! 👋', $result);
    }

    public function testSayBye_WithName_ReturnsBye(): void
    {
        $result = $this->engine->sayBye('Ali');
        $this->assertSame('خدانگهدار، Ali! 👋', $result);
    }

    public function testSayHello_WithDefaultConfig_UsesDefaultPrefix(): void
    {
        $engine = new GreetingEngine();  // بدون config
        $result = $engine->sayHello('Test');
        $this->assertStringContainsString('سلام', $result);
        $this->assertStringContainsString('Test', $result);
    }

    public function testSayHello_WithCustomPrefix_UsesCustomPrefix(): void
    {
        $engine = new GreetingEngine(['hello_prefix' => 'درود']);
        $result = $engine->sayHello('Ali');
        $this->assertSame('درود، Ali! 👋', $result);
    }
}
```

### اجرای تست

```bash
php bin/tvn test engines/greeting
# یا
vendor/bin/phpunit engines/greeting/tests/
```

خروجی:
```
OK (5 tests, 5 assertions)
```

---

## مرحله ۱۰ — استفاده از موتور در یک مسیر 🛣️

حالا موتور را در یک مسیر وب به‌کار می‌بریم.

در `routes/web.php`:

```php
<?php
declare(strict_types=1);

use Tavaan\Engine\Router\Route;
use Tavaan\Engine\Greeting\Facades\Greeting;

// مسیرهای قبلی شما (مثل /hello)
// ...

// مسیر جدید با استفاده از موتور Greeting
Route::get('/greet-engine/{name}', function (string $name) {
    return Greeting::sayHello($name);
});

Route::get('/bye-engine/{name}', function (string $name) {
    return Greeting::sayBye($name);
});
```

---

## مرحله ۱۱ — اجرا و تست نهایی ✅

سرور توسعه را اجرا کنید:

```bash
php bin/tvn serve
```

در مرورگر:

| URL | خروجی |
|---|---|
| `http://127.0.0.1:8000/greet-engine/Ali` | `سلام، Ali! 👋` |
| `http://127.0.0.1:8000/greet-engine/مریم` | `سلام، مریم! 👋` |
| `http://127.0.0.1:8000/bye-engine/Ali` | `خدانگهدار، Ali! 👋` |

### بررسی نصب موتور

```bash
php bin/tvn engines
```

در لیست باید `greeting` را ببینید:

```
container    ✅ loaded
config       ✅ loaded
event        ✅ loaded
...
greeting     ✅ loaded  ← موتور شما!
...
```

---

## جمع‌بندی — چه ساختید؟ 🎉

شما یک موتور تَوان **کامل** ساختید با:

| بخش | فایل | وضعیت |
|---|---|---|
| Manifest | `engine.json` | ✅ |
| Interface | `GreetingInterface.php` | ✅ |
| Engine | `GreetingEngine.php` | ✅ |
| ServiceProvider | `GreetingServiceProvider.php` | ✅ |
| Facade | `Facades/Greeting.php` | ✅ |
| Config | `config/greeting.php` | ✅ |
| Tests | `GreetingEngineTest.php` | ✅ (۵ تست) |
| Routes | ۲ مسیر وب | ✅ |

این، الگوی **همهٔ موتورهای تَوان** است. موتورهای بزرگ‌تر (مثل `database`، `orm`، `auth`) پیچیده‌ترند، اما ساختار پایه‌شان همین است:

```
Interface → Engine → ServiceProvider → Facade → Config → Tests
```

---

## تمثیل نهایی 🏠

موتور شما، یک «اتاق» در خانهٔ تَوان است:

| بخش موتور | بخش اتاق |
|---|---|
| `engine.json` | نقشه اتاق |
| `Interface` | قرارداد با صاحب خانه |
| `Engine` | خود اتاق |
| `ServiceProvider` | کلید اتاق |
| `Facade` | دستگیره در |
| `Config` | رنگ و مبلمان |
| `Tests` | بازرسی پایان کار |

---

## گام بعدی 🚶

اگر این آموزش را کامل کردید، آماده‌اید برای:

- [`first-module.md`](./first-module.md) — ساخت اولین ماژول تَوان (سطح متوسط).
- [`../00-learn/for-agents.md`](../00-learn/for-agents.md) — راهنمای کامل ایجنت.
- [`../03-engines/event/`](../03-engines/event/) — مطالعهٔ مستندات یک موتور واقعی (۱۷ بخش).
- [`../templates/engine-spec-template.md`](../templates/engine-spec-template.md) — قالب کامل ۱۷بخشی.

---

## چالش اضافی 🧠

برای تمرین بیشتر، این موارد را به موتورتان اضافه کنید:

1. **متد `sayWelcome(name)`** — «خوش آمدی، {name}!»
2. **پشتیبانی از زبان** — اگر `lang=en`، انگلیسی سلام کند.
3. **رویداد `greeting.said`** — وقتی `sayHello` فراخوانی شد، یک رویداد انتشار دهد.
4. **افزودن به بلوک YAML ماشین‌خوان** — فایل `17-machine-readable.yml` بسازید.

---

> **@TavaanOfficial**
> *«هر موتور، یک اتاق است. هر اتاق، یک داستان. داستان شما، اینجا شروع شد.»* 🧱
