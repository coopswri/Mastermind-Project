import pygame, sqlite3
from MergeSort import MergeSort

pygame.init()

connection = sqlite3.connect("Mastermind.db")
cursor = connection.cursor()



def CheckingName(username, password):
    cursor.execute("SELECT * FROM player_info WHERE username = ?", (username,))
    items = cursor.fetchall()
    if items == []:
        return True
    elif str(items[0][1]) == username and str(items[0][2]) == password:
        return True
    else:
        return False

    connection.commit()


def LoginOrSignup(username, password, score):
    cursor.execute("SELECT userID FROM player_info WHERE username = ?", (username,))

    result = cursor.fetchall()

    if result:
        userID = result[0][0]
        cursor.execute("SELECT first_score, second_score, third_score FROM player_scores WHERE userID = ?", (userID,))
        score_list = []

        for item in cursor.fetchall()[0]:
            score_list.append(item)
        score_list.append(score)
        
        new_score_list = MergeSort(score_list)
        new_score_list.reverse()
        new_score_list.pop()
        
        score_1 = new_score_list[0]
        score_2 = new_score_list[1]
        score_3 = new_score_list[2]
        average_score = 0

        for item in new_score_list:
            average_score += item 
        average_score = int(average_score / 3)

        cursor.execute("UPDATE player_scores SET first_score = ? WHERE userID = ? ", (score_1, userID))
        cursor.execute("UPDATE player_scores SET second_score = ? WHERE userID = ? ", (score_2, userID))
        cursor.execute("UPDATE player_scores SET third_score = ? WHERE userID = ? ", (score_3, userID))
        cursor.execute("UPDATE player_scores SET average_score = ? WHERE userID = ? ", (average_score, userID))

    else:
        cursor.execute("SELECT MAX(userID) FROM player_info")
        
        num = cursor.fetchall()[0][0]
        userID = num + 1

        cursor.execute("INSERT INTO player_info VALUES (?, ?, ?)", (userID, username, password))
        cursor.execute("INSERT INTO player_scores VALUES (?, ?, ?, ?, ?)", (userID, score, 0, 0, (score/3)))



    connection.commit()


def ScoreChecker(username):
    cursor.execute("SELECT userID FROM player_info WHERE username = ?", (username,))

    userID = cursor.fetchall()[0][0]
    cursor.execute("SELECT first_score, average_score FROM player_scores WHERE userID = ?", (userID,))
    return cursor.fetchall()

