# DOC-068-S03 — معماری داخلی (موتور realtime)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-068-S03 |
| موتور | `realtime` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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

---

## چک‌لیست ممیزی عملیاتی

- [ ] نمودار اجزا (ASCII/Mermaid) موجود است
- [ ] فهرست کلاس‌ها با نوع/مسئولیت موجود است
- [ ] نمودار توالی جریان اصلی موجود است
- [ ] نمودار وضعیت (در صورت State Machine) موجود است
- [ ] الگوهای طراحی ذکر شده

---

## وضعیت ممیزی

| شاخص | وضعیت |
|---|---|
| وضعیت محتوا | ✅ دارای محتوا |
| تعداد آیتم‌های چک‌لیست | 5 |
| نیاز به تکمیل | ✅ خیر |

---

## یادداشت‌های ممیزی‌کننده

> این بخش توسط ممیزی‌کننده پر می‌شود.

- **تاریخ ممیزی:** _TODO_
- **ممیزی‌کننده:** _TODO_
- **یادداشت:** _TODO_
