from flask import Blueprint, render_template, request
from Controllers.WordManager import WordManager

home_view = Blueprint('home_route', __name__, template_folder='templates')

word_manager = WordManager()

word_list = word_manager.get_word_list('enable.txt')

@home_view.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        letters = word_manager.get_letters(request.form)

        show_answers = request.form.get('show_answers')

        if len(letters) > 0:
            grouped_buildable_words, pangrams, total_words = word_manager.find_words_with_letters(word_list, letters, word_manager.special)

            matrix, word_grid, letterset, lengthset = word_manager.get_hint_information(grouped_buildable_words)

            prefix_counts = word_manager.create_matrix(matrix)

            return render_template('index.html', grouped_buildable_words=grouped_buildable_words, pangrams=pangrams, total_words=total_words, letters=letters, matrix=matrix, letterset=letterset, lengthset=lengthset, word_grid=word_grid, prefix_counts=prefix_counts, answers=show_answers)

    return render_template('index.html')