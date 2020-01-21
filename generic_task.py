import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class the_handler(PatternMatchingEventHandler):
    def on_created(self, event):
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime('.')))} - {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime('.')))} - {event.src_path} has been deleted!")

    def on_modified(self, event):
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime('.')))} - {event.src_path} has been modified")

    def on_moved(self, event):
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime('.')))} - {event.src_path} has been moved to {event.dest_path}")



if __name__=='__main__':
    changes = '*'
    ignore_changes = ''
    case_sensitive = True
    ignore_directories = False
    event_handler = the_handler(changes, ignore_changes, case_sensitive, ignore_directories)
    my_observer = Observer()
    my_observer.schedule(event_handler, path=".", recursive=True)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()


