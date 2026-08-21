try:
    with open("templates/home.html", "r") as file:

        lines = file.readlines()

        # Number of lines
        number_of_lines = len(lines)

        # Create one string containing the complete file
        text = "".join(lines)

        # Number of characters
        number_of_characters = len(text)

        # Convert text into words
        words = text.split()

        # Number of words
        number_of_words = len(words)

        # Count frequency of each word
        frequency = {}

        for word in words:
            word = word.lower()

            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        # Number of unique words
        unique_words = len(frequency)

        # Most frequent word
        most_frequent_word = max(frequency, key=frequency.get)

        print("Number of lines:", number_of_lines)
        print("Number of words:", number_of_words)
        print("Number of characters:", number_of_characters)
        print("Number of unique words:", unique_words)
        print("Most frequent word:", most_frequent_word)

except FileNotFoundError:
    print("File does not exist.")