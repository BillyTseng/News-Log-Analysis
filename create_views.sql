
/* For question 1 and 2*/
create view poparticle as
select path ,count(*) as num
from log where char_length(path) > 1
group by path
order by num desc;

/* For question 3*/
create view totalconn as
select time::date as day, count(*) as total_conn
from log
group by time::date;

create view failconn as
select time::date as day, count(*) as fail_conn
from log
where status = '404 NOT FOUND'
group by time::date
order by time::date;