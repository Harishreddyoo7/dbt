version: 2
 
models:
  - name: my_seed_table
    columns:
      - name: id
        tests:
          - unique
      - name: name
      - name: occupation
    seed:
      +file: C:\Users\harishreddy.kaki\dbt_core\dbt_demo\seeds\hacker_data.csv