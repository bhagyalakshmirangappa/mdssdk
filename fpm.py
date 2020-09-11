import logging
import re

class FPM:
    """
    FPM Module

    :example:
        >>> switch_obj = Switch(ip_address = switch_ip, username = switch_username, password = switch_password )
        >>> fpm_hand = switch_obj.fpm
        >>> print(fpm_hand)
        <mdslib.fpm.FPM object at 0x10ad710d0>

    """

    def __init__(self, sw):
        self._sw = sw

    def _show_fpm_registration_summary(self):

        """
        Sample output of this proc is as follows
        {'TABLE_fpm_registration_summary': {'ROW_fpm_registration_summary': [{'vsan': 1001, 'TABLE_device_info': {'ROW_device_info': [{'fcid': '0xec0000', 'pwwn': '21:00:f4:e9:d4:54:ad:a1', 'fpin_descriptor': ['Congestion Notification', 'Peer Congestion Notification', 'Link Integrity Notification', 'Delivery Notification'], 'congestion_signal': ['Warning', 'Alarm']}]}}]}}
        """
        out = self._sw.show("show fpm registration summary")
        if out:
            regDict = {}

            for line in out['TABLE_fpm_registration_summary']['ROW_fpm_registration_summary']:
                # print line['vsan']
                # print "---------------------------"
                for item in line['TABLE_device_info']['ROW_device_info']:
                    for key in item:
                        if key == "fcid":
                            regDict[item[key]] = []
                        # print key, item[key]
                # print "****************************"

            for line in out['TABLE_fpm_registration_summary']['ROW_fpm_registration_summary']:
                # print line['vsan']
                # print "---------------------------"
                for item in line['TABLE_device_info']['ROW_device_info']:
                    for fcid in regDict:
                        if item['fcid'] == fcid:
                            # print fcid
                            regDict[fcid].append(item['fpin_descriptor'])
                            regDict[fcid].append(item['pwwn'])
                            regDict[fcid].append(line['vsan'])
                            regDict[fcid].append(fcid)
                            regDict[fcid].append(item['congestion_signal'])

        else:
            return None
