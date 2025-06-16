--
INSERT INTO ppl_projects (id_person, id_project, project_status, fullname, person_status)
SELECT 
  ppl.id_person, 
  tmp_ppl_projects.id_project,
  projects.project_status,
  ppl.first_name || " " || ppl.last_name,
  ppl.status
FROM  ppl, tmp_ppl_projects, projects
WHERE ppl.id_person = tmp_ppl_projects.id_person
AND   tmp_ppl_projects.id_project = projects.id_project;
