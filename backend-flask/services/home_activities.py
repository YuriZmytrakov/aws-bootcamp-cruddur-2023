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
    
    # conn_string = "postgresql://postgres:password@db:5432/cruddur"
    # conn = psycopg2.connect(conn_string)
    # cur = conn.cursor(cursor_factory=RealDictCursor)
    # cur.execute("SELECT * FROM activities")
    
    # # Fetch all rows
    # rows = cur.fetchall()

    # # Serialize rows to dictionaries
    # serialized_rows = []
    # for row in rows:
    #     serialized_row = {
    #         "uuid": row["uuid"],
    #         "user_uuid": row["user_uuid"],
    #         "message": row["message"],
    #         "replies_count": row["replies_count"],
    #         "reposts_count": row["reposts_count"],
    #         "likes_count": row["likes_count"],
    #         "reply_to_activity_uuid": row["reply_to_activity_uuid"],
    #         "expires_at": str(row["expires_at"]),
    #         "created_at": str(row["created_at"])
    #     }
    #     serialized_rows.append(serialized_row)

    # cur.close()
    # conn.close()

    # return serialized_rows
