from google.cloud import pubsub_v1
import random
import string
import uuid
import json
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

class DataMocker:
    def __init__(self, project_id, topic_id):
        self.project_id = project_id
        self.topic_id = topic_id

    def initialize_pubsub(self):
        try:
            publisher = pubsub_v1.PublisherClient()
            topic_path = publisher.topic_path(self.project_id, self.topic_id)
            return publisher, topic_path
        except Exception as e:
            print(f"Failed to initialize Pub/Sub client: {e}")
            raise

    def generate_mock_date(self, nrows):
        try:
            data = []
            for _ in range(nrows):
                row_key = str(uuid.uuid4())
                row_data = {
                    "row_key": row_key,
                    "name": ''.join(random.choices(string.ascii_letters, k=10)),
                    "age": random.randint(18, 80),
                    "email": ''.join(random.choices(string.ascii_lowercase, k=7)) + ''.join(random.choices(string.digits, k=2)) + '@esample.com',
                    "join_date": (datetime.now() - timedelta(days=random.randint(0, 3650))).strftime("%Y-%m-%d"),
                    "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "loyalty_points": random.randint(0, 1000),
                    "account_balance": round(random.uniform(100, 10000), 2),
                    "is_active": random.choice([True, False]),
                    "inserted_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": None
                }

                data.append(row_data)

            return data
        except Exception as e:
            print(f"Failed to generate mock data: {e}")
            raise

    def publish_to_pubsub(self, publisher, topic_path, data):
        try:
            for record in data:
                message_json = json.dumps(record)
                message_bytes = message_json.encode('utf-8')
                future = publisher.publish(topic_path, data=message_bytes)

                print("Data :- ", message_json)
                print(f"Published message ID: {future.result()}")

            print(f"Published {len(data)} messages successfully.")
        except Exception as e:
            print(f"Failed to publish data: {e}")
            raise
    

if __name__ == '__main__':
    load_dotenv()

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/ritayanpatra/Projects/GCP/computer-systems-ritayan-patra-afa8542cacc2.json"

    project_id = os.getenv("PROJECT_ID")
    topic_id = os.getenv("TOPIC_ID")

    if not project_id or not topic_id:
        print("Please set PROJECT_ID and TOPIC_ID in the .env file.")
        exit(1)

    data_mocker = DataMocker(project_id, topic_id)

    try:
        publisher, topic_path = data_mocker.initialize_pubsub()

        # Generate and publish mock data
        mock_data = data_mocker.generate_mock_date(20)
        data_mocker.publish_to_pubsub(publisher, topic_path, mock_data)

    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

        

            