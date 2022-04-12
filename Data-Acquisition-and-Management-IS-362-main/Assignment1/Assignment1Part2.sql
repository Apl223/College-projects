SELECT month,AVG(dep_time) from flights WHERE month BETWEEN 1 and 12
GROUP BY month;