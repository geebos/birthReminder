import utils


if __name__ == '__main__':
    birthday = input('input birthday(mmdd, eg:0101): ')
    date_type = input('select date type: 1.lunar(阴历), 2.gregorian(阳历)\n')
    email = input("please input email: ")

    with open('birthdays.txt', 'a+') as f:
        f.write('%s %s %s' % (birthday, date_type, utils.encode(email)))
