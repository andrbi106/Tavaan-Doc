# DOC-082 — موتور Workflow | گردش‌کار

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-082 |
| Engine ID | `tavaan.engine.workflow` |
| Namespace | `Tavaan\Engine\Workflow\` |
| مسیر | `engines/workflow/` |
| وضعیت | Draft v0.0.1 |
| اولویت | P2 |
| فاز ساخت | M7 |
| وابستگی (سخت) | `config` |
| وابستگی (نرم/اختیاری) | `event`, `database`, `migration`, `rbac`, `queue`, `console`, `auth` |
| Facade | `Workflow` → accessor `workflow` |
| جداول DB | `tvn_workflows`, `tvn_process_instances`, `tvn_process_tasks`, `tvn_process_history` |
| LOC برآوردی | 2688 |
| مسئول | @andrbi106 |
| مرتبط | DOC-030 |

---

## ۱. هدف و دامنه

### ۱٫۱ هدف (Why)
موتور Workflow مدیریت فرآیندهای کسب‌وکار را با state machine، activity، trigger، transition و persistence فراهم می‌کند و اتوماسیون فرآیندهای طولانی را ممکن می‌سازد.

### ۱٫۲ دامنه (What)
- ✅ شامل: WorkflowManager، state machine، activities، triggers، transitions، persistence
- ❌ خارج از دامنه: Queue (در queue)، Schedule (در schedule)

### ۱٫۳ الزامات پوشش‌داده‌شده
| ID | الزام |
|---|---|
| FR-WF-01 | پیاده‌سازی هستهٔ موتور workflow به‌عنوان سرویس مستقل با Service Provider و Facade |
| FR-WF-02 | یکپارچگی با Container و سیستم پیکربندی Tavaan |
| FR-WF-03 | بارگذاری خودکار با autoload namespace-map طبق engine.json |

### ۱٫۴ مقایسه با مراجع
| مرجع | چه چیزی بهتر است | چه چیزی را تغییر دادیم | چرا |
|---|---|---|---|
| Laravel Workflow + Symfony Workflow | اکوسیستم بالغ، مستندات گسترده | جداسازی به‌عنوان موتور مستقل قابل نصب/حذف، پشتیبانی فارسی RTL در هسته | ZeroDependency، ماژولار بودن، بومی‌سازی |

---

## ۲. مفاهیم و واژگان
| واژه | تعریف |
|---|---|
| Engine | بستهٔ نرم‌افزاری مستقل در `engines/<name>/` با Service Provider و autoload |
| Service Provider | کلاس ثبت سرویس‌ها در Container و publish config/lang |
| Facade | accessor استاتیک برای دسترسی به سرویس موتور از Container |
| Namespace | پیشوند PSR-4 مخصوص موتور (مثلاً `Tavaan\Engine\Workflow\`) |
| ZeroDependency | بدون نیاز به ext-* خارجی یا composer package سنگین |

---

## ۳. معماری داخلی

### ۳٫۱ فهرست کلاس‌ها
بر اساس بررسی `src/` (در مجموع 32 فایل PHP):

| کلاس | نوع | مسئولیت |
|---|---|---|
| `WorkflowListCommand` | Command | `src/Console/WorkflowListCommand.php` |
| `WorkflowTimersCommand` | Command | `src/Console/WorkflowTimersCommand.php` |
| `Duration` | Class | `src/Duration.php` |
| `ProcessTransitioned` | Class | `src/Events/ProcessTransitioned.php` |
| `TaskCreated` | Class | `src/Events/TaskCreated.php` |
| `WorkflowCanceled` | Class | `src/Events/WorkflowCanceled.php` |
| `WorkflowCompleted` | Class | `src/Events/WorkflowCompleted.php` |
| `WorkflowStarted` | Class | `src/Events/WorkflowStarted.php` |
| `IllegalTransitionException` | Exception | `src/Exceptions/IllegalTransitionException.php` |
| `ProcessDefinitionException` | Exception | `src/Exceptions/ProcessDefinitionException.php` |
| `TaskException` | Exception | `src/Exceptions/TaskException.php` |
| `WorkflowException` | Exception | `src/Exceptions/WorkflowException.php` |
| `Workflow` | Facade | `src/Facades/Workflow.php` |
| `ProcessBuilder` | Builder | `src/ProcessBuilder.php` |
| `ProcessContext` | Class | `src/ProcessContext.php` |
| `ProcessDefinition` | Class | `src/ProcessDefinition.php` |
| `ProcessInstance` | Class | `src/ProcessInstance.php` |
| `StateDefinition` | Class | `src/StateDefinition.php` |
| `StateFluent` | Class | `src/StateFluent.php` |
| `StateType` | Class | `src/StateType.php` |
| `ArrayStore` | Store | `src/Store/ArrayStore.php` |
| `DatabaseStore` | Store | `src/Store/DatabaseStore.php` |
| `StoreInterface` | Contract/Interface | `src/Store/StoreInterface.php` |
| `Task` | Class | `src/Task.php` |
| `TimerDefinition` | Class | `src/TimerDefinition.php` |
| `TimerProcessor` | Class | `src/TimerProcessor.php` |
| `TransitionDefinition` | Class | `src/TransitionDefinition.php` |
| `TransitionFluent` | Class | `src/TransitionFluent.php` |
| `Visualizer` | Class | `src/Visualizer.php` |
| `WorkflowEngine` | Engine | `src/WorkflowEngine.php` |
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
فایل پیکربندی این موتور در `engines/workflow/config/workflow.php` قرار دارد (در صورت وجود). کلید پیکربندی در Repository: `engines.workflow.config.workflow`.

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
| AC-WORKFLOW-01 | موتور بدون خطا بوت می‌شود | `php bin/tvn engines` |
| AC-WORKFLOW-02 | Service Provider در Container ثبت می‌شود | `php bin/tvn engines --list` |

## ۱۵. محدودیت‌ها
- v0.0.1: اسکلت اولیه، بدون پیاده‌سازی کامل
- API عمومی هنوز ثابت نشده است
- آزمون‌های خودکار هنوز نوشته نشده‌اند

## ۱۶. مراجع
| منبع | الهام‌گرفته شد |
|---|---|
| Laravel Workflow + Symfony Workflow | طراحی API و الگوهای Service Provider/Facade |

## ۱۷. بلوک ماشین‌خوان 🧠

```yaml
# machine-readable: tavaan.engine.workflow.v1
engine:
  id: tavaan.engine.workflow
  namespace: Tavaan\Engine\Workflow\
  path: engines/workflow
  priority: P2
  phase: M7
  depends_on: [config]
  soft_depends_on: [event, database, migration, rbac, queue, console, auth]
  facade: {name: Workflow, accessor: workflow}
  tables: [tvn_workflows, tvn_process_instances, tvn_process_tasks, tvn_process_history]
  config_file: engines/workflow/config/workflow.php
  loc_estimate: 2688
  acceptance:
    - {id: AC-WORKFLOW-01, test: 'php bin/tvn engines'}
    - {id: AC-WORKFLOW-02, test: 'php bin/tvn engines --list'}
```
