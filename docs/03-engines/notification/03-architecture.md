# DOC-059-S03 — معماری داخلی (موتور notification)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-059-S03 |
| موتور | `notification` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
