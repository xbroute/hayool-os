> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — Commerce, Procurement, Inventory, WMS & Logistics Specification
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping

---

## 1. Purpose

Provide reusable physical-goods and service-trade capabilities needed by retailers, wholesalers, distributors, warehouses, manufacturers, farms and service companies.

---

## 2. Master data

### Item Master
Supports:
- physical product
- consumable
- raw material
- component
- finished good
- spare part
- service
- digital product
- bundle
- packaging unit.

Fields:
- internal SKU
- barcode/GTIN mapping
- variant attributes
- descriptions/translations
- units of measure
- dimensions/weight
- tax/category policy
- shelf life
- lot/serial policy
- storage conditions
- hazardous/restricted attributes
- purchase/sales status.

### Party Master
- customer
- supplier
- carrier
- marketplace provider
- manufacturer
- distributor.

### Location Master
- legal site
- warehouse
- zone
- aisle/bin
- store
- pickup point
- dock
- virtual location.

---

## 3. Units of measure

UOM engine:
- quantity
- mass
- length
- area
- volume
- time
- packaging
- domain-specific units through packs.

Conversions are deterministic, versioned where necessary and precision-aware.

---

## 4. Sales / Order Management

Support:
- quotation
- sales order
- reservation
- fulfillment
- partial fulfillment
- backorder
- shipment
- return
- refund
- recurring order
- channel/source
- promotion/discount policy.

Orders may originate from:
- admin
- website
- POS
- marketplace
- API
- external network.

---

## 5. Procurement

Lifecycle:
Need/Requisition
→ Approval
→ Source
→ RFQ
→ Supplier Quotes
→ Evaluation
→ Purchase Order
→ Receipt
→ Quality/Acceptance
→ Supplier Invoice
→ Payment.

Support:
- approved supplier lists
- contracts
- price lists
- minimum quantities
- lead time
- supplier reliability
- landed cost
- purchase budget
- three-way match where configured.

---

## 6. Inventory

Core:
- stock on hand
- available
- reserved
- incoming
- outgoing
- quarantine
- damaged
- consignment where supported.

Movements:
- receipt
- putaway
- pick
- pack
- ship
- transfer
- consume
- produce
- adjust
- return
- scrap.

Inventory movement is auditable.

---

## 7. Lot / serial / expiry

Support:
- lot/batch
- serial number
- manufacture date
- expiry
- source
- certificates
- recall/hold
- chain of custody.

FEFO/FIFO policies configurable.

---

## 8. WMS

Warehouse features:
- multi-warehouse
- zones/bins
- receiving
- putaway strategy
- replenishment
- wave/batch picking future/when needed
- barcode/mobile scanning
- packing
- dispatch
- cycle counting
- stocktake
- transfer
- dock/appointment hooks.

Do not force advanced WMS features on a small shop.

---

## 9. Replenishment

Policies:
- min/max
- reorder point
- safety stock
- forecast-driven
- planned purchase
- planned production.

Forecasting informs; deterministic policy creates approved replenishment actions.

---

## 10. Pricing

Commerce pricing supports:
- price lists
- customer groups
- contract price
- quantity breaks
- promotion
- coupon
- bundle
- channel price
- tax-inclusive/exclusive presentation
- currency.

Rules are versioned.

---

## 11. POS

Optional pack:
- touch-friendly
- product scan
- customer
- discounts under permission
- payment providers
- receipt
- cash session
- offline/degraded mode where practical
- inventory sync.

Fiscal requirements are country-pack dependent.

---

## 12. Logistics

Entities:
- Shipment
- Package
- Load
- Stop
- Route
- Carrier
- Vehicle
- Driver
- Pickup
- Delivery
- Proof of Delivery.

Support:
- own fleet
- third-party carrier
- local courier
- provider network
- customer pickup.

---

## 13. Route / dispatch optimization

Use a solver/route provider abstraction.

Inputs:
- pickup/delivery
- time windows
- vehicle capacity
- driver availability
- service time
- priorities
- road/network constraints.

Output:
- dispatch/route plan.

LLMs do not calculate route optimization.

---

## 14. Fleet

Optional:
- vehicles
- capacity
- assignment
- odometer
- fuel
- maintenance
- documents
- insurance/expiry
- incidents.

---

## 15. Traceability

Adopt globally interoperable identification/traceability concepts where useful.

Architecture should map to:
- GTIN/product identifiers
- GLN/location identifiers
- EPCIS-like event capture/query
- barcode/RFID identifiers

without making GS1 membership mandatory for every tenant.

Traceability event examples:
- received
- packed
- transformed
- shipped
- transported
- delivered.

---

## 16. Cold-chain / condition data

Lots/shipments may link:
- temperature
- humidity
- shock
- time
- sensor
- threshold violation.

Condition telemetry is time-series/event data, not ordinary invoice metadata.

---

## 17. Marketplace catalog federation

Providers may expose:
- catalog
- price
- availability
- delivery options
- service area

through:
- native Hayool portal
- API
- connector
- compatible open network.

---

## 18. Finance integration

Operational events map deterministically to:
- receivable
- payable
- inventory valuation
- COGS
- landed cost
- revenue
- tax
- cash/payment.

Accounting posting rules depend on accounting/country policy.

---

## 19. Multi-company/intercompany

Enterprise support:
- legal entity ownership
- cross-company orders
- intercompany invoice
- transfer
- elimination hooks
- consolidated reporting.

Intercompany accounting rules require explicit configuration.

---

## 20. V1 delivery

V1 baseline should support:
- item catalog
- sales order
- purchase order
- stock locations
- inventory movement
- lot/serial
- basic replenishment
- shipment/delivery
- barcode-ready mobile workflows
- finance links
- provider/connector abstraction.

Advanced WMS/TMS features may be activated through packs without architectural rewrite.

