# Hayool OS — Website, CMS, Commerce & SEO Experience Platform
Version: 6.0
Status: Product architecture

---

## 1. Goal

A tenant should be able to publish a professional website/portal/store connected directly to Hayool business data without maintaining a disconnected CMS.

The experience platform must also support headless/API use for customers who already have their own frontend.

---

## 2. Multi-site

Tenant may operate:
- corporate website
- brand site
- store
- landing pages
- client portal
- public talent page
- provider marketplace storefront.

Sites can have:
- domain
- locale
- brand theme
- navigation
- content permissions
- analytics configuration.

---

## 3. Page Builder

Block/component model:
- hero
- text/media
- cards
- grid
- gallery
- FAQ
- form
- CTA
- pricing
- catalog
- product list
- service list
- testimonials
- dynamic collection
- map
- custom approved component.

Admin may customize through safe design tokens and components.

No arbitrary unsafe script by default.

---

## 4. CMS

Content types:
- page
- blog/article
- case study
- FAQ
- documentation
- product/service content
- landing page
- custom content type.

Workflow:
Draft → Review → Approved → Scheduled → Published → Archived.

---

## 5. AI content

AI may:
- draft
- rewrite
- translate
- summarize
- propose SEO metadata
- create content brief
- propose internal links.

Publishing autonomy is policy-controlled.

Sources/claims should be reviewed where factual accuracy matters.

---

## 6. SEO

Baseline:
- title/meta description
- canonical
- robots
- XML sitemap
- redirects
- hreflang
- Open Graph/social metadata
- structured data/schema markup
- clean URLs
- image alt text
- internal linking
- indexation controls.

SEO module tracks:
- topic/keyword clusters
- content brief
- page target
- technical issues
- external analytics/search-console connectors
- ranking/traffic imports.

Do not promise ranking outcomes.

---

## 7. Performance

Web delivery must target:
- fast server response
- optimized images
- caching/CDN support
- minimal JS for public pages
- Core Web Vitals awareness
- SEO-safe rendering.

---

## 8. Accessibility

Public sites follow platform WCAG target.

Builder prevents obvious inaccessible combinations where practical.

---

## 9. Forms

Public forms connect directly to:
- lead
- project request
- support
- application
- order
- appointment
- custom workflow.

Spam/abuse protection required.

---

## 10. eCommerce

Storefront:
- catalog
- variants
- inventory availability
- price lists/promotions
- cart
- checkout
- delivery/pickup
- payment adapter
- order tracking
- return/refund.

Country/tax/payment policies govern checkout.

---

## 11. Personalization

Future:
- customer segment
- locale
- campaign
- consent
- previous behavior.

Do not create dark patterns or unlawful profiling.

---

## 12. Headless mode

Expose:
- catalog
- content
- search
- forms
- account
- cart/order
through stable APIs where entitlement allows.

---

## 13. V1 boundary

V1 ships a strong corporate/eCommerce builder integrated to Hayool data.

Do not attempt to equal every specialized design tool/plugin ecosystem before core business flows are stable.

