import ccm  
import random    
log=ccm.log(html=True)   

class Subway(ccm.Model):        # items in the environment look and act like chunks - but note the syntactic differences
    step1=ccm.Model(isa='3',peg='A')
    step2=ccm.Model(isa='2',peg='A')
    step3=ccm.Model(isa='3',peg='C')
    step4=ccm.Model(isa='1',peg='A')
    step5=ccm.Model(isa='3',peg='B')
    step6=ccm.Model(isa='2',peg='B')
    final=ccm.Model(isa='3',peg='A')



class MotorModule(ccm.Model):     # create a motor module do the actions 
    def do_step1(self):          
        yield 2                   
        self.parent.parent.step1.peg='C'
	print "Disk ", self.parent.parent.step1.isa ,"was moved to peg", self.parent.parent.step1.peg
    def do_step2(self):          
        yield 2                   
        self.parent.parent.step2.peg='B'
	print "Disk ", self.parent.parent.step2.isa ,"was moved to peg", self.parent.parent.step2.peg
    def do_step3(self):          
        yield 2                   
        self.parent.parent.step3.peg='B'
	print "Disk ", self.parent.parent.step3.isa ,"was moved to peg", self.parent.parent.step3.peg
    def do_step4(self):          
        yield 2                   
        self.parent.parent.step4.peg='C'
	print "Disk ", self.parent.parent.step4.isa ,"was moved to peg", self.parent.parent.step4.peg
    def do_step5(self):          
        yield 2                   
        self.parent.parent.step5.peg='A'
	print "Disk ", self.parent.parent.step5.isa ,"was moved to peg", self.parent.parent.step5.peg
    def do_step6(self):          
        yield 2                   
        self.parent.parent.step6.peg='C'
	print "Disk ", self.parent.parent.step6.isa ,"was moved to peg", self.parent.parent.step6.peg
    def do_final(self):          
        yield 2                   
        self.parent.parent.final.peg='C'
	print "Disk ", self.parent.parent.final.isa ,"was moved to peg", self.parent.parent.final.peg



from ccm.lib.actr import *        
class MyAgent(ACTR):    
    focus=Buffer()
    motor=MotorModule()

    def init():
        focus.set('hanoi step1')

    def step1(focus='hanoi step1'):
        print "Peg A has disks [1,2], peg B has disks [], peg C has disks [3]."
        focus.set('hanoi step2')
        motor.do_step1()                 

    def step2(focus='hanoi step2', step1='peg:C'):   
        print "Peg A has disks [1], peg B has disks [2], peg C has disks [3]."                                     
        focus.set('hanoi step3')                                     
        motor.do_step2()                                             

    def step3(focus='hanoi step3', step2='peg:B'):       
        print "Peg A has disks [1], peg B has disks [2, 3], peg C has disks []."
        focus.set('hanoi step4')
        motor.do_step3()

    def step4(focus='hanoi step4', step3='peg:B'):        
        print "Peg A has disks [], peg B has disks [2, 3], peg C has disks [1]."
        focus.set('hanoi step5')
        motor.do_step4()

    def step5(focus='hanoi step5', step4='peg:C'):        
        print "Peg A has disks [3], peg B has disks [2], peg C has disks [1]."
        focus.set('hanoi step6')
        motor.do_step5()

    def step6(focus='hanoi step6', step5='peg:A'):        
        print "Peg A has disks [3], peg B has disks [], peg C has disks [1,2]."
        focus.set('hanoi final')
        motor.do_step6()

    def final(focus='hanoi final', step6='peg:C'):        
        print "Peg A has disks [], peg B has disks [], peg C has disks [1,2,3]."
        focus.set('hanoi stop')
        motor.do_final()

    def stop_production(focus='hanoi stop', final='peg:C'):
        self.stop()


tim=MyAgent()
env=Subway()
env.agent=tim 
ccm.log_everything(env)

env.run()
ccm.finished()
