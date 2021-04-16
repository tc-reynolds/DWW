from factories.logger_factory import LoggerFactory
import constants
# from tqdm import tqdm_gui
import api_handler
import threading
import config
from threading import Thread, ThreadError
import time

class ThreadService:

    def __init__(self, states, master_logger, scrape_service):
        self.states = states
        self.master_logger = master_logger
        self.scrape_service = scrape_service

    def remove_dead_threads(self, my_threads):
        cp_threads = my_threads.copy()
        for state, thread in cp_threads.items():
            if not thread.is_alive():
                # get results from thread
                thread.handled = True
                self.master_logger.info("Thread for %s has ended and been removed", state)
                my_threads.pop(state)
                del thread
                self.master_logger.info("_______Remaining Threads_________")
                self.master_logger.info(my_threads.keys())
                self.master_logger.info("____________________________")
        return my_threads


    def throttle_threads(self, my_threads, threshold):
        timer_start = time.monotonic()
        while threading.active_count() > threshold:
            timer_end = time.monotonic() - timer_start
            #Every thirty seconds check for finished/dead threads
            if timer_end > 30:
                my_threads = self.remove_dead_threads(my_threads)
                timer_start = time.monotonic()
        return my_threads


    def start_threading(self, states):
        #Handles multiple states running at a time
        my_threads = {}
        threshold = config.THREADING_THRESHOLD
        for state in states:
            url = api_handler.get_url(state)
            try:
                scraper_thread = Thread(name=state, target=self.scrape_service.scrape_state, args=(state, states[state], url,))
                scraper_thread.start()
                my_threads[state] = scraper_thread
                my_threads = self.throttle_threads(my_threads, threshold)
            except ThreadError as te:
                self.master_logger.error(te.with_traceback())
        self.master_logger.info("All states threaded...")
        self.throttle_threads(my_threads, threshold=0)
        self.master_logger.info("All threads finished...Exiting...")


