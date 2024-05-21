from flask import Blueprint, render_template, request
from Controllers.WordCountManager import WordCountManager

wordcounter_view = Blueprint('wordcounter_view', __name__, template_folder='templates')

wordcount_manager = WordCountManager()

@wordcounter_view.route('/wordcounter', methods=['GET', 'POST'])
def wordcounter():
    if request:
        words = request.form.getlist('wordcounter_form')
        if (request.method == 'POST'):
          submitted_value = words[0]
          word_count = wordcount_manager.get_word_count(submitted_value)
          return render_template('wordcounter.html', total_word_count= word_count, submitted_value=submitted_value)
    return render_template('wordcounter.html')