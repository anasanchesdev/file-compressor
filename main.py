from zipper import zip_archive
import PySimpleGUI as ps

FONT = ('Segoe UI Black', 10)
ACTION_FONT = ('Segoe UI', 10)

ps.theme('Dark')
title = ps.Text('FILE COMPRESSOR', font=('Copperplate Gothic Bold', 20), text_color='green')
dev_credits = ps.Text('by: anasanchesdev', font=('Courier', 8), text_color='lime green', pad=((6, 0), (0, 15)))
z_file_label = ps.Text('Select files: ', font=FONT)
z_folder_label = ps.Text('Select destination folder: ', font=FONT, pad=((2, 0), (5, 0)))
z_name_label = ps.Text('Type in the zip file name: ', font=FONT, pad=((5, 0), (40, 0)))
zip_slider = ps.Text('ZIP')
unzip_slider = ps.Text('UNZIP')
slider = ps.Slider(key='slider', range=(0, 1), disable_number_display=True, enable_events=True, orientation='h',
                   size=(5, 5))
action_text = ps.Text('', key='action_text', font=ACTION_FONT)

z_file_input = ps.InputText(key='files_input')
z_folder_input = ps.InputText(key='folder_input')
z_name_input = ps.InputText(key='zip_name')

z_file_button = ps.FilesBrowse('Choose', key='files_button')
z_folder_button = ps.FolderBrowse('Choose', key='folder_button')
z_action_button = ps.Button('Compress', key='compress_button')

uz_file_label = ps.Text('Select files to compress: ', font=FONT)
uz_folder_label = ps.Text('Select destination folder: ', font=FONT, pad=((2, 0), (5, 0)))
uz_action_text = ps.Text('', key='uz_action_text', font=ACTION_FONT)

uz_files_input = ps.InputText(key='uz_files_input')
uz_folder_input = ps.InputText(key='uz_folder_input')

uz_file_button = ps.FileBrowse('Choose', key='uz_files_button')
uz_folder_button = ps.FolderBrowse('Choose', key='uz_folder_button')
uz_action_button = ps.Button('Compress', key='decompress_button')

zip_layout = [
    [z_file_label],
    [z_file_input, z_file_button],
    [z_folder_label],
    [z_folder_input, z_folder_button],
    [z_name_label],
    [z_name_input, z_action_button],
    [action_text]
]

unzip_layout = [
    [uz_file_label],
    [uz_files_input, uz_file_button],
    [uz_folder_label],
    [uz_folder_input, uz_folder_button],
]

layout = [
    [title],
    [dev_credits],
    [zip_slider, slider, unzip_slider],
    [ps.Column(zip_layout, key='zip')],
    [ps.Column(unzip_layout, key='unzip', visible=False)]
]

# ui format
window = ps.Window('File compressor', layout=layout)


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
