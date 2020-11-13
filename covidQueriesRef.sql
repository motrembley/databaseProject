-- #1 Gives the types of test available and the available units
SELECT t_type, t_units FROM Testing ORDER BY t_units DESC

-- #2 Gives the person ID of those who recieved tests
SELECT * FROM TestingAvailability WHERE ta_givenTest = 'YES'

-- #3 Gives the name of those who did not recieve tests
SELECT p_name FROM Person, TestingAvailability 
    WHERE ta_personID = p_ID AND ta_givenTest = 'NO'

-- #4 Gives the name and case ID for each test
SELECT p_name, r_caseID FROM Person, Results WHERE p_ID = r_personID

-- #5 Gives the name and important symptoms for each case
SELECT p_name, s_fever, s_dryCough, s_soreThroat 
    FROM Person, Results, Symptoms 
    WHERE p_ID = r_personID AND r_caseID = s_caseID

-- #6 Gives the name and severity of those with severity of symptoms greater than 5
SELECT p_name, s_severity FROM Person, Results, Symptoms 
    WHERE p_ID = r_personID AND r_caseID = s_caseID AND s_severity > 5

-- #7 Gives the name and address of hospitals with low risk
SELECT h_name, h_address FROM Hospitals WHERE h_riskLevel < 7

-- #8 Gives people born before 1971 (high risk)
SELECT * FROM Person WHERE strftime(p_dob) < strftime('1970-12-31')

-- #9 Gives the name of a person and their current 'outcome' (how they are doing)
SELECT p_name, o_status FROM Person, Results, Outcome 
    WHERE p_ID = r_personID AND r_caseID = o_caseID

-- #10 Gives name, days positive and comments from people who have been sick for 2 weeks +
SELECT p_name, o_dayspositive, o_comments FROM Person, Results, Outcome 
    WHERE p_ID = r_personID AND r_caseID = o_caseID AND o_dayspositive > 14

-- #11 Gives the Hospital name, city and state where the hospital is based (Bethesda right now)
SELECT h_name, l_city, l_state FROM Hospitals, Location 
    WHERE l_city LIKE '%Bethesda%' AND h_address LIKE '%Bethesda%'

-- #12 Gives the name, case number, symptom severity and the descision to admit for each case
SELECT p_name, r_caseID, nh_severity, nh_descision 
    FROM Person, NeedsHospital, Results 
    WHERE nh_address = p_address AND p_ID = r_personID

-- #13 Gives the name and best Hospital choice from those needed to be admitted from above query
SELECT DISTINCT p_name, r_caseID, h_name 
    FROM (SELECT p_name, r_caseID, nh_severity, nh_descision 
        FROM Person, NeedsHospital, Results 
        WHERE nh_address = p_address AND p_ID = r_personID) as t1, Hospitals 
    WHERE t1.nh_descision = 'YES' AND h_riskLevel < 8 GROUP BY p_name

-- #14 Gives the locations where there is any sort of lockdown
SELECT * FROM Location WHERE l_lockdown != 'NO'

-- #15 Gives cities in the US that are under lockdown from above result
SELECT t1.l_city FROM (SELECT * FROM Location WHERE l_lockdown != 'NO') as t1 
    where t1.l_country = 'United States'

-- #16 Gives the name, result of Covid test and current status of people who took those tests
SELECT p_name, r_result, o_status FROM Person, Results, Outcome 
    WHERE p_ID = r_personID AND r_caseID = o_caseID

-- #17 gives people and the number of tests they've taken ordered by number of tests then alphabetical order
SELECT p_name, count(r_caseID) FROM Person, Results 
    WHERE p_ID = r_personID GROUP BY r_caseID 
    ORDER BY count(r_caseID) DESC, p_name ASC

-- #18 gives the number of patients per doctor in each hospital and sorts ascending
SELECT h_name, h_patients / h_doctors FROM Hospitals 
    ORDER BY h_patients / h_doctors ASC, h_name ASC

-- #19 gives the ratio of positive cases to total cases (Not Currently Working)
SELECT CAST(CAST(t1.res as decimal(8,2)) / COUNT(r_caseID) as decimal(8, 2)) as ratio 
    FROM Results, (SELECT COUNT(r_result) as res FROM Results 
        WHERE r_result = 'POSITIVE') as t1

-- #20 takes the average results diplayed and compares for testing availability
SELECT t_type, AVG(t_units) FROM Testing 
    GROUP BY t_type HAVING AVG(t_units) < (SELECT AVG(ta_units) FROM TestingAvailability)
