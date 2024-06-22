import aiohttp
import discord
from bs4 import BeautifulSoup
import requests
import re



class SportBotLogic:
    @staticmethod
    def SeperateCharDigits(input_string):
        return re.sub(r"(?<=\D)(?=\d)", ", Number: ", input_string)

    @staticmethod
    def isDigit(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    @staticmethod
    def GetNFLRoster(abv, team_name):
        url = f"https://www.espn.com/nfl/team/roster/_/name/{abv}/{team_name}"
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page_to_scrape = requests.get(url, headers=Headers)
        if page_to_scrape.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page_to_scrape.status_code}")
            return

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        roster = soup.find("section", {"class": "Roster"})
        result = []
        if roster:
            print("Found the 'Roster' section")

        roster_table = soup.find("div", {"class": "Roster__MixedTables"})

        if roster_table:
            print("Found Roster Table")
        else:
            print("Roster Table not found")

        player_rows = roster_table.findAll("tr", attrs={"class": "Table__TR"})

        for row in player_rows:
            columns = row.findAll('td')
            if len(columns) >= 8:
                player_name = columns[1].text.strip()
                player_position = columns[2].text.strip()
                player_age = columns[3].text.strip()
                player_height = columns[4].text.strip()
                player_weight = columns[5].text.strip()
                player_exp = columns[6].text.strip()
                player_college = columns[7].text.strip()
                result.append(f"Name: {SportBotLogic.SeperateCharDigits(player_name)}, Position: {player_position}, Age: {player_age}, Height: {player_height}, Weight: {player_weight}, Experience: {player_exp}, College: {player_college}")
        return "\n".join(result)


    @staticmethod
    def GetNBARoster(abv, team_name):
        url = f"https://www.espn.com/nba/team/roster/_/name/{abv}/{team_name}"
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page_to_scrape = requests.get(url, headers=Headers)
        if page_to_scrape.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page_to_scrape.status_code}")
            return

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        roster = soup.find("section", {"class": "Roster"})

        if roster:
            print("Found the 'Roster' section")

        roster_table = soup.find("div", {"class": "Roster__MixedTables"})

        if roster_table:
            print("Found Roster Table")
        else:
            print("Roster Table not found")

        player_rows = roster_table.findAll("tr", attrs={"class": "Table__TR"})
        result = []
        for row in player_rows:
            columns = row.findAll('td')
            if len(columns) >= 7:
                player_name = columns[1].text.strip()
                player_position = columns[2].text.strip()
                player_age = columns[3].text.strip()
                player_height = columns[4].text.strip()
                player_weight = columns[5].text.strip()
                player_college = columns[6].text.strip()
                player_salary = columns[7].text.strip()
                result.append(f"Name: {SportBotLogic.SeperateCharDigits(player_name)}, Position: {player_position}, Age: {player_age}, Height: {player_height}, Weight: {player_weight}, College: {player_college}, Salary: {player_salary}")
        return "\n".join(result)

    @staticmethod
    def GetMLBRoster(abv, team_name):
        url = f"https://www.espn.com/mlb/team/roster/_/name/{abv}/{team_name}"
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page_to_scrape = requests.get(url, headers=Headers)
        if page_to_scrape.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page_to_scrape.status_code}")
            return

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        roster = soup.find("section", {"class": "Roster"})

        if roster:
            print("Found the 'Roster' section")

        roster_table = soup.find("div", {"class": "Roster__MixedTables"})

        if roster_table:
            print("Found Roster Table")
        else:
            print("Roster Table not found")

        player_rows = roster_table.findAll("tr", attrs={"class": "Table__TR"})
        result = []
        for row in player_rows:
            columns = row.findAll('td')
            if len(columns) >= 7:
                player_name = columns[1].text.strip()
                player_position = columns[2].text.strip()
                player_batting_hand = columns[3].text.strip()
                player_throwing_hand = columns[4].text.strip()
                player_age = columns[5].text.strip()
                player_height = columns[6].text.strip()
                player_weight = columns[7].text.strip()
                player_birth_place = columns[8].text.strip()
                result.append(f"Name: {SportBotLogic.SeperateCharDigits(player_name)}, Position: {player_position}, Batting Hand: {player_batting_hand}, Throwing Hand: {player_throwing_hand},  Age: {player_age}, Height: {player_height}, Weight: {player_weight}, Birth Place: {player_birth_place}")
        return "\n" .join(result)

    @staticmethod
    def GetNFLTeamStats(abv, year, seasontype):
        url = f"https://www.espn.com/nfl/team/stats/_/type/team/name/{abv}/season/{year}/seasontype/{seasontype}"
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page_to_scrape = requests.get(url, headers=Headers)
        if page_to_scrape.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page_to_scrape.status_code}")
            return
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        name_table = soup.find("tbody", {"class": "Table__TBODY"})

        stat_table = soup.find("div", attrs = {"class": "Table__ScrollerWrapper"})
        stat_table_body = stat_table.find("tbody", {"class": "Table__TBODY"})

        stat_row = stat_table_body.findAll("tr")
        if stat_table:
            print("stat table found")
        if name_table:
            print("name table found")
        if stat_table_body:
            print("Stat table body found")
        result = []
        rows = name_table.findAll("tr")
        for rows, stat_row in zip(rows, stat_row):
            data = rows.find("td")

            stat_data = stat_row.findAll("td", attrs = {"class": "Table__TD"})
            if len(stat_data) == 2:
                team_stat = stat_data[0].text.strip()
                opponent_stat = stat_data[1].text.strip()
                result.extend([data.text.strip(), "-", "Team:",  team_stat, " Opponents:", opponent_stat])
        return '\n'.join(result)

    @staticmethod
    def GetNFLPlayerStats(abv, year, player_name, seasonType ):
        url = f"https://www.espn.com/nfl/team/stats/_/name/{abv}/season/{year}/seasontype/{seasonType}"
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page_to_scrape = requests.get(url, headers=Headers)

        if page_to_scrape.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page_to_scrape.status_code}")
            return

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        tables = soup.findAll("div", {"class": "ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize"})

        for table in tables:
            player_names_table = table.findAll("a", attrs={"class": "AnchorLink"})
            table_title = table.find("div", attrs={"class": "Table__Title"})
            table_header = table.findAll("span", attrs ={"class": "fw-medium"})

            header_list = []
            player_stat_list = []
            result = []

            if table_header:
                for header in table_header:
                    header_list.append(header.text.strip())

            for idx, player in enumerate(player_names_table):
                if player and player.text.strip() == player_name:
                    player_stat_table = table.find("table", attrs={"class": "Table Table--align-right"})
                    player_stat_row = player_stat_table.findAll("tr", attrs = {"class": "Table__TR Table__TR--sm Table__even"})

                    if player_stat_row:
                        if idx < len(player_stat_row):
                            stat_cells = player_stat_row[idx].findAll("td")
                            for cell in stat_cells:
                                player_stat_list.append(cell.text.strip())
                    if table_header:
                        for header in table_header:
                            header_list.append(header.text.strip())

                    print(table_title.text.strip(), "Stats for", player.text.strip())
                    for index, stat in enumerate(player_stat_list):
                        result.extend([header_list[index], ": ", player_stat_list[index]])
            print(result)
            return "\n".join(result)


    @staticmethod
    def GetNBAPlayerStats(abv, year, player_name, seasonType):
        url = f"https://www.espn.com/nba/team/stats/_/name/{abv}/season/{year}/seasontype/{seasonType}"
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page_to_scrape = requests.get(url, headers=Headers)

        if page_to_scrape.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page_to_scrape.status_code}")
            return

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        tables = soup.findAll("div", {"class": "ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize"})

        for table in tables:
            player_names_table = table.findAll("a", attrs={"class": "AnchorLink"})
            table_title = table.find("div", attrs={"class": "Table__Title"})
            table_header = table.findAll("span", attrs ={"class": "fw-medium"})

            header_list = []
            player_stat_list = []
            result = []

            if table_header:
                for header in table_header:
                    header_list.append(header.text.strip())

            for idx, player in enumerate(player_names_table):
                if player and player.text.strip() == player_name:
                    player_stat_table = table.find("table", attrs={"class": "Table Table--align-right"})
                    player_stat_row = player_stat_table.findAll("tr", attrs = {"class": "Table__TR Table__TR--sm Table__even"})

                    if player_stat_row:
                        if idx < len(player_stat_row):
                            stat_cells = player_stat_row[idx].findAll("td")
                            for cell in stat_cells:
                                player_stat_list.append(cell.text.strip())
                    if table_header:
                        for header in table_header:
                            header_list.append(header.text.strip())

                    result.extend([table_title.text.strip(), "Stats for", player.text.strip()])
                    for index, stat in enumerate(player_stat_list):
                        result.extend([header_list[index], ": ", player_stat_list[index]])
            print(result)
            return "".join(result)

    @staticmethod
    def GetMLBPlayerStats(abv, year, player_name, seasonType):
        url = f"https://www.espn.com/mlb/team/stats/_/name/{abv}/season/{year}/seasontype/{seasonType}"
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page_to_scrape = requests.get(url, headers=Headers)

        if page_to_scrape.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page_to_scrape.status_code}")
            return

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        tables = soup.findAll("div", {"class": "ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize"})

        for table in tables:
            player_names_table = table.findAll("a", attrs={"class": "AnchorLink"})
            table_title = table.find("div", attrs={"class": "Table__Title"})
            table_header = table.findAll("span", attrs ={"class": "fw-medium"})

            header_list = []
            player_stat_list = []
            result = []

            if table_header:
                for header in table_header:
                    header_list.append(header.text.strip())

            for idx, player in enumerate(player_names_table):
                if player and player.text.strip() == player_name:
                    player_stat_table = table.find("table", attrs={"class": "Table Table--align-right"})
                    player_stat_row = player_stat_table.findAll("tr", attrs = {"class": "Table__TR Table__TR--sm Table__even"})

                    if player_stat_row:
                        if idx < len(player_stat_row):
                            stat_cells = player_stat_row[idx].findAll("td")
                            for cell in stat_cells:
                                player_stat_list.append(cell.text.strip())
                    if table_header:
                        for header in table_header:
                            header_list.append(header.text.strip())

                    result.extend([table_title.text.strip(), "Stats for", player.text.strip()])
                    for index, stat in enumerate(player_stat_list):
                        result.extend([header_list[index], player_stat_list[index]])
            return "".join(result)

    @staticmethod
    def GetNFLStandings(year, seasonType):
        url = f"https://www.nfl.com/standings/division/{year}/{seasonType}"
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        page_to_scrape = requests.get(url, headers=Headers)

        if page_to_scrape.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {page_to_scrape.status_code}")
            return

        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        tables = soup.findAll("div", attrs = {"class": "d3-o-table--horizontal-scroll"})

        if tables:
            print("tables found")

        for table in tables:
            teams = table.findAll("div", attrs = {"class": "d3-o-club-fullname"})
            headers = table.findAll("th")
            stats = table.findAll("td")
            stat_list = []
            team_list = []
            header_list = []

            for header in headers:
                header_list.append(header.text.strip())

            for stat in stats:
                if SportBotLogic.isDigit((stat.text.strip())):
                    stat_list.append(stat.text.strip())

            for team in teams:
                for sup in team.findAll("sup"):
                    sup.decompose()
                team_list.append(team.text.strip())
            print(header_list[0])

            for team in team_list[0:4]:
                print(header_list[1:8])
                print(team, stat_list[0:8])
            print("\n")




