def team_obj(team):
    return {
        "team_id": team.team_id,
        "name": team.name,
        "manager": team.manager,
        "captain": team.captain,
        "links": [
            {"rel": "self", "href": f"/teams/{team.team_id}"},
            {"rel": "players", "href": f"/teams/{team.team_id}/players"}
        ]
    }


def teams_obj(teams):
    teams_obj = []
    for team in teams:
        teams_obj.append(team_obj(team))
    return teams_obj
