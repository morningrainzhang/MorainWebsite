import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from library.models import Novel, Section, UserFav, UserReadRecord
from django.db.models.aggregates import Count
from django.contrib.auth import get_user_model

User = get_user_model()

from library.form import LoginForm, RegisterForm


# from utils import email_send

class UsersView(View):
    def get(self, request):
        content = {}
        return render(request, 'novel/book_login.html', content)

    def post(self, request):
        content = {}
        if len(request.POST) == 2:
            form = LoginForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data.get('password')
                username = form.cleaned_data.get('username')
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    # return render_to_response('novel/home.html')
                    return redirect('novels')
                    # return HttpResponseRedirect(reverse('user_home', args=(request.user.id,)))
                else:
                    return render(request, 'novel/book_login.html', {'login_msg': '用户名或者密码错误'})
            else:
                return render(request, 'novel/book_login.html', {
                    'login_form': form})
        elif len(request.POST) == 3:
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')
                # 通过Email来获取该对象查看是否存在
                user = User.objects.filter(Q(email=email) | Q(username=username))
                if user.exists() is False:
                    user = User()
                    # 对密码进行加密
                    user.username = username
                    # user.password = make_password(password)
                    user.password = password
                    user.email = email
                    user.save()
                    return render(request, 'novel/book_login.html', {
                        'register_msg': "注册成功！"})
                else:
                    # form = RegisterForm()
                    # return render_to_response('novel/login.html', {'msg': '邮箱已注册','form': form,})
                    return render(request, 'novel/book_login.html', {
                        'register_msg': '邮箱或用户名已注册！！！'
                    })
            else:
                return render(request, 'novel/book_login.html', {
                    'register_form': form})
        return render(request, 'novel/book_login.html', content)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(UsersView, self).dispatch(*args, **kwargs)


'''
返回所有书籍列表
'''


class NovelsView(View):
    def get(self, request):
        content = {}
        # novel_all_list = Novel.objects.all()
        novel_all_list = Novel.objects.all()
        paginator = Paginator(novel_all_list, 9)
        page_num = request.GET.get('page', 1)
        novel_list = paginator.get_page(page_num)
        currentr_page_num = novel_list.number
        page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + list(
            range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
        if page_range[0] - 1 >= 2:
            page_range.insert(0, -1)
        if paginator.num_pages - page_range[-1] >= 2:
            page_range.append(-1)
        if page_range[0] != 1:
            page_range.insert(0, 1)
        if page_range[-1] != paginator.num_pages:
            page_range.append(paginator.num_pages)

        if request.user.username:
            content['fav_novel_list'] = UserFav.objects.filter(user=self.request.user).values_list('novel', flat=True)
        content['novels'] = novel_list
        content['page_num'] = page_num
        content['page_range'] = page_range
        return render(request, 'novel/book_preview.html', content)


'''
返回所有章节列表
'''
class SectionsView(View):
    def get(self, request, novel_pk):
        novel = get_object_or_404(Novel, pk=novel_pk)
        section_all_list = Section.objects.filter(novel=novel).only('title')
        paginator = Paginator(section_all_list, 48)
        page_num = request.GET.get('page', 1)
        section_list = paginator.get_page(page_num)

        currentr_page_num = section_list.number
        page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + list(
            range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
        if page_range[0] - 1 >= 2:
            page_range.insert(0, -1)
        if paginator.num_pages - page_range[-1] >= 2:
            page_range.append(-1)
        if page_range[0] != 1:
            page_range.insert(0, 1)
        if page_range[-1] != paginator.num_pages:
            page_range.append(paginator.num_pages)
        content = {}
        content['novel'] = novel
        content['previous_novel'] = Novel.objects.filter(add_time__lt=novel.add_time).last()
        content['next_novel'] = Novel.objects.filter(add_time__gt=novel.add_time).first()
        content['section_list'] = section_list
        content['page_range'] = page_range

        return render(request, 'novel/book_sections.html', content)


'''
返回所有章节列表
'''


class DetailView(View):
    def get(self, request, section_pk):
        content = {}
        section = get_object_or_404(Section, pk=section_pk)
        # 用户查看小说 标记已读s
        if request.user.username:
            user_section = UserReadRecord(section=section, novel=section.novel, user=request.user)
            user_section.save()
        content['section'] = section
        content['novel'] = section.novel
        content['previous_section'] = Section.objects.filter(novel=section.novel).filter(
            add_time__lt=section.add_time).last()
        content['next_section'] = Section.objects.filter(novel=section.novel).filter(
            add_time__gt=section.add_time).first()

        return render(request, 'novel/book_details.html', content)


class BookrackView(View):
    def get(self, request):
        content = {}
        unread_num = 0
        user = request.user
        # user_novel = User_Novel.objects.filter(user=user)
        section_unread_list = []
        section_all_unread_list = []

        user_novel = UserFav.objects.filter(user=user)
        for novel in user_novel:
            section_info = UserReadRecord.objects.filter(novel=novel.novel, user=user).order_by("add_time").last()
            if section_info:
                # section_unread = Section.objects.filter(novel=novel.novel, date_update__gt=section_info.section.date_update)
                unread_num += \
                    Section.objects.filter(novel=novel.novel,
                                           add_time__gt=section_info.section.add_time).aggregate(
                        num_sections=Count('id'))['num_sections']
            else:
                unread_num += Section.objects.filter(novel=novel.novel).aggregate(num_sections=Count('id'))[
                    'num_sections']
                # print(Section.objects.filter(novel=novel.novel).annotate(num_sections=Count('id')))
        section_read_now = UserReadRecord.objects.filter(user=user).order_by("add_time").last()
        content['user_novel'] = user_novel
        content['section_read_now'] = section_read_now
        content['unread_num'] = unread_num
        return render(request, 'novel/book_bookrack.html', content)


def users_logout(request):
    logout(request)
    return redirect('users')


@login_required(login_url='/users/')
def novel_update(request):
    content = {}
    user = request.user
    section_unread = []
    userfav_list = UserFav.objects.filter(user=user)
    for userfav in userfav_list:
        readrecord = UserReadRecord.objects.filter(novel=userfav.novel, user=user).order_by("add_time").last()
        if readrecord:
            section_unread.extend(
                Section.objects.filter(novel=userfav.novel, is_new=True, add_time__gt=readrecord.section.add_time))
        else:
            print(userfav.novel)
            section_unread.extend(
                Section.objects.filter(novel=userfav.novel, is_new=True))
    section_read_now = UserReadRecord.objects.filter(user=user).order_by("-add_time").last()
    content['section_read_now'] = section_read_now
    content['section_unread'] = section_unread
    return render(request, 'novel/book_update.html', content)


@login_required(login_url='/users/')
def novel_fav(request, novel_pk):
    user = request.user
    if UserFav.objects.filter(user=user, novel_id=novel_pk).exists():
        UserFav.objects.filter(user=user, novel_id=novel_pk).delete()
    else:
        UserFav(user=user, novel_id=novel_pk).save()
    return redirect('novels')
