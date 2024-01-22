import PySimpleGUI as ps

label1 = ps.Text('Select files to compress: ')
label2 = ps.Text('Select destination folder: ')

input_box1 = ps.InputText('')
input_box2 = ps.InputText()

button1 = ps.FilesBrowse('Choose')
button2 = ps.FolderBrowse('Choose')
button3 = ps.Button('Compress')

window = ps.Window('File compressor', layout=[
    [label1, input_box1, button1],
    [label2, input_box2, button2],
    [button3]
])
window.read()
window.close()
