#encoding=utf-8

import schedule
import time


def job():
    print("I'm working...")
    print('-'*30)

schedule.every(1).second.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    print str(time.ctime(time.time())).center(100,"-")
    print('-' * 20)
    time.sleep(2)
