# coding: utf-8

import numpy as np
from SGA.family import Family
from SGA.configure import ParamsSGA, ObjectiveFunc
from SGA.tournament import Tournament
# from SGA.cp_tournament import Tournament


def leaders_indices(f, sga, tournament):
    indices = np.transpose(np.arange(0, f.search_group.size, 1))
    tournament_indices = tournament.tournament()
    tournament_indices = np.sort(tournament_indices)
    indices[np.arange(sga.elite, f.search_group.size)] = tournament_indices
    return indices


def run(sga=None, fobj=None):
    if not sga:
        sga = ParamsSGA()
    if not fobj:
        fobj = ObjectiveFunc()
    f = Family(sga, fobj)
    n_pertubed = int(f.search_group.size - sga.elite)
    tournament = Tournament(f.population.size, n_pertubed, sga.TournamentSize)
    rtournament = Tournament(f.search_group.size, sga.NPerturbed, sga.TournamentSize)
    f.update_leaders(leaders_indices(f, sga, tournament))
    iteration_data = np.zeros((sga.NIterations, f.dim + 1))

    for k in range(sga.NIterationsGlobal):
        perturbed_indices = rtournament.reverse_tournament()
        f.mutate_leaders(perturbed_indices)
        f.generation(sga.alfa(fobj.inf, fobj.sup))
        f.sort_leaders()
        iteration_data[k] = f.leaders[0]
        sga.update_iterarion()

    sga.alfa_local = True
    sga.current_iteration = 0

    for k in range(sga.NIterationsLocal):
        perturbed_indices = rtournament.reverse_tournament()
        f.mutate_leaders(perturbed_indices)
        f.local_generation(sga.alfa(fobj.inf, fobj.sup))
        f.sort_database()
        iteration_data[sga.NIterationsGlobal + k] = f.database[0]
        f.update_leaders(leaders_indices(f, sga, tournament))
        sga.update_iterarion()

    x = iteration_data[-1, 1:]
    y = iteration_data[-1, 0]
    return x, y


if __name__ == '__main__':
    x, y = run()
    print(x, y)
