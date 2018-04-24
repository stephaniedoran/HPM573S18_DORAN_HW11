import math

# part 1
rate_stroke_mortality = -math.log(1-(36.2/100000))
rate_background_mortality = -math.log(1-(17.638/1000))
print('the rate of stroke associated mortality is', rate_stroke_mortality)
print('the rate of background mortality (not including stroke) is', rate_background_mortality)

#  part 2
rate_stroke = -math.log(1-(15/1000))
print('the rate of stroke events is', rate_stroke)

#  part 3
rate_well_to_stroke = 0.9*rate_stroke
rate_well_to_stroke_death = 0.1*rate_stroke
print('the rate of transition from well to stroke is', rate_well_to_stroke)
print('the rate of transition from well to stroke death is', rate_well_to_stroke_death)

#  part 4
rate_recurrent_stroke= 0.17*rate_well_to_stroke
print('the rate of recurrent stroke events is', rate_recurrent_stroke)

#  part 5
rate_post_stroke_to_stroke = 0.8*rate_recurrent_stroke
rate_post_stroke_to_stroke_death = 0.2*rate_recurrent_stroke
print('the rate of transition from post stroke to stroke is', rate_post_stroke_to_stroke)
print('the rate of transition from post stroke to stroke death is', rate_post_stroke_to_stroke_death)

#  part 6
rate_stroke_to_post_stroke = -(1/52)*math.log(1-(15/1000))
print('the rate of transition from stroke to post stroke is', rate_stroke_to_post_stroke)
