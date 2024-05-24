############ 
### app.codesignal.com -- Exercises -- Databases ---
## Author:  Camila Pulido

CREATE PROCEDURE projectList()
BEGIN
	SElECT project_name, team_lead, income
	FROM Projects;
END$$

############

CREATE PROCEDURE countriesSelection()
BEGIN
	SELECT name, continent, population
	FROM countries
	WHERE continent = 'Africa'
	ORDER BY name;
END$$

############
CREATE PROCEDURE monthlyScholarships()
BEGIN
	SELECT id, scholarship/12
	FROM scholarships;
END$$

##########
CREATE PROCEDURE ProjectTeam()
BEGIN
	SElECT DISTINCT name
	FROM projectLog
	ORDER BY name ASC;
END&&

##########
CREATE PROCEDURE automaticNotifications()
BEGIN
    SELECT email
    FROM users
    WHERE role NOT IN ("admin", "premium")
    ORDER BY email;
END$$

##########
CREATE PROCEDURE volleyballResults()
BEGIN
	SELECT *
	FROM results
	ORDER BY wins ASC;
END$$


##########
CREATE PROCEDURE mostExpensive()
BEGIN
	SElECT name
	From Products
	Order By (price*quantity) DESC, name ASC
	LIMIT 1;
END$$

##########
CREATE PROCEDURE contestLeaderboard()
BEGIN
	SELECT name
	FROM leaderboard 
	ORDER BY score DESC
	LIMIT 5 OFFSET 3;
END$$

##########
CREATE PROCEDURE gradeDistribution()
BEGIN
	SELECT Name, ID
	FROM Grades
	WHERE Final > 0.25 * Midterm1 + 0.25 * Midterm2 + 0.5 * Final
	OR Final > 0.5 * Midterm1 + 0.5 * Midterm2
	ORDER BY substring(name,1,3), ID;	  
END$$

########
CREATE PROCEDURE mischievousNephews()
BEGIN
	SELECT weekday(mischief_date) AS weekday, mischief_date, author,title
	from mischief
	ORDER BY weekday, FIELD(author,'Huey','Dewey','Louie'),mischief_date,title; 
END$$

##########
CREATE PROCEDURE suspectInvestigation()
BEGIN
	select id,name,surname
	from Suspect
	where height <= 170 AND name LIKE 'B%' AND surname LIKE 'GRE_n'
	ORDER by id ASC;
END$$

###########
CREATE PROCEDURE suspectInvestigation2()
BEGIN
	select id, name, surname
	from Suspect
	where height <= 170 or name not like 'B%' or surname not like 'Gre_n'
	Order by id asc;
END$$

##########
CREATE PROCEDURE securityBreach()
BEGIN
	SELECT * From users
	WHERE attribute 
	LIKE BINARY concat('_%\%',first_name,'\_',second_name,'\%%');
END$$

#############
CREATE PROCEDURE testCheck()
    SELECT id, 
    IF (correct_answer = given_answer, 'correct',if(given_answer is NULL, "no answer",'incorrect')) 
    AS checks
    FROM answers
    ORDER BY id;

########
CREATE PROCEDURE expressionsVerification()
BEGIN
	SELECT * FROM expressions
	where CASE Operation
		When '+' then a+b
		when '-' then a-b
		when '*' then a*b
		when '/' then a/b
	end = c
	c = (IF(Operation='+',a+b,(IF(Operation='-',a-b,
	IF(Operation='*',a*b,a/b)))))
	Order by id;
END$$

#######
CREATE PROCEDURE newsSubscriber()
BEGIN
	SELECT subscriber FROM full_year where newspaper like '%Daily%'
	UNION
	SELECT subscriber FROM half_year where newspaper like '%Daily%'
	order by subscriber;
END$$

########
CREATE PROCEDURE countriesInfo()
BEGIN
	Select count(name) as number,AVG(population),sum(population)
	From countries;
END$$

########
CREATE PROCEDURE itemCounts()
BEGIN
	select item_name, item_type, count(*) as item_count
	from availableItems
	Group by item_type, item_name
	order by item_type asc, item_name ASC;
END$$

###########
CREATE PROCEDURE usersByContinent()
BEGIN
	select continent, sum(users) as users
	from countries
	group by continent
	order by users DESC;
END$$

############
CREATE PROCEDURE movieDirectors()
BEGIN
	select director from moviesInfo
	where year >2000
	group by director having sum(oscars) > 2
	order by director ASC;
END$$

##################
CREATE PROCEDURE travelDiary()
BEGIN
	select GROUP_CONCAT(DISTINCT country order by country SEPARATOR ';') as countries 
	from diary;
END&&

#################
CREATE PROCEDURE SoccerPlayers()
BEGIN
	select Group_concat(concat(first_name," ",surname," #",player_number) 
	order by  player_number separator "; ") 
	as players
	from soccer_team;
END$$

##############
CREATE PROCEDURE marketReport()
BEGIN
	SELECT country, count(distinct competitor) as competitors 
	from foreignCompetitors
	group by country
	union
	SELECT "Total:", count(competitor) from foreignCompetitors;
END$$$

#######################
