> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — Manufacturing, Asset, Maintenance, IoT & Edge Specification
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping
Principle: Integrate business operations with industrial systems without pretending a generic ERP is a PLC/SCADA/DCS

---

## 1. Manufacturing pack

Entities:
- Material
- BOM / Recipe / Formula
- Routing
- Operation
- Work Center
- Production Order
- Batch
- Work Instruction
- Quality Check
- Scrap
- Yield
- Downtime
- Production Output.

---

## 2. Planning

Capabilities:
- make-to-stock
- make-to-order
- material requirements
- capacity requirements
- planned production
- shortage detection.

Mathematical planning/solver output remains distinct from LLM recommendations.

---

## 3. BOM / recipe

Support:
- multi-level BOM
- revision/version
- effective dates
- substitutes
- by-products/co-products where pack allows
- unit conversions
- approved changes.

Food/chemical/process manufacturing can extend with formula/recipe controls.

---

## 4. Work centers

Track:
- capability
- calendar
- capacity
- setup/changeover
- operating cost
- maintenance status
- qualifications required.

---

## 5. Quality

Quality engine:
- inspection plan
- sampling
- result
- nonconformance
- hold/quarantine
- corrective action
- CAPA extension where required
- certificate/document.

Industry packs add regulated quality rules.

---

## 6. Asset / EAM

Asset hierarchy:
Site
→ Area
→ System
→ Equipment
→ Component.

Capabilities:
- asset register
- criticality
- warranty
- meter
- preventive maintenance
- condition maintenance hooks
- work order
- spare parts
- downtime
- failure mode
- maintenance history
- calibration/certification extension.

---

## 7. Field service

Work Order
→ technician/team
→ location
→ parts/tools
→ schedule
→ travel
→ work evidence
→ customer signoff
→ invoice.

Mobile/offline workflow is first-class for field use.

---

## 8. Industrial boundary

Hayool OS is primarily enterprise/business/workforce/orchestration software.

For industrial control:
- Level 4 enterprise/business planning is native.
- Manufacturing operations integration may bridge to Level 3 MES/MOM.
- PLC/DCS/SCADA control remains in specialized systems unless a dedicated certified product is later created.

Use ISA-95/IEC 62264 concepts as an interoperability reference.

---

## 9. OPC UA

Industrial connector architecture should allow OPC UA adapters through a controlled Edge Gateway.

Do not connect public-cloud application code directly to arbitrary plant-floor PLC networks.

---

## 10. MQTT / device telemetry

For lightweight devices/IoT, support MQTT adapters.

Telemetry pipeline:
Device
→ Edge/Connector
→ Event ingestion
→ validation
→ time-series/event store/read model
→ rules/alerts
→ business workflow.

Critical control loops should not depend on an LLM/cloud round trip.

---

## 11. Edge Gateway

Optional deployment component for:
- factories
- warehouses
- farms
- branches
- constrained/occasionally connected sites.

Functions:
- device/protocol connector
- local buffering
- local rule execution
- secure outbound connection
- store-and-forward
- certificate/device identity
- remote health/update.

---

## 12. Offline resilience

Operational mobile applications may require:
- local queue
- offline forms
- barcode scan
- attachment capture
- eventual sync
- conflict policy.

Financial finalization and other authoritative actions may require online validation.

---

## 13. Digital twin expansion

Physical Digital Twin can model:
- equipment
- production capacity
- maintenance state
- inventory
- work center
- transport capacity
- energy/condition metrics.

Simulation remains separate from control state.

---

## 14. Industrial cybersecurity

OT connectivity requires:
- network segmentation
- least privilege
- outbound-only patterns where possible
- certificate/device identity
- no unrestricted AI tool access to control systems
- audit
- protocol allowlists.

---

## 15. V1 boundary

Build ERP/MRP/EAM baseline and integration architecture.

Do not claim V1 is a safety-certified industrial control system.

