-- This portion of the query returns a AI, CI & PI publications
SELECT a.position
  , a.author_key 
	, b.pub_yr
	, b.title 
FROM acp_2023 a
JOIN tmp_outputs_author b 
	ON a.author_key= b.author_key
WHERE b.pub_yr = 2023
UNION
-- This portion of the query returns a AI, CI & PI w/o a publication.
SELECT position
  , author_key 
	, "2023" as pub_yr
	, "" AS title 
FROM acp_2023 a
WHERE id_person NOT IN ( 
      SELECT a.id_person
			FROM acp_2023 a
			JOIN tmp_outputs_author b 
				ON a.author_key= b.author_key
			WHERE b.pub_yr = 2023
			)
ORDER BY 1, 2
