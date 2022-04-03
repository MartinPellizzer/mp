font_family_h = 'family-inter'
font_family_p = 'family-open-sans'


import os

def write_head(f_w, file_path):
    page_title = file_path.split('/')[-1]
    f_w.write('<head>')
    f_w.write('<meta charset="UTF-8">')
    f_w.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
    f_w.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    f_w.write('<link rel="preconnect" href="https://fonts.googleapis.com">')
    f_w.write('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    # f_w.write('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">')
    # f_w.write('<link href="https://fonts.googleapis.com/css2?family=Hurricane&family=Open+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">')
    f_w.write('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&family=Open+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">')
    f_w.write('<link rel="stylesheet" href="/global.css">')
    f_w.write('<link rel="stylesheet" href="/tw.css">')
    f_w.write(f'<title>{page_title}</title>')
    f_w.write('</head>')

def write_body(f_w, file_path):
    f_w.write(f'<body class="bg-gray-100">')
    f_w.write(f'''
        <div class="max-w-screen-xl mx-auto flex flex-row bg-white px-64 py-16">
    ''')
    
    # write_left_menu(f_w)
    write_central_content(f_w, file_path)
    # write_right_menu(f_w)

    f_w.write('</div>')
    f_w.write('</body>')




def write_left_menu(f_w):
    f_w.write(f'<div class="flex-none w-64 px-8 pt-16 overflow-y-scroll">')
    f_w.write(f'<div class="fixed">')
    f_w.write(f'<p class="text-zinc-400">Offer</p>')
    f_w.write(f'<p class="text-zinc-400">Fanatical Prospecting</p>')
    f_w.write(f'</div>')
    f_w.write(f'</div>')
    
    '''
def write_right_menu(f_w):
    f_w.write(f'<div class="flex-none w-64 px-8 pt-16">')
    f_w.write(f'<div class="fixed">')

    with open("./notes/fanatical-prospecting.txt", "r+") as f_r:
        lines = f_r.readlines()
        for line in lines:
            if line.startswith('##### '):
                f_w.write(f'<h1 class="text-zinc-200 text-sm font-bold">')
                f_w.write(line[5:])
                f_w.write('</h1>')
            elif line.startswith('### '):
                f_w.write(f'<h2 class="text-zinc-400 text-sm font-normal ml-4">')
                f_w.write(line[3:])
                f_w.write('</h2>')

    f_w.write(f'</div>')
    f_w.write(f'</div>')
    '''

def write_h1(f_w, line):
    f_w.write(f'<h1 class="text-5xl text-gray-900 lowercase mb-2 lowercase {font_family_h}">')
    f_w.write(line[1:])
    f_w.write('</h1>')
    
def write_h2(f_w, line):
    f_w.write(f'<h2 class="text-3xl text-gray-900 mb-2 mt-16 lowercase {font_family_h}">')
    f_w.write(line[2:])
    f_w.write('</h2>')
    
def write_h3(f_w, line):
    f_w.write(f'<h3 class="text-xl text-gray-900 mb-2 mt-4 lowercase {font_family_h}">')
    f_w.write(line[3:])
    f_w.write('</h3>')

def write_crumbs(f_w, file_path):
    breadcrumb = ' &#x2E31; '.join(file_path.replace('.txt', '').replace('-', ' ').split('/')[2:])
    f_w.write(f'<p class="text-sm font-semibold lowercase text-sky-500 mb-4 {font_family_h}">')
    for b in breadcrumb:
        f_w.write(b)
    f_w.write('</p>')

def write_author(f_w):
    f_w.write(f'<p class="text-sm font-semibold lowercase text-gray-900 mb-4 {font_family_h}">')
    f_w.write('martin pellizzer')
    f_w.write('</p>')

    
def write_p(f_w, line):
    weight = 400
    color = 500
    if line.startswith('s:'):
        line = line[2:]
        weight = 700
        color = 900

    line = line.replace('fan fact:', f'<span class="text-gray-900 font-weight-700">fan fact:</span>')
    line = line.replace('mantra:', f'<span class="text-gray-900 font-weight-700">mantra:</span>')
    line = line.replace('harsh truth:', f'<span class="text-gray-900 font-weight-700">harsh truth:</span>')
    f_w.write(f'<p class="text-base text-gray-{color} font-weight-{weight} mb-4 {font_family_p}">')
    f_w.write(line)
    f_w.write('</p>')

    
def write_central_content(f_w, file_path):
    f_w.write(f'<div class="flex flex-row flex-auto overflow-auto">')
    f_w.write(f'<div class="px-8">')
    write_crumbs(f_w, file_path)
    with open(file_path, "r+") as f_r:
        lines = f_r.readlines()
        for line in lines:
            if line == '': continue
            if line.startswith('### '): write_h3(f_w, line)
            elif line.startswith('## '): write_h2(f_w, line)
            elif line.startswith('# '): write_h1(f_w, line)
            else: write_p(f_w, line)
    f_w.write(f'</div>')    


for folder in os.listdir("./notes"):
    if os.path.isdir(folder):
        for file in os.listdir(f'./notes/{folder}'):
            if file.endswith(".txt"):
                file_path = f'./notes/{folder}/{file}'

                print(f'{folder}/{file}')
                file = file.replace('.txt', '.html')

                with open(f'./{folder}/{file}', "w") as f_w:
                    f_w.write('<!DOCTYPE html>')
                    f_w.write('<html lang="en">')

                    write_head(f_w, file_path)
                    write_body(f_w, file_path)
                    
                    f_w.write('</html>')