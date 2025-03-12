SELECT gender, COUNT(*) AS n 
FROM ppl 
WHERE status = 'Active' 
GROUP BY gender 
ORDER BY 2 DESC;
