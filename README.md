# IRCTC Realtime ticket booking data sync to Google BigQuery

## Ovierview
This project provides a solution for syncing ticket booking data in real-time to Google BigQuery. It utilizes a combination of Python, Google Cloud Pub/Sub, GCP Dataflow (Apache Beam), and BigQuery to achieve this.

## Steps

###  Enable all service permissions

1.  Go to `IAM & Admin`
2.  Click on `Service Accounts` on the side panel and then click on the service accounts
<br>
<img width="1048" alt="image" src="https://github.com/user-attachments/assets/64f827a5-afd5-4ffa-bc81-a962c8ece4b8" />
<br>
3. Click on the `Permission` option in the tab and then `Manage Access`.
<br>
<img width="1101" alt="image" src="https://github.com/user-attachments/assets/00a288e9-12e1-4655-abed-6db9e1cc901c" />
<br>
4. Add all the necessary roles.
<br>
<img width="1673" alt="image" src="https://github.com/user-attachments/assets/70acb01b-21ab-45fa-bc36-8ef65ebee40b" />
<br>





### Create Topic in GCP Pub/Sub

1. Go to Pub/Sub in GCP
2. Click `Create Topic` option on the tab
<br>
<img width="982" alt="image" src="https://github.com/user-attachments/assets/5fd4272c-6ce9-43ed-bfe3-e9a2d0a1041d" />
<br>
3. Give a meaningful name to the topic. Select the required options below. If we want we can decide a schema too.




### Create table in GCP Bigquery

1. Open Bigquery in GCP
2. Create a data warehouse in the Bigquery to store the tables
<br>
<img width="969" alt="image" src="https://github.com/user-attachments/assets/534550b6-10f1-4aac-895e-2cd605edc733" />
<br>

3. Give a name and choose a location and click on `Create Dataset` button
<br>
<img width="574" alt="image" src="https://github.com/user-attachments/assets/b470b0aa-462b-49f9-8fa2-ac0a20280a2e" />
<br>
4. Create a table in that warehouse.
<br>
<img width="924" alt="image" src="https://github.com/user-attachments/assets/0262553c-99ab-4fee-97a7-820cc1ffc7e2" />
<br>
6. 
