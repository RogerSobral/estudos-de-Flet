from src.views.summaryPainelView import SummaryPainelView
from src.controllers.summaryPanelController import SummaryPanelController
def summaryPanelConstructor():
    summaryPanel=SummaryPainelView()
    summaryController=SummaryPanelController(summaryPanel)
    return summaryPanel