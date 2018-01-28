class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.is_activve = True

    def deactivate(self):
        """ Class method to deactivate user """
        self.is_activve = False
        print("Deativated " + self.name)

    def __repr__(self):
        """ Invoked when printed with print function """
        return("User: " + self.name + '\nactive ' + str(self.is_activve))

if __name__ == '__main__':
    new_user = User('Johnathan', 'johnathan.husky@uconn')
    print(new_user)
    new_user.email = 'johnathan.husky@uconn.edu'
    print(new_user.email)
