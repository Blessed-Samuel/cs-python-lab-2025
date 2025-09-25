# Base Class
class SmartPhone:
    def __init__(self, brand, color, storage, battery_life="100%"):
        self.brand = brand
        self.color = color
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"{self.brand} is calling {number}...")

    def send_message(self, message):
        print(f"{self.brand} sends message: {message}")

    def battery_lifespan(self):
        print(f"{self.brand} battery life is {self.battery_life}")


# Subclass: iPhone
class iPhone(SmartPhone):
    def __init__(self, color, storage, camera_quality, ios_version, app_store=True):
        super().__init__("iPhone", color, storage)
        self.camera_quality = camera_quality
        self.ios_version = ios_version
        self.app_store = app_store

    def take_shots(self, shots):
        print(f"{self.brand} takes {shots} photos with {self.camera_quality} camera")

    def use_siri(self):
        print(f"{self.brand} is activating Siri...")

    # Polymorphism (overrides)
    def send_message(self, message):
        print(f"{self.brand} (iMessage) sends: {message}")


# Subclass: Samsung
class Samsung(SmartPhone):
    def __init__(self, color, storage, battery_life, android_version, has_pen=False):
        super().__init__("Samsung", color, storage, battery_life)
        self.android_version = android_version
        self.has_pen = has_pen

    def use_pen(self):
        if self.has_pen:
            print(f"{self.brand} is using the S-Pen for note-taking.")
        else:
            print(f"{self.brand} has no S-Pen feature.")

    def customize_ui(self):
        print(f"{self.brand} is customizing the OneUI interface...")

    # Polymorphism
    def send_message(self, message):
        print(f"{self.brand} (Android SMS) sends: {message}")


# Subclass: Google Pixel
class GooglePixel(SmartPhone):
    def __init__(self, color, storage, battery_life, ai_features=True):
        super().__init__("Google Pixel", color, storage, battery_life)
        self.ai_features = ai_features

    def use_ai_camera(self):
        print(f"{self.brand} is enhancing photos using AI...")

    def get_updates(self):
        print(
            f"{self.brand} is downloading the latest Android updates directly from Google."
        )

    # Polymorphism
    def send_message(self, message):
        print(f"{self.brand} (Google Chat) sends: {message}")


# ==========================
# TESTING THE CLASSES
# ==========================

# Base class object
basic_phone = SmartPhone("Nokia", "Blue", 64, "5 days")
basic_phone.make_call("111222333")
basic_phone.send_message("Hello from a basic phone")
basic_phone.battery_lifespan()

print("----")

# iPhone object
my_iphone = iPhone("Gray", 128, "12MP", "iOS 17")
my_iphone.make_call("1234567890")
my_iphone.send_message("Hi from iMessage")
my_iphone.take_shots(5)
my_iphone.use_siri()
my_iphone.battery_lifespan()

print("----")

# Samsung object
my_samsung = Samsung("Black", 256, "85%", "Android 14", has_pen=True)
my_samsung.make_call("0987654321")
my_samsung.send_message("Hey from Samsung SMS")
my_samsung.use_pen()
my_samsung.customize_ui()
my_samsung.battery_lifespan()

print("----")

# Google Pixel object
my_pixel = GooglePixel("White", 128, "90%")
my_pixel.make_call("555444333")
my_pixel.send_message("Message from Google Chat")
my_pixel.use_ai_camera()
my_pixel.get_updates()
my_pixel.battery_lifespan()
