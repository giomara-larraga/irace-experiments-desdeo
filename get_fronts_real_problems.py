from CarSideImpact import car_side_impact
from desdeo_problem.testproblems.MultipleClutchBrakes import multiple_clutch_brakes
from desdeo_problem.testproblems.RiverPollution import river_pollution_problem
from desdeo_problem.testproblems.VehicleCrashworthiness import vehicle_crashworthiness

from desdeo_emo.EAs.IBEA import IBEA
from desdeo_emo.EAs.AutoNSGAIII import AutoNSGAIII


problems = [car_side_impact(), multiple_clutch_brakes(), river_pollution_problem(), vehicle_crashworthiness()]
objectiver = [3, 3, 4, 4]
#algorithms = [IBEA, RVEA]

def compute_front (problem):
    evolver = IBEA(
    problem,
    n_iterations=1,
    n_gen_per_iter=300,
    population_size=100,
    )
    evolver.start()
    while evolver.continue_evolution():
        evolver.iterate()
        print(f"Running iteration {evolver._iteration_counter}")
    #print(f"Number of non-dominated solutions: {len(evolver.non_dominated['objectives'])}")

    #pref, plot = evolver.iterate(pref)


    # obj = evolver.non_dominated["objectives"]
    _, obj, _ = evolver.end()
    #print(objective_values)
    # show some of the ibea pop somehow
    print("IBEA ideal",evolver.population.problem.ideal)
    return 0


if __name__== "__main__":
    compute_front(problems[3])
