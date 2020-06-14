"""
n]:
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def build(app):
    box = toga.Box()
    name_label = toga.Label('Name:')
    name_input = toga.TextInput()
    salute_label = toga.Label("")

    def button_handler(widget):
        salute_label.text = "Hello {}!".format(name_input.value)

    button = toga.Button('Salute', on_press=button_handler)
    button.style.padding = 20
    button.style.flex = 1
    name_label.style.update(width=100, padding_left=10)
    name_input.style.update(width=100, padding_top=10, padding_left=10)
    salute_label.style.update(width=100, padding_top=10, padding_left=10)
    box.add(name_label)
    box.add(name_input)
    box.add(salute_label)
    box.add(button)
    box.style.update(direction=COLUMN, width=100, padding_top=10)
    return box


def main():
    return toga.App('Assistant Boots', 'org.pybee.salute', startup=build)


if __name__ == '__main__':
    main().main_loop()
