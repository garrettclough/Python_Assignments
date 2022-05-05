class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        for s in self:
            print(s)
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
    def spend_points(self,amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        else:
            print("You do not have enough points")

user1 = User('Jack', 'Dorsey', 'jack@twitter.com', 42)
print(user1.first_name)
print(user1.last_name)
print(user1.email)
print(user1.age)

user1.enroll()
print(user1.is_rewards_member)
print(user1.gold_card_points)
user1.spend_points(199)
print(user1.gold_card_points)
user1.enroll()

user2 = User('Bill', 'Ackman', 'bill@twtr.com', 43)
user3 = User('Bill', 'Gates', 'bill@microsoft.com', 52)
user2.enroll()
user2.spend_points(30)
print(user2.gold_card_points)
