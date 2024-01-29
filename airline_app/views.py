from django.shortcuts import render, redirect, get_object_or_404
from .models import Airplane
from .forms import AirplaneForm

def airplane_list(request):
    airplanes = Airplane.objects.all()
    return render(request, 'airline_app/airplane_list.html', {'airplanes': airplanes})

def airplane_new(request):
    if request.method == "POST":
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airplane_list')
    else:
        form = AirplaneForm()
    return render(request, 'airline_app/edit.html', {'form': form})

def airplane_edit(request, pk):
    airplane = get_object_or_404(Airplane, pk=pk)
    if request.method == "POST":
        form = AirplaneForm(request.POST, instance=airplane)
        if form.is_valid():
            form.save()
            return redirect('airplane_list')
    else:
        form = AirplaneForm(instance=airplane)
    return render(request, 'airline_app/edit.html', {'form': form})

def airplane_delete(request, pk):
    airplane = get_object_or_404(Airplane, pk=pk)
    if request.method == "POST":
        airplane.delete()
        return redirect('airplane_list')
    return render(request, 'airline_app/delete.html', {'object': airplane})