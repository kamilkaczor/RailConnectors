from django.shortcuts import render, redirect
from .forms import SearchTerminal, AddToDb
from .models import Wires, Terminal, Connector
from django.http import HttpResponseRedirect


wire_cross_section = 0


def index(request):
    return render(request, 'base.html')


def add_terminal(request):
    form_add = AddToDb()
    print(request.method)
    if request.method == 'POST':
        form_add = AddToDb(request.POST)

        if form_add.is_valid():
            add_insert_dtr = form_add.cleaned_data['add_insert']
            add_manufacturer = form_add.cleaned_data['add_manufacturer']
            add_insert_manu_nr = form_add.cleaned_data['add_insert_manu_number']
            add_gender = form_add.cleaned_data['add_gender']
            add_terminal = form_add.cleaned_data['add_terminal']
            add_connector_family = form_add.cleaned_data['add_connector_family']
            add_project = form_add.cleaned_data['add_project']
            add_min_crosssection = form_add.cleaned_data['add_min_cross_section']
            add_max_crosssection = form_add.cleaned_data['add_max_cross_section']
            add_plating = form_add.cleaned_data['add_plating']
            add_terminal_manu_nr = form_add.cleaned_data['add_terminal_manu_number']
            print(add_insert_dtr, add_manufacturer, add_insert_manu_nr, add_gender, add_terminal, add_connector_family,
                  add_project, add_min_crosssection, add_max_crosssection, add_plating,
                  add_terminal_manu_nr)
            c = Connector(project=add_project, insert_DTR=add_insert_dtr, connector_manu=add_manufacturer,
                          connector_manu_num=add_insert_manu_nr, connector_family=add_connector_family,
                          insert_gender=add_gender)
            c.save()
            t = Terminal(project=add_project, DTR=add_terminal, connector_family=add_connector_family,
                       cross_section_min=add_min_crosssection, cross_section_max=add_max_crosssection,
                       plating=add_plating, gender=add_gender, manufacturer=add_manufacturer,
                       manuf_number=add_insert_manu_nr, insert_DTR=add_insert_dtr)
            t.save()
            return redirect('/terminal_selector/add_success')
    return render(request, 'add_terminal.html', {'form_add': form_add})


def search_terminal(request):
    global wire_cross_section
    form = SearchTerminal()
    if request.method == 'POST':
        form = SearchTerminal(request.POST)
        if form.is_valid():
            print(f"wire DTR: {request.POST['wire_dtr']}, insert DTR:  {request.POST['insert_dtr']}")
            wire_dtr = form.cleaned_data['wire_dtr']
            insert_dtr = form.cleaned_data['insert_dtr']
            print(insert_dtr)
            insert_exist_indb = Connector.objects.filter(insert_DTR=insert_dtr).exists()
            project = form.cleaned_data['project']
            if insert_exist_indb == True:
                insert_gender = Connector.objects.filter(insert_DTR__iexact=insert_dtr).values_list('insert_gender', flat=True)[0]
                wire_cross_section = Wires.objects.filter(wire__iexact=wire_dtr).values_list('wire_cross_section', flat=True)[0]
                terminal_dtr = Terminal.objects.filter(insert_DTR__contains=insert_dtr,
                                                       cross_section_min__lte=wire_cross_section,
                                                       cross_section_max__gte=wire_cross_section,
                                                       gender__iexact=insert_gender,
                                                       project__iexact=project).values_list('DTR', flat=True)
                terminal_pn = Terminal.objects.filter(insert_DTR__contains=insert_dtr,
                                                      cross_section_min__lte=wire_cross_section,
                                                      cross_section_max__gte=wire_cross_section,
                                                      gender__iexact=insert_gender,
                                                      project__iexact=project).values_list('manuf_number', flat=True)

                print(wire_cross_section, terminal_dtr)
                terminal_dict = dict(zip(terminal_dtr, terminal_pn))
                request.session['terminals'] = terminal_dict
                print(terminal_dict)
                return redirect('/terminal_selector/terminals')
            else:
                return redirect('/terminal_selector/no_insert')
        else:
            form = SearchTerminal()
            print(f"Form Errors: {form.is_valid} \n {form.errors}")
    return render(request, 'search_terminal.html', {'form': form})


def terminals(request):
    context = {}
    context['terminals'] = request.session.get('terminals')
    print(context)
    return render(request, 'terminals.html', context)

def no_insert(request):
    return render(request, 'no_insert.html')


def add_success(request):
    return render(request, 'add_success.html')


def list_all_inserts(request):
    context = {}
    connector_dict = {}
    connectors = list(Connector.objects.all().values_list('insert_DTR', flat=True))
    i = 0
    for item in connectors:
        connector_dict[i] = item
        i += 1
    context['connector_dict'] = connector_dict
    print(context)
    return render(request, 'list_all_inserts.html', context)


def about(request):
    return render(request, 'about.html')
