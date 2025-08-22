select
  customer_id,
  any_value(country) as country
from {{ ref('stg_retail') }}
where customer_id is not null
group by customer_id
