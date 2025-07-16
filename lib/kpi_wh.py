import sqlite3
import sys
from sqlite3 import OperationalError

p1 = sys.argv[2] # pid
p2 = sys.argv[3] # rpt_yr

def get_person(pid, rpt_yr):

    sqliteConnection = sqlite3.connect(sys.argv[1])
    cursor_obj       = sqliteConnection.cursor()

    result = cursor_obj.execute(
        '''
        SELECT ppl.id_person   AS 'ID_Person'
          , title         AS 'Title'
          , first_name    AS 'FirstName'
          , last_name     AS 'LastName'
          , career_stage  AS 'CareerStage'
          , status        AS 'State'
          , fte           AS 'FTE'
          , position      AS 'Position'
          , gender        AS 'Gender'
          , ppl.start_dt  AS 'StartDaate'
          , ppl.end_dt    AS 'EndDate'
          , org           AS 'Org'
          , organisation  AS 'Organisation'
          , saef_funded   AS 'SAEFFunded'
          , consent       AS 'Content'
          , orcid         AS 'ORCID'
          , email         AS 'Email'
          , post_nominals AS 'PostNominals'
          , ppl.role      AS 'Role'
          , student_project_title AS 'StudentProjectTitle'
          , GROUP_CONCAT( ppl_projects.project_code ) AS 'Projects'
        FROM ppl
        LEFT JOIN ppl_projects
          ON ppl_projects.id_person = ppl.id_person
        WHERE ppl.id_person = ?
        ''', 
        (pid,) ).fetchone()

    advisory = cursor_obj.execute(
        '''
        SELECT GROUP_CONCAT( TRIM (role) )
        FROM ppl_advisory
        WHERE (end_dt >= ? OR end_dt = '') AND (role <> '' )
        AND idf_person = ?
        ''', 
        (rpt_yr, pid,) ).fetchone()

    supervises = cursor_obj.execute(
        '''
        SELECT GROUP_CONCAT( TRIM (ppl.first_name || ' ' || ppl.last_name ) )
        FROM ppl
        JOIN ppl_supervision
          ON id_reportee = id_person
        WHERE id_mgr = ?
        ''', 
        (pid,) ).fetchone()

    crossnode_supervision = cursor_obj.execute(
        '''
        SELECT GROUP_CONCAT( TRIM (crossnode) )
        FROM ppl
        JOIN ppl_supervision
          ON id_reportee = id_person
        WHERE id_mgr = ?
        ''', 
        (pid,) ).fetchone()

    workshops = cursor_obj.execute(
        '''
        SELECT GROUP_CONCAT( TRIM (workshops.title) )
        FROM workshops
        JOIN ppl_workshops
          ON idf_workshop= id_workshop
        WHERE idf_person = ?
        ''', 
        (pid,) ).fetchone()

    grants = cursor_obj.execute(
        '''
        SELECT GROUP_CONCAT( TRIM (grants.title) )
        FROM grants
        JOIN ppl_grants
          ON idf_associated_grants = id_grants
        WHERE idf_person = ?
        AND grants.grant_year >= ?
        ''', 
        (pid, rpt_yr) ).fetchone()

    prizes = cursor_obj.execute(
        '''
        SELECT GROUP_CONCAT( TRIM (prizes.title) )
        FROM prizes
        WHERE idf_person = ?
        AND prizes.prize_year >= ?
        ''', 
        (pid, rpt_yr) ).fetchone()

    cursor_obj.close()

    return [result, supervises, crossnode_supervision, advisory, workshops, grants, prizes]

x = get_person( p1, p2 )
print(x)





