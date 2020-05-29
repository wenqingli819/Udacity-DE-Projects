# DROP TABLES

songplay_table_drop = "DROP table songplays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table time"

# CREATE TABLES
# ref: https://w3resource.com/PostgreSQL/data-types.php

time_table_create = """CREATE TABLE IF NOT EXISTS time
                        (start_time timestamp NOT NULL PRIMARY KEY,
                        hour int,
                        day int,
                        week int,
                        month int,
                        year int,
                        weekday varchar)
                        """

user_table_create = """CREATE TABLE IF NOT EXISTS users
                        (user_id int NOT NULL PRIMARY KEY,
                        first_name varchar NOT NULL,
                        last_name varchar NOT NULL,
                        gender varchar,
                        level varchar)
                        """


artist_table_create = """CREATE TABLE IF NOT EXISTS artists
                        (artist_id text NOT NULL PRIMARY KEY,
                        name varchar NOT NULL,
                        location text,
                        latitude float,
                        longitude float)
                        """

song_table_create = """CREATE TABLE IF NOT EXISTS songs
                        (song_id text NOT NULL PRIMARY KEY,
                        title varchar  NOT NULL,
                        artist_id text  NOT NULL REFERENCES artists(artist_id),
                        year int,
                        duration float)
                        """


songplay_table_create = """CREATE TABLE IF NOT EXISTS songplays
                        (songplay_id int NOT NULL PRIMARY KEY,
                        start_time timestamp REFERENCES time(start_time),
                        user_id int NOT NULL REFERENCES users(user_id),
                        level varchar,
                        artist_id text,
                        song_id text ,
                        session_id int,
                        location text,
                        user_agent varchar)
                        """


# INSERT RECORDS

songplay_table_insert = """
        INSERT INTO songplays
        (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (songplay_id) DO NOTHING;
"""

user_table_insert = """
        INSERT INTO users
        (user_id, first_name, last_name, gender, level)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (user_id) DO NOTHING;
"""

song_table_insert = """
        INSERT INTO songs
        (song_id, title, artist_id, year, duration)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (song_id) DO NOTHING;
"""

artist_table_insert = """
        INSERT INTO artists
        (artist_id, name, location, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (artist_id) DO NOTHING;
"""


time_table_insert = """
        INSERT INTO time
        (start_time, hour, day, week, month, year, weekday)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (start_time) DO NOTHING;
"""

# FIND SONGS

song_select = """
        SELECT song_id, artists.artist_id
        FROM songs JOIN artists ON songs.artist_id = artists.artist_id
        WHERE songs.title = %s
        AND artists.name = %s
        AND songs.duration = %s ;
"""

# QUERY LISTS

create_table_queries = [
    time_table_create,
    user_table_create,
    artist_table_create,
    song_table_create,
    songplay_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
