import argparse
import datetime
import time
from time import gmtime, strftime
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date

def main():
    parser = argparse.ArgumentParser(description='Starts a daily run and transfer data from the provided excel file')
    
    parser.add_argument('-hour')
    parser.add_argument('-day')


    hour = None
    

    day = None
    
    if day is not None and hour is not None:
        print("Job will run at the specified hour on the specified day of every month")

    if day is not None and hour is None:
        print("If no Hour mentioned, Job will run at midnight (12 AM) on the specified day of every month ")

    def this_job():
        process_file( 0)

    scheduler = BackgroundScheduler()

    if hour is None and day is None:
        print("No hour or days specified, Data Exported to CSV ")
        process_file(None)
    elif hour is not None and day is None: #  hourly run
        try:
            hour = int(hour)
            job = scheduler.add_job(this_job, 'cron', hour=str(hour))
        except ValueError:
            output_exit_error("Hour must be an integer")
    elif day is not None: # then executing on every X day
         try:
            hour = int(hour) if hour is not None else 0  # default the hour 
            day = int(day)
            job = scheduler.add_job(this_job, 'cron', day=str(day), hour=str(hour))
         except ValueError:
            output_exit_error("Month & Hour must be integers.")

    scheduler.start()
    print("Waiting for job execution")
    while True:
        time.sleep(1)
    

def process_file( hour):
    report_execution_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("hello")
    
main()
