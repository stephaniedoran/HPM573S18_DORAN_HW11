# Find the transition matrix when anticoagulation is used.
# Assume that the anticoagulation reduces the rate of stroke events
# while in “Post-Stroke” by 25% but increases the rate of non-stroke
# related mortality by 5%.

import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create and cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)

simOutputs = cohort.simulate()

print(P.calculate_prob_matrix_anticoag())
