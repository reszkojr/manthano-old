from django.shortcuts import render

from .forms import ClassroomCreationForm

from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

@login_required(login_url='/login')
def join_classroom(request):
    # The user does not have a classroom yet
    if not request.user.classroom:
        return redirect(request, 'classroom/join_or_create.html')
    if request.method == 'POST':
        form = ClassroomCreationForm(request.POST)
        if form.is_valid():
            classroom = ClassroomCreationForm.save(commit=False)
            classroom.save()
            return redirect('/home')
    else:
        form = ClassroomCreationForm()

    return render(request, 'classroom/create_classroom.html')