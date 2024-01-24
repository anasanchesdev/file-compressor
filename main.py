from zipper import zip_archive
import PySimpleGUI as ps

FONT = ('Segoe UI Black', 10)
ACTION_FONT = ('Segoe UI', 10)

print(ps.Text.fonts_installed_list())
ps.theme('Dark')
title = ps.Text('FILE COMPRESSOR', font=('Copperplate Gothic Bold', 20), text_color='green')
dev_credits = ps.Text('by: anasanchesdev', font=('Courier', 8), text_color='lime green', pad=((6, 0), (0, 15)))
label1 = ps.Text('Select files to compress: ', font=FONT)
label2 = ps.Text('Select destination folder: ', font=FONT, pad=((2, 0), (5, 0)))
label3 = ps.Text('Type in the zip file name: ', font=FONT, pad=((5, 0), (40, 0)))
action_text = ps.Text('', key='action_text', font=ACTION_FONT)

input_box1 = ps.InputText(key='files_input')
input_box2 = ps.InputText(key='folder_input')
input_box3 = ps.InputText(key='zip_name')

button1 = ps.FilesBrowse('Choose', key='files_button')
button2 = ps.FolderBrowse('Choose', key='folder_button')
button3 = ps.Button('Compress', key='compress_button')

# ui format
window = ps.Window('File compressor', layout=[
    [title],
    [dev_credits],
    [label1],
    [input_box1, button1],
    [label2],
    [input_box2, button2],
    [label3],
    [input_box3, button3],
    [action_text]
])

while True:

    event, values = window.read()  # event: pressed button // values (dict): respective inputs of the keys
    print(f'EVENT: {event}\nVALUES: {values}\n')  # test
    filepath = values['files_input'].split(';')  # separates multiple filepaths into list
    folder = values['folder_input']
    zip_name = values['zip_name']
    inputs = [filepath, folder, zip_name]
    print(f'FILEPATH: {filepath}\nFOLDER: {folder}\n')  # test

    if event == 'compress_button':
        if not all(inputs):
            window['action_text'].update(value=f'Please, fill in all the input fields before submitting.',
                                         text_color='red', font=ACTION_FONT)
            continue
        zip_archive(filepath, folder, zip_name)
        window['action_text'].update(value=f'"{zip_name}.zip" was compressed successfully.', text_color='lime green',
                                     font=ACTION_FONT)

    elif event == ps.WIN_CLOSED:
        break

window.close()
