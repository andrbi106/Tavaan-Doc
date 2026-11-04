# DOC-123 — بک‌لاگ ایجنت (فاز M0-M25)

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-123 |
| وضعیت | Approved v0.0.1 |
| نقش | تیکت‌های آمادهٔ ایجنت برای هر فاز |
| پیش‌نیاز | DOC-120, DOC-122 |

## قالب تیکت

```yaml
ticket:
  id: TVN-XXXX
  title: <عنوان>
  phase: M<N>
  engine: <engine-id>
  type: engine|module|feature|fix|docs|test
  priority: P0|P1|P2
  depends_on: [TVN-YYYY]
  estimate_loc: <int>
  docs: [DOC-XXX]
  acceptance: [list]
  status: todo|in_progress|review|done
```

## وضعیت کلی

| فاز | تیکت‌ها | وضعیت |
|---|---|---|
| M0 | ✅ کامل | — |
| M1-M5 | ✅ کامل | — |
| M6-M24 | ⚠️ اسکلت | ۵۲ تیکت |
| M25 | ⬜ آینده | ۸ تیکت |
| **مجموع** | — | **۶۰ تیکت باز** |

---

## تیکت‌های فاز M6 — HTTP بنیاد

### TVN-0060 — تکمیل موتور HTTP
```yaml
ticket:
  id: TVN-0060
  title: تکمیل پیاده‌سازی موتور HTTP
  phase: M6
  engine: tavaan.engine.http
  type: engine
  priority: P0
  depends_on: [TVN-0005]  # M5 engine-core
  estimate_loc: 2800
  docs: [DOC-039]
  acceptance:
    - AC-HTTP-01: Request immutable با PSR-7-like API
    - AC-HTTP-02: Response با status/headers/body
    - AC-HTTP-03: Kernel با middleware pipeline
    - AC-HTTP-04: Server adapter (PHP built-in)
  status: todo
```

---

## تیکت‌های فاز M7 — مسیریابی

### TVN-0070 — تکمیل موتور Router
```yaml
ticket:
  id: TVN-0070
  title: تکمیل Router با Compiled Trie
  phase: M7
  engine: tavaan.engine.router
  type: engine
  priority: P0
  depends_on: [TVN-0060]
  estimate_loc: 1400
  docs: [DOC-040]
  acceptance:
    - AC-ROUTER-01: match در ≤۵µs روی ۱۰۰۰ روت
    - AC-ROUTER-02: پشتیبانی از {param} و {param?}
    - AC-ROUTER-03: گروه‌بندی روت‌ها
    - AC-ROUTER-04: cache کامپایل
  status: todo
```

---

## تیکت‌های فاز M8 — وب پشتیبان

### TVN-0080 — تکمیل موتور Session
```yaml
ticket:
  id: TVN-0080
  title: تکمیل موتور Session
  phase: M8
  engine: tavaan.engine.session
  type: engine
  priority: P0
  depends_on: [TVN-0060]
  estimate_loc: 900
  docs: [DOC-042]
  acceptance:
    - AC-SESSION-01: start/destroy/regenerate
    - AC-SESSION-02: driver file/database/redis
    - AC-SESSION-03: SameSite cookie
  status: todo
```

### TVN-0081 — تکمیل موتور Cookie
```yaml
ticket:
  id: TVN-0081
  title: تکمیل موتور Cookie رمزنگاری‌شده
  phase: M8
  engine: tavaan.engine.cookie
  type: engine
  priority: P0
  depends_on: [TVN-0060]
  estimate_loc: 400
  acceptance:
    - AC-COOKIE-01: set/get/forget
    - AC-COOKIE-02: رمزنگاری با crypt
    - AC-COOKIE-03: HttpOnly + Secure + SameSite
  status: todo
```

### TVN-0082 — تکمیل موتور CORS
```yaml
ticket:
  id: TVN-0082
  title: تکمیل موتور CORS
  phase: M8
  engine: tavaan.engine.cors
  type: engine
  priority: P1
  depends_on: [TVN-0060]
  estimate_loc: 350
  acceptance:
    - AC-CORS-01: preflight handling
    - AC-CORS-02: configurable origins
  status: todo
```

---

## تیکت‌های فاز M9 — نما و i18n

### TVN-0090 — تکمیل موتور View
```yaml
ticket:
  id: TVN-0090
  title: تکمیل موتور View با .tv.php
  phase: M9
  engine: tavaan.engine.view
  type: engine
  priority: P0
  depends_on: [TVN-0005]
  estimate_loc: 1800
  acceptance:
    - AC-VIEW-01: {{ }} escape, {!! !!} raw
    - AC-VIEW-02: @directive (if/foreach/section)
    - AC-VIEW-03: layout و component
    - AC-VIEW-04: cache کامپایل
  status: todo
```

### TVN-0091 — تکمیل موتور Jalali
```yaml
ticket:
  id: TVN-0091
  title: تکمیل موتور Jalali
  phase: M9
  engine: tavaan.engine.jalali
  type: engine
  priority: P1
  depends_on: [TVN-0090]
  estimate_loc: 800
  acceptance:
    - AC-JAL-01: تبدیل میلادی↔جلالی
    - AC-JAL-02: ۱۰۰۰۰ Test Vector
    - AC-JAL-03: فرمت‌بندی فارسی
  status: todo
```

---

## تیکت‌های فاز M10 — دیتابیس

### TVN-0100 — تکمیل موتور Database
```yaml
ticket:
  id: TVN-0100
  title: تکمیل موتور Database
  phase: M10
  engine: tavaan.engine.database
  type: engine
  priority: P0
  depends_on: [TVN-0003]
  estimate_loc: 3200
  docs: [DOC-047]
  acceptance:
    - AC-DB-01: ConnectionManager چنددرایور
    - AC-DB-02: QueryBuilder با prepared statement
    - AC-DB-03: Grammar (MySQL/Postgres/SQLite)
    - AC-DB-04: Transaction با Savepoint
    - AC-DB-05: N+1 detection
    - AC-DB-06: Read/Write Splitting
  status: todo
```

---

## تیکت‌های فاز M11 — طرح و مهاجرت

### TVN-0110 — تکمیل موتور Schema
```yaml
ticket:
  id: TVN-0110
  title: تکمیل موتور Schema Builder
  phase: M11
  engine: tavaan.engine.schema
  type: engine
  priority: P0
  depends_on: [TVN-0100]
  estimate_loc: 1100
  acceptance:
    - AC-SCH-01: create/drop/alter table
    - AC-SCH-02: column types کامل
    - AC-SCH-03: index/unique/foreign key
  status: todo
```

### TVN-0111 — تکمیل موتور Migration
```yaml
ticket:
  id: TVN-0111
  title: تکمیل موتور Migration
  phase: M11
  engine: tavaan.engine.migration
  type: engine
  priority: P0
  depends_on: [TVN-0110]
  estimate_loc: 800
  acceptance:
    - AC-MIG-01: migrate/rollback/status
    - AC-MIG-02: batch migration
    - AC-MIG-03: zero-downtime (در صورت امکان)
  status: todo
```

---

## تیکت‌های فاز M12 — ORM

### TVN-0120 — تکمیل موتور ORM
```yaml
ticket:
  id: TVN-0120
  title: تکمیل موتور ORM (Active Record + Repository)
  phase: M12
  engine: tavaan.engine.orm
  type: engine
  priority: P0
  depends_on: [TVN-0100]
  estimate_loc: 4000
  acceptance:
    - AC-ORM-01: Active Record (find/save/delete)
    - AC-ORM-02: Repository pattern
    - AC-ORM-03: relations (hasOne/hasMany/belongsTo)
    - AC-ORM-04: eager loading
    - AC-ORM-05: casts و mutators
    - AC-ORM-06: soft delete
  status: todo
```

---

## تیکت‌های فاز M13-M24

برای اختصار، فقط عناوین:

| فاز | تیکت | عنوان | موتور | LOC |
|---|---|---|---|---|
| M13 | TVN-0130 | تکمیل Validation | validation | 2200 |
| M13 | TVN-0131 | تکمیل Search | search | 1500 |
| M14 | TVN-0140 | تکمیل Cache | cache | 1400 |
| M14 | TVN-0141 | تکمیل Queue | queue | 2000 |
| M14 | TVN-0142 | تکمیل Schedule | schedule | 800 |
| M15 | TVN-0150 | تکمیل Auth | auth | 2000 |
| M16 | TVN-0160 | تکمیل RBAC | rbac | 1600 |
| M16 | TVN-0161 | تکمیل Security | security | 1500 |
| M16 | TVN-0162 | تکمیل Audit | audit | 700 |
| M17 | TVN-0170 | تکمیل Mail | mail | 900 |
| M17 | TVN-0171 | تکمیل Notification | notification | 1100 |
| M18 | TVN-0180 | تکمیل Media | media | 800 |
| M18 | TVN-0181 | تکمیل HTTP-Client | http-client | 600 |
| M19 | TVN-0190 | تکمیل Observability | observability | 1200 |
| M19 | TVN-0191 | تکمیل Backup | backup | 700 |
| M20 | TVN-0200 | تکمیل Tenancy | tenancy | 1500 |
| M20 | TVN-0201 | تکمیل Feature-Flag | feature-flag | 400 |
| M21 | TVN-0210 | تکمیل API | api | 1000 |
| M21 | TVN-0211 | تکمیل Realtime | realtime | 1200 |
| M22 | TVN-0220 | تکمیل Workflow | workflow | 2000 |
| M22 | TVN-0221 | تکمیل Report | report | 1500 |
| M22 | TVN-0222 | تکمیل Payment | payment | 1800 |
| M23 | TVN-0230 | تکمیل Scaffold | scaffold | 1500 |
| M23 | TVN-0231 | تکمیل Admin | admin | 2000 |
| M23 | TVN-0232 | تکمیل Plugin | plugin | 1200 |
| M24 | TVN-0240 | تکمیل Test Framework | test | 1500 |
| M24 | TVN-0241 | تکمیل Upgrade | upgrade | 800 |

---

## الگوریتم انتخاب تیکت

```
pickNextTicket(agent):
  ready = [t for t in tickets if t.status == 'todo'
           and all(dep.status == 'done' for dep in t.depends_on)]
  if ready is empty:
    return "all blocked or done"
  # اولویت: فاز کمتر → P0 → تیکت با وابستگی بیشتر
  return sorted(ready, key=(phase, priority, -len(depends_on)))[0]
```

---

## گردش کار ایجنت (۹ مرحله)

۱. تیکت را از بک‌لاگ انتخاب کن (الگوریتم بالا)
۲. مستندات مرتبط را بخوان (DOC-010, DOC-011, DOC-012, <engine-doc>)
۳. ساختار پوشه را در DOC-080 بررسی کن
۴. قالب موتور DOC-150 را کپی کن
۵. بخش‌های ۱-۷ را قبل از کد کامل کن (Docs-First)
۶. Interface در `core/Contracts/` تعریف کن
۷. پیاده‌سازی در `engines/<name>/src/`
۸. آزمون از معیار پذیرش (بخش ۱۴) بنویس (TDD)
۹. `php bin/tvn engines` + `php -l` + PHPStan را اجرا کن
