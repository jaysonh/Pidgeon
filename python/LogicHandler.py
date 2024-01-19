import json

from jsonLogic import *
#from json_logic import jsonLogic
from LogicUnit import *
from JsonParams import *
class LogicHandler:
    def __init__(self, json_data : JsonParams):

        self.scheduler = BackgroundScheduler()
        for json_rule in json_data.getJson():
            logic = LogicUnit(json_rule)
            logic.add_cron( self.scheduler )

        rules = { "and" : [
            {"<" : [ { "var" : "temp" }, 110 ]},
            {"==" : [ { "var" : "pie.filling" }, "apple" ] }
        ] }

        data = { "temp" : 100, "pie" : { "filling" : "apple" } }

        # save json rules to file
        with open('../data/config/logicSave.json', 'w') as outfile:
            json.dump(rules, outfile)
    
        result = jsonLogic(rules, data)

        logger.info(f"logic result: f{result}" )
        