from abstract import AbstractMonitor


class BlankMonitor(AbstractMonitor):
  def __init_(self):
    AbstractMonitor.__init__(self)
    self._blank_monitor = True
    
  def get_temp(self):
    pass

  def get_wait_threshold(self):
    pass

  def get_continue_threshold(self):
    pass

  def _above_wait_threshold(self, temp):
    pass

  def _below_continue_threshold(self, temp):
    pass

