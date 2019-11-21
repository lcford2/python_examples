import sys
try:
    from pyomo.environ import *
except ModuleNotFoundError as e:
    print("##### pip install pyomo #####")
    sys.exit()

model = ConcreteModel(name="Mixed Product Strategy")

model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)


model.objective = Objective(
    expr=40 * model.x + 30 * model.y,
    sense=maximize
)

model.demand_x = Constraint(expr=model.x <= 40)
model.laborA_con = Constraint(expr=model.x + model.y <= 80)
model.laborB_con = Constraint(expr=2 * model.x + model.y <= 100)

solution = SolverFactory("gurobi").solve(model)
model.pprint()

print(f"Profit = ${model.objective():.2f}")
print(f"X units = {model.x():.0f}")
print(f"Y units = {model.y():.0f}")
