class OldBrowser:
    def start_brwser(self):
        print("Starting IE browser")
    def stop_browser(self):
        print("Stoping IE browser")

class Chrome(OldBrowser):
    def start_brwser(self):
        super().stop_browser()
        print("Starting better chrome browser")

    def stop_browser(self):
        print("Stopping better chrome browser")
obj_ref=Chrome()
obj_ref.start_brwser()
obj_ref.stop_browser()
