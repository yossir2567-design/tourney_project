from file_helper import printer

def chooce_search():
    while True:
        print("**** Options ****")
        print("1. Add team")
        print("2. Show all teamsw")
        print("3. Add match result")
        print("4. Show standings")
        print("5. Show leading team")
        print("6. Show best attacking team")
        print("7. Show team success rate")
        print("8. Show teams without wins")
        print("9. Show tournament summary")
        print("10. Check championship potential")
        print("0. Exit")

        val = input("Your choice: ")
        if val in ["0", "1","2", "3", "4", "5", "6", "7", "8", "9"]:
            return val
        else:
            mes = "Invalid choice, try agin"
            printer.print_message(mes)

def add_team():
    while True:
        id = input("Entar an ID: ")
        name = input("Enter team's name: ").strip()
        if not name:
            mes = "The name cannot be empty."
            printer.print_message(mes)
            continue
        try:
            id = int(id)
        except ValueError as e:
            mes = f"error: the ID must be an in integer {e}"
            printer.print_message(mes)
            continue
        return id, name

def valid_id_check(id):
    if id < 1:
        mes = "ID must be a positive integer"
        printer.print_message(mes)
        return False
    return True

def duplicate_id_check(id, teams):
    for team in teams:
        if team['id'] == id:
            mes = "ID already exists."
            printer.print_message(mes)
            return False
    return True
    

def valid_name_check(name):
    name = name.split()
    if not name:
        mes = "Team name cannot be empty."
        printer.print_message(mes)
    return True

def duplicate_name_check(name, teams):
    for team in teams:
        if team['name'].lower() == name.lower():
            mes = "Team name already exists."
            printer.print_message(mes)
    return True


def checking_whether_the_teams_have_already_played(home_team_id, away_taem_id, matches):
    for match in matches:
        if match.get("home_team_id") == home_team_id and match.get("away_taem_id") == away_taem_id:
            return False
    return True


def add_match_result(matches):
        home_team_id = input("Enter ID for home team: ")
        away_taem_id = input("Enter ID for away team: ")
        home_goals = input("Enter sum goals for home team: ")
        awey_gowls = input("Enter sum goals for awey team: ")
        try:
            home_team_id = int(home_team_id)
            away_taem_id = int(away_taem_id)
            home_goals = int(home_goals)
            awey_gowls = int(awey_gowls)
        except ValueError as e:
            mes = f"The IDs must be numbers {e}"
            printer.print_message(mes)
            return

        try:
            check_positive_home_team_id = valid_id_check(home_team_id)
            check_positive_away_taem_id = valid_id_check(away_taem_id)
            check_positive_home_goals = valid_id_check(home_goals)
            check_positive_awey_gowls = valid_id_check(awey_gowls)
            if check_positive_awey_gowls == True and check_positive_home_goals == True and check_positive_away_taem_id == True and check_positive_home_team_id == True:
                if home_team_id != away_taem_id:
                    last_check = checking_whether_the_teams_have_already_played(home_team_id, away_taem_id, matches)
                    if last_check == True:
                        return home_team_id, away_taem_id, home_goals, awey_gowls
                        
                    else:
                        mes = "The teams have already played."
                        printer.print_message(mes)
                        return
                mes = "Error: The ID numbers are the same."
                printer.print_message(mes)
                return
        except:
            mes = "IDs must be a positive integer or Different numbers. please Try again"
            printer.print_message(mes)
            return

def update_group_based_on_match_result(home_team_id, away_taem_id, home_goals, awey_gowls, teams):
    if home_goals == awey_gowls:
        draws = 1
    else:
        draws = 0
    
    for team in teams:
        if team.get("id") == home_team_id:
            if home_goals > awey_gowls:
                points_home = 3
                win_home = 1
                loss_home = 0
            elif home_goals < awey_gowls:
                points_home = 0
                win_home = 0
                loss_home = 1
            else:
                points_home = 1
                win_home = 0
                loss_home = 0     
            team["plaied"] += 1
            team["Wins"] += win_home
            team["Draws"] += draws
            team["Losses"] += loss_home
            team["Goals_for"] += home_goals
            team["Points"] += points_home
            team["Goals_against"] += awey_gowls
            
            
            
    for team in teams:
        if team.get("id") == away_taem_id:
            if awey_gowls > home_goals:
                points_awey = 3
                win_awey = 1
                loss_awey = 0
            elif awey_gowls < home_goals:
                points_awey = 0
                win_awey = 0
                loss_home = 1
            else:
                points_awey = 1
                win_awey = 0
                loss_awey = 0
            team["plaied"] += 1
            team["Wins"] += win_awey
            team["Draws"] += draws
            team["Losses"] += loss_awey
            team["Goals_for"] += awey_gowls 
            team["Points"] += points_awey
            team["Goals_against"] += home_goals




def show_standings(teams):
    if len(teams) == 1:
        return teams
    
    sorted_teams = sorted(teams, key=lambda t: t["points"], reverse=True)
    if sorted_teams[0]["points"] == sorted_teams[1]["points"]:
        sorted_teams = sorted(teams, key=lambda t: (t["Goals_for"] - t["Goals_against"]), reverse=True)
        one = teams[0]
        two = teams[1]
        if one["Goals_for"] - one["Goals_against"] == two["Goals_for"] - two["Goals_against"]:
            sorted_teams = sorted(teams, key=lambda t: t["Goals_for"])
            if sorted_teams[0]["Goals_for"] == sorted_teams[1]["Goals_for"]:
                sorted_teams = sorted(teams, key=lambda t: t["name"]) 
    return sorted_teams





        # if sorted_teams[0]

# print("--- רשימה ממוינת לפי נקודות (מהגבוה לנמוך) ---")
# for team in sorted_teams:
#     print(f"{team['name']}: {team['points']} נקודות")


# # 2. שליפת הקבוצה המנצחת (הראשונה אחרי המיון, או בעזרת max)
# # דרך א': הקבוצה הראשונה ברשימה הממוינת
# winner = sorted_teams[0]

# # דרך ב': מציאה ישירה בלי ממיין (יעיל יותר אם צריך רק את המנצחת)
# # winner = max(teams, key=lambda t: t['points'])

# print(f"\nהמנצחת (מקום ראשון): {winner['name']} עם {winner['points']} נקודות")


# # 3. שליפת הקבוצה לה היה הכי פחות שערים
# # משתמשים ב-min לפי מפתח ה-goals
# least_goals_team = min(teams, key=lambda t: t["goals"])

# print(f"הקבוצה עם הכי מעט שערים: {least_goals_team['name']} ({least_goals_team['goals']} שערים)")
    






# def Show_standings_1(teams, matches):
#     mes = "This is a function to display game results by searching for an ID, home team ID / away team ID"
#     printer.print_message(mes)

#     home_team_id = input("Enter ID's home team: ")
#     away_taem_id = input("Enter ID's away team: ")

#     check_positive_home_team_id = valid_id_check(home_team_id)
#     check_positive_away_taem_id = valid_id_check(away_taem_id)
    
#     if check_positive_home_team_id == True and check_positive_away_taem_id == True:

#         for game in matches:
#             if home_team_id == game["home_team_id"] and away_taem_id == game["away_taem_id"]:
#                 home_goals = game["home_goals"]
#                 awey_goals = game["awey_goals"]
#                 for team in teams:
#                     if home_team_id == team["id"]:
#                         home_team_name = team["name"]
#                     if away_taem_id == team["id"]:
#                         away_team_name = team["name"]
#             else:
#                 mes = "No game found"
#                 printer.print_message(mes)
#                 return mes
#         if home_goals > awey_goals:
#             winer = home_team_name
#             points_home = 3
#             points_away = 0
#         elif awey_goals > home_goals:
#             winer = away_team_name
#             points_away = 3
#             points_home = 0
#         else:
#             winer = "Draw"
#             points_home = 1
#             points_away = 1

#         return home_team_id ,away_taem_id, home_team_name, away_team_name, winer, points_home, points_away
#     else:
#         mes = "Invalid inputs"
#         printer.print_message(mes)

                 







teams = [{"id":1, "name":"Maccabi", "plaied": 0,
    "Wins": 0, "Draws": 0, "Losses": 0,
    "Goals_for": 0, "Goals_against": 0, "Points": 0}]
