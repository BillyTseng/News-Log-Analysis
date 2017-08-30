# News Log Analysis
This project answers three questions by querying the given database `newsdata.sql`.
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

It will show the answers in the terminal, and `exampleOutput.txt` is a plain text file that is a copy of what my program printed out.

## Environment

  - VirtualBox [here](https://www.virtualbox.org/wiki/Downloads)
  - Vagrant [here](https://www.vagrantup.com/downloads.html)
  - Python 3 [here](https://www.python.org/downloads/)
  - The VM configuration [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
  - `newsdata.sql` [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Create Views
```sql
    create view poparticle as
    select substring(path from 10) as slug ,count(*) as num
    from log where char_length(path) > 1
    group by slug
    order by num desc;
```
```sql
    create view totalconn as
    select time::date as day, count(*) as total_conn
    from log
    group by time::date;
```
```sql
    create view failconn as
    select time::date as day, count(*) as fail_conn
    from log
    where status = '404 NOT FOUND'
    group by time::date
    order by time::date;
```

## Execute

```
    python logAnalysis.py
```
