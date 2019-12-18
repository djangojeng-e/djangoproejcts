from django.http import HttpResponse
from django.shortcuts import render
import os
# Create your views here.


def post_list(request):
    # 상위폴더(blog) 의 상위폴더 (djangogirls)의
    # 하위폴더에 (templates)
    # 하위파일 (post_list.html)의 내용을 read() 한 결과를
    # httpresponse 에 인자로 전달

    cur_file_path = os.path.abspath(__file__)
    parent_dir_path = os.path.dirname(cur_file_path)
    root_dir_path = os.path.dirname(parent_dir_path)
    templates_dir_path = os.path.join(root_dir_path, 'templates')
    post_list_html_path = os.path.join(templates_dir_path,'post_list.html')

    f = open(post_list_html_path, 'rt')
    html = f.read()
    f.close()

    return HttpResponse(html)

