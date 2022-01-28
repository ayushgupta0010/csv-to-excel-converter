import pandas as pd

def add_default_columns(df, n, marks, subject):

    df.insert(0, "Subjects", [subject] * n, True)

    df.insert(1, "Topic", [subject] * n, True)

    df.insert(3, "Marks", [marks] * n, True)

    df.insert(4, "Levels", ['M'] * n, True)

    return df

while True:

    file = input('\nEnter the name of the file: ')

    if file == 'q':
        break

    try:

        csv = pd.read_csv(file, sep = ';', names = ['Question', 'Option1', 'Option2', 'Option3', 'Option4', 'CorrectOption'])

        marks = input('Enter the marks: ')

        subject = input('Enter the subject name: ')

        file_name = file.split('.')[0]

        start = csv['Question'][0]

        if start[0] == '1':

            csv['Question'] = csv['Question'].map(lambda x: x[2:])

        csv = add_default_columns(csv, csv.shape[0], marks, subject)

        csv.set_index('Subjects', inplace = True)

        print('\n', csv, '\n')

        cont = input('Do you want to convert this to excel? Enter y or n to convert: ')

        if cont == 'y':
    
            csv.to_excel(file_name + '.xlsx')
 
            print('Converting to excel...')

            print('Converted to excel.\n')
    except FileNotFoundError:
        print('\nThe specified file is not present.')