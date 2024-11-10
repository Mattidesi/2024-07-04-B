import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDYears(self):
        years = self._model.getYears()

        for year in years:
            self._view.ddyear.options.append(ft.dropdown.Option(year))

        self._view.update_page()

    def fillDDStates(self,e):
        self._view.ddstate.options.clear()
        states = self._model.getStates(self._view.ddyear.value)

        for state in states:
            self._view.ddstate.options.append(ft.dropdown.Option(state))

        self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result1.controls.clear()
        if self._view.ddyear.value is None or self._view.ddstate.value is None:
            self._view.txt_result1.controls.append(ft.Text("Inserisci uno stato e un anno!", color='red'))
            self._view.update_page()
            return
        self._model.buildGraph(self._view.ddyear.value, self._view.ddstate.value)
        nNodes, nEdges = self._model.getGraphDetails()
        nConn = self._model.getNumConnesse()
        maxConn = self._model.largestConnessa()

        self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {nNodes}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {nEdges}"))
        self._view.txt_result1.controls.append(ft.Text(f"il grafo ha: {nConn} componenti connesse"))
        self._view.txt_result1.controls.append(ft.Text(f"La componente connessa più grande è costituita da {len(maxConn)} nodi:"))
        self._view.update_page()

        for e in maxConn:
            self._view.txt_result1.controls.append(ft.Text(e))
            self._view.update_page()

    def handle_path(self, e):
        pass
