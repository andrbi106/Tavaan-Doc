# DOC-160 — رجیستری ماژول‌ها (Module Registry)

این سند فهرست رسمی ماژول‌های Tavaan است. هر ماژول پوشه‌ای با فایل‌های ممیزی عملیاتی است.
ماژول‌ها واحدهای HMVC خودبسنده هستند که توسط کیت‌ها ترکیب می‌شوند.

| DOC-ID | ماژول | عنوان فارسی | اولویت | وابستگی |
|---|---|---|---|---|
| DOC-161 | [CoreUser](./core-user/README.md) 📦 | هستهٔ کاربر | P0 | auth, rbac, session... |
| DOC-162 | [Content](./content/README.md) 📦 | محتوا | P0 | core-user, media, search... |
| DOC-163 | [Comment](./comment/README.md) 📦 | نظر | P1 | core-user, content |
| DOC-164 | [Category](./category/README.md) 📦 | دسته‌بندی | P1 | content |
| DOC-165 | [Shop](./shop/README.md) 📦 | فروشگاه | P0 | core-user, inventory, payment... |
| DOC-166 | [Inventory](./inventory/README.md) 📦 | انبار | P0 | database, notification |
| DOC-167 | [PaymentDomain](./payment/README.md) 📦 | پرداخت دامنه | P0 | core-user, database |
| DOC-168 | [Shipping](./shipping/README.md) 📦 | ارسال | P1 | inventory, shop |
| DOC-169 | [Tax](./tax/README.md) 📦 | مالیات | P1 | shop |
| DOC-170 | [Accounting](./accounting/README.md) 📦 | حسابداری | P0 | database, report |
| DOC-171 | [Procurement](./procurement/README.md) 📦 | خرید | P1 | inventory, accounting |
| DOC-172 | [Sales](./sales/README.md) 📦 | فروش | P0 | shop, accounting, crm |
| DOC-173 | [HR](./hr/README.md) 📦 | منابع انسانی | P1 | core-user, accounting |
| DOC-174 | [Production](./production/README.md) 📦 | تولید | P1 | inventory, accounting |
| DOC-175 | [Asset](./asset/README.md) 📦 | دارایی | P1 | accounting |
| DOC-176 | [FormBuilder](./form-builder/README.md) 📦 | سازنده فرم | P1 | database |
