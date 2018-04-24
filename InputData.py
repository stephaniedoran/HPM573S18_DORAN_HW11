POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

ADD_BACKGROUND_MORT = True  # if background mortality should be added

# transition matrix
TRANS_MATRIX = [
    [0.7324,  0.15,   0.0,    0.1,   0.0176],   # Well
    [0,     0.0,    1.0,    0.0,     0.0],      # Stroke
    [0,     0.25,   0.5324,   0.2,     0.0176],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0,     0.0],   # Stroke Dead
    [0.0,   0.0,    0.0,    0.0,     1.0],   # Background Dead
    ]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0  # dead
]

HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0
]

#  annual drug cost
Anticoag_COST = 2000

# annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 17.638 / 1000
