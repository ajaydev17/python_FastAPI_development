# **PostgreSQL Commands**

1.  Show table definition including constraints
    ```
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = 'category';
    ```
    
    ```
    SELECT constraint_name, constraint_type
    FROM information_schema.table_constraints
    WHERE table_name = 'category' AND constraint_type = 'CHECK';
    ```


2.  Show the definition of a specific constraints
    ```
    SELECT conname AS constraint_name, pg_get_constraintdef(oid) AS definition
    FROM pg_constraint
    WHERE conrelid = (
        SELECT oid
        FROM pg_class
        WHERE relname = 'category'
    ) AND contype = 'c' OR contype = 'u';
    ```