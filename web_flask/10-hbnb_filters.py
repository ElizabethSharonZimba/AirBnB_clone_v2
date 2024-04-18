
10. States and State
mandatory

Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
    To load all cities of a State:
        If your storage engine is DBStorage, you must use cities relationship
        Otherwise, use the public getter method cities
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
    Routes:
        /states: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
                LI tag: description of one State: <state.id>: <B><state.name></B>
        /states/<id>: display a HTML page: (inside the tag BODY)
            If a State object is found with this id:
                H1 tag: “State: ”
                H3 tag: “Cities:”
                UL tag: with the list of City objects linked to the State sorted by name (A->Z)
                    LI tag: description of one City: <city.id>: <B><city.name></B>
            Otherwise:
                H1 tag: “Not found!”
    You must use the option strict_slashes=False in your route definition
    Import this 7-dump to have some data

IMPORTANT

    Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository (Task)
    Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py

guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>State: Illinois</H1>
        <H3>Cities:</H3>
        <UL>
                <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>
        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>
guillaume@ubuntu:~$ 

Repo:

    GitHub repository: AirBnB_clone_v2
    File: web_flask/9-states.py, web_flask/templates/9-states.html


