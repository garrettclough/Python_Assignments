class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
        return self
    def spend_points(self,amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        else:
            print("You do not have enough points")
        return self

user1 = User('Jack', 'Dorsey', 'jack@twitter.com', 42)
user1.enroll().spend_points(199).display_info()

user2 = User('Bill', 'Ackman', 'bill@twtr.com', 43)
user3 = User('Bill', 'Gates', 'bill@microsoft.com', 52)
user2.enroll().spend_points(40).display_info()
