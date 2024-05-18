class Aircraft:
    def __init__(self, model, capacity):
        """Инициализация объекта самолета с моделью и вместимостью."""
        self.model = model
        self.capacity = capacity

    def get_model(self):
        """Метод для получения модели самолета."""
        return self.model

    def __str__(self):
        """Метод для представления объекта самолета в виде строки."""
        return f"{self.model} (вместимость: {self.capacity} пассажиров)"


class Route:
    def __init__(self, origin, destination):
        """Инициализация объекта маршрута с начальным и конечным пунктами."""
        self.origin = origin
        self.destination = destination

    def get_origin(self):
        """Метод для получения начального пункта маршрута."""
        return self.origin

    def get_destination(self):
        """Метод для получения конечного пункта маршрута."""
        return self.destination

    def __str__(self):
        """Метод для представления объекта маршрута в виде строки."""
        return f"{self.origin} -> {self.destination}"


class Airline:
    def __init__(self):
        """Инициализация объекта авиакомпании с пустыми списками самолетов и маршрутов."""
        self.aircraft_list = []
        self.route_list = []

    def add_aircraft(self, aircraft):
        """Добавляет самолет в список самолетов."""
        self.aircraft_list.append(aircraft)
        print(f"Самолет '{aircraft}' успешно добавлен в авиакомпанию.")

    def remove_aircraft(self, model):
        """Удаляет самолет из списка самолетов по модели."""
        for aircraft in self.aircraft_list:
            if aircraft.get_model() == model:
                self.aircraft_list.remove(aircraft)
                print(f"Самолет модели '{model}' успешно удален из авиакомпании.")
                return
        print(f"Самолет модели '{model}' не найден в авиакомпании.")

    def add_route(self, route):
        """Добавляет маршрут в список маршрутов."""
        self.route_list.append(route)
        print(f"Маршрут '{route}' успешно добавлен в авиакомпанию.")

    def remove_route(self, origin, destination):
        """Удаляет маршрут из списка маршрутов по начальному и конечному пунктам."""
        for route in self.route_list:
            if route.get_origin() == origin and route.get_destination() == destination:
                self.route_list.remove(route)
                print(f"Маршрут '{route}' успешно удален из авиакомпании.")
                return
        print(f"Маршрут от '{origin}' до '{destination}' не найден в авиакомпании.")

    def find_aircraft(self, model):
        """Ищет самолет в списке самолетов по модели."""
        found_aircraft = [aircraft for aircraft in self.aircraft_list if aircraft.get_model() == model]
        if found_aircraft:
            print(f"Найдены следующие самолеты модели '{model}':")
            for aircraft in found_aircraft:
                print(f"- {aircraft}")
        else:
            print(f"Самолеты модели '{model}' не найдены в авиакомпании.")

    def find_routes_for_city(self, city):
        """Ищет доступные маршруты для заданного города."""
        available_routes = [route for route in self.route_list if route.get_origin() == city]
        if available_routes:
            print(f"Доступные маршруты из города '{city}':")
            for route in available_routes:
                print(f"- {route.get_destination()}")
        else:
            print(f"Для города '{city}' нет доступных маршрутов.")

# Пример
if __name__ == "__main__":
    airline = Airline()

    aircraft1 = Aircraft("Airbus A320", 180)
    aircraft2 = Aircraft("Boeing 737", 200)
    airline.add_aircraft(aircraft1)
    airline.add_aircraft(aircraft2)

    route1 = Route("Москва", "Париж")
    route2 = Route("Москва", "Лондон")
    airline.add_route(route1)
    airline.add_route(route2)

    airline.find_aircraft("Airbus A320")
    airline.find_aircraft("Boeing 747")

    airline.find_routes_for_city("Москва")
    airline.find_routes_for_city("Лондон")

    airline.remove_aircraft("Airbus A320")
    airline.remove_route("Москва", "Лондон")
