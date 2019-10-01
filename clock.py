import os
from apscheduler.schedulers.blocking import BlockingScheduler
import worker


sched = BlockingScheduler(timezone="UTC")


@sched.scheduled_job('interval',
                     minutes=int(os.environ.get('REMO_CLOCK_INTERVAL', 1)))
def collect_remo_data():
    worker.run()


sched.start()
