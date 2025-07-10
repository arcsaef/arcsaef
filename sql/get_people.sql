
SELECT
  id_person      AS 'ID_Person'
  , title        AS 'Title'
  , first_name   AS 'FirstName'
  , last_name    AS 'LastName'
  , career_stage AS 'CareerStage'
  , status       AS 'State'
  , fte          AS 'FTE'
  , position     AS 'Position'
  , gender       AS 'Gender'
  , start_dt     AS 'StartDaate'
  , end_dt       AS 'EndDate'
  , org          AS 'Org'
  , organisation AS 'Organisation'




 
            'Profile':      prsn['fieldData']['Profile'],
            'SAEFFunded':   prsn['fieldData']['SAEFFunded'], 
            'Consent':      prsn['fieldData']['Consent'],
            'Orcid':        prsn['fieldData']['ORCID'],
            'Email':        prsn['fieldData']['Email'],
            'Postnominal':  prsn['fieldData']['PostNominals'],
            'Role':         prsn['fieldData']['Role'],
            'Grants':       prsn['portalData']['people_Grants'], 
            'Training':     prsn['portalData']['people_Training'], 
            'Prizes':       prsn['portalData']['Prizes'],
            'StudentProjectTitle':  prsn['fieldData']['StudentProjectTitle'], 
