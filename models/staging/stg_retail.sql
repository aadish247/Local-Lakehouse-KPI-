with raw as (
  select *
  from {{ ref('online_retail_II') }}
)
, cleaned as (
  select
    cast(InvoiceNo as varchar)        as invoice_id,
    cast(StockCode as varchar)        as sku,
    cast(Description as varchar)      as product_description,
    cast(Quantity as int)             as quantity,
    cast(strptime(InvoiceDate, '%d-%m-%Y %H:%M') as timestamp) as invoice_ts,
    cast(UnitPrice as double)         as unit_price,
    cast(CustomerID as varchar)       as customer_id,
    cast(Country as varchar)          as country
  from raw
  where Quantity > 0
    and unit_price >= 0
    and CustomerID is not null
)
select * from cleaned