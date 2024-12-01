# Create a class, with public and private variable and method to access them outside

class Flight:
    def __init__(self, passenger):
        self.public_passenger = passenger

    def show_gen_passenger(self):
        return self.public_passenger

    def show_Vip_passenger(self):
        self.__private_VIP_passenger = "President -India"
        return self.__private_VIP_passenger

    def assign_gen_passenger_seats(self, seat_num):
        print("Passenger{passenger} seat no is: ", seat_num)

    def __assign_vip_passenger_seat(self):
        self.__vip_seat_num = 333
        print("VIP Passenger{passenger} seat no is: ", self.__vip_seat_num)

    def display_Vip_seat_num(self):
        self.__assign_vip_passenger_seat()


flight_ref = Flight("Jatin Shah")
print("Public variable : ", flight_ref.public_passenger)
print("Public function accessed: ", flight_ref.show_gen_passenger())
# print(flight_ref.__private_VIP_passenger)           #Error -private variable cant be accessed directly
print("Private variable accessed through a class member function: ", flight_ref.show_Vip_passenger())
flight_ref.assign_gen_passenger_seats(204)  # public function
# flight_ref.__assign_vip_passenger_seat()                    # private function cant be acessed directly
print("Private function accessed through a class member function ")
print("*********************************************************")
flight_ref.display_Vip_seat_num()
