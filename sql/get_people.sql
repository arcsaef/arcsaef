
SELECT
  id_person       AS 'ID_Person'
  , title         AS 'Title'
  , first_name    AS 'FirstName'
  , last_name    AS 'LastName'
  , career_stage  AS 'CareerStage'
  , status        AS 'State'
  , fte           AS 'FTE'
  , position      AS 'Position'
  , gender        AS 'Gender'
  , start_dt      AS 'StartDaate'
  , end_dt        AS 'EndDate'
  , org           AS 'Org'
  , organisation  AS 'Organisation'
  -- MISSING PROFILE
  , saef_funded   AS 'SAEFFunded'
  , consent       AS 'Content'
  , orcid         AS 'ORCID'
  , email         AS 'Email'
  , post_nominals AS 'PostNominals'
  , role          AS 'Role'
  , student_project_title AS 'StudentProjectTitle'
  , (SELECT title from grants join ppl_grants on  id_grants = idf_associated_grants WHERE idf_person = ppl.id_person) AS 'Grants'

FROM ppl;

 
            -- 'Profile':      prsn['fieldData']['Profile'],
            -- 'Training':     prsn['portalData']['people_Training'], 
            -- 'Prizes':       prsn['portalData']['Prizes'],

