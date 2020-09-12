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

    def show_fpm_registration_summary(self):

        """
        Sample output of this proc is as follows
        {'TABLE_fpm_registration_summary': {'ROW_fpm_registration_summary': [{'vsan': 1001, 'TABLE_device_info': {'ROW_device_info': [{'fcid': '0xec0000', 'pwwn': '21:00:f4:e9:d4:54:ad:a1', 'fpin_descriptor': ['Congestion Notification', 'Peer Congestion Notification', 'Link Integrity Notification', 'Delivery Notification'], 'congestion_signal': ['Warning', 'Alarm']}]}}]}}
        """
        out = self._sw.show("show fpm registration summary")
        if out:
            reg_dict = {}
            for line in out['TABLE_fpm_registration_summary']['ROW_fpm_registration_summary']:

                for item in line['TABLE_device_info']['ROW_device_info']:
                    for key in item:
                        if key == "fcid":
                            reg_dict[item[key]] = []
            for line in out['TABLE_fpm_registration_summary']['ROW_fpm_registration_summary']:

                for item in line['TABLE_device_info']['ROW_device_info']:
                    for fcid in reg_dict:
                        if item['fcid'] == fcid:
                            # print fcid
                            reg_dict[fcid].append(item['fpin_descriptor'])
                            reg_dict[fcid].append(item['pwwn'])
                            reg_dict[fcid].append(line['vsan'])
                            reg_dict[fcid].append(fcid)
                            reg_dict[fcid].append(item['congestion_signal'])
            return reg_dict

        else:
            return None

    def show_fpm_slow_device_database(self):

        """
        Sample output of this proc is as follows
        {'TABLE_vsan_list': {'ROW_vsan_list': [{'vsan': 1001, 'TABLE_device_info': {'ROW_device_info': [{'pwwn': '21:00:f4:e9:d4:54:ad:a1', 'fcid': '0xec0000'}, {'pwwn': '10:00:02:c8:01:cc:01:06', 'fcid': '0xec0040'}]}}]}}
        """
        out = self._sw.show("show fpm slow-device database vsan 1001")
        if out == {'TABLE_vsan_list': {'ROW_vsan_list': [{'vsan': 1001}]}}:
            out = None
        if out:
            reg_dict = {}
            for line in out['TABLE_vsan_list']['ROW_vsan_list']:
                for item in line['TABLE_device_info']['ROW_device_info']:
                    for key in item:
                        if key == "fcid":
                            reg_dict[item[key]] = []

            for line in out['TABLE_vsan_list']['ROW_vsan_list']:
                for item in line['TABLE_device_info']['ROW_device_info']:
                    for fcid in reg_dict:
                        if item['fcid'] == fcid:
                            reg_dict[fcid].append(item['pwwn'])
                            reg_dict[fcid].append(fcid)
                            reg_dict[fcid].append(line['vsan'])
            return reg_dict

        else:
            return None


