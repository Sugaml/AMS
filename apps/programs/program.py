from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from apps.models import Program, Semester, Subject
from .forms import ProgramForm, SemesterForm, SubjectForm

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'programs/program_list.html', {'programs': programs})

def program_create(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'programs/program_form.html', {'form': form})

def program_update(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm(instance=program)
    return render(request, 'programs/program_form.html', {'form': form})

def program_delete(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('program_list')
    return render(request, 'programs/program_confirm_delete.html', {'program': program})

def program_toggle_active(request, pk):
    program = get_object_or_404(Program, pk=pk)
    program.is_active = not program.is_active
    program.save()
    return redirect('program_list')
