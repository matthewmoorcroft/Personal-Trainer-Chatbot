import requests
import uuid
import time
from controller import processor
from connections.database import Database
from model.logger import log


uid = str(uuid.uuid4())

#
# try:
#     conn = psycopg2.connect("dbname='pt' user='matthew' host='localhost' password='1245788956'")
# except:
#     print ("ERROR: Unable to connect to the database")

if __name__ == "__main__":

    db = Database.get_instance()
    while True:
        # text = input("Enter a phrase you want Sam to send: ")
        # message = URL+"sendMessage?chat_id=375033117&text="+text

        # cur = conn.cursor()
        #
        # cur.execute("UPDATE webhook.incoming_messages set assigned_to='" + uid + "' where id = (SELECT id FROM webhook.incoming_messages where source='Telegram' and assigned_to is null LIMIT 1)")
        #
        # conn.commit()
        #
        # cur.execute("SELECT id, message from webhook.incoming_messages where assigned_to='" + uid + "' and processed_on is null LIMIT 1")
        #
        # rows = cur.fetchall()
        # rowcount = cur.rowcount
        #
        # if rowcount:
        #
        # 	for row in rows:
        # 		row_id = row[0]
        # 		raw_message = json.loads(row[1])
        try:
            row_id, raw_message = db.get_message(uid)

            # processor = processor(raw_message['message'])
            processor.process_message(raw_message)

            # message = URL+"sendMessage?chat_id=375033117&text="+raw_message["message"]["text"]
            # r = requests.get(message)
            db.update_processed(row_id)
            # cur.execute("UPDATE webhook.incoming_messages SET processed_on='" + str(datetime.datetime.now()) + "' where id='" + str(row_id) + "'")
            # conn.commit()
            # cur.close()
        except Exception as e:
            print(e)
            time.sleep(1)
