class Membership:
    """Object to store the membership details"""
    def __init__(self, name, img, member_no):
        self.name = name
        self.img = img
        self.member_no = member_no



if __name__ == '__main__':
    test = Membership("test", "Testimg", 123456)
    print(test.name)
    print(test.img)
    print(test.member_no)
