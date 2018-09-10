-- ProblemSet<03>, August <16> <2018> -- Submission by srikantan.prakash@accenture.com

1. Find the titles of all movies directed by Steven Spielberg.

select title from Movie where director='Steven Spielberg';

E.T.
Raiders of the Lost Ark

2. Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order.

select m.year from movie m inner join Rating r on m.mID=r.mID where stars=4 or stars=5 order by year;

1937
1937
1939
1981
1981
2009

3. Find the titles of all movies that have no ratings.

select title from movie where mID not in (select mID from Rating);

Star Wars
Titanic

4. Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date.

select r.name from Reviewer r inner join Rating r1 on r.rID=r1.rID where r1.ratingDate is null;

Daniel Lewis
Chris Jackson

5. Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars.

select r.name,m.title,r1.stars,r1.ratingDate from Rating r1 inner join Movie m on r1.mID=m.mID inner join Reviewer r on r1.rID=r.rID order by r.name,m.title,r1.stars;

Ashley White|E.T.|3|2011-01-02
Brittany Harris|Raiders of the Lost Ark|2|2011-01-30
Brittany Harris|Raiders of the Lost Ark|4|2011-01-12
Brittany Harris|The Sound of Music|2|2011-01-20
Chris Jackson|E.T.|2|2011-01-22
Chris Jackson|Raiders of the Lost Ark|4|
Chris Jackson|The Sound of Music|3|2011-01-27
Daniel Lewis|Snow White|4|
Elizabeth Thomas|Avatar|3|2011-01-15
Elizabeth Thomas|Snow White|5|2011-01-19
James Cameron|Avatar|5|2011-01-20
Mike Anderson|Gone with the Wind|3|2011-01-09
Sarah Martinez|Gone with the Wind|2|2011-01-22
Sarah Martinez|Gone with the Wind|4|2011-01-27

6. For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name and the title of the movie.



7. For each movie that has at least one rating, find the highest number of stars that movie received. Return the movie title and number of stars. Sort by movie title.

select m.title,r1.stars from Rating r1 inner join Movie m on r1.mID=m.mID group by m.title having max(r1.stars) order by m.title;

Avatar|5
E.T.|3
Gone with the Wind|4
Raiders of the Lost Ark|4
Snow White|5
The Sound of Music|3

8. For each movie, return the title and the 'rating spread', that is, the difference between highest and lowest ratings given to that movie. Sort by rating spread from highest to lowest, then by movie title.

select m.title,max(r1.stars)-min(r1.stars) as rating_spread from Movie m inner join Rating r1 on m.mID=r1.mID group by m.title order by rating_spread desc,m.title;

Avatar|2
Gone with the Wind|2
Raiders of the Lost Ark|2
E.T.|1
Snow White|1
The Sound of Music|1

9. Find the difference between the average rating of movies released before 1980 and the average rating of movies released after 1980. (Make sure to calculate the average rating for each movie, then the average of those averages for movies before 1980 and movies after. Don't just calculate the overall average rating before and after 1980.)




10. Find the names of all reviewers who rated Gone with the Wind.

select distinct(r.name) from Rating r1 inner join Reviewer r on r1.rID=r.rID inner join Movie m on r1.mID=m.mID where m.title='Gone with the Wind';

Sarah Martinez
Mike Anderson

11. For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars.

select m.title,r.name,r1.stars from Rating r1 inner join Reviewer r on r1.rID=r.rID inner join Movie m on r1.mID=m.mID where m.director=r.name;

Avatar|James Cameron|5

12. Return all reviewer names and movie names together in a single list, alphabetized. (Sorting by the first name of the reviewer and first word in the title is fine; no need for special processing on last names or removing "The".)
select r.name,m.title from Rating r1 inner join Movie m on r1.mID=m.mID inner join Reviewer r on r1.rID=r.rID where r.rID=r1.rID order by r.name,m.title;

Ashley White|E.T.
Brittany Harris|Raiders of the Lost Ark
Brittany Harris|Raiders of the Lost Ark
Brittany Harris|The Sound of Music
Chris Jackson|E.T.
Chris Jackson|Raiders of the Lost Ark
Chris Jackson|The Sound of Music
Daniel Lewis|Snow White
Elizabeth Thomas|Avatar
Elizabeth Thomas|Snow White
James Cameron|Avatar
Mike Anderson|Gone with the Wind
Sarah Martinez|Gone with the Wind
Sarah Martinez|Gone with the Wind

13. Find the titles of all movies not reviewed by Chris Jackson.

select distinct m.title from Movie m left outer join Rating r1 on r1.mID=m.mID where m.mID not in (select r3.mID from Rating r3 inner join Reviewer r4 on r3.rID=r4.rId where r4.name='Chris Jackson');

Gone with the Wind
Star Wars
Titanic
Snow White
Avatar

14. For all pairs of reviewers such that both reviewers gave a rating to the same movie, return the names of both reviewers. Eliminate duplicates, don't pair reviewers with themselves, and include each pair only once. For each pair, return the names in the pair in alphabetical order.







15. For each rating that is the lowest (fewest stars) currently in the database, return the reviewer name, movie title, and number of stars.

select r.name,m.title,r1.stars from Rating r1 inner join Movie m on r1.mID=m.mID inner join Reviewer r on r1.rID=r.rID group by m.title,r.name having min(r1.stars);

Elizabeth Thomas|Avatar|3
James Cameron|Avatar|5
Ashley White|E.T.|3
Chris Jackson|E.T.|2
Mike Anderson|Gone with the Wind|3
Sarah Martinez|Gone with the Wind|2
Brittany Harris|Raiders of the Lost Ark|2
Chris Jackson|Raiders of the Lost Ark|4
Daniel Lewis|Snow White|4
Elizabeth Thomas|Snow White|5
Brittany Harris|The Sound of Music|2
Chris Jackson|The Sound of Music|3

16. List movie titles and average ratings, from highest-rated to lowest-rated. If two or more movies have the same average rating, list them in alphabetical order.

select m.title,AVG(r1.stars) as average from Rating r1 inner join Movie m on r1.mID=m.mID group by m.title order by average,m.title;

E.T.|2.5
The Sound of Music|2.5
Gone with the Wind|3.0
Raiders of the Lost Ark|3.33333333333333
Avatar|4.0
Snow White|4.5

17)Find the names of all reviewers who have contributed three or more ratings. (As an extra challenge, try writing the query without HAVING or without COUNT.) (1 point possible)

select name from Reviewer r where (select count(*) from Rating r where r.rId = r.rId) >= 3;
Brittany Harris
Chris Jackson

18)Some directors directed more than one movie. For all such directors, return the titles of all movies directed by them, along with the director name. Sort by director name, then movie title. (As an extra challenge, try writing the query both with and without COUNT.) (1 point possible)

select director,title from movie where director in(select director from movie group by director having count(director)>1) order by director,title;
James Cameron|Avatar
James Cameron|Titanic
Steven Spielberg|E.T.
Steven Spielberg|Raiders of the Lost Ark

19)Find the movie(s) with the highest average rating. Return the movie title(s) and average rating. (Hint: This query is more difficult to write in SQLite than other systems; you might think of it as finding the highest average rating and then choosing the movie(s) with that average rating.) (1 point possible)

select m.title,avg(r.stars) as average from movie m inner join rating r on m.mID=r.rID group by m.title having average>( select avg(stars) from rating);
Avatar|4.0
Raiders of the Lost Ark|3.33333333333333
Snow White|4.5

20)Find the movie(s) with the lowest average rating. Return the movie title(s) and average rating. (Hint: This query may be more difficult to write in SQLite than other systems; you might think of it as finding the lowest average rating and then choosing the movie(s) with that average rating.) (1 point possible)

select m.title,avg(r.stars) as average from movie m inner join rating r on m.mID=r.mID group by m.title having average<( select avg(stars) from rating);
E.T.|2.5
Gone with the Wind|3.0
The Sound of Music|2.5

21)For each director, return the director's name together with the title(s) of the movie(s) they directed that received the highest rating among all of their movies, and the value of that rating. Ignore movies whose director is NULL. (1 point possible)

select m.director,m.title,max(r.stars) from movie m inner join rating r on m.mID=r.mID where m.director is not null group by m.director;
James Cameron|Avatar|5
Robert Wise|The Sound of Music|3
Steven Spielberg|Raiders of the Lost Ark|4
Victor Fleming|Gone with the Wind|4
