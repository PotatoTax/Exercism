def tally(rows):
    teams = {}
    for row in rows:
        a, b, result = row.split(";")
        if a not in teams:
            teams[a] = {"win": 0, "draw": 0, "loss": 0, "matches": 0, "points": 0}
        if b not in teams:
            teams[b] = {"win": 0, "draw": 0, "loss": 0, "matches": 0, "points": 0}
        teams[a]["matches"] += 1
        teams[b]["matches"] += 1
        if result == "win":
            teams[a]["win"] += 1
            teams[a]["points"] += 3
            teams[b]["loss"] += 1
        elif result == "loss":
            teams[b]["win"] += 1
            teams[b]["points"] += 3
            teams[a]["loss"] += 1
        else:
            teams[b]["draw"] += 1
            teams[a]["draw"] += 1
            teams[a]["points"] += 1
            teams[b]["points"] += 1

    result = ["Team                           | MP |  W |  D |  L |  P"]

    teams = {key: teams[key] for key in sorted(teams)}
    teams = {k: v for k, v in sorted(teams.items(), key=lambda x: x[1]["points"], reverse=True)}

    for team in teams:
        result.append(
            f"{team:<30} | "
            f"{teams[team]['matches']:>2} | "
            f"{teams[team]['win']:>2} | "
            f"{teams[team]['draw']:>2} | "
            f"{teams[team]['loss']:>2} | "
            f"{teams[team]['points']:>2}"
        )

    return result
