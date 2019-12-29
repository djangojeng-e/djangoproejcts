from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        # form_valid method 는 업로드를 끝내고 이동할 페이지를 호출
        # 작성자는 현재 로그인한 사용자로 설정
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # is_valid() method는 입력된 값들을 검증함.
            # 검증이 끝난후 redirect('/') 현재페이지로 다시 리다이렉트
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})
            # form 이 valid 하지 않다면, 작성된 내용을 그대로 작성 페이지에 표시.


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = {'photo', 'text'}
    template_name = 'photo/update.html'

