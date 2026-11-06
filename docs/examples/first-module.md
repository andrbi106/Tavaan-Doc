# ساخت اولین ماژول تَوان — ماژول Todo 📦

| متادیتا | مقدار |
|---|---|
| DOC-ID | DOC-E03 |
| وضعیت | Approved v0.0.1 |
| نقش | آموزش گام‌به‌گام ساخت یک ماژول HMVC تَوان با CRUD کامل |
| سطح | ⭐⭐ متوسط |
| مدت | ~۲ ساعت |
| پیش‌نیاز | تکمیل [`first-engine.md`](./first-engine.md) |
| مخاطب | توسعه‌دهنده میانه / ایجنت پیاده‌ساز |
| مسئول | @TavaanOfficial |

---

## هدف 🎯

در پایان این آموزش، شما خواهید داشت:

- یک ماژول تَوان به‌نام `todo` با عملیات CRUD کامل (ایجاد، خواندن، ویرایش، حذف).
- تعریف Contract و Entity.
- Migration و Repository.
- Routes و Controllers.
- Views (نماها) با قالب `.tv.php`.
- سیستم مجوزها.
- تست ماژول.

«ماژول Todo» یک کارهای-روزانه ساده است، اما تمام الگوهای یک ماژول HMVC واقعی تَوان را نشان می‌دهد.

> **تفاوت با موتور:** موتور (مثل `greeting`) یک «ابزار» است — یک قابلیت تکنیکی. ماژول (مثل `todo`) یک «دامنهٔ کاربردی» است — یک بخش از کسب‌وکار. موتورها قلب تَوان‌اند، ماژول‌ها اتاق‌های آن.

---

## پیش‌نیازها ✅

| چی | توضیح |
|---|---|
| تَوان نصب و اجرا | [`hello-world.md`](./hello-world.md) |
| موتور Greeting ساخته | [`first-engine.md`](./first-engine.md) |
| آشنایی با HMVC و CRUD | [`../00-learn/glossary-simple.md`](../00-learn/glossary-simple.md) |
| موتور Database نصب | برای ذخیره‌سازی واقعی |

---

## ساختار ماژول تَوان 📁

هر ماژول تَوان این ساختار را دارد (بر اساس الگوی HMVC):

```
modules/<name>/
├── module.json             ← manifest ماژول
├── config/
│   └── <name>.php          ← پیکربندی ماژول
├── src/
│   ├── Contracts/          ← Interfaceها
│   ├── Controllers/        ← کنترلرها
│   ├── Entities/           ← موجودیت‌ها
│   ├── Repositories/       ← انبارها (دسترسی داده)
│   ├── Requests/           ← درخواست‌های اعتبارسنجی
│   ├── Services/           ← سرویس‌های دامنه
│   └── <Name>ServiceProvider.php
├── Database/
│   ├── Migrations/         ← مهاجرت‌ها
│   └── Seeders/            ← داده‌های اولیه
├── Routes/
│   ├── web.php             ← مسیرهای وب
│   └── api.php             ← مسیرهای API
├── Resources/
│   ├── views/              ← نماها
│   └── lang/               ← زبان‌ها
└── Tests/
    └── <Name>Test.php
```

برای `todo`:

```
modules/todo/
├── module.json
├── config/todo.php
├── src/
│   ├── Contracts/
│   │   ├── TodoInterface.php
│   │   └── TodoRepositoryInterface.php
│   ├── Controllers/
│   │   └── TodoController.php
│   ├── Entities/
│   │   └── Todo.php
│   ├── Repositories/
│   │   └── TodoRepository.php
│   ├── Requests/
│   │   └── StoreTodoRequest.php
│   └── TodoServiceProvider.php
├── Database/
│   └── Migrations/
│       └── 2026_11_06_120000_create_todos_table.php
├── Routes/
│   ├── web.php
│   └── api.php
├── Resources/
│   └── views/
│       ├── index.tv.php
│       ├── show.tv.php
│       ├── create.tv.php
│       └── edit.tv.php
└── Tests/
    └── TodoModuleTest.php
```

---

## مرحله ۱ — ساخت پوشه‌ها 📂

```bash
mkdir -p modules/todo/{config,src/{Contracts,Controllers,Entities,Repositories,Requests}}
mkdir -p modules/todo/Database/{Migrations,Seeders}
mkdir -p modules/todo/Routes
mkdir -p modules/todo/Resources/{views,lang/fa}
mkdir -p modules/todo/Tests
```

---

## مرحله ۲ — فایل `module.json` 📋

فایل `modules/todo/module.json`:

```json
{
    "id": "tavaan.module.todo",
    "name": "Todo",
    "description": "ماژول مدیریت کارهای روزانه با CRUD کامل",
    "namespace": "Modules\\Todo\\",
    "path": "modules/todo",
    "type": "hmvc",
    "priority": "P2",
    "phase": "M19",
    "depends_on": ["core-user", "database"],
    "soft_depends_on": ["validation"],
    "permissions": [
        "todo.view",
        "todo.create",
        "todo.update",
        "todo.delete"
    ],
    "events_emitted": [
        "todo.created",
        "todo.updated",
        "todo.completed",
        "todo.deleted"
    ],
    "events_consumed": [],
    "config_file": "modules/todo/config/todo.php",
    "owner": "@TavaanOfficial",
    "status": "draft"
}
```

### توضیح فیلدها

| فیلد | معنا |
|---|---|
| `id` | شناسه یکتای ماژول |
| `type` | نوع ماژول: `hmvc`، `simple` |
| `depends_on` | موتورها/ماژول‌های مورد نیاز |
| `permissions` | مجوزهای تعریف‌شده |
| `events_emitted` | رویدادهایی که این ماژول منتشر می‌کند |

---

## مرحله ۳ — Entity (موجودیت) 📝

Entity، نمایش «شیء» دامنه است — اینجا، یک کار.

فایل `modules/todo/src/Entities/Todo.php`:

```php
<?php
declare(strict_types=1);

namespace Modules\Todo\Entities;

/**
 * موجودیت Todo — یک کار روزانه.
 */
class Todo
{
    public function __construct(
        public readonly ?int $id = null,
        public readonly ?int $user_id = null,
        public string $title = '',
        public ?string $description = null,
        public bool $is_completed = false,
        public ?string $due_date = null,
        public ?string $created_at = null,
        public ?string $updated_at = null,
    ) {}

    /**
     * ساختن Entity از داده‌های دیتابیس.
     */
    public static function fromArray(array $data): self
    {
        return new self(
            id: $data['id'] ?? null,
            user_id: $data['user_id'] ?? null,
            title: $data['title'] ?? '',
            description: $data['description'] ?? null,
            is_completed: (bool) ($data['is_completed'] ?? false),
            due_date: $data['due_date'] ?? null,
            created_at: $data['created_at'] ?? null,
            updated_at: $data['updated_at'] ?? null,
        );
    }

    /**
     * تبدیل Entity به آرایه (برای ذخیره در DB).
     */
    public function toArray(): array
    {
        return [
            'id' => $this->id,
            'user_id' => $this->user_id,
            'title' => $this->title,
            'description' => $this->description,
            'is_completed' => $this->is_completed,
            'due_date' => $this->due_date,
            'created_at' => $this->created_at,
            'updated_at' => $this->updated_at,
        ];
    }
}
```

---

## مرحله ۴ — Contracts (قراردادها) 📜

### ۴.۱ Repository Interface

فایل `modules/todo/src/Contracts/TodoRepositoryInterface.php`:

```php
<?php
declare(strict_types=1);

namespace Modules\Todo\Contracts;

use Modules\Todo\Entities\Todo;

/**
 * قرارداد انبار Todo.
 * پیاده‌سازی واقعی می‌تواند Database، InMemory یا Redis باشد.
 */
interface TodoRepositoryInterface
{
    public function find(int $id): ?Todo;
    public function all(int $userId, int $limit = 20, int $offset = 0): array;
    public function create(array $data): Todo;
    public function update(int $id, array $data): ?Todo;
    public function delete(int $id): bool;
    public function markCompleted(int $id, bool $completed = true): ?Todo;
}
```

### ۴.۲ Service Interface

فایل `modules/todo/src/Contracts/TodoInterface.php`:

```php
<?php
declare(strict_types=1);

namespace Modules\Todo\Contracts;

use Modules\Todo\Entities\Todo;

/**
 * قرارداد سرویس Todo — لایهٔ کاربرد.
 */
interface TodoInterface
{
    public function listTodos(int $userId): array;
    public function getTodo(int $id): ?Todo;
    public function createTodo(array $data, int $userId): Todo;
    public function updateTodo(int $id, array $data): ?Todo;
    public function deleteTodo(int $id): bool;
    public function completeTodo(int $id): ?Todo;
}
```

> **چرا دو Interface؟** Repository با داده سر و کار دارد (پایین). Service با منطق کسب‌وکار (بالا). جداسازی این دو، یک الگوی رایج است.

---

## مرحله ۵ — Repository (انبار) 🗄️

فایل `modules/todo/src/Repositories/TodoRepository.php`:

```php
<?php
declare(strict_types=1);

namespace Modules\Todo\Repositories;

use Tavaan\Engine\Database\ConnectionInterface;
use Modules\Todo\Contracts\TodoRepositoryInterface;
use Modules\Todo\Entities\Todo;

/**
 * پیاده‌سازی Repository با موتور Database تَوان.
 */
class TodoRepository implements TodoRepositoryInterface
{
    private string $table = 'todos';

    public function __construct(
        private readonly ConnectionInterface $db
    ) {}

    public function find(int $id): ?Todo
    {
        $row = $this->db->table($this->table)
            ->where('id', '=', $id)
            ->first();

        return $row ? Todo::fromArray($row) : null;
    }

    public function all(int $userId, int $limit = 20, int $offset = 0): array
    {
        $rows = $this->db->table($this->table)
            ->where('user_id', '=', $userId)
            ->orderBy('created_at', 'DESC')
            ->limit($limit)
            ->offset($offset)
            ->get();

        return array_map(fn ($row) => Todo::fromArray($row), $rows);
    }

    public function create(array $data): Todo
    {
        $data['created_at'] = date('Y-m-d H:i:s');
        $id = $this->db->table($this->table)->insert($data);

        return $this->find($id);
    }

    public function update(int $id, array $data): ?Todo
    {
        $data['updated_at'] = date('Y-m-d H:i:s');
        $this->db->table($this->table)
            ->where('id', '=', $id)
            ->update($data);

        return $this->find($id);
    }

    public function delete(int $id): bool
    {
        return $this->db->table($this->table)
            ->where('id', '=', $id)
            ->delete() > 0;
    }

    public function markCompleted(int $id, bool $completed = true): ?Todo
    {
        return $this->update($id, ['is_completed' => $completed]);
    }
}
```

> **نکته:** از Prepared Statement استفاده شده (R9). هیچ SQL رشته‌ای.

---

## مرحله ۶ — Service (سرویس دامنه) 🧠

فایل `modules/todo/src/TodoService.php` (پیاده‌سازی `TodoInterface`):

```php
<?php
declare(strict_types=1);

namespace Modules\Todo;

use Tavaan\Engine\Event\Facades\Event;
use Modules\Todo\Contracts\TodoInterface;
use Modules\Todo\Contracts\TodoRepositoryInterface;
use Modules\Todo\Entities\Todo;

/**
 * سرویس دامنهٔ Todo.
 * لایهٔ کاربرد — منطق کسب‌وکار اینجاست.
 */
class TodoService implements TodoInterface
{
    public function __construct(
        private readonly TodoRepositoryInterface $repo
    ) {}

    public function listTodos(int $userId): array
    {
        return $this->repo->all($userId);
    }

    public function getTodo(int $id): ?Todo
    {
        return $this->repo->find($id);
    }

    public function createTodo(array $data, int $userId): Todo
    {
        $data['user_id'] = $userId;
        $data['is_completed'] = false;

        $todo = $this->repo->create($data);

        // انتشار رویداد
        Event::dispatch('todo.created', ['todoId' => $todo->id]);

        return $todo;
    }

    public function updateTodo(int $id, array $data): ?Todo
    {
        $todo = $this->repo->update($id, $data);

        if ($todo) {
            Event::dispatch('todo.updated', ['todoId' => $id]);
        }

        return $todo;
    }

    public function deleteTodo(int $id): bool
    {
        $deleted = $this->repo->delete($id);

        if ($deleted) {
            Event::dispatch('todo.deleted', ['todoId' => $id]);
        }

        return $deleted;
    }

    public function completeTodo(int $id): ?Todo
    {
        $todo = $this->repo->markCompleted($id, true);

        if ($todo) {
            Event::dispatch('todo.completed', ['todoId' => $id]);
        }

        return $todo;
    }
}
```

> **نکته:** هر عملیات مهم، یک رویداد منتشر می‌کند (P5 — Events over Calls).

---

## مرحله ۷ — Migration (مهاجرت پایگاه داده) 📊

فایل `modules/todo/Database/Migrations/2026_11_06_120000_create_todos_table.php`:

```php
<?php
declare(strict_types=1);

namespace Modules\Todo\Database\Migrations;

use Tavaan\Engine\Schema\SchemaBuilder;
use Tavaan\Engine\Schema\Blueprint;

/**
 * ساخت جدول todos.
 */
return function (SchemaBuilder $schema): void {
    $schema->create('todos', function (Blueprint $table) {
        $table->bigIncrements('id');
        $table->unsignedBigInteger('user_id');
        $table->string('title', 200);
        $table->text('description')->nullable();
        $table->boolean('is_completed')->default(false);
        $table->date('due_date')->nullable();

        // ستون‌های پایه استاندارد تَوان
        $table->datetime('created_at')->useCurrent();
        $table->datetime('updated_at')->nullable();
        $table->datetime('deleted_at')->nullable();
        $table->unsignedBigInteger('created_by')->nullable();
        $table->unsignedBigInteger('updated_by')->nullable();
        $table->unsignedBigInteger('tenant_id')->nullable();
        $table->unsignedInteger('version')->default(1);

        // ایندکس‌ها
        $table->index('idx_todos_user_id', ['user_id']);
        $table->index('idx_todos_due_date', ['due_date']);
        $table->index('idx_todos_is_completed', ['is_completed']);

        // کلید خارجی
        $table->foreign('fk_todos_user_id', 'user_id', 'users', 'id');
    });
};
```

### اجرای Migration

```bash
php bin/tvn migrate
```

خروجی:
```
Migrating: 2026_11_06_120000_create_todos_table
Migrated:  2026_11_06_120000_create_todos_table (0.05s)
```

> **تمثیل:** Migration مثل ساختن قفسه‌های بایگانی است — قبل از آنکه پرونده‌ها را بگذارید، قفسه باید آماده باشد.

---

## مرحله ۸ — Controller 🎮

فایل `modules/todo/src/Controllers/TodoController.php`:

```php
<?php
declare(strict_types=1);

namespace Modules\Todo\Controllers;

use Tavaan\Engine\Http\Request;
use Tavaan\Engine\Http\Response;
use Tavaan\Engine\Router\Route;
use Modules\Todo\Contracts\TodoInterface;

/**
 * کنترلر ماژول Todo.
 */
class TodoController
{
    public function __construct(
        private readonly TodoInterface $todoService
    ) {}

    /**
     * GET /todos — لیست همه کارهای کاربر
     */
    public function index(Request $req): Response
    {
        $userId = $req->user()?->id ?? 1;  // موقتاً کاربر ۱
        $todos = $this->todoService->listTodos($userId);

        return Response::view('todo::index', ['todos' => $todos]);
    }

    /**
     * GET /todos/{id} — نمایش یک کار
     */
    public function show(Request $req, int $id): Response
    {
        $todo = $this->todoService->getTodo($id);

        if (!$todo) {
            return Response::notFound('کار یافت نشد');
        }

        return Response::view('todo::show', ['todo' => $todo]);
    }

    /**
     * GET /todos/create — فرم ساخت کار جدید
     */
    public function create(): Response
    {
        return Response::view('todo::create');
    }

    /**
     * POST /todos — ذخیره کار جدید
     */
    public function store(Request $req): Response
    {
        $data = $req->only(['title', 'description', 'due_date']);
        $userId = $req->user()?->id ?? 1;

        $todo = $this->todoService->createTodo($data, $userId);

        return Response::redirect("/todos/{$todo->id}")
            ->with('success', 'کار با موفقیت ساخته شد.');
    }

    /**
     * GET /todos/{id}/edit — فرم ویرایش
     */
    public function edit(int $id): Response
    {
        $todo = $this->todoService->getTodo($id);

        if (!$todo) {
            return Response::notFound();
        }

        return Response::view('todo::edit', ['todo' => $todo]);
    }

    /**
     * PUT/PATCH /todos/{id} — به‌روزرسانی
     */
    public function update(Request $req, int $id): Response
    {
        $data = $req->only(['title', 'description', 'due_date']);
        $todo = $this->todoService->updateTodo($id, $data);

        return Response::redirect("/todos/{$id}")
            ->with('success', 'کار به‌روزرسانی شد.');
    }

    /**
     * POST /todos/{id}/complete — تکمیل کار
     */
    public function complete(int $id): Response
    {
        $this->todoService->completeTodo($id);

        return Response::redirect('/todos')
            ->with('success', 'کار تکمیل شد! 🎉');
    }

    /**
     * DELETE /todos/{id} — حذف
     */
    public function destroy(int $id): Response
    {
        $this->todoService->deleteTodo($id);

        return Response::redirect('/todos')
            ->with('success', 'کار حذف شد.');
    }
}
```

---

## مرحله ۹ — Routes (مسیرها) 🛣️

### ۹.۱ مسیرهای وب

فایل `modules/todo/Routes/web.php`:

```php
<?php
declare(strict_types=1);

use Tavaan\Engine\Router\Route;
use Modules\Todo\Controllers\TodoController;

// گروه مسیرها با پیشوند /todos و میان‌افزار auth
Route::group([
    'prefix' => '/todos',
    'middleware' => ['auth'],
], function (Route $router) {

    // GET /todos — لیست
    $router->get('/', [TodoController::class, 'index'])
        ->name('todo.index')
        ->middleware('can:todo.view');

    // GET /todos/create — فرم ساخت
    $router->get('/create', [TodoController::class, 'create'])
        ->name('todo.create')
        ->middleware('can:todo.create');

    // POST /todos — ذخیره
    $router->post('/', [TodoController::class, 'store'])
        ->name('todo.store')
        ->middleware('can:todo.create');

    // GET /todos/{id} — نمایش
    $router->get('/{id}', [TodoController::class, 'show'])
        ->name('todo.show')
        ->middleware('can:todo.view')
        ->where('id', '[0-9]+');

    // GET /todos/{id}/edit — فرم ویرایش
    $router->get('/{id}/edit', [TodoController::class, 'edit'])
        ->name('todo.edit')
        ->middleware('can:todo.update')
        ->where('id', '[0-9]+');

    // PUT /todos/{id} — به‌روزرسانی
    $router->put('/{id}', [TodoController::class, 'update'])
        ->name('todo.update')
        ->middleware('can:todo.update')
        ->where('id', '[0-9]+');

    // POST /todos/{id}/complete — تکمیل
    $router->post('/{id}/complete', [TodoController::class, 'complete'])
        ->name('todo.complete')
        ->middleware('can:todo.update')
        ->where('id', '[0-9]+');

    // DELETE /todos/{id} — حذف
    $router->delete('/{id}', [TodoController::class, 'destroy'])
        ->name('todo.delete')
        ->middleware('can:todo.delete')
        ->where('id', '[0-9]+');
});
```

### ۹.۲ مسیرهای API

فایل `modules/todo/Routes/api.php`:

```php
<?php
declare(strict_types=1);

use Tavaan\Engine\Router\Route;
use Modules\Todo\Controllers\TodoController;

Route::group([
    'prefix' => '/api/todos',
    'middleware' => ['api', 'auth:token'],
], function (Route $router) {

    $router->get('/', [TodoController::class, 'index']);
    $router->post('/', [TodoController::class, 'store']);
    $router->get('/{id}', [TodoController::class, 'show']);
    $router->put('/{id}', [TodoController::class, 'update']);
    $router->delete('/{id}', [TodoController::class, 'destroy']);
    $router->post('/{id}/complete', [TodoController::class, 'complete']);
});
```

---

## مرحله ۱۰ — Views (نماها) 🎨

### ۱۰.۱ نمای فهرست

فایل `modules/todo/Resources/views/index.tv.php`:

```php
@extends('layouts.app')

@section('title', 'کارهای من')

@section('content')
<h1>کارهای من 📝</h1>

<a href="{{ route('todo.create') }}" class="btn btn-primary">+ کار جدید</a>

<ul class="todo-list">
    @foreach ($todos as $todo)
    <li class="{{ $todo->is_completed ? 'completed' : '' }}">
        <strong>{{ $todo->title }}</strong>
        @if ($todo->due_date)
            <small>(موعد: {{ jdate($todo->due_date)->format('Y/m/d') }})</small>
        @endif

        <div class="actions">
            <a href="{{ route('todo.show', ['id' => $todo->id]) }}">نمایش</a>
            <a href="{{ route('todo.edit', ['id' => $todo->id]) }}">ویرایش</a>

            @if (!$todo->is_completed)
            <form method="POST" action="{{ route('todo.complete', ['id' => $todo->id]) }}">
                <button type="submit">✓ تکمیل</button>
            </form>
            @endif

            <form method="POST" action="{{ route('todo.delete', ['id' => $todo->id]) }}"
                  onsubmit="return confirm('مطمئنی؟')">
                <input type="hidden" name="_method" value="DELETE">
                <button type="submit">🗑 حذف</button>
            </form>
        </div>
    </li>
    @endforeach
</ul>
@endsection
```

### ۱۰.۲ نمای ساخت

فایل `modules/todo/Resources/views/create.tv.php`:

```php
@extends('layouts.app')

@section('title', 'کار جدید')

@section('content')
<h1>کار جدید ➕</h1>

<form method="POST" action="{{ route('todo.store') }}">
    <div>
        <label>عنوان:</label>
        <input type="text" name="title" required>
    </div>

    <div>
        <label>توضیحات:</label>
        <textarea name="description"></textarea>
    </div>

    <div>
        <label>موعد:</label>
        <input type="date" name="due_date">
    </div>

    <button type="submit" class="btn btn-primary">ذخیره</button>
    <a href="{{ route('todo.index') }}" class="btn">انصراف</a>
</form>
@endsection
```

> **نکته:** در `.tv.php`، `{{ }}` به‌طور خودکار HTML escape می‌کند (R7 — Secure by Default).

---

## مرحله ۱۱ — ServiceProvider 🏪

فایل `modules/todo/src/TodoServiceProvider.php`:

```php
<?php
declare(strict_types=1);

namespace Modules\Todo;

use Tavaan\Core\Container\ServiceProvider;
use Modules\Todo\Contracts\TodoInterface;
use Modules\Todo\Contracts\TodoRepositoryInterface;

/**
 * ServiceProvider ماژول Todo.
 */
class TodoServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        // ثبت Repository
        $this->app->singleton(
            TodoRepositoryInterface::class,
            Repositories\TodoRepository::class
        );

        // ثبت Service
        $this->app->singleton(
            TodoInterface::class,
            TodoService::class
        );

        // ثبت مسیرها
        $this->loadRoutesFrom(__DIR__ . '/../Routes/web.php');
        $this->loadRoutesFrom(__DIR__ . '/../Routes/api.php');

        // ثبت نماها
        $this->loadViewsFrom(__DIR__ . '/../Resources/views', 'todo');

        // ثبت مهاجرت‌ها
        $this->loadMigrationsFrom(__DIR__ . '/../Database/Migrations');

        // ثبت مجوزها
        $this->registerPermissions();
    }

    public function boot(): void
    {
        // ثبت شنوندگان رویداد (در صورت نیاز)
        // Event::listen('todo.created', ...);
    }

    /**
     * ثبت مجوزهای ماژول.
     */
    private function registerPermissions(): void
    {
        $this->app->make('permissions')
            ->register('todo', [
                'todo.view'    => 'مشاهده کارها',
                'todo.create'  => 'ساخت کار جدید',
                'todo.update'  => 'ویرایش کار',
                'todo.delete'  => 'حذف کار',
            ]);
    }
}
```

---

## مرحله ۱۲ — پیکربندی ⚙️

فایل `modules/todo/config/todo.php`:

```php
<?php
declare(strict_types=1);

return [
    // تعداد آیتم‌ها در هر صفحه
    'per_page' => 20,

    // اجازه کارهای گذشته به کاربر
    'allow_past_due' => true,

    // رنگ‌بندی بر اساس وضعیت
    'colors' => [
        'completed' => '#28a745',
        'pending'   => '#ffc107',
        'overdue'   => '#dc3545',
    ],
];
```

---

## مرحله ۱۳ — تست ماژول 🧪

فایل `modules/todo/Tests/TodoModuleTest.php`:

```php
<?php
declare(strict_types=1);

namespace Modules\Todo\Tests;

use PHPUnit\Framework\TestCase;
use Modules\Todo\TodoService;
use Modules\Todo\Contracts\TodoRepositoryInterface;
use Modules\Todo\Entities\Todo;

/**
 * تست ماژول Todo با Fake Repository.
 */
class TodoModuleTest extends TestCase
{
    private TodoService $service;
    private InMemoryTodoRepository $repo;

    protected function setUp(): void
    {
        $this->repo = new InMemoryTodoRepository();
        $this->service = new TodoService($this->repo);
    }

    public function testCreateTodo_ReturnsTodoWithId(): void
    {
        $todo = $this->service->createTodo(
            ['title' => 'خرید شیر'],
            userId: 1
        );

        $this->assertNotNull($todo->id);
        $this->assertSame('خرید شیر', $todo->title);
        $this->assertFalse($todo->is_completed);
    }

    public function testCompleteTodo_MarksCompleted(): void
    {
        $todo = $this->service->createTodo(
            ['title' => 'خرید نان'],
            userId: 1
        );

        $completed = $this->service->completeTodo($todo->id);

        $this->assertTrue($completed->is_completed);
    }

    public function testDeleteTodo_RemovesIt(): void
    {
        $todo = $this->service->createTodo(
            ['title' => 'خرید میوه'],
            userId: 1
        );

        $this->assertTrue($this->service->deleteTodo($todo->id));
        $this->assertNull($this->service->getTodo($todo->id));
    }

    public function testListTodos_ReturnsOnlyUserTodos(): void
    {
        $this->service->createTodo(['title' => 'کار ۱'], userId: 1);
        $this->service->createTodo(['title' => 'کار ۲'], userId: 1);
        $this->service->createTodo(['title' => 'کار ۳'], userId: 2);

        $todos = $this->service->listTodos(1);

        $this->assertCount(2, $todos);
    }
}

/**
 * Repository در-حافظه برای تست.
 */
class InMemoryTodoRepository implements TodoRepositoryInterface
{
    private array $storage = [];
    private int $nextId = 1;

    public function find(int $id): ?Todo
    {
        return isset($this->storage[$id])
            ? Todo::fromArray($this->storage[$id])
            : null;
    }

    public function all(int $userId, int $limit = 20, int $offset = 0): array
    {
        $items = array_filter($this->storage, fn ($r) => $r['user_id'] === $userId);
        return array_map(fn ($r) => Todo::fromArray($r), array_slice($items, $offset, $limit));
    }

    public function create(array $data): Todo
    {
        $id = $this->nextId++;
        $data['id'] = $id;
        $this->storage[$id] = $data;
        return $this->find($id);
    }

    public function update(int $id, array $data): ?Todo
    {
        if (!isset($this->storage[$id])) return null;
        $this->storage[$id] = array_merge($this->storage[$id], $data);
        return $this->find($id);
    }

    public function delete(int $id): bool
    {
        if (!isset($this->storage[$id])) return false;
        unset($this->storage[$id]);
        return true;
    }

    public function markCompleted(int $id, bool $completed = true): ?Todo
    {
        return $this->update($id, ['is_completed' => $completed]);
    }
}
```

### اجرای تست

```bash
php bin/tvn test modules/todo
```

خروجی:
```
OK (4 tests, 6 assertions)
```

---

## مرحله ۱۴ — ثبت ماژول در پروژه 📋

در `config/modules.php` (یا manifest پروژه):

```php
<?php
declare(strict_types=1);

return [
    // ... ماژول‌های دیگر ...

    'todo' => [
        'id' => 'tavaan.module.todo',
        'provider' => \Modules\Todo\TodoServiceProvider::class,
        'enabled' => true,
        'namespace' => 'Modules\\Todo\\',
        'path' => 'modules/todo',
    ],
];
```

در `config/autoload.php`:

```php
<?php
declare(strict_types=1);

return [
    // ...
    'Modules\\Todo\\' => __DIR__ . '/../modules/todo/src/',
];
```

---

## مرحله ۱۵ — اجرا و تست نهایی ✅

```bash
# ۱) مهاجرت
php bin/tvn migrate

# ۲) اجرای سرور
php bin/tvn serve
```

در مرورگر:

| URL | عمل |
|---|---|
| `http://127.0.0.1:8000/todos` | لیست کارها |
| `http://127.0.0.1:8000/todos/create` | فرم ساخت |
| `http://127.0.0.1:8000/todos/1` | نمایش کار ۱ |
| `http://127.0.0.1:8000/todos/1/edit` | ویرایش کار ۱ |
| `http://127.0.0.1:8000/api/todos` | API (JSON) |

### بررسی نصب ماژول

```bash
php bin/tvn modules
```

در لیست باید `todo` را ببینید:
```
core-user    ✅ loaded
content      ✅ loaded
todo         ✅ loaded  ← ماژول شما!
...
```

---

## جمع‌بندی — چه ساختید؟ 🎉

شما یک ماژول تَوان **کامل HMVC** با CRUD ساختی:

| بخش | فایل | وضعیت |
|---|---|---|
| Manifest | `module.json` | ✅ |
| Entity | `Todo.php` | ✅ |
| Repository Interface | `TodoRepositoryInterface.php` | ✅ |
| Repository | `TodoRepository.php` | ✅ |
| Service Interface | `TodoInterface.php` | ✅ |
| Service | `TodoService.php` | ✅ |
| Controller | `TodoController.php` | ✅ (۷ اکشن) |
| Migration | `create_todos_table.php` | ✅ |
| Routes (web) | `Routes/web.php` | ✅ (۷ مسیر) |
| Routes (api) | `Routes/api.php` | ✅ (۶ مسیر) |
| Views | `index.tv.php`، `create.tv.php` | ✅ |
| ServiceProvider | `TodoServiceProvider.php` | ✅ |
| Config | `config/todo.php` | ✅ |
| Tests | `TodoModuleTest.php` | ✅ (۴ تست) |
| Permissions | ۴ مجوز | ✅ |
| Events | ۴ رویداد | ✅ |

این، الگوی **همهٔ ماژول‌های تَوان** است. ماژول‌های واقعی (مثل `shop`، `accounting`، `comment`) پیچیده‌ترند، اما ساختار پایه‌شان همین است:

```
Entity → Repository → Service → Controller → Routes → Views → Tests
```

---

## تمثیل نهایی 🏠

ماژول شما، یک «اتاق کاربردی» در خانهٔ تَوان است:

| بخش ماژول | بخش اتاق |
|---|---|
| `module.json` | نقشه اتاق |
| `Entity` | اشیاء اتاق (میز، صندلی) |
| `Repository` | قفسه‌بندی اشیاء |
| `Service` | قواعد استفاده از اشیاء |
| `Controller` | دربان اتاق |
| `Routes` | راه‌های ورود به اتاق |
| `Views` | دیزاین اتاق |
| `Migration` | تأسیسات (برق، آب) |
| `Permissions` | قفل در |
| `Events` | زنگ خبر |

---

## گام بعدی 🚶

اگر این آموزش را کامل کردید، آماده‌اید برای:

- [`../10-modules/comment/`](../10-modules/comment/) — مطالعهٔ مستندات یک ماژول واقعی.
- [`../templates/module-template.md`](../templates/module-template.md) — قالب کامل ماژول (۱۵ بخش).
- [`../00-learn/for-agents.md`](../00-learn/for-agents.md) — راهنمای کامل ایجنت.
- [`../05-applications/`](../05-applications/) — کیت‌های آماده (Blog، Shop، ...).

---

## چالش اضافی 🧠

برای تمرین بیشتر:

1. **اعتبارسنجی** — `StoreTodoRequest` بسازید که `title` را الزامی و حداکثر ۲۰۰ کاراکتر کند.
2. **تقویم جلالی** — موعد را به‌جادی `Y/m/d` نمایش دهید.
3. **دسته‌بندی** — فیلد `category_id` اضافه کنید و ارتباط با ماژول `category` برقرار کنید.
4. **API Token** — احراز هویت API با توکن.
5. **Soft Delete** — `deleted_at` اضافه کنید و حذف نرم پیاده کنید.

---

> **@TavaanOfficial**
> *«هر ماژول، یک اتاق است. هر اتاق، یک داستان زندگی. داستان کارهای روزانه شما، همین‌جا نوشته شد.»* 📦
