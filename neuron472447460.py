'''
Defines a class, Neuron472447460, of neurons from Allen Brain Institute's model 472447460

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472447460:
    def __init__(self, name="Neuron472447460", x=0, y=0, z=0):
        '''Instantiate Neuron472447460.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472447460_instance is used instead
        '''
        
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Gad2-IRES-Cre_Ai14_IVSCC_-177637.02.02.01_475124390_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472447460_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 158.06
            sec.e_pas = -85.7733612061
        
        for sec in self.axon:
            sec.cm = 2.9
            sec.g_pas = 3.30198657744e-05
        for sec in self.dend:
            sec.cm = 2.9
            sec.g_pas = 9.02884734738e-06
        for sec in self.soma:
            sec.cm = 2.9
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 0.000457946
            sec.gbar_NaV = 0.111471
            sec.gbar_Kd = 0.00607458
            sec.gbar_Kv2like = 0.574798
            sec.gbar_Kv3_1 = 1.81329
            sec.gbar_K_T = 0.00295039
            sec.gbar_Im_v2 = 0.000832888
            sec.gbar_SK = 0
            sec.gbar_Ca_HVA = 9.00658e-05
            sec.gbar_Ca_LVA = 0.0059567
            sec.gamma_CaDynamics = 0.0220328
            sec.decay_CaDynamics = 188.134
            sec.g_pas = 4.70154e-05
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

