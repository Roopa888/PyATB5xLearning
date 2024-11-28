# Task 2
# Create a Class Name API - RestfulBooker
# name, list_of_api , links {}
# print_apis, print_set()
class RestfulBooker:
    name = None
    list_of_api = []
    links = {}

    def __init__(self, name, list_of_api, links):
        self.name = name
        self.list_of_api = list_of_api
        self.links = links

    def print_APIs(self):
        print(f"List of APIs-{self.name}")
        print(self.list_of_api)

    def print_links(self):
        print(f"List of API links-{self.name}")
        print(self.links)


API1 = RestfulBooker("Rest1", ["restbk1", "restbk2", "restbk3"],
                     {"https://www.postman1.com/", "https://www.postman2.com/}", "https://www.postman3.com/"})
API1.print_APIs()
API1.print_links()
API2 = RestfulBooker("Rest2", ["restbk3", "restbk4", "restbk5"],
                     {"https://www.postman3.com/", "https://www.postman4.com/}", "https://www.postman5.com/"})
print("***********")
print(API2.list_of_api)
print("***********")
API2.print_APIs()
API2.print_links()