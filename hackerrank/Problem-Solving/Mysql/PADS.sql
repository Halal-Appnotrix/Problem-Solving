/* Preblem Link:-https://www.hackerrank.com/challenges/the-pads/problem */

select concat(Name, case when occupation = "Doctor" Then "(D)"
             when occupation = "Actor" Then "(A)"
             when occupation = "Singer" then "(S)"
             when occupation = "Professor" then "(P)"
             end
             )from Occupations order by Name, occupation;
select "There are a total of", count(occupation), concat(lower(occupation), "s.")
        from Occupations group by occupation order by count(occupation) asc, occupation asc;



/* Another way */
select concat(Name, '(', left(occupation, 1), ')') from Occupations order by name, occupation;

select concat("There are a total of ", count(occupation), ' ', lower(occupation), 's.')
        from Occupations group by occupation order by count(occupation), occupation;
