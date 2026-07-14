import os

folders = [
    "static",
    "static/css",
    "static/js",
    "static/images",

    "templates",

    "models",

    "dataset",

    "utils",

    "database"
]

files = [
    "app.py",
    "config.py",
    "requirements.txt",
    "README.md",

    "templates/index.html",
    "templates/login.html",
    "templates/register.html",
    "templates/dashboard.html",
    "templates/crop_prediction.html",
    "templates/fertilizer.html",
    "templates/irrigation.html",
    "templates/weather.html",
    "templates/market.html",
    "templates/result.html",

    "static/css/style.css",
    "static/js/script.js",

    "utils/database.py",
    "utils/prediction.py",

    "database/agricrop.sql"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        pass

print("===================================")
print(" OptiCrop Project Structure Created ")
print("===================================")