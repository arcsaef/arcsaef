## Initial table creation
CREATE TABLE ppl_projects(
	id_person TEXT, 
	id_project TEXT, 
	project_status TEXT, 
	fullname TEXT, 
	person_status TEXT);

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
	organisation TEXT,
	status TEXT,
	start_dt DATE,
	end_dt DATE,
	author_key TEXT);

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
