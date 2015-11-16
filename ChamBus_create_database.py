# coding: utf-8

# https://github.com/ChamGeeks/GetAroundChamonix/blob/master/www/js/services/TripPlanner.js

import datetime, os, requests, sqlite3

db_filename = 'ChamBus.db'
db_url = 'https://chx-transit-db.herokuapp.com/api/export/sql'
    
if os.path.exists(db_filename):
    exit(db_filename + ' already exists.  Rename or delete it and rerun this script.')

print('Initializing {}...'.format(db_filename))
start = datetime.datetime.now()
with sqlite3.connect(db_filename) as conn:
    print('Reading sql commands from: {} ...'.format(db_url))
    cursor = conn.executescript(requests.get(db_url).text)
    print('Database tables are:')
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print('\n'.join(sorted(x[0] for x in cursor.fetchall())))
    conn.commit()
print('Elapsed time: {}'.format(datetime.datetime.now() - start)) 
print('=====\nDone.')
