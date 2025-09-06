SELECT 
  a.title
  , a.first_name
	, a.last_name
	, a.organisation
	, a.position
	, a.start_dt
	, a.end_dt
FROM ppl a
WHERE  a.sql != "No"
AND a.status = 'Active'
