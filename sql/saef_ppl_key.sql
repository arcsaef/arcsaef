
SELECT id_person
	, orcid
 	, author_key
	, first_name
	, last_name
FROM ppl
WHERE status LIKE 'Active'
AND sql NOT LIKE 'No'
ORDER BY 3;