# Inventory movement versus stocktake and valuation

Status: specified V1.8. REQ-UNI-003 owns quantity movement and reservation; REQ-UNI-022 owns count-adjustment approval, cost basis/valuation/COGS and exact finance reconciliation. Manufacturing, fulfillment and commerce disputes can reference movements but cannot silently edit posted count or journal history.

Movement ledger preserves tenant/entity/site/bin/item/lot/serial/UOM/source/actor/time and idempotency, reservation source and lifecycle. Stocktake captures frozen count window, counted evidence, variance reason, independent approval and compensating movement. Valuation records book/entity, inventory ownership, effective cost method/version, currency/FX and rounded cost layers; ledger posting is authoritative for accounting values, no inventory quantity edit can invent actual financial posting. Unknown policy blocks real method selection.

`TEST-REQ-UNI-003`: two concurrent reservations, wrong-lot dispatch, duplicate receipt/return and partial pick conserve exact quantities. `TEST-REQ-UNI-022`: physical recount, damaged batch, return, cost change and closed period produce approved adjustment and independently computed roll-forward matching COGS/stock ledger; wrong entity, missing cost basis or stale count cannot silently post. GJ-05 includes both.
