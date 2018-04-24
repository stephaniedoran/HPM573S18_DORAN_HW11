#Perform economic evaluation using cost-utility analysis with discount rate 3%. Assume that:
#- The utility of being in state “Well” is 1, in state “Stroke” is 0.2, and in state “Post-Stroke”
# is 0.9.
#- The annual cost of being in “Post-Stroke” is $200 and when anticoagulation is used, this cost
#increases to $750.
#- Stoke results in a one-time cost of $5,000.
# Note: Since the cycle length for this problem will be quite small, we don’t need to
#  perform half-cycle correction.

import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov

# create and cohort
cohort_anticoag = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs_anticoag = cohort_anticoag.simulate()

cohort_none = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)

simOutputs_none = cohort_none.simulate()


SupportMarkov.report_CEA_CBA(simOutputs_none=simOutputs_none, simOutputs_anticoag=simOutputs_anticoag)
