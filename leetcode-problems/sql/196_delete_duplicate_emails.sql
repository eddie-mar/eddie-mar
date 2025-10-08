DELETE FROM Person WHERE id IN (
    SELECT id FROM 
        (SELECT *, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id ASC) AS rn
        FROM Person)
    WHERE rn > 1
)