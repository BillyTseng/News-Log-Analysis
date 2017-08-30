#!python3.5.2
import psycopg2


def PopularThreeArticles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''select title, num from articles, poparticle
                 where articles.slug = poparticle.slug
                 order by num desc limit 3;''')
    articles = c.fetchall()
    print("\n1. What are the most popular three articles of all time?")
    for text, views in articles:
        print("    \"" + text + "\" - " + str(views) + " views")
    db.close()


def AuthorsRank():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''select name, counting from authors,
                (select author, sum(poparticle.num) as counting
                from articles, poparticle
                where articles.slug = poparticle.slug
                group by author
                order by counting desc limit 4) as newladder
                where authors.id = newladder.author;''')
    articles = c.fetchall()
    print("\n2. Who are the most popular article authors of all time?")
    for name, cnt in articles:
        print("    \"" + name + "\" - " + str(cnt) + " views")
    db.close()


def ErrorRate():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''select *
                from (select totalconn.day,
                    round(100.0*(fail_conn::numeric / total_conn::numeric), 2)
                    as "err_rate"
                    from totalconn, failconn
                    where totalconn.day = failconn.day) as results
                where err_rate > 1;''')
    articles = c.fetchall()
    print("\n3. On which days did more than 1% of requests lead to errors?")
    for day, rate in articles:
        print("    \"" + str(day) + "\" - " + str(rate) + "% errors\n")
    db.close()


if __name__ == '__main__':
    PopularThreeArticles()
    AuthorsRank()
    ErrorRate()
