def main():
    with open("lists.txt", "r") as companies:
        the_set = set()
        count_copies = 0
        
        for company in companies:
            company.lower()
            company = company.strip()  # Remove leading/trailing whitespace and newline characters
            print(company)
            curr_count = len(the_set)
            the_set.add(company)

            if curr_count == len(the_set):
                count_copies += 1

        print(f"Number of duplicate entries: {count_copies}")
        print(f"Unique companies: {the_set}")

main()
