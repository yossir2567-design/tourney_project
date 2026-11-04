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
    id = int(input("Entar an ID: "))
    name = input("Enter team's name: ")
    return id, name

def Valid_id_check(id):
    if id < 0:
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
    

def Valid_name_check(name):
    if not name.strip():
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
    while True:
        home_team_id = input()
        away_taem_id = input()
        home_goals = input()
        awey_gowls = input()
        try:
            home_team_id = int(home_team_id)
            away_taem_id = int(away_taem_id)
            home_goals = int(home_goals)
            awey_gowls = int(awey_gowls)
        except ValueError as e:
            mes = f"The IDs must be numbers {e}"
            printer.print_message(mes)

        try:
            check_positive_home_team_id = Valid_id_check(home_team_id)
            check_positive_away_taem_id = Valid_id_check(away_taem_id)
            check_positive_home_goals = Valid_id_check(home_goals)
            check_positive_awey_gowls = Valid_id_check(awey_gowls)
            if check_positive_awey_gowls == True and check_positive_home_goals == True and check_positive_away_taem_id == True and check_positive_home_team_id == True:
                if home_team_id != away_taem_id:
                    last_check = checking_whether_the_teams_have_already_played(home_team_id, away_taem_id, matches)
                    if last_check == True:
                        return home_team_id, away_taem_id, home_goals, awey_gowls
                    else:
                        mes = "The teams have already played."
                        printer.print_message(mes)
                mes = "Error: The ID numbers are the same."
                printer.print_message(mes)
        except:
            mes = "IDs must be a positive integer or Different numbers. please Try again"
            printer.print_message(mes)

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

        

teams = [{"id":1, "name":"Maccabi", "plaied": 0,
    "Wins": 0, "Draws": 0, "Losses": 0,
    "Goals_for": 0, "Goals_against": 0, "Points": 0}]
