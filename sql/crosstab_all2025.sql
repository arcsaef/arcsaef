-- This portion of the query returns saef researchers listed on a publications
SELECT a.position
  , a.author_key 
	, b.pub_yr
	, b.title 
FROM ppl a
JOIN tmp_outputs_author b 
	ON a.author_key= b.author_key
WHERE b.pub_yr = 2025
UNION
-- This portion of the query returns saef researchers w/o a publication.
SELECT position
  , author_key 
	, "2025" as pub_yr
	, "" AS title 
FROM ppl a
WHERE id_person NOT IN ( SELECT a.id_person
													FROM ppl a
													JOIN tmp_outputs_author b 
															ON a.author_key= b.author_key
													WHERE b.pub_yr = 2025)
ORDER BY 1, 2
