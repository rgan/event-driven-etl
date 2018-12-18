Event driven ETL processing framework

Requirements: Python 3

Create a virtual env and pip install dev-requirements.txt

Use event_driven_infrastructure.json file to create an AWS cloud formation stack.
It provisions an ETLTopic, ETLQueue, ETLUser with the appropriate permissions.

Start the ETL processes using the virtual env:

python log_processor.py &
python loader.py &

Publish a message to the SNS topic: ETLTopic 
{"type": "batch_collected", "batch_id": "20181201"}
It should trigger the log processsor and in-turn the loader.


