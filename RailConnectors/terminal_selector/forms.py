from django import forms
choices_cross_section = (
            ('0.14','0.14'),
            ('0.34','0.34'),
            ('0.5','0.5'),
            ('0.75','0.75'),
            ('1','1'),
            ('1.5','1.5'),
            ('2.5', '2.5'),
            ('4', '4'),
            ('6', '6'),
            ('10', '10'),
            ('16', '16'),
            ('25', '25'),
            ('35', '35'),
            ('50', '50'),
            ('70', '70'),
            ('95', '95'),
            ('120', '120'),
        )
projects = (
    ('Main PPL', 'Main PPL'),
    ('SAV', 'SAV')
)
gender = (
            ('male', 'male'),
            ('female', 'female')
         )


plating = (
    ('silver', 'silver'),
    ('gold', 'gold'),
    ('zinc', 'zinc'),
)

class SearchTerminal(forms.Form):
    project = forms.ChoiceField(choices=projects)
    insert_dtr = forms.CharField(label='Insert DTR', max_length=30)
    wire_dtr = forms.CharField(label='Wire DTR', max_length=30, required=False)
    #wire_cross_section = forms.ChoiceField(required=False, choices=choices_cross_section)

class AddToDb(forms.Form):
    add_insert = forms.CharField(label='Insert DTR', max_length=30)
    add_manufacturer = forms.CharField(label='Manufacturer', max_length=30)
    add_insert_manu_number = forms.CharField(label='Insert manufacturer number', max_length=30)
    add_gender = forms.ChoiceField( label='Gender', choices=gender)
    add_terminal = forms.CharField(label='Terminal DTR', max_length=30)
    add_connector_family = forms.CharField(label='Connector family' ,required=False, max_length=30)
    add_project = forms.ChoiceField(label='Project', required=True, choices=projects)
    add_min_cross_section = forms.CharField(label='Minimal cross section', max_length=30)
    add_max_cross_section = forms.CharField(label='Maximal cross section', max_length=30)
    add_plating = forms.ChoiceField(label='Plating', choices=plating)
    add_terminal_manu_number = forms.CharField(label='Terminal manufacturer number', max_length=30)