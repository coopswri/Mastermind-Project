import pygame, sqlite3
from MergeSort import MergeSort

pygame.init()

#this creates a connection between the program and the database
connection = sqlite3.connect("Mastermind.db")

#this makes the cursor to interact with the database
cursor = connection.cursor()


#this function checks if the username and password entered are already within the database and either returns True or False
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

#this function checks if the username exists already and if it does logs in and if not makes a new account for the user
def LoginOrSignup(username, password, score):
    cursor.execute("SELECT userID FROM player_info WHERE username = ?", (username,))

    result = cursor.fetchall()

    if result:
        userID = result[0][0]
        cursor.execute("SELECT first_score, second_score, third_score FROM player_scores WHERE userID = ?", (userID,))
        score_list = []

        #adds all the scores to a list and adds the users latest score
        for item in cursor.fetchall()[0]:
            score_list.append(item)
        score_list.append(score)
        
        #enters the merge sort file and removes the lowest num
        new_score_list = MergeSort(score_list)
        new_score_list.reverse()
        new_score_list.pop()
        
        #assigns the scores to a variable
        score_1 = new_score_list[0]
        score_2 = new_score_list[1]
        score_3 = new_score_list[2]
        average_score = 0

        #adds all the scores together and divides it by three to get the average score, making sure it is a whole number
        for item in new_score_list:
            average_score += item 
        average_score = int(average_score / 3)

        #inputs the new list of scores into the database, by using the userID
        cursor.execute("UPDATE player_scores SET first_score = ? WHERE userID = ? ", (score_1, userID))
        cursor.execute("UPDATE player_scores SET second_score = ? WHERE userID = ? ", (score_2, userID))
        cursor.execute("UPDATE player_scores SET third_score = ? WHERE userID = ? ", (score_3, userID))
        cursor.execute("UPDATE player_scores SET average_score = ? WHERE userID = ? ", (average_score, userID))

    else:
        #selects the highest userID in the database and adds one to it for the new users userID
        cursor.execute("SELECT MAX(userID) FROM player_info")
        
        num = cursor.fetchall()[0][0]
        userID = num + 1

        #creates the new records in both the player_info and player_scores table
        cursor.execute("INSERT INTO player_info VALUES (?, ?, ?)", (userID, username, password))
        cursor.execute("INSERT INTO player_scores VALUES (?, ?, ?, ?, ?)", (userID, score, 0, 0, (score/3)))



    connection.commit()

#this function selects the highest and average score from the record for the user and returns them
def ScoreChecker(username):
    cursor.execute("SELECT userID FROM player_info WHERE username = ?", (username,))

    userID = cursor.fetchall()[0][0]
    cursor.execute("SELECT first_score, average_score FROM player_scores WHERE userID = ?", (userID,))
    return cursor.fetchall()

