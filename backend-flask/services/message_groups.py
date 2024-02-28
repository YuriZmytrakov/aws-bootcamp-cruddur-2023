from datetime import datetime, timedelta, timezone

from lib.ddb import Ddb
from lib.db import db

import boto3


class MessageGroups:
  def run(cognito_user_id):
    model = {
      'errors': None,
      'data': None
    }

    sql = db.template('users', 'uuid_from_cognito_user_id')
    my_user_uuid = db.query_value(sql,{
      'cognito_user_id': cognito_user_id
    })
    # my_user_uuid = "5fb5055a-f0e5-409e-aede-89506af1f6a9"

    print(f"UUID: {my_user_uuid}")

    ddb = Ddb.client()
    data = Ddb.list_message_groups(ddb, my_user_uuid)
    print("list_message_groups:",data)

    model['data'] = data
    return model