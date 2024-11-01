"""
    declar a method
"""
class Phone:
    price = 18798
    color = "blue"
    brand = "apple"

    def call(self):
        print("call my phone")
    # create multiple method
    def send_massage(self, msg):
        return f"sending message: {msg}"

my_phone = Phone()
my_phone.call()

print(my_phone.send_massage("Recharge your battery"))