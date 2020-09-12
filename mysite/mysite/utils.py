

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.mail import send_mail, EmailMessage
import glob
import os




class Watcher:
    DIRECTORY_TO_WATCH = "/Users/husj/PycharmProjects/Finalrepo/COIRequestReal/mysite/pdf/pdf"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)



            list_of_files = glob.glob('/Users/husj/PycharmProjects/Finalrepo/COIRequestReal/mysite/pdf/pdf/*')  # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            print(latest_file)


            email = EmailMessage(
                subject='email with attachment',
                body='your attachment',
                from_email='jhaverihussain@gmail.com',
                to=['jhaverihussain@gmail.com'],
            )
            email.attach_file(latest_file)
            email.send()

            print("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()