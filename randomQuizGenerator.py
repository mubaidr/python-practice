#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import os
import sys
import shutil
import random

# The quiz data. Keys are states and values are their CAPITALS.
CAPITALS = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
QUIZ_DIR = 'dist\\quiz'
KEY_DIR = 'dist\\key'

# Get count from command line
if len(sys.argv) < 2:
    print(
        'Missing count. Usage: python randomQuizGenerator.py [n] - generates n number of quizes.')
    exit()
else:
    global COUNT
    try:
        COUNT = int(sys.argv[1])
    except ValueError:
        print(
            'Invalid count. Usage: python randomQuizGenerator.py [n] - generates n number of quizes.')
        exit()

# Check if output folder exists
if not os.path.isdir(os.path.join(os.getcwd(), QUIZ_DIR)):
    os.makedirs(os.path.join(os.getcwd(), QUIZ_DIR))
if not os.path.isdir(os.path.join(os.getcwd(), KEY_DIR)):
    os.makedirs(os.path.join(os.getcwd(), KEY_DIR))

# Clean given folder


def cleanPath(path):
    FOLDER = os.path.join(os.getcwd(), path)
    for the_file in os.listdir(FOLDER):
        file_path = os.path.join(FOLDER, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


# Cleanup output folder
cleanPath(QUIZ_DIR)
cleanPath(KEY_DIR)


# Generate new quizes
for i in range(COUNT):
    # Genrate quiz & answer files
    quizFile = open(os.path.join(
        QUIZ_DIR, 'quiz-{0}.txt'.format(i + 1)), mode='w+')
    keysFile = open(os.path.join(
        KEY_DIR, 'key-{0}.txt'.format(i + 1)), mode='w+')
    # quiz headers
    quizFile.write('Name: \nDate: \n\n')
    quizFile.write('State Capitals Quiz (Form {0})'.format(i + 1))
    quizFile.write('\n\n\n')
    # Key headers
    keysFile.write('State Capitals Key (Form {0})'.format(i + 1))
    keysFile.write('\n\n\n')
    # Shuffle the order of the states.
    states = list(CAPITALS.keys())
    random.shuffle(states)
    # Loop through all states, making a question for each.
    for stateIndex, state in enumerate(states):
        # Quiz file
        quizFile.write(
            '{0}: What is capital of {1}? \n'.format(stateIndex + 1, state))
        quizFile.write('')
        correctAnswer = CAPITALS[state]
        wrongAnswers = list(CAPITALS.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        for answerIndex, answer in enumerate(answerOptions):
            quizFile.write(
                (' ' * 10) + '{0}: {1}'.format(answerIndex + 1, answer))
            quizFile.write('\n')
        quizFile.write('\n')
        # Key file
        keysFile.write('{0}: {1}'.format(stateIndex + 1, correctAnswer))
        keysFile.write('\n')
    quizFile.close()
    keysFile.close()

print('Done! Quiz and keys are located in: ' + os.getcwd())
exit()
