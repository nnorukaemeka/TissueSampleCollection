from app import app
import os





if __name__=='__main__':
    # scheduler.add_job(id = 'sheduled task', func = activateInterest, trigger = 'interval', seconds = 5)
    # scheduler.start()
    app.run(host='0.0.0.0', port=os.environ.get('PORT'))
    # app.run()