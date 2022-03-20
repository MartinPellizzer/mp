h1 = 'text-3xl text-zinc-100 mb-4 mt-16'
h2 = 'text-xl text-zinc-100 mb-4 mt-8'
p = 'text-base text-zinc-400 mb-2'

def write_left_menu(f_w):
    f_w.write(f'<div class="flex-none w-64 px-8 pt-16 overflow-y-scroll">')
    f_w.write(f'<div class="fixed">')
    f_w.write(f'<p class="text-zinc-400">Offer</p>')
    f_w.write(f'<p class="text-zinc-400">Fanatical Prospecting</p>')
    f_w.write(f'</div>')
    f_w.write(f'</div>')
    
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
    
def write_central_content(f_w):
    f_w.write(f'<div class="flex flex-row flex-auto overflow-auto">')
    f_w.write(f'<div class="px-8">')
    with open("./notes/fanatical-prospecting.txt", "r+") as f_r:
        lines = f_r.readlines()
        for line in lines:
            if line == '': continue
            if line.startswith('##### '):
                f_w.write(f'<h1 class="{h1}">')
                f_w.write(line[5:])
                f_w.write('</h1>')
            elif line.startswith('### '):
                f_w.write(f'<h2 class="{h2}">')
                f_w.write(line[3:])
                f_w.write('</h2>')
            elif line.startswith('# '):
                f_w.write(f'<p class="{p}">')
                f_w.write(line[1:])
                f_w.write('</p>')
            else:
                f_w.write(f'<p class="{p}">')
                f_w.write(line)
                f_w.write('</p>')
    f_w.write(f'</div>')    

def write_body(f_w):
    f_w.write(f'<body class="bg-zinc-900 ">')
    f_w.write(f'<div class="max-w-screen-xl mx-auto flex flex-row">')
    
    write_left_menu(f_w)
    write_central_content(f_w)
    write_right_menu(f_w)

    f_w.write('</div>')
    f_w.write('</body>')

with open("./marketing/fanatical-prospecting.html", "w") as f_w:
    f_w.write('<!DOCTYPE html>')
    f_w.write('<html lang="en">')
    f_w.write('<head>')
    f_w.write('<meta charset="UTF-8">')
    f_w.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
    f_w.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    f_w.write('<link rel="preconnect" href="https://fonts.googleapis.com">')
    f_w.write('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    f_w.write('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">')
    f_w.write('<link rel="stylesheet" href="/style1.css">')
    f_w.write('<title>Financial Prospecting</title>')
    f_w.write('</head>')

    write_body(f_w)
    
    f_w.write('</html>')
    