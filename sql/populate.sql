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

-- Create author key
UPDATE ppl SET author_key = first_name || last_name;

-- Update ppl org from organisations
UPDATE ppl 
  SET org = t.org
  FROM (SELECT org, id_organisation
        FROM organisations) AS t
WHERE ppl.idf_organisation = t.id_organisation;

-- Update ppl organisation from organisations
UPDATE ppl 
UPDATE ppl 
  SET organisation = t.organisation
  FROM (SELECT organisation, id_organisation
        FROM organisations) AS t
WHERE ppl.idf_organisation = t.id_organisation;
