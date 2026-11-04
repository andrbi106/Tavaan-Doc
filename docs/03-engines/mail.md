# DOC-055 — موتور Mail | پست الکترونیک

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-055 |
| Engine ID | `tavaan.engine.mail` |
| Namespace | `Tavaan\Engine\Mail\` |
| مسیر | `engines/mail/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P1 |
| فاز ساخت | M5 |
| وابستگی (سخت) | `config`, `event` |
| وابستگی (نرم/اختیاری) | — |
| Facade | `Mail` → accessor `mailer` |
| جداول DB | — |
| LOC برآوردی | 1716 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Mail ارسال ایمیل را با چند transport (SMTP، Sendmail، Log، Array)، Mailable objects، Markdown، queue و templating فراهم می‌کند.

### ۱٫۲ دامنه (What)
- ✅ شامل: Mailer، transports (SMTP/Sendmail/Log/Array)، Mailable، Markdown، queued mail
- ❌ خارج از دامنه: Notification (در notification)، Queue (در queue)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-MAIL-01 | پیاده‌سازی هستهٔ موتور mail به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-MAIL-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-MAIL-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Mail + Symfony Mailer | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Mail\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 19 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `Attachment` | Class | `src/Attachment.php` |
| `TransportInterface` | Contract/Interface | `src/Contracts/TransportInterface.php` |
| `MessageSending` | Class | `src/Events/MessageSending.php` |
| `MessageSent` | Class | `src/Events/MessageSent.php` |
| `Mail` | Facade | `src/Facades/Mail.php` |
| `SendQueuedMail` | Class | `src/Jobs/SendQueuedMail.php` |
| `MailEngine` | Engine | `src/MailEngine.php` |
| `MailException` | Exception | `src/MailException.php` |
| `MailManager` | Manager | `src/MailManager.php` |
| `MailServiceProvider` | ServiceProvider | `src/MailServiceProvider.php` |
| `Mailable` | Class | `src/Mailable.php` |
| `Mailer` | Class | `src/Mailer.php` |
| `Message` | Class | `src/Message.php` |
| `MimeBuilder` | Builder | `src/MimeBuilder.php` |
| `ArrayAndLogTransports` | Class | `src/Transports/ArrayAndLogTransports.php` |
| `MailTransport` | Class | `src/Transports/MailTransport.php` |
| `SendmailTransport` | Class | `src/Transports/SendmailTransport.php` |
| `SesTransport` | Class | `src/Transports/SesTransport.php` |
| `SmtpTransport` | Class | `src/Transports/SmtpTransport.php` |

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
فایل پیکربندی: `engines/mail/config/mail.php`

کلیدهای اصلی:
`driver`, `log_path`, `from`, `address`, `name`, `smtp`, `host`, `port`, `encryption`, `username`, `password`

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
| AC-MAIL-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-MAIL-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Mail + Symfony Mailer | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.mail.v1
engine:
  id: tavaan.engine.mail
  namespace: Tavaan\Engine\Mail\
  path: engines/mail
  priority: P1
  phase: M5
  depends_on: [config, event]
  soft_depends_on: []
  facade: {name: Mail, accessor: mailer}
  tables: []
  config_file: engines/mail/config/mail.php
  loc_estimate: 1716
  acceptance:
    - {id: AC-MAIL-01, test: 'php bin/tvn engines'}
    - {id: AC-MAIL-02, test: 'php bin/tvn engines --list'}
```
