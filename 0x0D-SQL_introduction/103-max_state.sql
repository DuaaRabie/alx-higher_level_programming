-- Temperatures 2
SELECT state, AVG(value) AS avg_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
