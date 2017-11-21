from abstract import AbstractMonitor


class RPiMonitor(AbstractMonitor):
  def __init__(self, wait_signal=None, continue_signal=None):
    AbstractMonitor.__init__(self)
    

  def get_temp(self):
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as temp_file:
      t = temp_file.read()
    return float(t) / 1000
  
  def get_wait_threshold(self):
    return 70

  def get_continue_threshold(self):
    return 65
  
  def _above_wait_threshold(self, temp):
    if wait_signal is None:
      print("above wait threshold {:2.1f}".format(temp))
    else:
      wait_signal(temp)
    return

  def _below_continue_threshold(self, temp):
    if continue_signal is None:
      print("below continue threshold {:2.1f}".format(temp))
    else:
      continue_signal(temp)
    return





if __name__ == "__main__":
  import os
  print(os.uname())  

  monitor = RPiMonitor()
  print(monitor.get_wait_threshold())
  print(monitor.get_temp())
  while(True):
    monitor.check_wait_temp()


