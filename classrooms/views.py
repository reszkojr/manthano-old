from django.shortcuts import redirect, render

from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ClassroomCreationForm

from users.models    import User

@login_required(login_url='/user/login')
def classroom(request, code):
    if not request.user.classroom:
        return redirect('class:create_classroom')
    if request.user.classroom.code != code:
        messages.error(request, "You are not a member of this class!")
        return redirect('main:home')
    return render(request, 'classroom/chat.html')

@login_required(login_url='/user/login')
def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomCreationForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.save()
            User.objects.filter(id=request.user.id).update(classroom=classroom)
            return redirect('class:classroom', code=classroom.code)
    else:
        form = ClassroomCreationForm()

    return render(request, 'classroom/create_classroom.html', {'classroom_form': form})
