--  For each name, return a project(s) string
-- REPLACE(a.fullname,' ', '')
SELECT REPLACE(a.fullname,' ', '') 	AS Prsn, 
	   GROUP_CONCAT(b.project ) 	AS Projects
FROM ppl_projects a
JOIN projectKey b ON a.id_project 	= b.id_project
WHERE a.person_status  				= 'Active'
AND   a.project_status 				= 'Active'
GROUP BY a.fullname;
