-- Current list: all "active" members of SAEF
-- This query is typically used for Steven Chown
SELECT 
	a.title,
	a.first_name,
	a.last_name,
	a.organisation,
	a.position,
	a.start_dt,
	a.end_dt
FROM ppl a
WHERE a.status 	== 'Active'
ORDER BY a.first_name; 

