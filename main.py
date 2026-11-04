import json
import logging
import file_helper as fh


def main():
    while True:
        val = fh.chooce_search() 

        if val == "1":
            id, name = fh.add_team()

            valid_id = fh.valid_id_check(id)
            valid_name = fh.valid_name_check(name)
            unique_id = fh.duplicate_id_check(id, teams)
            unique_name = fh.duplicate_name_check(name, teams)
            if valid_id == True and valid_name == True and unique_id == True and unique_name == True:
                teams.append({"id":id, "name":name, "plaied": 0,
                    "wins": 0, "draws": 0, "losses": 0,
                    "goals_for": 0, "goals_against": 0, "points": 0})
                mes = "Group added successfully"
                fh.print_message(mes)
                logging.info(f"group added, id: {id}, name: {name}")
            else:
                mes = "Attempt to add a group failed"
                fh.print_message(mes)
                logging.error(mes)
                continue

        elif val == "2":
            fh.print_message(teams)
            logging.info("Show all teams")
            continue

        elif val == "3":
            try:
                home_team_id, away_taem_id, home_goals, awey_gowls = fh.add_match_result(matches)
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
                fh.print_message(mes)
                logging.error(mes)
                continue

        elif val == "4":
            try:
                result = fh.show_standings(teams)
                fh.print_message(result)
                logging.info("Showed standings")
                continue
            except:
                mes = "Showed standings was failed"
                fh.print_message(mes)
                logging.error(mes)
                continue

        elif val == "5":
            try:
                result = fh.show_standings(teams)
                result = result[0]
                fh.print_message(result)
                logging.info("showed standings")
                continue
            except:
                mes = "showed standings pyled"
                logging.error(mes)
                continue



        elif val == "6":
            try:
                best_attacking_team = fh.show_best_attacking_team(teams)
                fh.print_message(best_attacking_team)
                logging.info("showed best")
                continue
            except:
                mes = "showed best was failed"
                fh.print_message(mes)
                logging.error(mes)
                continue

        
        
        elif val == "7":  
            try:  
                result = fh.show_team_success_rate(teams)
                fh.print_message(result)
                logging.info("show team success rate")
                continue
            except:
                mes = "show team success rate was failed"
                fh.print_message(mes)
                logging.error(mes)
                continue


        elif val == "8":
            try:
                result = fh.show_teams_without_wins(teams)
                if result == []:
                    result = "There is no team that hasn't won."
                fh.print_message(result)
                logging.info("show teams without wins")
                continue
            except:
                mes = "show teams without wins was failed"
                fh.print_message(mes)
                logging.error(mes)


        elif val == "9":
            try:
                result = fh.show_tournament_summary(teams, matches)
                fh.print_message(result)
                logging.info("show tournament summary")
                continue
            except:
                mes = "show tournament summary was failed"
                fh.print_message(mes)




        elif val == "0":
            mes = "Exiting the program, Goodbye!"
            fh.print_message(mes)
            break

teams = [
    {"id": 1, "name": "Hapoel Hadera", "played": 28, "wins": 28, "draws": 0, "losses": 0, "goals_for": 46, "goals_against": 0, "points": 84},
    {"id": 2, "name": "Hapoel Beer Sheva", "played": 28, "wins": 28, "draws": 0, "losses": 0, "goals_for": 31, "goals_against": 0, "points": 84},
    {"id": 3, "name": "Maccabi Tel Aviv", "played": 29, "wins": 26, "draws": 3, "losses": 0, "goals_for": 27, "goals_against": 1, "points": 81},
    {"id": 4, "name": "Maccabi Jaffa", "played": 27, "wins": 19, "draws": 7, "losses": 1, "goals_for": 31, "goals_against": 5, "points": 64},
    {"id": 5, "name": "Hapoel Petah Tikva", "played": 25, "wins": 20, "draws": 4, "losses": 1, "goals_for": 25, "goals_against": 2, "points": 64},
    {"id": 6, "name": "Maccabi Petah Tikva", "played": 21, "wins": 21, "draws": 0, "losses": 0, "goals_for": 57, "goals_against": 0, "points": 63},
    {"id": 7, "name": "Bnei Yehuda", "played": 24, "wins": 20, "draws": 3, "losses": 1, "goals_for": 39, "goals_against": 4, "points": 63},
    {"id": 8, "name": "Maccabi Netanya", "played": 29, "wins": 17, "draws": 10, "losses": 2, "goals_for": 57, "goals_against": 8, "points": 61},
    {"id": 9, "name": "Bnei Sakhnin", "played": 21, "wins": 15, "draws": 2, "losses": 4, "goals_for": 34, "goals_against": 11, "points": 47},
    {"id": 10, "name": "F.C. Ashdod", "played": 25, "wins": 15, "draws": 1, "losses": 9, "goals_for": 39, "goals_against": 13, "points": 46},
    {"id": 11, "name": "Hapoel Ramat Gan", "played": 23, "wins": 11, "draws": 11, "losses": 1, "goals_for": 43, "goals_against": 9, "points": 44},
    {"id": 12, "name": "Maccabi Haifa", "played": 26, "wins": 10, "draws": 14, "losses": 2, "goals_for": 18, "goals_against": 3, "points": 44},
    {"id": 13, "name": "Hapoel Kfar Saba", "played": 23, "wins": 11, "draws": 10, "losses": 2, "goals_for": 14, "goals_against": 6, "points": 43},
    {"id": 14, "name": "Hapoel Jerusalem", "played": 28, "wins": 10, "draws": 10, "losses": 8, "goals_for": 13, "goals_against": 23, "points": 40},
    {"id": 15, "name": "Hapoel Rishon LeZion", "played": 26, "wins": 12, "draws": 1, "losses": 13, "goals_for": 15, "goals_against": 27, "points": 37},
    {"id": 16, "name": "Maccabi Bnei Reineh", "played": 25, "wins": 11, "draws": 0, "losses": 14, "goals_for": 22, "goals_against": 38, "points": 33},
    {"id": 17, "name": "Beitar Jerusalem", "played": 23, "wins": 2, "draws": 21, "losses": 0, "goals_for": 18, "goals_against": 7, "points": 27},
    {"id": 18, "name": "Ironi Kiryat Shmona", "played": 26, "wins": 2, "draws": 19, "losses": 5, "goals_for": 14, "goals_against": 17, "points": 25},
    {"id": 19, "name": "Hapoel Tel Aviv", "played": 27, "wins": 2, "draws": 15, "losses": 10, "goals_for": 5, "goals_against": 45, "points": 21},
    {"id": 20, "name": "Hapoel Haifa", "played": 25, "wins": 2, "draws": 7, "losses": 16, "goals_for": 3, "goals_against": 54, "points": 13}
]


matches = [{"home_team_id":4, "away_taem_id":2, "home_goals":3, "awey_gowles": 1},
           {"home_team_id":2, "away_taem_id":1, "home_goals":5, "awey_gowles": 0}]


if __name__ == "__main__":
    main()        
    
    
    
    # elif val == "11":

    #             home_team_id ,away_taem_id, home_team_name, away_team_name, winer, points_home, points_away = fh.Show_standings(teams, matches)
    #             mes = "***** Game Results *****\n "