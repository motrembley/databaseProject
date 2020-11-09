DROP TABLE hospital;
DROP TABLE Location;
DROP TABLE NeedsHospal;
DROP TABLE Outcome;
DROP TABLE Person; 
DROP TABLE Results;
DROP TABLE Symptoms;
DROP TABLE Testing;
DROP TABLE TestingAvlability;


CREATE TABLE hospital (
                h_name char(32) NOT NULL,
                h_doctors decimal (8,0) NOT NULL,
                h_patients decimal (8,0) NOT NULL,
                h_riskLevel decimal (1,0) NOT NULL,
                h_address char (32) NOT NULL,
                h_comments varchar (128) NOT NULL
            );

CREATE TABLE NeedsHospital (
                nh_address char(32) NOT NULL,
                nh_riskLevel decimal(1,0) NOT NULL,
                nh_fever char(8) NOT NULL,
                nh_tiredness char(8) NOT NULL,
                nh_dryCough char(8) NOT NULL,
                nh_breathingDifficulty char(8) NOT NULL,
                nh_soreThroat char(8) NOT NULL,
                nh_severity decimal(1, 0) NOT NULL,
                nh_decision char(8) NOT NULL
            );

CREATE TABLE Symptoms (
                s_caseID decimal(8,0) NOT NULL,
                s_fever char(8) NOT NULL,
                s_tiredness char(8) NOT NULL,
                s_dryCough char(8) NOT NULL,
                s_breathingDifficulty char(8) NOT NULL,
                s_soreThroat char(8) NOT NULL,
                s_severity decimal(1,0) NOT NULL
            );

CREATE TABLE Outcome (
                o_caseID decimal(8,0) NOT NULL,
                o_dayspositive decimal(4,0) NOT NULL,
                o_status char(16) NOT NULL,
                o_comments varchar(128) NOT NULL
            );

CREATE TABLE TestingAvailability (
                ta_personID decimal(8,0) NOT NULL,
                ta_type char(16) NOT NULL,
                ta_units decimal(12,0) NOT NULL,
                ta_givenTest char(8) NOT NULL,
                ta_comment varchar(128) NOT NULL
            );

CREATE TABLE Testing (
                t_type char(16) NOT NULL,
                t_units decimal(12,0) NOT NULL,
                t_requests decimal(12,0) NOT NULL
            );

CREATE TABLE Results (
                r_caseID decimal(8,0) NOT NULL,
                r_personID decimal(8,0) NOT NULL,
                r_date date NOT NULL,
                r_result char(16) NOT NULL
            );

CREATE TABLE Person (
                p_ID decimal(8,0) NOT NULL,
                p_name char(32) NOT NULL,
                p_address char(32) NOT NULL,
                p_dob date NOT NULL,
                p_comment varchar(128)
            );

CREATE TABLE Location (
                l_city char(32) NOT NULL,
                l_country char(32) NOT NULL,
                l_state char(32) NOT NULL,
                l_lockdown char(8)
            );