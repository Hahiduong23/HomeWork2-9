class Toppings:

    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type  
        self.__weight = weight  

    #getter và setter cho topping_type
    def get_topping_type(self):
        return self.__topping_type
    def set_topping_type(self, topping_type):
        self.__topping_type = topping_type

    #getter và setter cho weight
    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self.__weight = weight


class Dough:  

    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type  
        self.__baking_technique = baking_technique 
        self.__weight = weight  

    #getter và setter cho flour_type
    def get_flour_type(self):
        return self.__flour_type
    def set_flour_type(self, flour_type):
        self.__flour_type = flour_type

    # getter và setter cho baking_technique
    def get_baking_technique(self):
        return self.__baking_technique
    def set_baking_technique(self, baking_technique):
        self.__baking_technique = baking_technique

    #getter và setter cho weight
    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self.__weight = weight


class Pizza:
    
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name  
        self.__dough = dough 
        self.__toppings_capacity = toppings_capacity  
        self.__toppings = {}  

    #getter và setter cho name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    # getter và setter cho dough
    def get_dough(self):
        return self.__dough
    def set_dough(self, dough):
        self.__dough = dough

    #getter cho toppings
    def get_toppings(self):
        return self.__toppings

    #getter và setter cho toppings_capacity
    def get_toppings_capacity(self):
        return self.__toppings_capacity
    def set_toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    def add_topping(self, topping):
        topping_type = topping.get_topping_type()
        if len(self.__toppings) >= self.__toppings_capacity:
            raise ValueError("Ko đủ không gian để thêm topping vào pizaa")
        if topping_type in self.__toppings:
            self.__toppings[topping_type] += topping.get_weight()
        else:
            self.__toppings[topping_type] = topping.get_weight()

    def calculate_total_weight(self):
        total_weight = self.__dough.get_weight()  
        total_weight += sum(self.__toppings.values()) 
        return total_weight



topping1 = Toppings("Thit", 500)
topping2 = Toppings("Hành", 30)
dough = Dough("Cà chua", "Dưa chuôt", 200)
pizza = Pizza("Margherita", dough, 2)
pizza.add_topping(topping1)
pizza.add_topping(topping2)
print(f"Tổng khối lượng pizza: {pizza.calculate_total_weight()} gam")
