from django.shortcuts import redirect, render

from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .forms import ClassroomCreationForm

@login_required(login_url='/user/login')
def join_classroom(request):
    # The user does not have a classroom yet
    if not request.user.classroom:
        return redirect('class:create_classroom')
    if request.method == 'POST':
        form = ClassroomCreationForm(request.POST)
        if form.is_valid():
            classroom = ClassroomCreationForm.save(commit=False)
            classroom.save()
            return redirect('/home')
    else:
        form = ClassroomCreationForm()

    return render(request, 'classroom/classroom.html')

@login_required(login_url='/user/login')
def create_classroom(request):
    return render(request, 'classroom/create_classroom.html')
