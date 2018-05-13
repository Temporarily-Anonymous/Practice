state_need = set(["mt","wa","or","id","nv","ut","ca","az"])

stations = {}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])

final_stations = set()

while state_need:
    best_station = None
    states_coverd = set()
    for station, states_for_station in stations.items():
        coverd = state_need & states_for_station
        if len(coverd) > len(states_coverd):
            best_station = station
            states_coverd = coverd
    final_stations.add(best_station)
    state_need -= states_coverd

print (final_stations)