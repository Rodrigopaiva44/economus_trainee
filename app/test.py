import PySimpleGUI as sg
import in_out_plot
import cash_flow_plot


def app():
    # PySimpleGUI GUI interface
    layout = [
        [sg.Canvas(size=(100, 100), key='-CANVAS-')],
        [sg.Button('Exit'), sg.Button("Entrada/Saida"), sg.Button("Capital")]
    ]

    window = sg.Window('Pet Shop', layout, finalize=True)

    # Event loop for the GUI
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == "Entrada/Saida":
            in_out_plot.create_in_out_plot()
        if event == "Capital":
            cash_flow_plot.create_cash_flow_plot()
    window.close()


if __name__ == "__main__":
    app()
