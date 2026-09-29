# Hayool OS — طرح جامع محصول، اکوسیستم و مدل کسب‌وکار نسخه ۶
تاریخ: ۲۲ سپتامبر ۲۰۲۶
وضعیت: Baseline راهبردی برای M0

---

# ۱. خلاصه مدیریتی

Hayool OS نباید یک ERP باشد که تیم Hayool مجبور باشد برای هر صنعت ماژول تازه‌ای به Core آن اضافه کند.

تعریف نسخه ۶:

> **Hayool OS یک پلتفرم عامل‌پذیر و قابل توسعه برای اداره کسب‌وکار، کار، منابع، تراکنش‌ها و هوش است.**

هسته محصول باید نیازهای عمومی و حساس را بسیار حرفه‌ای حل کند:
- Identity / Tenant / Permission
- Finance / Accounting
- Work / Project / Task
- HR / Talent
- CRM / Sales
- Order / Procurement / Inventory
- Documents / Workflow
- Audit / Security
- AI / Analytics

اما پوشش صنایع مختلف از طریق سه لایه رشد می‌کند:

1. **Hayool Studio** برای افراد غیر برنامه‌نویس؛
2. **Developer Platform** برای برنامه‌نویسان و شرکت‌های نرم‌افزاری؛
3. **Marketplace / Industry Packs / Connectors** برای Community و Partnerها.

به این ترتیب Hayool می‌تواند در بلندمدت بازار بسیار بزرگی داشته باشد، بدون اینکه خودش مجبور باشد Core Banking، EHR پزشکی، سیستم دامداری، نرم‌افزار کارخانه، CRM تخصصی و ده‌ها سیستم دیگر را شخصاً از صفر بسازد.

---

# ۲. تز اصلی تجاری

مزیت پایدار Hayool نباید «تعداد Feature» باشد.

دو Moat اصلی باید ساخته شود:

## ۲.۱ Data / Outcome Moat

Hayool رابطه میان این‌ها را به مرور یاد می‌گیرد:

Goal
→ Work
→ Resource
→ Cost
→ Transaction
→ Outcome.

این داده Pricing، Staffing، Forecasting، Capacity و Automation را بهتر می‌کند.

## ۲.۲ Ecosystem Moat

هر Developer/Partner می‌تواند قابلیت جدیدی بسازد، بفروشد و نگهداری کند.

هر App/Pack جدید باعث می‌شود:
- مشتری بیشتری جذب شود؛
- نیازهای بیشتری بدون توسعه Core حل شوند؛
- Developer بیشتری وارد شود؛
- ارزش Marketplace بیشتر شود.

ترکیب Data Moat + Ecosystem Moat دفاع‌پذیرتر از صرفاً داشتن مدل AI است.

---

# ۳. چرا این اصلاح از نظر فنی ضروری است؟

اگر همه نیازها مستقیم وارد Core شوند، مشکلات زیر ایجاد می‌شود:

- وابستگی بیش از حد Domainها
- Migration سخت
- UI شلوغ
- Regression زیاد
- Update پرریسک
- درخواست سفارشی بی‌پایان
- هزینه Support زیاد
- سرعت توسعه پایین
- Vendor lock-in ناسالم
- دشواری ورود Community.

معماری Clean Core باعث می‌شود Core کوچک‌تر از مجموع Product باشد.

Product بزرگ است، Core کنترل‌شده است.

---

# ۴. معماری پنج لایه‌ای محصول

## لایه ۱: Universal Core

Primitiveهای پایدار:
- Person
- Organization
- Location
- Product/Service
- Resource
- Work
- Order
- Contract
- Payment
- Inventory
- Asset
- Document
- Policy
- Event
- Outcome.

## لایه ۲: Hayool Studio

برای Business Builder:
- Object
- Field
- Relation
- Form
- View
- Dashboard
- Report
- Workflow
- Approval
- Portal
- Template.

## لایه ۳: Developer Platform

برای Developer:
- API
- Events
- SDK
- CLI
- Test Tenant
- App Manifest
- UI Extension
- Connector
- Workflow Activity.

## لایه ۴: Marketplace / Network

- App
- Industry Pack
- Country Pack
- Theme
- Connector
- Agent
- Workflow
- Report.

## لایه ۵: Intelligence

- Rule Engine
- Solver
- ML
- Jev
- LLM/Agents
- Digital Twin
- Learning Flywheel.

---

# ۵. مدل چهار سطح سفارشی‌سازی

هر درخواست باید ابتدا در پایین‌ترین سطح مناسب حل شود.

## Level 0 — Configuration

مثلاً:
- وضعیت‌ها
- شماره‌گذاری
- رنگ
- Role
- Threshold
- Template.

## Level 1 — No-code

مثلاً یک کلینیک دامپزشکی Object حیوان و ویزیت و پرونده بسازد.

## Level 2 — Low-code

فرمول، Mapping، Workflow و Connector ساده.

## Level 3 — Pro-code

App کامل با Backend، UI و Storage اختصاصی.

## Level 4 — Native Core

فقط وقتی قابلیت واقعاً عمومی/حیاتی است.

این مدل باید Policy رسمی Product باشد.

---

# ۶. تجربه کاربر غیر برنامه‌نویس

کاربر نباید بفهمد پشت سیستم چقدر معماری وجود دارد.

او می‌تواند بگوید:

> «من شرکت اجاره تجهیزات ساختمانی دارم.»

AI Builder سؤال می‌پرسد:

- چه تجهیزاتی؟
- اجاره روزانه یا ماهانه؟
- ودیعه؟
- تحویل؟
- خرابی؟
- اپراتور؟
- سرویس دوره‌ای؟

سپس Draft Solution می‌سازد:

Customer  
Equipment  
Rental Contract  
Reservation  
Delivery  
Return  
Damage  
Maintenance  
Invoice.

کاربر Preview می‌کند.

AI اینجا نقش Builder Assistant دارد؛ نه اینکه هر چیزی را مستقیماً Production کند.

---

# ۷. تجربه Developer

هدف DX:

یک Developer ماهر باید بتواند طی زمان کوتاه اولین Extension آزمایشی را بسازد.

Developer Platform باید شامل:

- Portal
- Documentation
- CLI
- SDK
- OpenAPI
- AsyncAPI/Event Catalog
- App Manifest
- Webhook
- Test Tenant
- Sample Data
- Logs
- API Explorer
- Example Apps
- Testing Kit
- Migration Guide.

Developer نباید برای هر چیز به تیم Hayool Ticket بزند.

---

# ۸. Runtime امن Extension

یک اشتباه خطرناک این است که Plugin ثالث را مستقیم داخل Backend اصلی load کنیم.

ترتیب ترجیحی:

Declarative Package
→ Remote App
→ Managed Isolated Runtime
→ Native Core فقط برای First-party.

Remote App می‌تواند خودش Database داشته باشد.

Hayool فقط Contract و Permission فراهم می‌کند.

برای Cloud و On-Prem هر دو باید معماری مشخص باشد.

---

# ۹. Permission برای App

App یک Principal مستقل است.

App نمی‌تواند چون Admin آن را نصب کرده تمام داده Admin را ببیند.

Scopeها باید دقیق باشند.

مثلاً:
`orders.read`
`inventory.write`
`customer.contact.read`

اگر Version بعد App بخواهد Payroll هم بخواند، Permission Expansion محسوب می‌شود و Admin باید تأیید کند.

---

# ۱۰. Marketplace

Marketplace نباید فقط فروشگاه Plugin باشد.

باید موتور توسعه بازار باشد.

انواع محصول:
- App
- Industry Pack
- Workflow
- Report
- Theme
- Connector
- AI Agent
- Assessment
- Country Pack.

مدل قیمت:
Free  
Open Source  
Paid  
Subscription  
Usage-based  
Enterprise.

---

# ۱۱. Capability Request / Bounty

یکی از فرصت‌های استراتژیک مهم:

مشتری Feature می‌خواهد که وجود ندارد.

به‌جای اینکه فقط Feature Request بدهد:

> «برای ساخت این قابلیت X بودجه دارم.»

Developer یا Partner می‌تواند آن را قبول کند.

بعد از تحویل، در صورت توافق:
- Private بماند
- یا در Marketplace به بقیه فروخته شود.

این مدل می‌تواند هزینه R&D Hayool را کاهش دهد و Community را درآمدزا کند.

---

# ۱۲. Community

Community باید سه گروه داشته باشد:

### Builders
افراد بدون کد.

### Developers
کدنویسان.

### Experts
حسابدار، HR، کارشناس صنعت، وکیل، متخصص لجستیک، متخصص کشاورزی.

Expert لزوماً کد نمی‌زند؛ می‌تواند Template و Pack طراحی کند و با Developer شریک شود.

---

# ۱۳. Partner Network

انواع Partner:
- Implementer
- Developer
- Industry Consultant
- Accountant
- Payroll/Tax
- Country Partner
- Integration
- Hosting.

این شبکه برای جهانی‌شدن حیاتی است.

Hayool نمی‌تواند قوانین و فرایندهای تمام کشورهای دنیا را خودش با تیم مرکزی مدیریت کند.

---

# ۱۴. Open-source strategy

برای رشد اکوسیستم بهتر است بخش‌هایی باز باشند:

- SDK
- CLI
- schemas/specs
- starter apps
- example connectors.

Core Product می‌تواند proprietary بماند.

این تعادل برای اعتماد Developer مناسب است.

---

# ۱۵. هوش مصنوعی — سیاست نسخه ۶

اصل:

> AI فقط وقتی استفاده شود که نسبت Value/Cost منطقی دارد.

AI-native نباید به AI spam تبدیل شود.

---

# ۱۶. AI Necessity Gate

قبل از هر AI feature:

- مشکل چیست؟
- Rule کافی است؟
- Search کافی است؟
- Solver کافی است؟
- Statistical Model کافی است؟
- Semantic judgement لازم است؟
- Generation لازم است؟

اگر خروجی دقیق deterministic داریم، استفاده از LLM فقط هزینه و Risk اضافه است.

---

# ۱۷. AI Cost Governance

هر Call باید Cost attribution داشته باشد.

مثلاً:

Tenant A  
Project B  
Support Agent  
Model X  
Raw Cost = $0.014  
Search Cost = $0.002  
Platform Cost = $0.003  
Charged = 12 Credits.

این داده هم برای Pricing و هم برای Optimization لازم است.

---

# ۱۸. AI Budget Governor

Admin می‌تواند:

- Budget ماهانه
- Budget پروژه
- Budget User
- Budget Agent

تعریف کند.

وقتی Budget نزدیک Limit است:
- Alert
- Model cheaper
- Disable optional AI
- BYOK
- Manual fallback.

---

# ۱۹. AI Credit Economics

AI Credit نباید Token مستقیم باشد.

چون:
- Provider تغییر می‌کند.
- مدل‌ها Cost مختلف دارند.
- Tool/Search هزینه دارد.
- orchestration ارزش دارد.

Credit یک abstraction تجاری است.

---

# ۲۰. Pricing Strategy

قیمت‌گذاری نباید یک عدد ثابت باشد که سالی یک بار مدیر حدس بزند.

Hayool باید Pricing Intelligence داشته باشد.

اما Price AI نباید آزادانه قیمت هر فرد را دستکاری کند.

---

# ۲۱. سود حداقل مدیر

مدیر باید چند Level تعیین کند:

Minimum Gross Margin  
Minimum Contribution Margin  
Target Fully Loaded Margin  
Minimum AI Margin.

مثلاً Target Fully Loaded Margin = 25%.

اگر Fully Loaded Cost = 100:

Minimum Price = 100 / 0.75 = 133.33.

این Floor است.

AI می‌تواند بالاتر از آن Optimize کند.

---

# ۲۲. چرا «سود خالص هر فروش» دقیق نیست؟

Net Profit در حسابداری معمولاً Period-level است.

ولی برای Pricing می‌توان هزینه Overhead را Allocate کرد و:

Estimated Fully Loaded Margin

داشت.

UI باید دقیقاً تفاوت را نشان دهد.

این جلوی تصمیم غلط را می‌گیرد.

---

# ۲۳. Pricing Lab

Experiment entity:

Hypothesis  
Control  
Variant  
Audience  
Metrics  
Guardrails  
Result.

هدف می‌تواند باشد:
- Contribution Profit
- LTV
- ARR
- Adoption.

نه اینکه همیشه Conversion را maximize کنیم.

---

# ۲۴. Price Experiment Safety

قیمت را بر اساس Race، Religion، Health و ویژگی حساس مخفی تغییر نمی‌دهیم.

Geography/market/volume ممکن است Legitimate باشد؛ Country policy باید بررسی کند.

Customer trust مهم‌تر از چند درصد Revenue کوتاه‌مدت است.

---

# ۲۵. هزینه AI در قیمت

AI Cost باید به Plan برگردد.

اگر Plan شامل ۱۰۰هزار Credit است:

Pricing Engine باید Forecast کند:
- average use
- heavy users
- provider mix
- worst-case reasonable use.

Unlimited AI بدون Fair Use/Cost guardrail می‌تواند Margin را نابود کند.

---

# ۲۶. Revenue Engines

V6:

- Annual License
- AI Credits
- Cloud
- Dedicated
- On-Prem
- Modules
- Industry Packs
- Country Packs
- Marketplace Share
- Managed Extension Runtime
- Certification
- Implementation
- Support
- Managed Workforce
- Managed Outcome
- Transaction Orchestration.

هر Stream P&L مستقل.

---

# ۲۷. Branding

Hayool نباید شبیه یک محصول شلوغ معرفی شود.

Masterbrand:
**Hayool OS**

پیام Platform:
**Run it. Customize it. Extend it.**

پیام عمومی:
**Tell Hayool what needs to happen.**

پیام Developer:
**Build once. Extend Hayool. Reach businesses.**

---

# ۲۸. چرا نباید در بازاریابی بگوییم «برای همه دنیا آماده‌ایم»؟

Enterprise Buyer این ادعا را باور نمی‌کند.

باید بگوییم:

Platform globally adaptable.

و در صفحه Industry:

Professional Services — Verified  
Retail — Beta/Starter  
Manufacturing — Starter  
Agriculture — Beta.

صداقت Product maturity اعتماد می‌سازد.

---

# ۲۹. Market Entry

GTM اولیه همچنان:
- Software House
- Agency
- Consulting
- Professional Services.

چرا؟

چون Hayool خودش Domain knowledge دارد.

ولی Developer Platform از روز اول اجازه می‌دهد Customer دیگری معطل Roadmap نباشد.

---

# ۳۰. روان‌شناسی Enterprise

ترس‌های Enterprise:

- Lock-in
- Upgrade break
- security
- data ownership
- hidden AI
- unpredictable price.

راه‌حل:

- export
- API
- SDK
- On-Prem
- permission manifest
- stable contract
- price policy
- AI Off/BYOK.

---

# ۳۱. روان‌شناسی Developer

Developer Ecosystem زمانی شکل می‌گیرد که:

- API stable باشد.
- Docs عالی باشد.
- Runtime امن و predictable باشد.
- Developer درآمد داشته باشد.
- Marketplace distribution داشته باشد.
- Hayool App او را بدون دلیل clone نکند.

Partner policy باید اعتمادساز باشد.

---

# ۳۲. روان‌شناسی کاربر عادی

کاربر عادی نباید Studio و Extension SDK ببیند.

او باید:
- Intent
- Workspace
- Notifications
- Tasks
- simple forms

ببیند.

Power باید پشت Progressive Disclosure باشد.

---

# ۳۳. Accessibility

V6 باید Accessibility را Product Quality بداند.

- WCAG 2.2 AA target
- Keyboard
- screen reader
- RTL/LTR
- touch
- low bandwidth
- readable errors
- responsive
- offline where relevant.

---

# ۳۴. Globalization

Global = Locale + Country + Law + Integration.

نه فقط Translation.

Country Pack:
- Tax
- Payroll
- eInvoice
- privacy
- employment
- payment
- document.

Partnerها می‌توانند Country Pack بسازند، ولی Certification لازم است.

---

# ۳۵. قانون و Marketplace

App ممکن است Data customer را خارج ببرد.

پس App Listing باید اعلام کند:
- Data accessed
- external storage
- region
- retention
- AI providers
- privacy policy.

Admin قبل Install می‌بیند.

---

# ۳۶. قانون Employment AI

اگر Extension برای Hiring ساخته شد، همان Employment AI governance روی آن اعمال می‌شود.

Third-party App نمی‌تواند Guardrail مرکزی را دور بزند.

---

# ۳۷. Regulated Industries

Developer می‌تواند Banking/Clinical/Industrial App بسازد.

اما Listing باید دقیق بگوید:
- jurisdiction
- certification
- responsible vendor
- supported deployment.

Hayool Core automatically certified محسوب نمی‌شود.

---

# ۳۸. آینده Platform

اگر Ecosystem موفق شود، Hayool می‌تواند بیشتر شبیه:

Business Application Platform

باشد تا ERP Vendor.

این بزرگ‌ترین Upside پروژه است.

---

# ۳۹. معیار موفقیت Developer Platform

- time to first app
- active developers
- apps built
- paid app GMV
- % customer feature needs solved without core changes
- API breakage
- app retention
- partner revenue.

---

# ۴۰. معیار موفقیت AI

- cost per successful outcome
- % requests handled with cheaper model
- cache hit
- AI gross margin
- eval quality
- human override
- business value.

نه تعداد Token مصرف‌شده.

---

# ۴۱. معیار موفقیت Pricing

- Contribution Profit
- retention
- conversion
- expansion
- LTV
- discount leakage
- gross/net margin target attainment.

---

# ۴۲. نقاط کور باقی‌مانده

### Extension ecosystem cold start
راه‌حل:
First-party templates + design partners + paid bounties.

### Low-code becomes chaotic
راه‌حل:
Solution packages + environments + versioning.

### Plugin security
راه‌حل:
Remote/sandbox + scopes + review.

### Price optimization harms trust
راه‌حل:
transparent policies + controlled cohorts + manager floors.

### AI cost grows faster than revenue
راه‌حل:
AI ledger + model router + margin floor.

### Partner quality variance
راه‌حل:
certification + reviews + SLA.

### Marketplace abandonment
راه‌حل:
maintenance status + migration path.

### Too much configuration
راه‌حل:
templates + guided onboarding + AI Builder.

---

# ۴۳. نتیجه نهایی نسخه ۶

بهترین نسخه Hayool نه محصولی است که خودش همه صنایع را نوشته باشد و نه یک Platform خالی که برای هر چیز نیاز به توسعه دارد.

تعادل:

**Excellent Core + Excellent Studio + Excellent Developer Platform + Strong Ecosystem.**

این ترکیب باعث می‌شود:

- روز اول Product واقعی داشته باشیم؛
- در آینده Market بسیار وسیع شود؛
- تیم Core زیر Feature Request له نشود؛
- Community درآمد داشته باشد؛
- Enterprise از Customization نترسد؛
- AI Cost کنترل شود؛
- Pricing به‌صورت علمی رشد کند.

این نسخه باید Baseline معماری M0 باشد.

