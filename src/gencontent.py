from markdown_blocks import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path, 'r')
    from_text = f.read()
    f.close()
    f = open(template_path, 'r')
    template_text = f.read()
    f.close()
    html_string = markdown_to_html_node(from_text).to_html()
    title = extract_title(from_text)
    full_html = template_text.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_string)
    print(f"dest_path is {dest_path}")
    dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dir_name):
        print("path does not exist")
        os.makedirs(dir_name, exist_ok=True)
    f = open(dest_path, 'w')
    f.write(full_html)
    f.close()

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        to_path = os.path.join(dest_dir_path, filename)
        print(f"from_path is: {from_path} isfile? {os.path.isfile(from_path)} isdir? {os.path.isdir(from_path)}")
        print(f"to_path is: {to_path} isfile? {os.path.isfile(to_path)} isdir? {os.path.isdir(to_path)}")
        if os.path.isfile(from_path):
            #os.makedirs(to_path, exist_ok=True)
            to_path = to_path.replace(".md", ".html")
            generate_page(from_path, template_path, to_path) 
        else:
            generate_page_recursive(from_path, template_path, to_path)

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            line = line.replace('# ', '')
            line = line.strip()
            return line
    raise Exception("no h1 header")
     