submissions = input()
submissions_language = {}
submissions_points = {}
 
while not submissions == "exam finished":
    if "banned" in submissions:
        banned_user, banned = submissions.split("-")
        submissions_points.pop(banned_user)
 
    else:
        username, language, points = submissions.split("-")
        points = int(points)
 
        # Points submissions
        if username not in submissions_points:
            submissions_points[username] = [points]
        else:
            submissions_points[username].append(points)
 
        # Language submissions
        if language not in submissions_language:
            submissions_language[language] = [username]
        else:
            submissions_language[language].append(username)
 
    submissions = input()
 
print("Results:")
for user, points in sorted(submissions_points.items(), key=lambda x: x[1], reverse=True):
    print(f"{user} | {max(points)}")
 
print("Submissions:")
for language, number in sorted(submissions_language.items()):
    print(f"{language} - {len(number)}")