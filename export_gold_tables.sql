-- DuckDB SQL script to export gold tables to Parquet files for Power BI

COPY fact_sales      TO '../bi/fact_sales.parquet' (FORMAT PARQUET);
COPY dim_customer    TO '../bi/dim_customer.parquet' (FORMAT PARQUET);
COPY dim_product     TO '../bi/dim_product.parquet' (FORMAT PARQUET);
