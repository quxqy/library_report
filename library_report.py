import requests
from datetime import datetime

url_books = 'https://json.medrocket.ru/library/books'
url_events = 'https://json.medrocket.ru/library/events'
url_users = 'https://json.medrocket.ru/library/users'


def library_report():
    try:
        res_users = requests.get(url_users)
        users_list = res_users.json()

        res_books = requests.get(url_books)
        books_list = res_books.json()

        res_events = requests.get(url_events)
        events_list = res_events.json()

        books_count = {}
        for book in books_list:
            if book in books_count:
                books_count[book] += 1
            else:
                books_count[book] = 1

        events_take = [event for event in events_list if (event['action'] == 'take') and event['target'] in books_count]

        taken_books = {}
        users_dict = {user['id']: user['username'] for user in users_list}
        for event in events_take:
            book = event['target']
            user = str(event['actor_id'])
            if user in users_dict:
                if book in taken_books:
                    taken_books[book].append(users_dict[user])
                else:
                    taken_books[book] = [users_dict[user]]

        current_time = datetime.now().strftime('%Y-%m-%dT%H;%M')
        file_name = f'Library_report_{current_time}.txt'

        with open(file_name, 'w') as f:
            f.write('# Available in the library:\n')
            if len(books_count) > 0:
                for book, count in books_count.items():
                    text = f'({count})' if count != 1 else ''
                    f.write(f'- {book} {text}\n')
            else:
                f.write('No books available\n')

            f.write('\n\n# Unavailable books:\n')
            if len(taken_books) > 0:
                for book, users in taken_books.items():
                    for user in users:
                        f.write(f'- {book} - читает {user}\n')
            else:
                f.write('There are no unavailable books\n')

        print(f'The report was successfully saved to a file: {file_name}')

    except requests.exceptions.RequestException as error:
        print(f'Request execution error: {error}')

    except IOError as error:
        print(f'Error writing to disk: {error}')


library_report()