import logging
from time import sleep

from base_processor import BaseProcessor, get_args


class Loader(BaseProcessor):

    def run(self, msg):
        # will need to handle failures and retry
        logging.info("load Batch id: {0}".format(msg.batch_id))
        sleep(10)
        self.done(msg.batch_id)

    def process_message(self, msg):
        if msg.is_log_processed():
            self.run(msg)
            return True
        return False

    def done(self, batch_id):
        self.publish({"type":"batch_loaded", "batch_id" : batch_id})

def main():
    args = get_args()
    Loader(args.topicArn, args.queueUrl).process()

if __name__ == "__main__":
    main()