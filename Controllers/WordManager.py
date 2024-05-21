from collections import defaultdict, OrderedDict


class WordManager:

    def __init__(self):
        self.special = None

    def get_word_list(self, file):
        try:
            word_list = []
            with open(file, "r") as word_file:
                for line in word_file:
                    for word in line.split():
                        if len(word) >= 4:
                            word_list.append(word)
            return word_list
        except Exception as e:
            print(f"Error opening file to get word_list {e}")

    def get_letters(self, letter_form):
        if letter_form:
            try:
                letters = ""
                special = letter_form["data-0"].lower()
                outer_1 = letter_form["data-1"].lower()
                outer_2 = letter_form["data-2"].lower()
                outer_3 = letter_form["data-3"].lower()
                outer_4 = letter_form["data-4"].lower()
                outer_5 = letter_form["data-5"].lower()
                outer_6 = letter_form["data-6"].lower()

                self.special = special

                letters += (
                    special + outer_1 + outer_2 + outer_3 + outer_4 + outer_5 + outer_6
                )

                return letters

            except Exception as e:
                return f"Error {e}"
        else:
            return "Error getting letter form"

    def ispangram(self, str, letters):
        for char in letters:
            if char not in str.lower():
                return False

        for letter in str:
            if letter not in letters:
                return False

        return True

    def find_words_with_letters(self, word_list, letters, special):

        grouped_words = defaultdict(list)
        pangrams = []

        for word in word_list:
            if all(letter in letters for letter in word) and special in word:
                grouped_words[len(word)].append({"word": word})
                pangram_check = self.ispangram(word, letters)
                if len(word) >= 7 and pangram_check:
                    pangrams.append({"word": word})

        total_words = len(
            {
                word
                for word in word_list
                if all(letter in letters for letter in word) and special in word
            }
        )
        grouped_words = OrderedDict(sorted(grouped_words.items()))

        return grouped_words, pangrams, total_words

    def get_hint_information(self, grouped_buildable_words):

        matrix = self.build_word_matrix_hints(grouped_buildable_words)
        word_grid = self.build_word_grid_hints(grouped_buildable_words)
        letterset = self.build_letter_set(grouped_buildable_words)
        lengthset = self.build_length_set(grouped_buildable_words)

        return matrix, word_grid, letterset, lengthset

    def build_word_grid_hints(self, grouped_words):
        word_grid = {}
        for item in grouped_words:
            words_arr = grouped_words[item]
            if item not in word_grid:
                word_grid[item] = {}
            for word in words_arr:
                starting_letter = word["word"][:1].upper()
                word_grid[item][starting_letter] = (
                    word_grid[item].get(starting_letter, 0) + 1
                )
        return word_grid

    def build_word_matrix_hints(self, grouped_words):

        matrix = {}

        for item in grouped_words:
            words_arr = grouped_words[item]
            for word in words_arr:
                prefix = word["word"][:2].upper()
                matrix[prefix] = matrix.get(prefix, 0) + 1

        matrix = dict(sorted(matrix.items()))

        return matrix

    def build_length_set(self, grouped_words):
        lengthset = set()
        for item in grouped_words:
            lengthset.add(item)

        return lengthset

    def build_letter_set(self, grouped_words):
        letterset = set()
        for item in grouped_words:
            words_arr = grouped_words[item]
            for word in words_arr:
                starting_letter = word["word"][:1].upper()
                letterset.add(starting_letter)

        return letterset

    def create_matrix(self, matrix):
        prefix_counts = {}
        for item in matrix:
            first = item[:1]
            if first not in prefix_counts:
                prefix_counts[first] = [{"Prefix": item, "Count": matrix[item]}]
            else:
                prefix_counts[first].append({"Prefix": item, "Count": matrix[item]})

        return prefix_counts
