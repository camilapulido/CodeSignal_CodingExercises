
CREATE PROCEDURE projectList()
BEGIN
	SElECT project_name, team_lead, income
	FROM Projects;
END

##

CREATE PROCEDURE solution()
BEGIN
	SELECT name, continent, population
	FROM countries
	WHERE continent = 'Africa'
	ORDER BY name;
END