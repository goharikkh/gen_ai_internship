class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.manufacturer}, {self.total}, {self.allocated})"

    def claim(self, n):
        if self.available >= n:
            self._allocated += n
        else:
            print("Not enough inventory")

    def freeup(self, n):
        if self.allocated >= n:
            self._allocated -= n
        else:
            print("Not enough inventory")

    def died(self, n):
        if self.available >= n:
            self._total -= n
        else:
            print("Not enough inventory")

    def purchased(self, n):
        self._total += n

    @property
    def category(self):
        return self.__class__.__name__.lower()

    @property
    def available(self):
        return self.total - self.allocated


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, interface, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores
        self._interface = interface
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores

    @property
    def interface(self):
        return self._interface

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.manufacturer}, " \
               f"{self.total}, {self.allocated}, {self.capacity_GB}, {self.interface})"


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.manufacturer}, " \
               f"{self.total}, {self.allocated}, {self.capacity_GB}, {self.size}, {self.rpm})"


