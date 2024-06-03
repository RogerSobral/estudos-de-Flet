from src.views.cardIncomeView import CardIncomeView
from src.views.summaryPainelView import SummaryPainelView
from src.main.constructor.cardIncomeConstructor import cardIncomeConstructor
class SummaryPanelController:

    def __init__(self,summaryPanelView:SummaryPainelView,cardIncome:CardIncomeView):
        self.summaryPanel=summaryPanelView
        self.cardIncome=cardIncome
        #verificar os eventos e pegar o icone receita
        self.summaryPanel.iconReceita.on_click=self.openCardIncome
        self.cardIncome.btnClose.on_click= self.closeCardIncome


    def openCardIncome(self,e):
        self.cardIncome.open=True
        self.cardIncome.update()

    def closeCardIncome(self,e):
        self.cardIncome.open = False
        self.cardIncome.update()
