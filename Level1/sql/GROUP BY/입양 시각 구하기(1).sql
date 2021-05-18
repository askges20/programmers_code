SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 AND HOUR < 20
ORDER BY HOUR;
