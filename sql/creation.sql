## Initial table creation
DROP TABLE IF EXISTS ppl;
CREATE TABLE ppl(
  id_person TEXT PRiMARY KEY, 
  title TEXT, 
  first_name TEXT, 
  last_name TEXT,
  post_nominals TEXT, 
  career_stage TEXT,
  gender TEXT, 
  email TEXT,
  position TEXT,
  idf_organisation TEXT,
  status TEXT,
  start_dt TEXT,                -- Stored as 'DD/MM/YYYY'
  arc_start_dt TEXT,            -- Stored as 'DD/MM/YYYY'
  end_dt TEXT,                  -- Stored as 'DD/MM/YYYY'
  sql TEXT,                     -- 'No' means exclude from a query
  orcid TEXT,
  role TEXT,
  fte TEXT,
  phd_completion_dt TEXT,       -- Stored as 'DD/MM/YYYY'
  phd_exit_category TEXT,
  on_email TEXT,
  on_website TEXT,
  allow_email TEXT,
  consent TEXT,
  saef_funded TEXT,
  peg_approved TEXT,
  student_project_title TEXT,
  australian TEXT,
  org TEXT,
  organisation TEXT,
  author_key TEXT);

DROP TABLE IF EXISTS projects;
CREATE TABLE projects(
  id_project TEXT, 
  project_code TEXT,
  project_alias TEXT,
  project_state TEXT,
  project_status TEXT, 
  project_contact TEXT,
  project_title TEXT,
  project_lead_org TEXT);

DROP TABLE IF EXISTS organisations;
CREATE TABLE organisations(
  id_organisation TEXT,
  org TEXT, 
  organisation TEXT,
  iso3 TEXT,
  status TEXT);

DROP TABLE IF EXISTS grants;
CREATE TABLE grants(
  id_grants TEXT, 
  title TEXT,
  grant_year TEXT,
  value TEXT);

DROP TABLE IF EXISTS workshops;
CREATE TABLE workshops(
  id_workshop TEXT, 
  title TEXT,
  start_dt TEXT,    -- Stored as 'DD/MM/YYYY'
  end_dt TEXT);     -- Stored as 'DD/MM/YYYY'

DROP TABLE IF EXISTS prizes;
CREATE TABLE prizes(
  id_prize TEXT, 
  title TEXT,
  type TEXT,
  prize_year TEXT,
  idf_person TEXT);

DROP TABLE IF EXISTS ppl_advisory;
CREATE TABLE ppl_advisory(
  id_person_advisory TEXT, 
  idf_person TEXT,
  start_dt TEXT,  -- Stored as 'DD/MM/YYYY'
  end_dt TEXT,    -- Stored as 'DD/MM/YYYY'
  role TEXT, 
  scar TEXT);

DROP TABLE IF EXISTS ppl_grants;
CREATE TABLE ppl_grants(
  id_ppl_associated_grants TEXT,
  idf_person TEXT, 
  idf_associated_grants);

DROP TABLE IF EXISTS ppl_workshops;
CREATE TABLE ppl_workshops(
  id_project_workshop TEXT, 
  idf_workshop TEXT, 
  idf_person TEXT);

DROP TABLE IF EXISTS ppl_supervision;
CREATE TABLE ppl_supervision(
  id_ppl_supervision TEXT, 
  id_reportee TEXT,
  id_mgr TEXT,
  role TEXT, 
  crossnode TEXT);

DROP TABLE IF EXISTS ppl_projects;
CREATE TABLE ppl_projects(
  id_person TEXT, 
  id_project TEXT, 
  project_code TEXT,
  project_status TEXT, 
  fullname TEXT, 
  person_status TEXT,
  project_role TEXT,
  project_fte TEXT);

DROP TABLE IF EXISTS tmp_ppl_projects;
CREATE TABLE tmp_ppl_projects(
  idf_person TEXT,
  idf_project TEXT, 
  role TEXT,
  fte TEXT);

-- These tables are used to create crosstab: AI, CI & PI
CREATE TABLE IF NOT EXISTS acp_2021(
  id_person TEXT PRiMARY KEY, 
  author_key TEXT,
  position TEXT);

CREATE TABLE IF NOT EXISTS  acp_2022(
  id_person TEXT PRiMARY KEY, 
  author_key TEXT,
  position TEXT);

CREATE TABLE IF NOT EXISTS  acp_2023(
  id_person TEXT PRiMARY KEY, 
  author_key TEXT,
  position TEXT);

CREATE TABLE IF NOT EXISTS  acp_2024(
  id_person TEXT PRiMARY KEY, 
  author_key TEXT,
  position TEXT);

CREATE TABLE IF NOT EXISTS  acp_2025(
  id_person TEXT PRiMARY KEY, 
  author_key TEXT,
  position TEXT);
