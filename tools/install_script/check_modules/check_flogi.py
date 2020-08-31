from .check import Check


class Check_Flogi(Check):
    def __init__(self, sw):
        super().__init__(sw)
        self.name = "FLOGI"
        self.cmd_list = ["show flogi database"]

    def compare(self):
        pass