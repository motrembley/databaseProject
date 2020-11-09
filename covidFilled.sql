--     -- Hospital​

--     --     h_name, h_address, h_doctors, h_patients, h_riskLevel​

--     -- Outcome​

--     --     o_caseID, o_dayspositive, o_comments, o_status​

--     -- Location​

--     --     l_city, l_country, l_state, l_lockdown​

--     -- Person​

--     --     p_name, p_address, p_dob, p_comment​

--     -- Result ​

--     --     r_personID, r_caseID, r_date, r_result​

--     -- Symptoms ​

--     --     s_caseID, s_symptom, s_severity ​

--     -- Testing​

--     --     t_type, t_units, t_D.O.B​

--     -- Needs Hospital​

--     --     nh_address, nh_riskLevel, nh_symptom, nh_severity, nh_descision​

--     -- Testing Availability​

--     --     ta_personID, ta_type, ta_units, ta_comment, ta_givenTest​

-- CREATE TABLE Location(
--     l_city char(32) NOT NULL, 
--     l_country char(32) NOT NULL, 
--     l_state char(32) NOT NULL, 
--     l_lockdown char(8)
-- );

INSERT INTO Location  VALUES('San Diego','United States','California','YES')
INSERT INTO Location  VALUES('Phoenix','United States','Arizona','PARTIAL')
INSERT INTO Location  VALUES('Bethesda','United States','Maryland','YES')
INSERT INTO Location  VALUES('Paris','France','Île-de-France','YES')
INSERT INTO Location  VALUES('Newcastle','United Kingdom','High Heaton','NO')

-- CREATE TABLE Person(
--     p_ID decimal(8, 0) NOT NULL,
--     p_name char(32) NOT NULL, 
--     p_address char(32) NOT NULL, 
--     p_dob date NOT NULL, 
--     p_comment varchar(128)
-- );

INSERT INTO Person VALUES(1, 'John King', '893 Maria Avenue, San Diego, California', '1987-03-27', 'Started feeling sick yesterday')
INSERT INTO Person VALUES(2, 'Rachel Levine', '72 Adams Avenue, Phoenix, Arizona', '1999-06-13', 'Came in contact with someone that had Covid')
INSERT INTO Person VALUES(3, 'Caroline Nader', '1353 1st Street, Bethesda, Maryland', '1956-08-28', 'Worried about having Covid')
INSERT INTO Person VALUES(4, 'Micheal Walters', '17 Markel Street, Newcastle, UK', '1978-03-02', 'Feel Ok')
INSERT INTO Person VALUES(5, 'Chris Tate', '144 New Haven Court, Santa Ana, California', '1993-10-28', 'Someone coughed near me the other day')

-- CREATE TABLE Results(
--     r_caseID decimal(8, 0) NOT NULL,
--     r_personID decimal(8, 0) NOT NULL,
--     r_date date NOT NULL,
--     r_result char(16) NOT NULL
-- );

INSERT INTO Results VALUES(1, 1, '2020-06-23', 'POSITIVE')
INSERT INTO Results VALUES(2, 2, '2020-08-15', 'POSITIVE')
INSERT INTO Results VALUES(3, 3, '2020-03-29', 'POSITIVE')
INSERT INTO Results VALUES(4, 4, '2020-09-09', 'NEGATIVE')
INSERT INTO Results VALUES(5, 5, '2020-10-04', 'NEGATIVE')

-- CREATE TABLE Symptoms(
--     s_caseID decimal(8, 0) NOT NULL, 
--     s_fever char(8) NOT NULL, 
--     s_tiredness char(8) NOT NULL, 
--     s_dryCough char(8) NOT NULL, 
--     s_breathingDifficulty char(8) NOT NULL, 
--     s_soreThroat char(8) NOT NULL, 
--     s_severity ​decimal(1, 0) NOT NULL
-- );

INSERT INTO Symptoms VALUES(1, 'NO', 'NO', 'YES', 'YES', 'NO', 3)
INSERT INTO Symptoms VALUES(2, 'NO', 'YES', 'NO', 'YES', 'NO', 2)
INSERT INTO Symptoms VALUES(3, 'YES', 'NO', 'YES', 'YES', 'YES', 8)
INSERT INTO Symptoms VALUES(4, 'YES', 'NO', 'YES', 'NO', 'NO', 6)
INSERT INTO Symptoms VALUES(5, 'NO', 'YES', 'YES', 'NO', 'NO', 2)

-- CREATE TABLE Testing(  
--     t_type char(16) NOT NULL, 
--     t_units decimal(12, 0) NOT NULL, 
--     ​t_requests decimal(12, 0) NOT NULL
-- );

INSERT INTO Testing VALUES('RAPID', 8089, 15012)
INSERT INTO Testing VALUES('4 DAY', 15325, 45197)
INSERT INTO Testing VALUES('SAME DAY', 12400, 30092)
INSERT INTO Testing VALUES('1 WEEK', 52170, 153842)

-- CREATE TABLE NeedsHospital(
--     nh_address char(32) NOT NULL, 
--     nh_riskLevel decimal(1, 0) NOT NULL, 
--     nh_fever char(8) NOT NULL, 
--     nh_tiredness char(8) NOT NULL, 
--     nh_dryCough char(8) NOT NULL, 
--     nh_breathingDifficulty char(8) NOT NULL, 
--     nh_soreThroat char(8) NOT NULL, 
--     nh_severity decimal(1, 0) NOT NULL, 
--     nh_descision char(8) NOT NULL
-- );

INSERT INTO NeedsHospital VALUES('893 Maria Avenue, San Diego, California', 1, 'NO', 'NO', 'YES', 'YES', 'NO', 3, 'NO')
INSERT INTO NeedsHospital VALUES('72 Adams Avenue, Phoenix, Arizona', 2, 'NO', 'YES', 'NO', 'YES', 'NO', 2, 'NO')
INSERT INTO NeedsHospital VALUES('1353 1st Street, Bethesda, Maryland', 9,'YES', 'NO', 'YES', 'YES', 'YES', 8, 'YES')
INSERT INTO NeedsHospital VALUES('17 Markel Street, Newcastle, UK', 5, 'YES', 'NO', 'YES', 'NO', 'NO', 6, 'YES')
INSERT INTO NeedsHospital VALUES('144 New Haven Court, Santa Ana, California', 5, 'NO', 'YES', 'YES', 'NO', 'NO', 2, 'NO')

-- CREATE TABLE TestingAvailability(
--     ta_personID decimal(8, 0) NOT NULL,
--     ta_type char(16) NOT NULL,
--     ta_units decimal(12, 0) NOT NULL,
--     ta_givenTest char(8) NOT NULL,
--     ta_comment varchar(128) NOT NULL
-- );

INSERT INTO TestingAvailability VALUES(1, '1 WEEK', 52170, 'YES', 'Quick and Easy')
INSERT INTO TestingAvailability VALUES(2, '1 WEEK', 52170, 'NO', 'Unneeded')
INSERT INTO TestingAvailability VALUES(3, 'RAPID', 8089, 'YES', 'High Risk Patient')
INSERT INTO TestingAvailability VALUES(3, 'SAME DAY', 12400, 'YES', 'For Confirmation')
INSERT INTO TestingAvailability VALUES(4, '4 DAY', 15325, 'YES', 'Had difficulty getting sample')
INSERT INTO TestingAvailability VALUES(5, '4 DAY', 15325, 'NO', 'No signs or symptoms')

-- CREATE TABLE Hospitals(
--     h_name char(32) NOT NULL,
--     h_doctors decimal(8, 0) NOT NULL,
--     h_patients decimal(8, 0) NOT NULL,
--     h_riskLevel decimal(1, 0) NOT NULL,
--     h_address char(32) NOT NULL,
--     h_comments varchar(128) NOT NULL
-- );

-- CREATE TABLE Outcome(
--     o_caseID decimal(8, 0) NOT NULL, 
--     o_dayspositive decimal(4, 0) NOT NULL,
--     o_status char(16) NOT NULL, 
--     o_comments varchar(128) NOT NULL
-- );

INSERT INTO Hospitals VALUES('Walter Reed', 200, 450, 4, '4494 Palmer Rd N, Bethesda, MD 20814', 'Excellent Care')
INSERT INTO Hospitals VALUES('Sharp Healthcare', 40, 200, 6, '765 Medical Center Ct, Chula Vista, CA 91911', 'Ok Care')
INSERT INTO Hospitals VALUES('Ronald Reagan UCLA Medical Center', 150, 500, 7, '757 Westwood Plaza, Los Angeles, CA 90095', 'Covid-19 Testing Available')
INSERT INTO Hospitals VALUES('Mayo Clinic', 250, 600, 8, '5777 East Mayo Boulevard. Phoenix, AZ 85054', 'Best in the World')
INSERT INTO Hospitals VALUES('Freeman Hospital', 50, 150, 3, 'Freeman Rd, High Heaton, Newcastle upon Tyne NE7 7DN, United Kingdom', 'World Class Care')

INSERT INTO Outcome VALUES(1, 17, 'doing well', 'no issues')
INSERT INTO Outcome VALUES(2, 5, 'needs fluids', 'has aches and a sore throat')
INSERT INTO Outcome VALUES(3, 8, 'struggling', 'needed respirator and fluids on day 6')
INSERT INTO Outcome VALUES(4, 32, 'seems fully recovered', 'had difficulty breathing for 2 days, no need for ventilator and is doing well now')
INSERT INTO Outcome VALUES(5, 2, 'no symptoms as of yet', 'came into contact with 3 family members in the last 3 days')

