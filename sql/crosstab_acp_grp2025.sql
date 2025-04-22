SELECT a.Position,  a.author_key, COUNT(b.author_key)
FROM acp_2025 a
LEFT JOIN 
(
  SELECT author_key
  FROM tmp_outputs_author
  WHERE pub_yr = 2025
) b
ON a.author_key=b.author_key
GROUP BY a.author_key
ORDER BY 1, 2;
