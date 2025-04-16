

-- This portion of the query returns all publications
-- in 2021 by an AI, PI or CI. A start date, end date
-- filter is not required because of the prior
-- restriction, i.e. you published in 2021.
SELECT 
a.position
  , a.author_key 
	, b.pub_yr
	, b.title 
FROM ppl a
JOIN tmp_outputs_author b 
	ON a.author_key= b.author_key
WHERE a.position in ('Associate Investigator', 'Chief Investigator',
 'Partner Investigator')
AND b.pub_yr = 2024
UNION
SELECT 
a.position
  , a.author_key 
	, "2024" as pub_yr
	, "" AS title 
FROM ppl a
WHERE a.author_key NOT IN ( SELECT a.author_key
							FROM ppl a
							JOIN tmp_outputs_author b 
								ON a.author_key= b.author_key
							WHERE b.pub_yr = 2024
							AND a.position in ('Associate Investigator', 
								'Chief Investigator', 'Partner Investigator'))
AND a.position in ('Associate Investigator', 'Chief Investigator',
 'Partner Investigator')
AND a.start_dt <= '2024-12-31' -- Commenced b/4 the end of calendar year
AND a.end_dt > '2023-12-31' OR a.end_dt is NULL -- Terminated after start of calendar year or on going
ORDER BY 1, 2
