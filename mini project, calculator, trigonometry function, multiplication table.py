from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math


# -----------------------------------------
# TRIGONOMETRY EXACT VALUES
# -----------------------------------------
exact_values = {
    "sin": {
        0: "0", 30: "1/2", 45: "1/√2", 60: "√3/2", 90: "1",
        180: "0", 360: "0"
    },
    "cos": {
        0: "1", 30: "√3/2", 45: "1/√2", 60: "1/2", 90: "0",
        180: "-1", 360: "1"
    },
    "tan": {
        0: "0", 30: "1/√3", 45: "1", 60: "√3", 90: "undefined",
        180: "0", 360: "0"
    }
}


# -----------------------------------------
# FUNCTION TO EVALUATE TRIGONOMETRY
# -----------------------------------------
def evaluate_trig(expr):
    expr = expr.strip().lower()

    func = expr.split("(")[0]
    angle = int(expr.split("(")[1][:-1])

    if func in exact_values and angle in exact_values[func]:
        return exact_values[func][angle]

    rad = math.radians(angle)

    if func == "sin":
        return math.sin(rad)
    elif func == "cos":
        return math.cos(rad)
    elif func == "tan":
        return math.tan(rad)
    else:
        return "Invalid function"


# -----------------------------------------
# SCREEN 1: CALCULATOR
# -----------------------------------------
class CalculatorScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.num1 = TextInput(hint_text="Enter number 1", multiline=False)
        self.num2 = TextInput(hint_text="Enter number 2", multiline=False)
        self.op = TextInput(hint_text="Enter operator (+, -, *, %)", multiline=False)

        self.output = Label(text="Result will appear here")

        btn = Button(text="Calculate", on_press=self.calculate)

        nav = Button(text="Go to Table Screen",
                     on_press=lambda x: setattr(self.manager, "current", "table"))

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)
        layout.add_widget(self.op)
        layout.add_widget(btn)
        layout.add_widget(self.output)
        layout.add_widget(nav)

        self.add_widget(layout)

    def calculate(self, instance):
        try:
            a = float(self.num1.text)
            b = float(self.num2.text)
            op = self.op.text

            if op == "+":
                self.output.text = f"Sum = {a + b}"
            elif op == "-":
                self.output.text = f"Difference = {a - b}"
            elif op == "*":
                self.output.text = f"Product = {a * b}"
            elif op == "%":
                self.output.text = f"Remainder = {a % b}"
            else:
                self.output.text = "Invalid operator!"

        except:
            self.output.text = "Error: Enter valid numbers"


# -----------------------------------------
# SCREEN 2: TABLE
# -----------------------------------------
class TableScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.num = TextInput(hint_text="Enter number", multiline=False)
        self.output = Label(text="Table will appear here")

        btn = Button(text="Show Table", on_press=self.show_table)

        nav = Button(text="Go to Trigonometry Screen",
                     on_press=lambda x: setattr(self.manager, "current", "trig"))

        layout.add_widget(self.num)
        layout.add_widget(btn)
        layout.add_widget(self.output)
        layout.add_widget(nav)

        self.add_widget(layout)

    def show_table(self, instance):
        try:
            n = int(self.num.text)
            table = ""

            for i in range(1, 11):
                table += f"{n} × {i} = {n * i}\n"

            self.output.text = table

        except:
            self.output.text = "Error: Enter a valid number"


# -----------------------------------------
# SCREEN 3: TRIGONOMETRY
# -----------------------------------------
class TrigScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.expr = TextInput(hint_text="Enter (ex: sin(30))", multiline=False)
        self.output = Label(text="Result will appear here")

        btn = Button(text="Solve", on_press=self.solve)

        nav = Button(text="Go to Calculator",
                     on_press=lambda x: setattr(self.manager, "current", "calc"))

        layout.add_widget(self.expr)
        layout.add_widget(btn)
        layout.add_widget(self.output)
        layout.add_widget(nav)

        self.add_widget(layout)

    def solve(self, instance):
        try:
            self.output.text = str(evaluate_trig(self.expr.text))
        except:
            self.output.text = "Invalid expression"


# -----------------------------------------
# MAIN APP / SCREEN MANAGER
# -----------------------------------------
class MyApp(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(CalculatorScreen(name="calc"))
        sm.add_widget(TableScreen(name="table"))
        sm.add_widget(TrigScreen(name="trig"))

        return sm


# -----------------------------------------
# RUN APP
# -----------------------------------------
MyApp().run()