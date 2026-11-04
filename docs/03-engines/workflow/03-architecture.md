# DOC-082-S03 — معماری داخلی (موتور workflow)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-082-S03 |
| موتور | `workflow` |
| بخش | ۳ — معماری داخلی |
| وضعیت | Draft v0.0.1 |
| نوع | فایل ممیزی عملیاتی |

---

## محتوای فعلی

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
