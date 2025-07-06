CREATE TABLE IF NOT EXISTS `ritayan_dwh.irctc_stream_data` (
  row_key  STRING,
  name STRING,
  age INT64,
  email STRING,
  join_date DATE,
  last_login TIMESTAMP,
  loyalty_points INT64,
  account_balance FLOAT64,
  is_active BOOL,
  inserted_at TIMESTAMP,
  updated_at TIMESTAMP,
  loyalty_status STRING,
  account_age_days INT64
);

SELECT * FROM `ritayan_dwh.irctc_stream_data`;