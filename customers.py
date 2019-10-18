"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first, last, email, password):

        self.first_name = first
        self.last_name = last
        self.email = email
        self.password = password

    def __repr__(self):

        return "<Customer: {}, {}, {}>".format(self.first_name, self.last_name, self.email)


def read_customers_from_file(filepath):

    customer_info = {}

    with open(filepath) as file:
        for line in file:
            (first_name, 
             last_name,
             email,
             password) = line.strip().split('|')

            customer_info[email] = Customer(first_name, 
                                            last_name,
                                            email,
                                            password)
    return customer_info          


def get_by_email(email):

    return customer_dictionary[email]


customer_dictionary = read_customers_from_file("customers.txt")
