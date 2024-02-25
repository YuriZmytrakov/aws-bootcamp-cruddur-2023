from datetime import datetime, timedelta, timezone
# import logging
from lib.db import db

import psycopg2
from psycopg2.extras import RealDictCursor

class HomeActivities:
  def run(cognito_user_id=None):
    sql = db.template('activities', 'home')
    results = db.query_array_json(sql)
    return results
