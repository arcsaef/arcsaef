## Initial table creation
DROP TABLE IF EXISTS ppl_projects;
CREATE TABLE ppl_projects(
	id_person TEXT, 
	id_project TEXT, 
	project_status TEXT, 
	fullname TEXT, 
	person_status TEXT);

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
	start_dt DATE,
	end_dt DATE,
	sql TEXT,
	orcid TEXT,
	author_key TEXT,
	org TEXT,
	organisation TEXT);

DROP TABLE IF EXISTS projects;
CREATE TABLE projects(
	id_project TEXT, 
	project_code TEXT,
	project_status TEXT, 
	project_state TEXT,
	project_contact TEXT);


DROP TABLE IF EXISTS tmp_ppl_projects;
CREATE TABLE tmp_ppl_projects(
	id_person TEXT,
	id_project TEXT, 
	role TEXT);

DROP TABLE IF EXISTS organisations;
CREATE TABLE organisations(
	id_organisation TEXT,
	org TEXT, 
	organisation TEXT,
	iso3 TEXT,
	status TEXT);

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
