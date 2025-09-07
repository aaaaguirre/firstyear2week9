# Q1
class KeroseneDeliveryTruck:
    deliveries_today = 0
    total_sales = 0

    def __init__(self, price_per_litre_in, truck_capacity_in, min_delivery_qty_in, litres_in_truck = 0):
        if price_per_litre_in > 0:
            self.__price = price_per_litre_in
        else:
            self.__price = 0
        if truck_capacity_in > 0:
            self.__capacity = truck_capacity_in
        else:
            self.__capacity = 0
        if min_delivery_qty_in > 0:
            self.__delivery_qty = min_delivery_qty_in
        else:
            self.__delivery_qty = 0
        if litres_in_truck is not None:
            self.__litres = litres_in_truck
        else:
            self.__litres = 0

    def fill_truck(self, fill_amount_in):
        if fill_amount_in > 0:
            self.__litres += fill_amount_in
        else:
            self.__litres = 0

    # def make_delivery(self,litres_for_delivery):
    #     if litres_for_delivery >= min_delivery_qty_in:
    #         return deliveries_today, litres_in

    def set_price_per_lire(self, new_price_per_litre):
        if new_price_per_litre > 0:
            self.__price += new_price_per_litre

    def print(self):
        print()