# DOC-046-S03 — معماری داخلی (موتور event)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-046-S03 |
| موتور | `event` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
