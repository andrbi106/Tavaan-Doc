# DOC-068 — موتور Realtime | بلادرنگ

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-068 |
| Engine ID | `tavaan.engine.realtime` |
| Namespace | `Tavaan\Engine\Realtime\` |
| مسیر | `engines/realtime/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P0 |
| فاز ساخت | M2 |
| وابستگی (سخت) | `config`, `event`, `http` |
| وابستگی (نرم/اختیاری) | `database`, `cache`, `queue`, `auth` |
| Facade | — (بدون Facade) |
| جداول DB | — |
| LOC برآوردی | 2027 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Realtime ارتباطات bidirectional را با WebSocket server، broadcasting، presence channel و push integration فراهم می‌کند و قابلیت‌های chat/live dashboard را ممکن می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: WebSocket server، Broadcasting، Presence channels، Push adapters
- ❌ خارج از دامنه: Notification (در notification)، Queue (در queue)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-RT-01 | پیاده‌سازی هستهٔ موتور realtime به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-RT-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-RT-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Echo + Soketi + Reverb | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Realtime\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 20 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Broadcast` | Class | `src/Broadcast.php` |
| `BroadcastingAuthController` | Controller | `src/BroadcastingAuthController.php` |
| `ArrayBroker` | Class | `src/Brokers/ArrayBroker.php` |
| `DatabaseBroker` | Class | `src/Brokers/DatabaseBroker.php` |
| `RedisBroker` | Class | `src/Brokers/RedisBroker.php` |
| `ChannelRegistry` | Class | `src/ChannelRegistry.php` |
| `RealtimeWebSocketCommand` | Command | `src/Console/RealtimeWebSocketCommand.php` |
| `BrokerInterface` | Contract/Interface | `src/Contracts/BrokerInterface.php` |
| `ShouldBroadcast` | Class | `src/Contracts/ShouldBroadcast.php` |
| `RealtimeException` | Exception | `src/Exceptions/RealtimeException.php` |
| `Broadcast` | Facade | `src/Facades/Broadcast.php` |
| `Realtime` | Facade | `src/Facades/Realtime.php` |
| `PresenceManager` | Manager | `src/PresenceManager.php` |
| `RealtimeEngine` | Engine | `src/RealtimeEngine.php` |
| `RealtimeFacadeRoot` | Class | `src/RealtimeFacadeRoot.php` |
| `SseStreamer` | Class | `src/Sse/SseStreamer.php` |
| `WebSocketFrame` | Class | `src/WebSocket/WebSocketFrame.php` |
| `WebSocketProtocolException` | Exception | `src/WebSocket/WebSocketProtocolException.php` |
| `WebSocketServer` | Class | `src/WebSocket/WebSocketServer.php` |
| `realtime` | Class | `src/realtime.php` |

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
فایل پیکربندی این موتور در `engines/realtime/config/realtime.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.realtime.config.realtime`.

در v0.0.1 فقط ساختار اولیه پشتیبانی می‌شود.

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
| AC-REALTIME-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-REALTIME-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Echo + Soketi + Reverb | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.realtime.v1
engine:
  id: tavaan.engine.realtime
  namespace: Tavaan\Engine\Realtime\
  path: engines/realtime
  priority: P0
  phase: M2
  depends_on: [config, event, http]
  soft_depends_on: [database, cache, queue, auth]
  facade: {name: , accessor: }
  tables: []
  config_file: engines/realtime/config/realtime.php
  loc_estimate: 2027
  acceptance:
    - {id: AC-REALTIME-01, test: 'php bin/tvn engines'}
    - {id: AC-REALTIME-02, test: 'php bin/tvn engines --list'}
```
