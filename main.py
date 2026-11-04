import logging


# from file_helper.printer import print_message ,Show_all_teamsw
# from file_helper.data_acquisition import chooce_search ,Valid_id_check,add_match_result,add_team,checking_whether_the_teams_have_already_played,duplicate_id_check,duplicate_name_check,update_group_based_on_match_result,Valid_name_check
import file_helper as fh


def main():
    val = fh.chooce_search() 

    if val == "1":
        id, name = fh.add_team()

        valid_id = fh.Valid_id_check(id)
        valid_name = fh.Valid_name_check(name)
        unique_id = fh.duplicate_id_check(id, teams)
        unique_name = fh.duplicate_name_check(name, teams)
        if valid_id == True and valid_name == True and unique_id == True and unique_name == True:
            teams.append({"id":id, "name":name, "plaied": 0,
                "Wins": 0, "Draws": 0, "Losses": 0,
                "Goals_for": 0, "Goals_against": 0, "Points": 0})
            mes = "Group added successfully"
            fh.print_message(mes)

            logging.info(f"group added, id: {id}, name: {name}")
        else:
            logging.error("Attempt to add a group failed")

    elif val == "2":
        fh.Show_all_teamsw(teams)
        logging.info("Show all teams")

    elif val == "3":
        try:
            home_team_id, away_taem_id, home_goals, awey_gowls = fh.data_acquisition.add_match_result(matches)
            matches.append({"home_team_id":home_team_id,
                            "away_taem_id":away_taem_id,
                            "home_goals":home_goals,
                            "awey_gowles": awey_gowls
                            })
            mes = "Game added successfully"
            fh.print_message(mes)
            logging.info("Game added successfully")
            fh.update_group_based_on_match_result(home_team_id, away_taem_id, home_goals, awey_gowls, teams)
            logging.info("The groups were successfully updated after the game.")
        except:
            mes = "Adding the game failed"
            fh.printer(mes)


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
        mes = "Exiting the program."
        fh.print_message(mes)
        return

teams = [{"id":1, "name":"Maccabi", "plaied": 0,
    "Wins": 0, "Draws": 0, "Losses": 0,
    "Goals_for": 0, "Goals_against": 0, "Points": 0}]

matches = [{"home_team_id":1, "away_taem_id":2,
            "home_goals":3, "awey_gowles": 1}]


if __name__ == "__main__":
    main()