class membership:
    def __init__(self, name, img, member_no):
        self.name = name
        self.img = img
        self.member_no = member_no

test = membership("test", "Testimg", 123456)

print(test.name)
print(test.img)
print(test.member_no)
