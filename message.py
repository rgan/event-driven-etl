import json


class Message:

    def __init__(self, msg):
        self.msg_json = json.loads(json.loads(msg)["Message"])
        self.batch_id = self.msg_json["batch_id"]
        self.msg_type = self.msg_json["type"]

    def is_log_collected(self):
        return self.msg_type == "batch_collected"

    def is_log_processed(self):
        return self.msg_type == "batch_processed"

    def batch_id(self):
        return self.batch_id