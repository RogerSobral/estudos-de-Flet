from src.views.cardIncomeView import CardIncomeView
from src.views.summaryPainelView import SummaryPainelView
class SummaryPanelController:

    def __init__(self,summaryPanelView:SummaryPainelView,cardIncome:CardIncomeView):
        self.summaryPanel=summaryPanelView
        self.cardIncome=cardIncome
        #verificar os eventos e pegar o icone receita
        self.summaryPanel.iconReceita.on_click=self.openCardIncome


    def openCardIncome(self,e):
        self.cardIncome.open=True
        self.cardIncome.update()
