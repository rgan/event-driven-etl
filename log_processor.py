import argparse
import logging
from time import sleep

from base_processor import BaseProcessor, get_args


class LogProcessor(BaseProcessor):

    def run(self, msg):
        # will need to handle failures and retry
        logging.info("process_logs Batch id: {0}".format(msg.batch_id))
        sleep(10)
        self.done(msg.batch_id)

    def process_message(self, msg):
        if msg.is_log_collected():
            self.run(msg)
            return True
        return False

    def done(self, batch_id):
        self.publish({"type":"batch_processed", "batch_id" : batch_id})


def main():
    args = get_args()
    LogProcessor(args.topicArn, args.queueUrl).process()


if __name__ == "__main__":
    main()