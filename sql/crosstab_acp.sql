


SELECT 
	a.author_key
	, a.position
	, b.pub_yr
	, b.title 
FROM ppl a
JOIN tmp_outputs_author b 
	ON a.author_key= b.author_key
WHERE a.position in ('Associate Investigator', 'Chief Investigator',
 'Partner Investigator')
AND b.pub_yr = 2021
AND a.start_dt <= '2021-12-31'
AND a.end_dt > '2021-12-31' OR a.end_dt is NULL
UNION
SELECT 
	a.author_key
	, a.position
	, "2021" as pub_yr
	, "" AS title 
FROM ppl a
WHERE a.author_key NOT IN ( SELECT a.author_key
							FROM ppl a
							JOIN tmp_outputs_author b 
								ON a.author_key= b.author_key
							WHERE b.pub_yr = 2021
							AND a.start_dt <= '2021-12-31'
							AND a.end_dt > '2021-12-31' OR a.end_dt is NULL
							AND a.position in ('Associate Investigator', 
								'Chief Investigator', 'Partner Investigator'))
AND a.position in ('Associate Investigator', 'Chief Investigator',
 'Partner Investigator')
AND a.start_dt <= '2021-12-31'
AND a.end_dt > '2021-12-31' OR a.end_dt is NULL
ORDER BY 2, 1
