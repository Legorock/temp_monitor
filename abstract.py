from abc import ABC, abstractmethod
import time
import logging

class AbstractMonitor(ABC):

  def __init__(self):
    self.sleep = 1
    self._blank_monitor = False

  def check_wait_temp(self):
    wait_threshold = self.get_wait_threshold()
    continue_threshold = self.get_continue_threshold()

    if(self._blank_monitor):
      print("Blank Monitor, no monitoring is available!!")
      return

    if (continue_threshold > wait_threshold):
      raise ValueError("continue threshold is larger than wait threshold, it would wait forever!!")
    
    curr_t = self.get_temp()
    if (curr_t > wait_threshold):
      self._above_wait_threshold(curr_t)

      while(not curr_t < continue_threshold):
        time.sleep(self.sleep)
        curr_t = self.get_temp()

      self._below_continue_threshold(curr_t)
            
  def set_sleep(self, sleep_sec):
    self.sleep = sleep_sec

  def get_sleep(self):
    return self.sleep

  @abstractmethod
  def get_temp(self):
    pass

  @abstractmethod
  def get_wait_threshold(self):
    pass

  @abstractmethod
  def get_continue_threshold(self):
    pass

  @abstractmethod
  def _above_wait_threshold(self, temp):
    pass

  @abstractmethod
  def _below_continue_threshold(self, temp):
    pass
