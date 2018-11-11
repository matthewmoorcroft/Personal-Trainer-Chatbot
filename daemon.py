from flask import Flask
import requests
import psycopg2
import uuid
import json
import datetime
import time

BOT_ID = "725490953"
BOT_TOKEN = "AAF79oRlrKI6SqZNCqjOLRtRwzmOF7A-Yt4"
URL = "https://api.telegram.org/bot" + BOT_ID + ":" + BOT_TOKEN +"/"


uid = str(uuid.uuid4())


try:
    conn = psycopg2.connect("dbname='pt' user='matthew' host='localhost' password='1245788956'")
except:
    print ("ERROR: Unable to connect to the database")

if __name__ == "__main__":
    
	while True:
		#text = input("Enter a phrase you want Sam to send: ")
		#message = URL+"sendMessage?chat_id=375033117&text="+text
		
		cur = conn.cursor()

		cur.execute("UPDATE webhook.incoming_messages set assigned_to='" + uid + "' where id = (SELECT id FROM webhook.incoming_messages where source='Telegram' and assigned_to is null LIMIT 1)")
	
		conn.commit()
		
		cur.execute("SELECT id, message from webhook.incoming_messages where assigned_to='" + uid + "' and processed_on is null LIMIT 1")
		conn.commit()
		rows = cur.fetchall()
		rowcount = cur.rowcount
		
		if rowcount:
			
			for row in rows:
				row_id = row[0]
				raw_message = json.loads(row[1])
			
			message = URL+"sendMessage?chat_id=375033117&text="+raw_message["message"]["text"]
			r = requests.get(message)
			cur.execute("UPDATE webhook.incoming_messages SET processed_on='" + str(datetime.datetime.now()) + "' where id='" + str(row_id) + "'")		
			conn.commit()
			cur.close()
		else:
			time.sleep(1)
		
	