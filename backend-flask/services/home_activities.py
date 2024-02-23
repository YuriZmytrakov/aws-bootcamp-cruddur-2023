from datetime import datetime, timedelta, timezone
# import logging
from lib.db import pool, query_wrap_object, query_wrap_array

import psycopg2
from psycopg2.extras import RealDictCursor

class HomeActivities:
  def run(cognito_user_id=None):
    # logger.info("HomeActivities")
    # now = datetime.now(timezone.utc).astimezone()
    # results = [{
    #   'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
    #   'handle':  'Andrew Brown',
    #   'message': 'Cloud is fun!',
    #   'created_at': (now - timedelta(days=2)).isoformat(),
    #   'expires_at': (now + timedelta(days=5)).isoformat(),
    #   'likes_count': 5,query_wrap_object
    #   'replies_count': 1,
    #   'reposts_count': 0,
    #   'replies': [{
    #     'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
    #     'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
    #     'handle':  'Worf',
    #     'message': 'This post has no honor!',
    #     'likes_count': 0,
    #     'replies_count': 0,
    #     'reposts_count': 0,
    #     'created_at': (now - timedelta(days=2)).isoformat()
    #   }],
    # },
    # {
    #   'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
    #   'handle':  'Worf',
    #   'message': 'I am out of prune juice',
    #   'created_at': (now - timedelta(days=7)).isoformat(),
    #   'expires_at': (now + timedelta(days=9)).isoformat(),
    #   'likes': 0,
    #   'replies': []
    # },
    # {
    #   'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
    #   'handle':  'Garek',
    #   'message': 'My dear doctor, I am just simple tailor',
    #   'created_at': (now - timedelta(hours=1)).isoformat(),
    #   'expires_at': (now + timedelta(hours=12)).isoformat(),
    #   'likes': 0,
    #   'replies': []
    # }
    # ]
    # if cognito_user_id != None:
    #   extra_crud = {
    #     'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
    #     'handle':  'Garek',
    #     'message': 'My dear doctor, I am just simple tailor',
    #     'created_at': (now - timedelta(hours=1)).isoformat(),
    #     'expires_at': (now + timedelta(hours=12)).isoformat(),
    #     'likes': 0,
    #     'replies': []
    #   }
    #   results.insert(0, extra_crud)

    sql = query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)

    with pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
    return json[0]

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
