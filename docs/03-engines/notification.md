# DOC-059 — موتور Notification | آگاه‌سازی

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-059 |
| Engine ID | `tavaan.engine.notification` |
| Namespace | `Tavaan\Engine\Notification\` |
| مسیر | `engines/notification/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `event` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Notification` → accessor `notification` |
| جداول DB | — |
| LOC برآوردی | 2003 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Notification ارسال اعلان‌های چندکاناله (Mail، SMS، Database، Broadcast، Webhook) را با queued dispatch و on-demand فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: NotificationDispatcher، channels (Mail/SMS/Database/Broadcast/Webhook)، Queued، on-demand
- ❌ خارج از دامنه: Mail (در mail)، Realtime (در realtime)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-NOTIF-01 | پیاده‌سازی هستهٔ موتور notification به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-NOTIF-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-NOTIF-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Notifications | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Notification\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 34 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `AnonymousNotifiable` | Class | `src/AnonymousNotifiable.php` |
| `ArrayNotification` | Class | `src/ArrayNotification.php` |
| `BroadcastChannel` | Class | `src/Channels/BroadcastChannel.php` |
| `Channels` | Class | `src/Channels/Channels.php` |
| `PushChannel` | Class | `src/Channels/PushChannel.php` |
| `TelegramChannel` | Class | `src/Channels/TelegramChannel.php` |
| `WebhookChannel` | Class | `src/Channels/WebhookChannel.php` |
| `Notifiable` | Class | `src/Contracts/Notifiable.php` |
| `NotificationFailed` | Class | `src/Events/NotificationFailed.php` |
| `NotificationSending` | Class | `src/Events/NotificationSending.php` |
| `NotificationSent` | Class | `src/Events/NotificationSent.php` |
| `NotificationException` | Exception | `src/Exceptions/NotificationException.php` |
| `Notification` | Facade | `src/Facades/Notification.php` |
| `SendQueuedNotification` | Class | `src/Jobs/SendQueuedNotification.php` |
| `MailMessage` | Class | `src/Messages/MailMessage.php` |
| `SmsMessage` | Class | `src/Messages/SmsMessage.php` |
| `TelegramMessage` | Class | `src/Messages/TelegramMessage.php` |
| `WebhookMessage` | Class | `src/Messages/WebhookMessage.php` |
| `Notification` | Class | `src/Notification.php` |
| `NotificationEngine` | Engine | `src/NotificationEngine.php` |
| `NotificationManager` | Manager | `src/NotificationManager.php` |
| `NotificationSender` | Class | `src/NotificationSender.php` |
| `NotificationServiceProvider` | ServiceProvider | `src/NotificationServiceProvider.php` |
| `RoutesNotifications` | Class | `src/RoutesNotifications.php` |
| `AbstractHttpSmsGateway` | Class | `src/Sms/AbstractHttpSmsGateway.php` |
| `DeliveryStatus` | Class | `src/Sms/DeliveryStatus.php` |
| `FarazSmsGateway` | Class | `src/Sms/Gateways/FarazSmsGateway.php` |
| `GhasedakGateway` | Class | `src/Sms/Gateways/GhasedakGateway.php` |
| `KavenegarGateway` | Class | `src/Sms/Gateways/KavenegarGateway.php` |
| `MelipayamakGateway` | Class | `src/Sms/Gateways/MelipayamakGateway.php` |
| _(و دیگر کلاس‌ها)_ | — | — |

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
فایل پیکربندی: `engines/notification/config/notification.php`

کلیدهای اصلی:
`channels`, `queue`

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
| AC-NOTIFICATION-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-NOTIFICATION-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Notifications | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.notification.v1
engine:
  id: tavaan.engine.notification
  namespace: Tavaan\Engine\Notification\
  path: engines/notification
  priority: P1
  phase: M5
  depends_on: [config, event]
  soft_depends_on: []
  facade: {name: Notification, accessor: notification}
  tables: []
  config_file: engines/notification/config/notification.php
  loc_estimate: 2003
  acceptance:
    - {id: AC-NOTIFICATION-01, test: 'php bin/tvn engines'}
    - {id: AC-NOTIFICATION-02, test: 'php bin/tvn engines --list'}
```
