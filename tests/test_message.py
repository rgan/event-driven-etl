import json

from message import Message


def test_creates_message():
    log_msg = json.dumps({"type":"batch_collected", "batch_id" : "20181201"})
    msg = json.dumps({ "Message" : log_msg })
    assert Message(msg).batch_id == "20181201"
    assert Message(msg).msg_type == "batch_collected"


def test_is_log_collected():
    log_msg = json.dumps({"type": "batch_collected", "batch_id": "20181201"})
    msg = json.dumps({"Message": log_msg})
    assert Message(msg).is_log_collected()


def test_is_log_processed():
    log_msg = json.dumps({"type": "batch_processed", "batch_id": "20181201"})
    msg = json.dumps({"Message": log_msg})
    assert Message(msg).is_log_processed()