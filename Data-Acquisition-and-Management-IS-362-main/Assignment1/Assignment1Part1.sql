# Question 1
SELECT COUNT(speed) FROM planes WHERE speed IS NOT NULL;
SELECT MAX(speed) FROM planes;
SELECT MIN(speed) FROM planes;

# Question 2
SELECT SUM(distance) AS 'Total distance' FROM flights
WHERE (year = 2013 AND month = 1);
SELECT SUM(distance) AS 'Total distance' FROM flights
WHERE (year = 2013 AND month = 1) AND tailnum IS NULL;	

#Question 3
SELECT COUNT(*) AS 'Flights', SUM(distance) AS 'Total distance', manufacturer AS 'Manufacturer'
FROM flights INNER JOIN planes ON flights.tailnum = planes.tailnum
WHERE (flights.year = 2013 AND flights.month = 7 AND flights.day = 5)
GROUP BY manufacturer;

SELECT COUNT(*) AS 'Flights', SUM(distance) AS 'Total distance', manufacturer AS 'Manufacturer'
FROM flights LEFT JOIN planes ON flights.tailnum = planes.tailnum
WHERE (flights.year = 2013 AND flights.month = 7 AND flights.day = 5)
GROUP BY manufacturer;
#LEFT JOIN has 140 more flights with no manufacturer listed

/*
Question 4
What is the total distance flown for all planes on August 
2013 by American Airlines grouped by aircraft manufacturer?  
*/

SELECT SUM(distance) AS 'Total distance', manufacturer AS 'Manufacturer'
FROM flights LEFT JOIN planes ON flights.tailnum = planes.tailnum
LEFT JOIN airlines ON flights.carrier = airlines.carrier
WHERE (flights.year = 2013 AND flights.month = 8)
GROUP BY manufacturer;