import requests
import argparse
import pprint

if __name__  == 'main':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', help="your action (save ,create , delete , comment )", action="store",
                        type=str,
                        required=True)
    args = parser.parse_args()
    url = "https://jsonplaceholder.typicode.com/posts"
    if args.action == "save":
        address = input("Enter address file :")
        data = requests.get(url)
        with open(f'{address}', 'w') as f:
            output = pprint.PrettyPrinter(indent=2, stream=f)
            output.pprint(data.json())
        print(">>>>successful")
    elif args.action == "create":
        title = input(">>>>Title :")
        body = input(">>>>Body :")
        user_id = int(input(">>>>User ID :"))
        params = {
            'title': f'{title}',
            'body': f'{body}',
            'userid': f'{user_id}',
        }
        resp = requests.post(url, params=params)
        result = requests.get(f'{url}/{resp.json()["id"]}')
        output = pprint.PrettyPrinter(indent=4)
        output.pprint(result.json())
    elif args.action == "delete":
        delete_id = int(input(">>>>Enter id for Delete :"))
        delete= requests.delete(f'{url}/{delete_id}')
        print(f'{delete_id} Deleted')
    elif args.action == "comment":
        comment_id = int(input(">>>>Enter id for comment :"))
        comment = requests.get(f'{url}/{comment_id}/comments')
        output = pprint.PrettyPrinter(indent=4)
        output.pprint(comment.json())