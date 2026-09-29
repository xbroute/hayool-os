# بازنگری جامع Hayool OS — نسخه ۶
تاریخ: ۲۲ سپتامبر ۲۰۲۶

## نتیجه کلیدی

اصلاح مهم نسخه ۶ این است:

**Hayool نباید برای پوشش همه مشاغل، خودش همه نرم‌افزارهای دنیا را بسازد.**

چیزی که باید از روز اول بسازیم یک Platform قابل توسعه است که:

1. بخش‌های عمومی و حیاتی را خودش بسیار حرفه‌ای ارائه کند؛
2. فرد غیر برنامه‌نویس بتواند با Studio آن را تغییر دهد؛
3. برنامه‌نویس بتواند با SDK/API/Event/UI Extension قابلیت کاملاً جدید بسازد؛
4. شرکت‌های نرم‌افزاری و متخصصان بتوانند Pack/App خود را بفروشند؛
5. Core در اثر سفارشی‌سازی خراب و غیرقابل Upgrade نشود.

این تغییر، جاه‌طلبی محصول را کاهش نمی‌دهد؛ برعکس، آن را عملی‌تر می‌کند.

---

## تعریف نهایی محصول

> Hayool OS یک Business Operating Platform قابل توسعه است که کار، منابع، تراکنش، انسان و AI را هماهنگ می‌کند؛ و به افراد و توسعه‌دهندگان اجازه می‌دهد صنایع و فرایندهای جدید را بدون شکستن Core روی آن بسازند.

---

## پنج لایه محصول

### ۱. Core Kernel
هویت، Tenant، Permission، Finance، Work، Transaction، Inventory، Audit و primitiveهای حیاتی.

### ۲. Hayool Studio
No-code برای ساخت Object، Form، Workflow، Dashboard، Portal و Automation.

### ۳. Developer Platform
API، Events، SDK، CLI، Extension Runtime و UI Extension.

### ۴. Marketplace / Community
Industry Pack، Connector، App، Theme، Workflow، Agent، Report.

### ۵. Intelligence
AI، Jev، Solver، Forecasting، Digital Twin و Analytics.

---

## چرا این مدل برای بازار بزرگ بهتر است؟

اگر یک دامپزشک نیاز خاصی دارد، Hayool نباید ۶ ماه منتظر بماند تا تیم Core یک Veterinary ERP بنویسد.

یک متخصص صنعت + برنامه‌نویس می‌تواند Pack بسازد.

اگر یک بانک Workflow عجیب دارد، Developer می‌تواند Remote App تخصصی بسازد که با Core Banking آن بانک ارتباط بگیرد.

اگر یک کارخانه سیستم MES خاص دارد، Connector آن ساخته می‌شود.

Platform گسترش پیدا می‌کند بدون اینکه Core به کد سفارشی مشتری آلوده شود.

---

## تجربه فرد غیر برنامه‌نویس

کاربر می‌تواند به AI Builder بگوید:

«برای کارگاه کابینت‌سازی سیستم می‌خوام. سفارش مشتری، اندازه‌گیری، طراحی، برش، مونتاژ، نصب، هزینه مواد و نصاب داشته باشه.»

Hayool یک Draft Solution می‌سازد.

مدیر Preview و Test می‌کند.

اگر نیاز بسیار خاص داشت:
Marketplace پیشنهاد Extension می‌دهد یا Capability Request ثبت می‌شود.

---

## تجربه برنامه‌نویس

Developer باید بتواند در کمتر از حدود ۳۰ دقیقه اولین App آزمایشی را بالا بیاورد.

نیاز داریم:
- Developer Portal
- SDK
- CLI
- Test Tenant
- Mock data
- Events
- OpenAPI
- AsyncAPI
- Starter Apps
- Logs
- App analytics.

---

## مدل Extension

اولویت:

Configuration
→ Studio
→ Low-code
→ Pro-code Extension
→ First-party Core.

هر چیزی که فقط یک مشتری لازم دارد نباید به Core اضافه شود.

---

## نکته مهم امنیت

Extension third-party نباید داخل API اصلی هر کدی که خواست اجرا کند.

Remote App یا Runtime ایزوله دارد.

App فقط Scopeهایی را می‌گیرد که Tenant تأیید کرده.

اگر Version جدید Scope بیشتری خواست، Admin باید دوباره تأیید کند.

---

## Marketplace

Community می‌تواند:
- رایگان
- Open Source
- پولی
- اشتراکی
- Usage-based

App منتشر کند.

Hayool از Marketplace، runtime، certification و distribution درآمد می‌گیرد.

این خودش یک Revenue Engine جدید است.

---

## Capability Request Marketplace

یکی از ایده‌های مهم نسخه ۶:

شرکت می‌تواند بگوید:
«این قابلیت را ندارید، من X بودجه برای ساختش دارم.»

Partner/Developer می‌تواند آن را بسازد.

بعد در صورت توافق آن App برای بقیه Marketplace هم فروخته شود.

این باعث می‌شود پول مشتری مستقیماً Ecosystem را توسعه دهد.

---

## هوش مصنوعی: کمتر ولی بهتر

نسخه‌های قبلی هنوز خطر Over-AI داشتند.

قانون نسخه ۶:

**AI باید دلیل اقتصادی یا کیفی داشته باشد.**

اگر یک Query ساده کافی است، LLM ممنوع نیست ولی بی‌دلیل استفاده نمی‌شود.

اگر Solver بهتر است، Solver.

اگر Rule بهتر است، Rule.

اگر Semantic Judgment لازم است، Jev.

اگر Conversation/Generation لازم است، LLM.

---

## AI Unit Economics

هر AI Call هزینه واقعی دارد.

Hayool باید بداند:

Provider + Gateway + Search + Vector + Tool + Retry + Compute = Cost.

بعد بداند چند AI Credit از مشتری گرفته شده.

برای هر Tenant/Feature/Agent Margin داریم.

اگر Provider گران شد سیستم باید:
- مدل جایگزین بررسی کند
- Budget را تنظیم کند
- Credit schedule جدید پیشنهاد دهد.

---

## قیمت‌گذاری

مدیر باید حداقل سود را تعیین کند.

اما نرم‌افزار باید بین این‌ها فرق بگذارد:

Gross Margin
Contribution Margin
Estimated Fully Loaded Margin
Accounting Net Profit.

«سود خالص هر تراکنش» همیشه مفهوم دقیق حسابداری نیست.

پس مدیر می‌تواند Target Fully Loaded Margin مثلاً ۲۵٪ بگذارد.

سیستم Cost را کامل حساب می‌کند و Price Floor می‌سازد.

AI حق ندارد پایین‌تر از Floor قیمت بدهد مگر Approval.

---

## Pricing Lab

Hayool باید دائماً Price و Package را یاد بگیرد.

ولی نه با قیمت‌گذاری تصادفی و غیرمنصفانه.

Experiment:
Hypothesis
→ Control
→ Variant
→ Conversion
→ Retention
→ LTV
→ Contribution Profit.

اگر قیمت بالاتر Conversion را کمی کم کند ولی Profit و Retention بهتر شود، ممکن است برنده باشد.

سیستم بهترین Objective را از خودش اختراع نمی‌کند؛ مدیر انتخاب می‌کند.

---

## بازار جهانی

برای جهانی شدن مهم‌ترین محصول ما ممکن است خود Platform باشد، نه Packهای First-party.

یک Partner در امارات Country Pack.
یک شرکت در آلمان Connector.
یک شرکت کشاورزی Pack.
یک توسعه‌دهنده Clinic Workflow.

Hayool زیرساخت Distribution، Permission، Upgrade، Billing و Marketplace را می‌دهد.

---

## Branding

Hayool نباید بگوید:

«ما همه نرم‌افزارهای دنیا را ساخته‌ایم.»

باید بگوید:

> **Run it. Build it. Extend it.**

پیام محصول:

> **Tell Hayool what needs to happen — use what already exists, customize it, or build the missing capability on the same platform.**

فارسی:

> **بگو چه می‌خواهی؛ استفاده کن، شخصی‌سازی کن، یا همان‌جا قابلیت جدید بساز.**

---

## روان‌شناسی مشتری

Enterprise از Vendor lock-in می‌ترسد.

پس:
- Export
- Public API
- SDK
- On-Prem
- Open Extension contracts
- data portability

خودشان Feature فروش هستند.

---

## روان‌شناسی Developer

Developer باید حس کند Platform علیه او نیست.

باید:
- درآمد داشته باشد
- API پایدار ببیند
- Documentation عالی داشته باشد
- App خودش را مالک باشد
- Analytics داشته باشد
- Marketplace distribution داشته باشد.

---

## مزیت رقابتی جدید

قبلاً Moat بیشتر Data/Outcome Graph بود.

نسخه ۶ دو Moat دارد:

### Data Moat
Work/Resource/Transaction outcome history.

### Ecosystem Moat
Apps/Packs/Developers/Partners.

این دو یکدیگر را تقویت می‌کنند.

---

## بازار ورود همچنان باریک است

Architecture = Universal.

GTM اول:
Software / Digital Agencies / Professional Services.

بعد:
Retail / Distribution / Field Service.

اما Developer Platform از ابتدا وجود دارد تا صنعت‌های عجیب منتظر Roadmap Hayool نمانند.

---

## نتیجه

Hayool باید شبیه یک «Platform که روی آن Business Software ساخته می‌شود» طراحی شود، نه فقط یک «Business Software با Moduleهای زیاد».

این مهم‌ترین اصلاح راهبردی نسخه ۶ است.

