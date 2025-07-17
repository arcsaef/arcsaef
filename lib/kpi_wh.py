import sqlite3
import sys
import pandas as pd
from sqlite3 import OperationalError

def get_person(data, pid, rpt_yr):

    sqliteConnection = sqlite3.connect(data)
    cursor_obj       = sqliteConnection.cursor()

    core = cursor_obj.execute(
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
          , trim(title)||' '||trim(first_name)||' '||trim(last_name)||' '||trim(post_nominals)  AS 'Salutation'
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

    return [core, supervises, crossnode_supervision, advisory, workshops, grants, prizes]

''' Create a biographic dataset of SAEF '''
def people_construct(data, rpt_yr):

    sqliteConnection = sqlite3.connect(data)
    cursor_obj       = sqliteConnection.cursor()
    people, ppl_hash = {}, {}

    result = cursor_obj.execute("SELECT id_person FROM ppl").fetchall()

    for row in result:
        pid = row[0]

        # build SAEF person data point
        core = cursor_obj.execute(
        '''
        SELECT 
          title 
          , first_name 
          , last_name
          , career_stage 
          , status
          , fte 
          , position 
          , gender 
          , ppl.start_dt 
          , ppl.end_dt 
          , org
          , organisation
          , saef_funded
          , consent 
          , orcid 
          , email 
          , post_nominals 
          , ppl.role 
          , student_project_title
          , GROUP_CONCAT( ppl_projects.project_code )
          , trim(title)||' '||trim(first_name)||' '||trim(last_name)||' '||trim(post_nominals)
          , replace(first_name, ' ', '')||replace(last_name, ' ', '')
        FROM ppl
        LEFT JOIN ppl_projects
          ON ppl_projects.id_person = ppl.id_person
        WHERE ppl.id_person = ?
        ''', 
        (pid, ) ).fetchone()

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

        # Build a dataset of SAEF persons
        people[pid] = {'Title':         core[0],
                       'FirstName':     core[1],
                       'LastName':      core[2],
                       'CareerStage':   core[3],
                       'State':         core[4],
                       'FTE':           core[5],
                       'Position':      core[6],
                       'Gender':        core[7],
                       'StartDate':     core[8],
                       'EndDate':       core[9],
                       'Org':           core[10],
                       'Organisation':  core[11],
                       'SAEFFunded':    core[12],
                       'Cnsent':        core[13],
                       'ORCID':         core[14],
                       'Email':         core[15],
                       'PostNominals':  core[16],
                       'Role':          core[17],
                       'StudentProjectTitle': core[18],
                       'Projects':      core[19],
                       'Salutation':    core[20],
                       'Workshops':     list(workshops),
                       'Supervises':    list(supervises), 
                       'Advisory':      list(advisory), 
                       'CrossnodeSupervision': list(crossnode_supervision),
                       'Grants':        list(grants),
                       'Prizes':        list(prizes)}
        ppl_hash[core[21]] = pid

    cursor_obj.close()

    return people, ppl_hash


def projects_construct(data):
    sqliteConnection = sqlite3.connect(data)
    cursor_obj       = sqliteConnection.cursor()


    query = ''' SELECT 
             project_code       AS ProjectCode
           , project_contact    AS Contact
           , (SELECT fullname 
              FROM ppl_projects 
              WHERE project_role = 'Manager' 
              AND id_project = projects.id_project) AS Manager
           , project_alias      AS ProjectAlias
           , project_title      AS ProjectTitle
           , project_lead_org   AS ProjectLeadOrganisation
           , project_status     AS Status    
          FROM projects 
          ORDER BY 1; '''

    df = pd.read_sql_query(query, sqliteConnection)

    return df


#### Test harness ###
# p0 = sys.argv[1] # data
# p1 = sys.argv[2] # pid
# p2 = sys.argv[3] # rpt_yr
# x = get_person( p0, p1, p2 )
# y = people_construct( p0, p2 )
# z = projects_construct(p0)
# print(x)
# print(y[0])
# print(z)/
