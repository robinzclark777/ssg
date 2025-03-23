from textnode import TextNode
import shutil
import os
from copystatic import copy_files
from gencontent import generate_page, generate_page_recursive
import sys

dir_path_static = "./static/"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = '/'

def main():
  basepath = default_basepath
  if len(sys.argv) > 1:
    basepath = sys.argv[1]
  if os.path.exists(dir_path_public):
    shutil.rmtree(dir_path_public)
  copy_files(dir_path_static, dir_path_public)
  generate_page_recursive(dir_path_content, template_path, dir_path_public, basepath)

if __name__ == "__main__":
  main()
