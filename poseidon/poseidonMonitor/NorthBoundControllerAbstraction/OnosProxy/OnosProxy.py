#!/usr/bin/env python
#
#   Copyright (c) 2016 In-Q-Tel, Inc, All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Created on 11 July 2016
@author: kylez
"""

from poseidon.poseidonMonitor.NorthBoundControllerAbstraction.ControllerProxy.ControllerProxy import ControllerProxy

class OnosProxy(ControllerProxy):
    def __init__(self, base_uri, auth=None):
        super(OnosProxy, self).__init__(base_uri)
        self.auth = auth

    def get_devices(self, devices_resource="devices"):
        """
        GET list of devices from the controller.
        """
        j = self.get_json_resource(devices_resource, auth=self.auth)
        return j

    def get_hosts(self, hosts_resource="hosts"):
        """
        GET list of hosts from the controller
        """
        j = self.get_json_resource(hosts_resource, auth=self.auth)
        return j

    def get_flows(self, flows_resource="flows"):
        """
        GET list of flows from the controller
        """
        j = self.get_json_resource(flows_resource, auth=self.auth)
        return j

