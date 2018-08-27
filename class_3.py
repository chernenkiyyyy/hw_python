class LogIn:
    __slots__ = ["__dict__"]

    def __init__(self):
        self.unit_name = "user001"
        self.mac_address = "123.153.256.96"
        self.ip_address = "12.34.54.25"
        self.login = "user001@gmail.com"
        self.password = "qwerty001"

    @property
    def get_unit_name(self):
        return self.unit_name

    @get_unit_name.setter
    def get_unit_name(self, new_unit_name):
        self.unit_name = new_unit_name

    @property
    def get_mac_address(self):
        return self.mac_address

    @get_mac_address.setter
    def get_mac_address(self, new_mac_address):
        self.mac_address = new_mac_address\

    @property
    def get_ip_address(self):
        return self.ip_address

    @get_ip_address.setter
    def get_ip_address(self, new_ip_address):
        self.ip_address = new_ip_address

    @property
    def get_login(self):
        return self.login

    @get_login.setter
    def get_login(self, new_login):
        self.login = new_login

    @property
    def get_password(self):
        return self.password

    @get_password.setter
    def get_password(self, new_password):
        self.password = new_password





log = LogIn()
print(log.__dict__)
log.get_unit_name = "00000"
log.get_mac_address = "11111"
log.get_ip_address = "22222"
log.get_login = "33333"
log.get_password = "44444"
print(log.__dict__)