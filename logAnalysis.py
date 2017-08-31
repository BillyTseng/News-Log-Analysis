#! /usr/bin/env python3
import psycopg2


def PopularThreeArticles():
    """Input SQL query to print the top three articles."""
    query = '''select title, num from articles, poparticle
                 where '/article/' || articles.slug = poparticle.path
                 order by num desc limit 3;'''
    results = execute_query(query)
    print("\n1. What are the most popular three articles of all time?")
    for title, views in results:
        print('    \"{}\" - {} views'.format(title, views))


def AuthorsRank():
    """Input SQL query to print the rank of all authors."""
    query = '''select name, counting from authors,
                (select author, sum(poparticle.num) as counting
                from articles, poparticle
                where '/article/' || articles.slug = poparticle.path
                group by author
                order by counting desc limit 4) as newladder
                where authors.id = newladder.author;'''
    results = execute_query(query)
    print("\n2. Who are the most popular article authors of all time?")
    for name, cnt in results:
        print('    \"{}\" - {} views'.format(name, cnt))


def ErrorRate():
    """Input SQL query to print the days which error rate was more than 1%."""
    query = '''select *
                from (select totalconn.day,
                    round(100.0*(fail_conn::numeric / total_conn::numeric), 2)
                    as "err_rate"
                    from totalconn, failconn
                    where totalconn.day = failconn.day) as results
                where err_rate > 1;'''
    results = execute_query(query)
    print("\n3. On which days did more than 1% of requests lead to errors?")
    for day, rate in results:
        print('    {:%B %d, %Y} - {}% errors\n'.format(day, rate))


def execute_query(query):
    """execute_query takes an SQL query as a parameter.
        Executes the query and returns the results as a list of tuples.
        args:
            query - an SQL query statement to be executed.
        returns:
            A list of tuples containing the results of the query.
    """
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    PopularThreeArticles()
    AuthorsRank()
    ErrorRate()
