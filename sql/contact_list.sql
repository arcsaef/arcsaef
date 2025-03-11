-- Contact list
-- For each person, append a project(s) string or None
SELECT 
	a.title,
	a.first_name,
	a.last_name,
	a.email,
	a.organisation,
	a.position,
	GROUP_CONCAT(c.project ) 	AS Projects
FROM ppl 		  a
LEFT JOIN ppl_projects b ON a.id_person  = b.id_person
LEFT JOIN projectKey   c ON b.id_project = c.id_project
WHERE a.status 					== 'Active'
AND a.position 					!= 'Advisory'
AND (b.project_status 			== 'Active' OR b.project_status IS NULL)
GROUP BY 
	a.id_person
ORDER BY  
	a.first_name,
	a.last_name,
	a.email,
	a.organisation,
	a.position,
	a.title; 

