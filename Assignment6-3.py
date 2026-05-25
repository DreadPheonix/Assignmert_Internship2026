import requests

def search_book(book_name):

    url = f"https://openlibrary.org/search.json?q={book_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # Checking if results exist
        if data["numFound"] == 0:
            print("No book found.")
            return

        # Taking first result
        book = data["docs"][0]

        title = book.get("title", "Not Available")

        author = book.get("author_name", ["Not Available"])[0]

        publish_year = book.get("first_publish_year", "Not Available")

        edition_count = book.get("edition_count", "Not Available")

        print("\n------ Book Information ------")
        print("Title:", title)
        print("Author:", author)
        print("First Publish Year:", publish_year)
        print("Edition Count:", edition_count)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

book_name = input("Enter book name: ")

search_book(book_name)