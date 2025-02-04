import PySimpleGUI as sg

layout = [
    [sg.Text('Vælg imellem BMI udregner eller arbejdstid')],
    [sg.Button('BMI'), sg.Button('Arbejdstid')]
]

window = sg.Window('Startside', layout)

event, values = window.read()

if event == 'BMI':
    window.close()
    layout = [
        [sg.Text('BMI udregner')],
        [sg.Text('Indtast din højde i meter')],
        [sg.Input('', key='input_højde')],
        [sg.Text('Indtast din vægt i kilogram')],
        [sg.Input('', key='input_vægt')],
        [sg.Button('Udregn BMI')],
    ]
    window = sg.Window('BMIudregner', layout)

    event, values = window.read()
    if event == 'Udregn BMI':
        window.close()

        try:
            højde = float(values['input_højde'])
            vægt = float(values['input_vægt'])
            højde_i_anden = højde * højde
            BMI = vægt / højde_i_anden
        except:
            BMI = 'ugyldig value'

        layout = [
            [sg.Text(f'Din BMI er: {BMI}')],
            [sg.Button('OK')],
        ]
        window = sg.Window('BMIudregner', layout)
        event, values = window.read()
        if event == 'OK':
            window.close()




if event == 'Arbejdstid':
    window.close()
    layout = [
        [sg.Text('Indtast mødetid(i timer og minutter): ')],
        [sg.Input('', key='input_mødetid_t'), sg.Input('', key='input_mødetid_m')],
        [sg.Text('Indtast afgangstid(i timer og minutter): ')],
        [sg.Input('', key='input_afgangstid_t'), sg.Input('', key='input_afgangstid_m'),],
        [sg.Button('Udregn arbejdstid'), sg.Button('Exit')]
    ]

    window = sg.Window('Calculate celcius to fahrenheit', layout)

    event, values = window.read()

    if event == 'Udregn arbejdstid':
        window.close()

        try:
            mødetid_t = int(values['input_mødetid_t'])
            mødetid_m = int(values['input_mødetid_m'])
            afgangstid_t = int(values['input_afgangstid_t'])
            afgangstid_m = int(values['input_afgangstid_m'])

            # fejlsafe
            if mødetid_t < 0 or mødetid_t > 23:
                print("ugyldigt tal, skal være imellem 0 og 23")

            # fejlsafe
            if mødetid_m < 0 or mødetid_m > 59:
                print("ugyldigt tal, skal være imellem 0 og 59")

            # fejlsafe
            if afgangstid_t < 0 or afgangstid_t > 23:
                print("ugyldigt tal, skal være mellem 0 og 23")

            # fejlsafe
            if afgangstid_m < 0 or afgangstid_m > 59:
                print("ugyldigt tal, skal være imellem 0 og 59")

            arbejdstid_t = afgangstid_t - mødetid_t
            arbejdstid_m = afgangstid_m - mødetid_m

            if arbejdstid_t < 0:
                arbejdstid_t -= 1
                arbejdstid_m += 60

            if arbejdstid_m > 59:
                arbejdstid_t += 1
                arbejdstid_m -= 60

            if arbejdstid_m < 0:
                arbejdstid_t -= 1
                arbejdstid_m += 60

        except:
            arbejdstid = 'ugyldig value'

        layout = [
            [sg.Text(f'Du har arbejdet i: {arbejdstid_t}:{arbejdstid_m} timer')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Arbejdstid', layout)
        event, values = window.read()

    window.close()


    if event == 'Exit':
        window.close()