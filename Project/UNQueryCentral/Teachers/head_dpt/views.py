from django.shortcuts import render

def head_dpt_dashboard(request):
    return render(request, 'head_dpt/head_dptUI.html')
