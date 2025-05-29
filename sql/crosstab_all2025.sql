-- This portion of the query returns saef researchers listed on a publications
SELECT a.position
  , a.author_key 
	, b.pub_yr
	, b.title 
FROM ppl a
JOIN tmp_outputs_author b 
	ON a.author_key= b.author_key
WHERE b.pub_yr = 2025
AND a.sql != "No"
AND DATE(SUBSTR(a.end_dt, -4)||'-'||SUBSTR(a.end_dt, INSTR(a.end_dt, "/")+1, 2)||'-'||SUBSTR('00'||SUBSTR(a.end_dt, 0, INSTR(a.end_dt, "/")), -2)  ) >= "2025-01-01"
UNION
-- This portion of the query returns saef researchers w/o a publication.
SELECT position
  , author_key 
	, "2025" as pub_yr
	, "" AS title 
FROM ppl a
WHERE a.sql != "No"
AND DATE(SUBSTR(a.end_dt, -4)||'-'||SUBSTR(a.end_dt, INSTR(a.end_dt, "/")+1, 2)||'-'||SUBSTR('00'||SUBSTR(a.end_dt, 0, INSTR(a.end_dt, "/")), -2)  ) >= "2025-01-01"
AND id_person NOT IN ( SELECT a.id_person
													FROM ppl a
													JOIN tmp_outputs_author b 
															ON a.author_key= b.author_key
													WHERE b.pub_yr = 2025
													AND DATE(SUBSTR(a.end_dt, -4)||'-'||SUBSTR(a.end_dt, INSTR(a.end_dt, "/")+1, 2)||'-'||SUBSTR('00'||SUBSTR(a.end_dt, 0, INSTR(a.end_dt, "/")), -2)  ) >= "2025-01-01"
													AND a.sql != "No")
ORDER BY 1, 2
