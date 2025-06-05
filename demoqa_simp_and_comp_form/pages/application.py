from demoqa_simp_and_comp_form.pages.simple_page import SimlePage
from demoqa_simp_and_comp_form.pages.complex_page import ComplexPage


class Applecation:
    def __init__(self):
        self.simple_app = SimlePage()
        self.complex_page = ComplexPage()


app = Applecation()
