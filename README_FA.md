# Hayool OS — بسته نهایی حقیقت مرجع پیش از کدنویسی

نسخهٔ ۷.۲، ۲۶ سپتامبر ۲۰۲۶. این بسته بازبینی سخت‌گیرانهٔ V7.1 است و ۶۱ منبع اصلی V6 و V7 و خود بستهٔ V7.1 را بدون حذف نگه می‌دارد. هیچ کد محصولی نوشته نشده و مرحلهٔ دوم آغاز نشده است. نسخه‌های خام منابع در `archive/sources/` و بستهٔ پیشین در `archive/V7.1/` قرار دارند. مبنای طراحی، `docs/SOURCE_OF_TRUTH_INDEX.md`، حل تعارض‌ها و کاتالوگ ۱۹۴ REQ و ۳۱ رکورد ADR (۳۰ فعال، یک superseded) است. ادعای پیاده‌سازی، تأیید قانون یا آمادگی بازار در این بسته وجود ندارد.

## تحویل‌ها و مسیر مطالعه

| خواسته | سند اصلی |
|---|---|
| بستهٔ نهایی حقیقت مرجع و منشأ منابع | `docs/SOURCE_OF_TRUTH_INDEX.md`, `SOURCE_MANIFEST.json`, `docs/requirements/SOURCE_COVERAGE.md`, `PACKAGE_MANIFEST.json` |
| معماری نهایی و قراردادهای دامنه | `docs/architecture/FINAL_ARCHITECTURE.md`, `DOMAIN_CONTRACTS.md` |
| کاتالوگ کامل نیازمندی‌ها و ADR | `docs/requirements/REQUIREMENTS_CATALOG.md`, `docs/adr/ADR_CATALOG.md` |
| نقشهٔ راه M0 تا V1.10 و بعد | `docs/releases/RELEASE_ROADMAP.md` |
| آزمون و شواهد | `docs/testing/TESTING_STRATEGY.md`, `docs/evidence/EVIDENCE_INDEX.md` |
| توسعه/رفع خطا/به‌روزرسانی خودکار | `docs/engineering/AUTONOMOUS_ENGINEERING_PLAN.md` |
| کشورها، حوزه‌های قضایی و تأمین‌کنندگان | `docs/country-packs/GLOBAL_JURISDICTION_ARCHITECTURE.md` |
| امنیت، حریم خصوصی و انطباق | `docs/security/SECURITY_PRIVACY_COMPLIANCE.md` |
| مالی و مدل کسب‌وکار | `docs/finance/FINANCIAL_BUSINESS_REQUIREMENTS.md` |
| Budget، Cost/Profit Center و reconciliation | `docs/finance/BUDGET_COST_CENTER_CONTRACT.md` |
| Incident، Asset، Secrets Vault، Meeting | قراردادهای مستقل در `docs/operations/`, `docs/security/`, `docs/ai/` |
| Market/Brand/Psychology/Value/GTM نهایی | `docs/market/MARKET_BRAND_PSYCHOLOGY_VALUE_GTM_FINAL.md` |
| ممیزی ۱۳۸ REQ پیشین و ۲۵ بُعد طراحی | `docs/requirements/GRANULARITY_REVIEW.md`, `docs/audit/MULTIDIMENSIONAL_DESIGN_AUDIT.md` |
| Studio/Developer/Marketplace | `docs/platform/DEVELOPER_STUDIO_MARKETPLACE_ARCHITECTURE.md` |
| وضعیت، اقدام‌های بعدی و تصمیم مالک | `PROJECT_STATE.md`, `NEXT_ACTIONS.md`, `docs/OWNER_DECISIONS.md` |

تمام قابلیت‌های مهم V7.1، از جریان پروژه و مالی و نیروی انسانی تا CMS/eCommerce، تولید و زنجیرهٔ تأمین، حفظ شده‌اند. V1 مجموعهٔ V1.0 تا V1.10 است. معماری بسته‌های Country/Subnational برای همهٔ کشورها تعریف شده اما فعال‌سازی هر قابلیت/مسیر نیازمند شواهد جداگانه است. پیش‌فرض محصول برای ایران `DOMESTIC_ONLY` باقی مانده؛ تعریف facts و evaluator داخلی هر کشور را Country Pack معتبر تعیین می‌کند. بدون آن، جستجوی واقعی استعداد مجاز فرض نمی‌شود.

**M0.1 DOCUMENTATION GATE = PASS**، صرفاً برای Source of Truth پیش از کدنویسی: ۶۱ منبع و بستهٔ پیشین، ۱۹۴ REQ، ۳۱ رکورد ADR، دو بازبینی مستقل روی digest یکسان و manifest/ZIP بررسی شده‌اند. این PASS به معنی پیاده‌سازی، ارزیابی امنیت محصول، انطباق حقوقی یا آمادگی بازار نیست. **M0.0 = PENDING; M0.2 = PENDING**. تصمیم‌های فنی در ADR ثبت شده‌اند. شروع کدنویسی در این درخواست مجاز نیست؛ تصمیم‌های حقوقی، مالی و تجاری در `docs/OWNER_DECISIONS.md` با دروازهٔ زمانی خود آمده‌اند.
