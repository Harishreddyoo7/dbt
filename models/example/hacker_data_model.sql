


with source_data as (
     Select * from {{ source( 'src_postgres', 'hacker_data' ) }}
)
Select
          name,
          id, 
          occupation
from source_data