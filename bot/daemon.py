import uuid
import time
from controller import processor
from connections.database import Database
from model.logger import log
import traceback


uid = str(uuid.uuid4())


if __name__ == "__main__":

    db = Database.get_instance()
    while True:

        try:
            row_id, raw_message = db.get_message(uid)
            log(str(raw_message))
            processor.process_message(raw_message)
            db.update_processed(row_id)

        except TypeError:

            time.sleep(1)
        except Exception as e:
            print(e)
            traceback.print_exc()
