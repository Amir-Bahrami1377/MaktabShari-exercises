from model import SuperUser
import argparse
from database_manager.manager import DBModel, DBManager


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SuperUser Registration script')
    parser.add_argument('-f', '--fullname', metavar='FullName', action='store', required=True, help='Full Name')
    parser.add_argument('-pa', '--password', metavar='Password', action='store', required=True, help='Password')
    parser.add_argument('-ph', '--phone', metavar='Phone', action='store', required=True, help='Phone number')
    parser.add_argument('-b', '--balance', metavar='Balance', action='store', default=0, help='Account Balance')

    args = parser.parse_args()
    admin = SuperUser(full_name=args.fullname, password=args.password, phone=args.phone, balance=args.balance)
    dbmanager = DBManager()
    dbmanager.create(admin)
    print(f"admin created and id is {admin.id}")
