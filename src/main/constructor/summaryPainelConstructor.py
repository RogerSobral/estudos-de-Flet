from src.views.summaryPainelView import SummaryPainelView
from src.controllers.summaryPanelController import SummaryPanelController
from src.views.cardIncomeView import CardIncomeView

def summaryPanelConstructor():
    summaryPanel=SummaryPainelView()
    cardIncomePainel=CardIncomeView()
    summaryController=SummaryPanelController(summaryPanel,cardIncomePainel)
    return summaryController