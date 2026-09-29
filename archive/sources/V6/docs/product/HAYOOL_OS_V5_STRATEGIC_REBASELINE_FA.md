# بازنگری نهایی استراتژیک Hayool OS — نسخه ۵
تاریخ: ۲۲ سپتامبر ۲۰۲۶

## نتیجه اصلی

Hayool OS در نسخه ۵ دیگر نباید حتی از نظر معماری «نرم‌افزار مخصوص شرکت‌های خدمات دیجیتال» تلقی شود. بازار ورود همچنان شرکت‌های پروژه‌محور و دیجیتال است، اما هسته محصول باید **Universal Business Platform** باشد.

تعریف نهایی:

> **Hayool OS یک سیستم‌عامل هوشمند برای اداره کار، منابع و تراکنش‌های یک کسب‌وکار است؛ نیاز را می‌فهمد، آن را به برنامه اجرایی تبدیل می‌کند، انسان/تیم/کالا/تجهیزات/تأمین‌کننده/AI مناسب را پیدا می‌کند، اجرا و پول و نتیجه را مدیریت می‌کند و از نتیجه یاد می‌گیرد.**

بنابراین Work & Workforce هنوز مزیت اصلی است، اما دیگر تنها محور نیست. سه Graph اصلی داریم:

- Work Graph
- Resource & Supply Graph
- Transaction & Outcome Graph

اتصال این سه Graph دارایی استراتژیک Hayool است.

## چرا این تغییر لازم بود؟

یک شرکت نرم‌افزاری، فروشگاه، کارخانه، مزرعه و بانک در ظاهر بسیار متفاوت‌اند؛ اما زیرساخت مشترک زیادی دارند:

- افراد و سازمان‌ها
- مکان
- کالا/خدمت
- منابع
- کار
- سفارش/تعهد
- قرارداد
- پرداخت
- سند
- موجودی/دارایی
- رویداد
- تأیید
- نتیجه.

اگر این primitives درست طراحی شوند، Industry Pack می‌تواند تجربه تخصصی هر حوزه را روی همان هسته بسازد.

اشتباه این بود که برای هر صنعت یک ERP جدا داخل Hayool بسازیم.

## مدل صحیح برای «همه کسب‌وکارها»

هسته قوی + Studio + Pack.

شرکت کوچک می‌تواند فقط:
CRM + فاکتور + سایت + فروش.

یک انبار:
Inventory + Barcode + Procurement + Logistics.

کارخانه:
MRP + BOM + Quality + Maintenance + اتصال MES/SCADA.

مزرعه:
Field + Crop Cycle + Input + Harvest + Traceability.

بانک:
HR + Procurement + Service/Case + Documents + Projects + Integrations.

بانک برای Core Banking از سیستم تخصصی خود استفاده می‌کند و Hayool آن را Integrate می‌کند، مگر روزی Banking Core مستقل و تأییدشده ساخته شود.

این مرزبندی نشانه ضعف نیست؛ شرط حرفه‌ای بودن است.

## قابلیت پرچمدار جدید: Intent-to-Outcome

رابط عمومی Hayool می‌تواند یک کادر ساده باشد:

«چه می‌خواهی؟»

اگر کسی بنویسد:

«۵ کیلو گوشت تا ساعت ۷ می‌خوام»

سیستم درخواست را تبدیل می‌کند به:

Need → Product Constraints → Seller Discovery → Inventory/Price → Delivery Provider → Order → Delivery → Payment → Acceptance.

اگر فروشنده خودش تحویل نداشت، Fulfillment Planner می‌تواند Courier/Taxi/Delivery Provider جدا پیدا کند.

این معماری شبیه یک Marketplace بسته نیست؛ Network Orchestration است.

امکان واقعی بودن آن وابسته به Provider coverage و Connector است. Hayool نباید ادعا کند در شهری که هیچ فروشنده/حمل‌ونقل متصل ندارد این درخواست را خودکار انجام می‌دهد.

## Hayool Studio

برای اینکه یک محصول واقعاً «برای همه» شود، Custom Field کافی نیست.

Studio باید اجازه بدهد بدون کدنویسی:

- Object
- Field
- Relationship
- Form
- List
- Dashboard
- Workflow
- Approval
- Report
- Portal
- Automation

ساخته شود.

AI نیز از شرح کسب‌وکار یک Draft Solution می‌سازد.

مثلاً تعمیرگاه موبایل توضیح می‌دهد چه کار می‌کند و Hayool پیشنهاد می‌دهد:

Customer + Device + Repair Ticket + Technician + Part + Warranty + Invoice.

مدیر Preview می‌کند و Publish می‌زند.

## الگوریتم‌ها

نسخه ۵ یک اصلاح بنیادی دارد: «AI» یک ابزار واحد نیست.

برای هر مسئله Engine مناسب انتخاب می‌شود:

- محاسبات/قانون → Deterministic Rule Engine
- زمان‌بندی/مسیر/Allocation → Mathematical Solver
- Forecast → Predictive ML
- قضاوت semantic → Jev
- گفتگو/تولید/برنامه‌ریزی → LLM/Agent

این تصمیم برای کارخانه، لجستیک و منابع انسانی حیاتی است.

LLM نباید برای Vehicle Routing یا Inventory Math جای Solver استفاده شود.

## زنجیره تأمین

برای جهانی شدن، Product/Inventory/Logistics باید از V1 در Kernel جدی باشند:

Product / Service
Warehouse / Location
Lot / Serial
Stock Movement
Procurement
Order
Shipment
Delivery
Return
Traceability.

استانداردهای GS1/EPCIS باید به‌صورت Mapping/Adapter پشتیبانی شوند، نه اینکه به تمام کسب‌وکارها تحمیل شوند.

## صنعت

V1 باید Kernel را برای صنایع مختلف آماده کند اما ادعای Market Readiness همه حوزه‌ها نداشته باشد.

سطوح:

Kernel
Starter
Verified
Regulated/Certified
Partner
Future.

مثلاً:
Professional Services می‌تواند Verified باشد.
Retail/Wholesale/Light Manufacturing Starter.
Agriculture Beta.
Core Banking خارج از Generic Core.

## جهانی شدن

جهانی‌شدن فقط ترجمه انگلیسی نیست.

نیاز داریم:

Country Pack
Currency
Tax
Payroll
E-invoice
Address
Calendar
Unit
Employment
Privacy
Data Residency
Industry Rules.

قواعد Versioned و Effective-dated هستند.

## تجربه کاربری

اگر ۵۰ Module در Sidebar نشان داده شود پروژه شکست می‌خورد.

رابط باید دو حالت همزمان داشته باشد:

1. Intent-first: «چه می‌خواهی؟»
2. Expert Workspace: ابزار تخصصی برای حسابدار/انباردار/مدیر/اپراتور.

هر Role فقط Workspace خودش را می‌بیند.

## بازار و برند

قرار نیست در تبلیغ روز اول بگوییم:

«برای هر کسب‌وکاری در جهان.»

این پیام اعتبار را کم می‌کند.

Brand Vision می‌تواند جهانی باشد؛ GTM باید مشخص باشد.

ورود:
شرکت‌های دیجیتال و پروژه‌محور.

سپس:
Retail / Distribution / Field Service / Light Manufacturing.

بعد:
Agriculture و Industries تخصصی.

Brand Promise:

> **Tell Hayool what needs to happen. Hayool turns it into people, resources, workflows and outcomes.**

ترجمه مفهومی:

> **بگو چه می‌خواهی؛ Hayool کار، منابع و اجرا را هماهنگ می‌کند.**

## نقطه تمایز

Odoo وسعت Application دارد.
Power Platform انعطاف Custom App دارد.
ServiceNow Workflow Platform است.
SAP عمق Enterprise/Industry دارد.
Upwork/Deel/Gloat/Workday بخش Workforce را پوشش می‌دهند.

Hayool اگر فقط مجموعه این Featureها باشد، مزیت پایدار ندارد.

ترکیب متمایز:

Intent
+ Work Graph
+ Resource/Supply Graph
+ Workforce
+ Transaction/Fulfillment
+ Finance
+ AI/Decision/Solver
+ Learning.

## ریسک اصلی نسخه ۵

جاه‌طلبی هنوز بزرگ‌ترین Risk است.

راه‌حل «Feature کمتر» نیست؛ راه‌حل معماری Pack و Market Readiness Gate است.

هسته V1 باید قدرتمند باشد، ولی هر Industry فقط وقتی Market-ready اعلام شود که Pack آن واقعاً تست شده باشد.

## نتیجه

نسخه ۵ باید به‌عنوان «Universal Business Platform Architecture» ساخته شود، اما به‌عنوان «Project-Based Company OS» وارد بازار شود.

این دو با هم تناقض ندارند.

Architecture وسیع است.
Distribution باریک شروع می‌شود.

