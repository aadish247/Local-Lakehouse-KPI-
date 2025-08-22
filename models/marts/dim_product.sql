select
  sku,
  any_value(product_description) as product_description
from {{ ref('stg_retail') }}
group by sku
