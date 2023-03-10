from PySide6.QtWidgets import QMessageBox

class CustomMessageBox(QMessageBox):

    def __init__(self, *__args):
        QMessageBox.__init__(self)
        self.timeout = 0
        self.autoclose = False
        self.currentTime = 0

    def showEvent(self, QShowEvent):
        """Called when the widget is shown."""
        self.currentTime = 0
        if self.autoclose:
            self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        """Called when the timer is triggered."""
        self.currentTime += 1
        if self.currentTime >= self.timeout:
            self.done(0)

    @staticmethod
    def showWithTimeout(timeout_seconds, title, message, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        """Show a message box with a timeout."""
        w = CustomMessageBox()
        w.autoclose = bool(timeout_seconds)
        w.timeout = timeout_seconds
        w.setText(message)
        w.setWindowTitle(title)
        w.setIcon(icon)
        w.setStandardButtons(buttons)
        w.exec()
    
    