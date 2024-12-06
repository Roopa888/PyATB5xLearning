from abc import ABC, abstractmethod
class ExcelReader(ABC):
    @abstractmethod
    def read_excel(self):
        pass


class Browser(ExcelReader):
    @abstractmethod
    def start_browser(self):
        self.read_excel()


    @abstractmethod
    def stop_browser(self):
        pass
    def read_excel(self):
        print("Excel read")


class TC(Browser):
    # def read_excel(self):
    #     print("Excel is read,data is present")

    def start_browser(self):
        print("Started the chromebrowser")

    def stop_browser(self):
        print("Stopped the chromebrowser")

    def runTC(self):
        self.start_browser()
        self.read_excel()
        self.stop_browser()


tc1 = TC()
tc1.runTC()
