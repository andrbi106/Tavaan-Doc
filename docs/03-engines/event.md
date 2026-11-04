# DOC-046 — موتور Event | رویداد و Outbox

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-046 |
| Engine ID | `tavaan.engine.event` |
| Namespace | `Tavaan\Engine\Event\` |
| مسیر | `engines/event/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M1 |
| وابستگی (سخت) | `container`, `config` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Event` → accessor `events` |
| جداول DB | — |
| LOC برآوردی | 1222 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Event زیرساخت pub/sub داخلی را با Dispatcher، Listener registration، queued listeners و wildcards فراهم می‌کند و ارتباط loosely-coupled بین موتورها را ممکن می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: EventDispatcher، Listener registration، Queued listeners، Wildcard listeners
- ❌ خارج از دامنه: Queue (در queue)، Realtime (در realtime)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-EVENT-01 | پیاده‌سازی هستهٔ موتور event به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-EVENT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-EVENT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Events + Symfony EventDispatcher | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Event\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 15 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `OutboxRelayCommand` | Command | `src/Console/OutboxRelayCommand.php` |
| `DispatcherInterface` | Contract/Interface | `src/Contracts/DispatcherInterface.php` |
| `EventDispatcher` | Class | `src/EventDispatcher.php` |
| `EventEngine` | Engine | `src/EventEngine.php` |
| `EventServiceProvider` | ServiceProvider | `src/EventServiceProvider.php` |
| `EventNotAllowlistedException` | Exception | `src/Exceptions/EventNotAllowlistedException.php` |
| `ListenerException` | Exception | `src/Exceptions/ListenerException.php` |
| `MaxListenersExceededException` | Exception | `src/Exceptions/MaxListenersExceededException.php` |
| `ListenerRegistry` | Class | `src/ListenerRegistry.php` |
| `ListenerResolver` | Class | `src/ListenerResolver.php` |
| `DatabaseOutbox` | Class | `src/Outbox/DatabaseOutbox.php` |
| `OutboxRelay` | Class | `src/OutboxRelay.php` |
| `RegisteredListener` | Class | `src/RegisteredListener.php` |
| `TrieNode` | Class | `src/TrieNode.php` |
| `WildcardMatcher` | Class | `src/WildcardMatcher.php` |

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
فایل پیکربندی: `engines/event/config/event.php`

کلیدهای اصلی:
`fake`, `wildcard_default`, `discovery`, `enabled`, `cache`

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
| AC-EVENT-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-EVENT-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Events + Symfony EventDispatcher | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.event.v1
engine:
  id: tavaan.engine.event
  namespace: Tavaan\Engine\Event\
  path: engines/event
  priority: P0
  phase: M1
  depends_on: [container, config]
  soft_depends_on: []
  facade: {name: Event, accessor: events}
  tables: []
  config_file: engines/event/config/event.php
  loc_estimate: 1222
  acceptance:
    - {id: AC-EVENT-01, test: 'php bin/tvn engines'}
    - {id: AC-EVENT-02, test: 'php bin/tvn engines --list'}
```
