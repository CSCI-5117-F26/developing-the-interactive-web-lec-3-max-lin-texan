from halo import Halo
import time

spinner = Halo(text='Loading', spinner='dots')
spinner.start()
time.sleep(2)
# Run time consuming work here
# You can also change properties for spinner as and when you want

spinner.stop()