from textnode import TextNode
import shutil
import os
from copystatic import copy_files
from gencontent import generate_page, generate_page_recursive

dir_path_static = "./static/"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
  if os.path.exists(dir_path_public):
    shutil.rmtree(dir_path_public)
  copy_files(dir_path_static, dir_path_public)
  generate_page_recursive(dir_path_content, template_path, dir_path_public)

if __name__ == "__main__":
  main()
