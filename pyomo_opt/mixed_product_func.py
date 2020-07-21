import sys
try:
    from pyomo.environ import *
except ModuleNotFoundError as e:
    print("##### pip install pyomo #####")
    sys.exit()

from IPython import embed as II
from pyomo.environ import *

model = AbstractModel(name="Mixed Product Strategy")

model.indexSet = RangeSet(0, 1)
# Decision Variables
model.x = Var(model.indexSet, domain=NonNegativeReals)
# Parameters
model.price = Param(model.indexSet)

model.labor_bounds = Param(model.indexSet)
model.labor_coefs = Param(model.indexSet, model.indexSet)
model.demand_bounds = Param(model.indexSet)

def ProfitFunction(model):  # Objective Function
    return sum(model.price[i] * model.x[i] for i in model.indexSet)
model.objective = Objective(rule=ProfitFunction, sense=maximize)

def Pfunc2(model):
    return sum(model.x[i] for i in model.indexSet)
    
def DemandConstraint(model, var_id):
    return model.x[var_id] <= model.demand_bounds[var_id]
model.demand_x = Constraint(model.indexSet, rule=DemandConstraint)

def LaborConstraint(model, con_id):
    return sum(model.labor_coefs[con_id, i] * model.x[i] for i in model.indexSet) <= model.labor_bounds[con_id]
model.labor_con = Constraint(model.indexSet, rule=LaborConstraint)

model.dual = Suffix(direction=Suffix.IMPORT_EXPORT)
model.slack = Suffix(direction=Suffix.IMPORT_EXPORT)

instance = model.create_instance("mixed_product.dat") # load data
opt = SolverFactory("gurobi") # create solver interface
results = opt.solve(instance, tee = False)
instance.pprint()
II()
# Print results
print(f"Profit = ${instance.objective():.2f}")
print(f"X units = {instance.x[0].value:.0f}")
print(f"Y units = {instance.x[1].value:.0f}")
