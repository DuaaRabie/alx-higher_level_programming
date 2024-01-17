-- Temperatures 1
SELECT city, MAX(value) AS max_temp
FROM temperatures
WHERE EXTRACT(MONTH FROM date) IN (7, 8)
GROUP BY city
ORDER BY max_temp DESC
LIMIT 3;
