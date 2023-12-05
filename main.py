def count_words(example_string: str):
    words = example_string.split()
    return len(words)

def count_letters(example_string: str):
    counts = {}
    for ch in example_string:
        if not ch.isalpha(): continue
        lowered_ch = ch.lower()
        if lowered_ch in counts:
            counts[lowered_ch] += 1
        else:
            counts[lowered_ch] = 1
    return counts

def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    letter_counts = count_letters(file_contents)

    report_header = f"--- Begin report of {file_name} ---\n"
    report_words = f"{word_count} words found in the document\n\n"

    def report_letter(letter, count):
        return f"The \'{letter}\' character was found {count} times\n"

    letter_counts_sorted = list(letter_counts.items())
    letter_counts_sorted.sort(key=lambda ele: ele[1], reverse=True)
    report_letters = ""
    for letter, count in letter_counts_sorted:
        report_letters += report_letter(letter, count)
    report_footer = "--- End report ---"
    report = report_header + report_words + report_letters + report_footer
    print(report)

if __name__ == "__main__":
    main()
