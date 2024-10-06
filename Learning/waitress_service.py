import win32serviceutil
import win32service
import win32event
import servicemanager
from waitress import serve
from flask_app import app  # Import the Flask app from flask_app.py

class FlaskWaitressService(win32serviceutil.ServiceFramework):
    _svc_name_ = "FlaskWaitressService"
    _svc_display_name_ = "Flask Waitress Service"
    _svc_description_ = "This service runs the Flask app using the Waitress WSGI server."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        # Start the Waitress WSGI server and run the Flask app
        serve(app, host='0.0.0.0', port=5000)  # Host and port as specified in your Flask app

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(FlaskWaitressService)
