SELECT 
 a.author_key
  , COUNT(*) AS Total
FROM ppl a
JOIN tmp_outputs_author b 
  ON a.author_key= b.author_key
WHERE a.position in ('Associate Investigator', 'Chief Investigator',
 'Partner Investigator')
AND b.pub_yr = 2024
AND a.start_dt <= '2024-12-31'
AND a.end_dt > '2024-12-31' OR a.end_dt is NULL
GROUP BY a.author_key
UNION
SELECT 
  a.author_key
  , '0' AS Total
FROM ppl a
WHERE a.author_key NOT IN ( SELECT a.author_key
              FROM ppl a
              JOIN tmp_outputs_author b 
                ON a.author_key= b.author_key
              WHERE b.pub_yr = 2024
              AND a.start_dt <= '2024-12-31'
              AND a.end_dt > '2024-12-31' OR a.end_dt is NULL
              AND a.position in ('Associate Investigator', 
                'Chief Investigator', 'Partner Investigator'))
AND a.position in ('Associate Investigator', 'Chief Investigator',
 'Partner Investigator')
AND a.start_dt <= '2024-12-31'
AND a.end_dt > '2024-12-31' OR a.end_dt is NULL
GROUP BY a.author_key
