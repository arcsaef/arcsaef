/* Return an orcid, firstname last name double.
   RemeMber to set :orcid_end_dt param BEFORE
   the query is run. E.g. .param set :orcid_end_dt "'YYYY-MM-DD'"
*/

SELECT
  orcid, position
  , first_name || ' ' || last_name

FROM ppl
WHERE sql != 'No'
AND orcid <> ''
AND (date(substr(end_dt, -4, 4) || '-' || substr(end_dt, -7, 2) || '-01')  > 
     date(:orcid_end_dt) OR end_dt == '')
AND position IN ('Chief Investigator', 'Partner Investigator', 'Post Doc')
ORDER BY position, first_name;
