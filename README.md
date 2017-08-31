# News Log Analysis
This project provided a Python script uses the psycopg2 library to query a PostgreSQL database of a mock news website. The Python script produces a report that answers the following three questions:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

It will show the answers in the terminal, and `exampleOutput.txt` is a plain text file that is a copy of what my program printed out.

## Install Virtual Machine
  1. Download and install VirtualBox [here](https://www.virtualbox.org/wiki/Downloads)
  2. Download and install Vagrant [here](https://www.vagrantup.com/downloads.html)

## Configure Virtual Machine
  0. Download and unzip this project into the working directory.
  1. Use a terminal to type command `vagrant init` in the working directory.
  2. Go to [here](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile) to copy and save the text as `Vagrantfile`.
  3. Replace the old `Vagrantfile` with the new `Vagrantfile` in your working directory.
  4. Type command `vagrant up` on the terminal to turn on the virtual machine. It will take a while when the first booting.
  5. Once the virtual machine is done booting, type command `vagrant ssh` on the terminal to log in the virtual machine.

## Setup Database
  1. Download and unzip [`newsdata.sql`](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) into your working directory.
  2. Type `cd /vagrant` to navigate to the vagrant share directory.
  3. To load the database, use the command `psql -d news -f newsdata.sql`.

## Create Views
To achieve the purpose of reducing the complexity of the SQL query, I made a script `create_views.sql` to create three views (the view in SQL just like the variable in Python). Type the command `psql -d news -f create_views.sql` on the terminal.

## Execute
The script `logAnalysis.py` can be executed in both Python 2 and Python 3.
You can input `python logAnalysis.py` or `python3 logAnalysis.py` to generate the report.
