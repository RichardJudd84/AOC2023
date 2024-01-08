import re
import queue
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

####################################### part 1 #######################################

# broadcast module includes button  
class Module:
    broadcaster: 'Module' = None
    pulseQue = queue.Queue()
    modulesDict: {str: 'Module'} = {}
    LowPulses = 0
    HighPulses = 0

    def __init__(self, id:str, destinationModuleIds: [str]) -> None:
        self.id = id
        self.state = False
        self.destinationModules: {'Module': bool} = dict()
        self.nextPulse = queue.Queue()
        self.destinationModuleIds = destinationModuleIds
        self.lastPulse = None        
        self.inputModules: ['Module'] = []

    def sendPulse(self, pulse = None):
        if pulse == None and not self.nextPulse.empty():
            pulse, sendingModule = self.nextPulse.get()
            sendingModule.pulseConfirmation(self)
            if pulse == None:
                return
        self.lastPulse = pulse 
       
        for module in self.destinationModules:
            self.destinationModules[module] = False
            module.receivePulse(pulse, self)
            Module.pulseQue.put(module)
            #print(self.id, pulse, module.id) 
            if pulse:
                Module.HighPulses += 1
            else:
                Module.LowPulses +=1

    def receivePulse(self, pulse:bool, sendingModule: 'Module'):
        self.nextPulse.put((pulse, sendingModule))
    

    
    def pulseConfirmation(self, receivingModule: 'Module'):
        self.destinationModules[receivingModule] = True

    @staticmethod
    def setup():
        Module.modulesDict['output'] = Module('output', [])
        Module.broadcaster = Module.modulesDict['broadcaster']
        for module in list(Module.modulesDict.values()).copy():
            for moduleKey in module.destinationModuleIds:
                if moduleKey not in Module.modulesDict:
                    Module.modulesDict[moduleKey] = Module(moduleKey, []) 

        for module in Module.modulesDict.values():
            for moduleKey in module.destinationModuleIds:
                if moduleKey not in Module.modulesDict:
                    Module.modulesDict[moduleKey] = Module(moduleKey, [])

            module.destinationModules = {Module.modulesDict[key]: True for key in module.destinationModuleIds}
            for destinationModule in module.destinationModules:
                destinationModule.inputModules.append(module)

    @staticmethod
    def pressButton():
        Module.broadcaster.sendPulse(False)
        Module.LowPulses += 1

# %
class FlipFlopModule(Module):

    def receivePulse(self, pulse:bool, sendingModule: 'Module'):
        if pulse:
            pulse = None
        else: 
            self.state = not self.state
            pulse = self.state

        self.nextPulse.put((pulse, sendingModule))


# &
class ConjunctionModule(Module):
    def receivePulse(self, pulse:bool, sendingModule: 'Module'):
        allHigh = True
        for module in self.inputModules:
            if not module.lastPulse:
                allHigh = False

        if allHigh:
            pulse = False
        else:
            pulse = True

        self.nextPulse.put((pulse, sendingModule))



for line in res:
    moduleType, destinationModules = line.strip().split('->')
    destinationModules = re.findall('\w+',destinationModules)
    moduleType = moduleType.strip()
    if '%' in moduleType:
        moduleType = moduleType[1:] 
        module = FlipFlopModule(moduleType, destinationModules)
    elif '&' in moduleType:
        moduleType = moduleType[1:] 
        module = ConjunctionModule(moduleType, destinationModules)

    else:
        module = FlipFlopModule(moduleType, destinationModules)

    Module.modulesDict[moduleType] = module

Module.setup()




for r in range(1000):
    Module.pressButton()
    while not Module.pulseQue.empty():
        module = Module.pulseQue.get()
        module.sendPulse()
    #input()

print(Module.LowPulses* Module.HighPulses)





