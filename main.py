import logging
from data_acquisition import add_team, chooce_search, Valid_id_check, Valid_name_check ,duplicate_id_check, duplicate_name_check, add_match_result, update_group_based_on_match_result
from printer import Show_all_teamsw


teams = [{"id":1, "name":"Maccabi", "plaied": 0,
    "Wins": 0, "Draws": 0, "Losses": 0,
    "Goals_for": 0, "Goals_against": 0, "Points": 0}]

matches = [{"home_team_id":1, "away_taem_id":2,
            "home_goals":3, "awey_gowles": 1}]


def main():
    val = choose_search() 

    if val == "1":
        id, name = add_team()

        valid_id = Valid_id_check(id)
        valid_name = Valid_name_check(name)
        unique_id = duplicate_id_check(id, teams)
        unique_name = duplicate_name_check(name, teams)
        if valid_id == True and valid_name == True and unique_id == True and unique_name == True:
            teams.append({"id":id, "name":name, "plaied": 0,
                "Wins": 0, "Draws": 0, "Losses": 0,
                "Goals_for": 0, "Goals_against": 0, "Points": 0})
            print(f"Group added successfully")
            logging.info(f"group added, id: {id}, name: {name}")
        else:
            logging.error("Attempt to add a group failed")

    elif val == "2":
        Show_all_teamsw(teams)
        logging.info("Show all teams")

    elif val == "3":
        try:
            home_team_id, away_taem_id, home_goals, awey_gowls = add_match_result()
            matches.append({"home_team_id":home_team_id,
                            "away_taem_id":away_taem_id,
                            "home_goals":home_goals,
                            "awey_gowles": awey_gowls
                            })
            print("Game added successfully")
            logging.info("Game added successfully")
            update_group_based_on_match_result(home_team_id, away_taem_id, home_goals, awey_gowls, teams)
            logging.info("The groups were successfully updated after the game.")
        except:
            print("Adding the game failed")

    elif val == "4":
        ...
    elif val == "5":
        ...
    elif val == "6":
        ...
    elif val == "7":
        ...
    elif val == "8":
        ...
    elif val == "9":
        ...
    elif val == "0":
        print("Exiting the program.")
        return
