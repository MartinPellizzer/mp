import os

for folder in os.listdir("./notes"):
    if os.path.isdir(folder):
        for file in os.listdir(f'./notes/{folder}'):
            if file.endswith(".html"):
                file_path = f'./notes/{folder}/{file}'

                with open(f'./{folder}/{file}', "w") as f_w:
                    f_w.write('<!DOCTYPE html>')
                    f_w.write('<html lang="en">')

                    page_title = file_path.split('/')[-1]
                    
                    f_w.write('<head>')
                    f_w.write('<meta charset="UTF-8">')
                    f_w.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
                    f_w.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
                    f_w.write('<link rel="preconnect" href="https://fonts.googleapis.com">')
                    f_w.write('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
                    f_w.write('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&family=Open+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">')
                    f_w.write('<link rel="stylesheet" href="/style.css">')
                    f_w.write(f'<title>{page_title}</title>')
                    f_w.write('</head>')

                    f_w.write('<body>')
                    with open(file_path, "r+") as f_r:
                        lines = f_r.readlines()
                        for line in lines:
                            f_w.write(line)
                    f_w.write('</body>')
                    
                    f_w.write('</html>')