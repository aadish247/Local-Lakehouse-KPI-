with base as (
  select
    invoice_id,
    customer_id,
    sku,
    invoice_ts::date as order_date,
    quantity,
    unit_price,
    quantity * unit_price as line_amount
  from {{ ref('stg_retail') }}
)
select * from base
