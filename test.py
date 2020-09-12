import logging

# Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
logging.getLogger().setLevel(logging.NOTSET)
logFileFormatter = logging.Formatter(
    "[%(asctime)s] [%(module)-14.14s] [%(lineno)d] [%(levelname)-5.5s] %(message)s"
)
logConsoleFormatter = logging.Formatter(
    "[%(asctime)s] %(message)s"
)
logging.getLogger("paramiko").setLevel(logging.WARNING)
# Add stdout handler, with level INFO
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logConsoleFormatter)
logging.getLogger().addHandler(console)
from mdssdk.switch import Switch
from mdssdk.switch import Switch

import time
from mdssdk.vsan import Vsan

sw = Switch("10.197.106.40", "admin", "nbv_!2345", verify_ssl=False, connection_type="https", port="8443")
print(sw.version)
print("--------")
print(sw.form_factor)

# sw.feature("analytics",enable=True)8
# out = sw.feature("analytics")
# print(out)

# e = Vsan(sw,200)
#
# e.create("SDK vsan")
#
# print (e.name)
# print (e.id)
#
# e.name = "Bhagayamvsan setter"


# anaHandler = sw.analytics
#
# scsi_profile_few = {
#             'protocol': 'scsi',
#
#             }
# # anaHandler.purge(scsi_profile_few)
# out = sw.show("show fpm slow-device database vsan 1001")
# print ("--------")
# print(out)

fpmHandler = sw.fpm
regDict = fpmHandler.show_fpm_slow_device_database()
print (regDict)
if regDict is not None:
    print("No of slow device :" + str(len(regDict.keys())))
