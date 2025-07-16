-- Create ppl->projects (active only) association
INSERT INTO ppl_projects (id_person, id_project, project_code
                          , project_status, fullname, person_status
                          , project_role, project_fte)
SELECT 
  ppl.id_person, 
  tmp_ppl_projects.idf_project,
  projects.project_code,
  projects.project_status,
  ppl.first_name || " " || ppl.last_name,
  ppl.status,
  tmp_ppl_projects.role,
  tmp_ppl_projects.fte
FROM  ppl, tmp_ppl_projects, projects
WHERE ppl.id_person = tmp_ppl_projects.idf_person
AND   tmp_ppl_projects.idf_project = projects.id_project
AND projects.project_state = 'Active';

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
  SET organisation = t.organisation
  FROM (SELECT organisation, id_organisation
        FROM organisations) AS t
WHERE ppl.idf_organisation = t.id_organisation;
