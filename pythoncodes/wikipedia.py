import wikipedia
import sys

def search_wikipedia(query):
    try:
        search_results = wikipedia.search(query)
        if not search_results:
            print("No results found for your query.")
            return
        page_title = search_results[0]
        page = wikipedia.page(page_title)
        print_summary(page)
        print_page_details(page)
        print_sections(page)
        print_references(page)
        print_links(page)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Your query resulted in a disambiguation page. Possible options are:")
        for option in e.options:
            print(option)
    except wikipedia.exceptions.PageError:
        print("Page not found.")
    except wikipedia.exceptions.HTTPTimeoutError:
        print("Request timed out. Please try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_summary(page):
    print("\nSummary:\n")
    print(page.summary)
    print("\n")

def print_page_details(page):
    print("\nPage Details:\n")
    print(f"Title: {page.title}")
    print(f"URL: {page.url}")
    print(f"Content Length: {len(page.content)} characters")
    print(f"Categories: {', '.join(page.categories[:5])}")
    print(f"References Count: {len(page.references)}")
    print(f"Links Count: {len(page.links)}")

def print_sections(page):
    print("\nSections:\n")
    for section in page.sections:
        print(section)

def print_references(page):
    print("\nReferences:\n")
    for ref in page.references[:5]:
        print(ref)

def print_links(page):
    print("\nLinks:\n")
    for link in page.links[:5]:
        print(link)

def get_user_input():
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("Enter a keyword to search on Wikipedia: ")
    return query

def main():
    query = get_user_input()
    search_wikipedia(query)

if __name__ == "__main__":
    main()

def usage_instructions():
    print("Usage Instructions:\n")
    print("This script retrieves important details about a keyword from Wikipedia.")
    print("Run the script with a keyword as an argument, or enter it when prompted.")
    print("Example: python search_wikipedia.py 'Artificial Intelligence'")

def validate_and_run():
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        usage_instructions()
        sys.exit(0)
    main()

validate_and_run()
