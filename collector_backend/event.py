from datetime import datetime
from tzlocal import get_localzone
import json
from json import JSONDecodeError
import logging

from flask import request
from flask_restx import Namespace, Resource, fields

from collector_backend import event_log_helper

ns = Namespace("event", "Event Collection API")


MODEL_ACTION = ns.model('ACTION', {
    'time': fields.String(description='Event time', example='2018-10-18T21:37:28-06:00'),
    'type': fields.String(description='Event type', example='CLICK'),
    'properties': fields.String(description='Additional fields for each event type', example={
        "locationX": 52,
        "locationY": 11
    }),
})
FIELD_WILD_ACTIONS = fields.Wildcard(fields.Nested(MODEL_ACTION), required=True, example=[
    {
      "time": "2018-10-18T21:37:28-06:00",
      "type": "CLICK",
      "properties": {
        "locationX": 52,
        "locationY": 11
      }
    },
    {
      "time": "2018-10-18T21:37:30-06:00",
      "type": "VIEW",
      "properties": {
        "viewedId": "FDJKLHSLD"
      }
    },
    {
      "time": "2018-10-18T21:37:30-06:00",
      "type": "NAVIGATE",
      "properties": {
        "pageFrom": "communities",
        "pageTo": "inventory"
      }
    }
  ])
MODEL_EVENTS_REPORT = ns.model('ModelEventsReport', {
    'userId': fields.String(description='User ID', required=True, example='ABC123XYZ'),
    'sessionId': fields.String(description='Session ID', required=True, example='XYZ456ABC'),
    'actions': FIELD_WILD_ACTIONS,
})


@ns.route("/report")
class Report(Resource):
    @ns.expect(MODEL_EVENTS_REPORT)
    @ns.doc(responses={
                200: 'Success',
                400: 'Detect the broken format',
                422: 'Insufficient data'})
    def post(self):
        try:
            json_data = json.loads(request.data)
        except JSONDecodeError as e:
            ns.abort(400)

        user_id = json_data.get("userId", None)
        session_id = json_data.get("sessionId", None)
        actions = json_data.get("actions", None)

        if not user_id or not session_id or not actions:
            ns.abort(422)

        event_logger = logging.getLogger("event_logger")
        now = datetime.now(get_localzone())
        timestamp = now.strftime("%Y-%m-%dT%H:%M:%S%z")
        for a in actions:
            event_logger.info(event_log_helper.format_event_log(timestamp, user_id, session_id, a))

        return {'result_msg': 'Success'}, 200
