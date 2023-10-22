# Library Report

This script generates a library report based on data retrieved from a JSON API. The report includes information about available books in the library and the users who have taken books.

## Dependencies

This script requires the following packages to be installed:

- requests
```
pip install requests
```

## Usage

1. Import the requests package and the datetime module:
```
import requests
from datetime import datetime
```

2. Define the URLs of the JSON API endpoints:
```
url_books = 'https://json.medrocket.ru/library/books'
url_events = 'https://json.medrocket.ru/library/events'
url_users = 'https://json.medrocket.ru/library/users'
```

3. Define the library_report() function:
```
def library_report():
  # Function implementation...
```

4. Call the library_report() function:
```
library_report()
```

This will generate a library report file with a name in the format
   **Library_report_<current_time>.txt <p> where <current_time> is the current date and time in the format YYYY-MM-DDTHH:MM.**

## Function Description

The library_report() function accesses the JSON API endpoints to retrieve information about books, events, and users. It then processes this data to generate a library report.

### Steps:

1. Send GET requests to the URLs of the JSON API endpoints.
2. Parse the JSON responses into respective Python objects (users_list, books_list, events_list).
3. Count the number of available copies for each book by creating a dictionary books_count.
4. Filter the events to include only the "take" events for books that are in the books_count dictionary.
5. Create a dictionary taken_books to store the books that are currently taken along with the users who have taken them.
6. Iterate over the filtered events and populate the taken_books dictionary.
7. Get the current date and time and format it as a string.
8. Generate a unique file name for the library report in the format Library_report_<current_time>.txt.
9. Open the file in write mode and write the report contents.
10. Close the file.
11. Print a success message with the file name.

## Output

The script generates a library report file in plain text format. The report includes two sections:

1. Available books in the library:
   - Each book is listed with its title and the number of available copies.<p>
     Example:

          # Available in the library:
     - Book 1
     - Book 2 (3)
     - Book 3
     

2. Unavailable books:
   - Each book is listed along with the users who have taken it.<p>
     Example:

          # Unavailable books:
     - Book 2 - reads User 1
     - Book 2 - reads User 2
     - Book 3 - reads User 3
     

If there are no available books or no unavailable books, the corresponding section will indicate this.

## Error Handling

The script includes error handling for the following cases:

- Request errors:
  - If there is an error while making a request to the JSON API, an error message will be printed. <p>
  **Request execution error {error name}** 
- File write errors:
  - If there is an error while writing the library report file, an error message will be printed.<p>
  **Error writing to disk {error name}**
