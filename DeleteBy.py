import os
import datetime
import re

def append_date_to_directory(input_folder, days_to_add):
    today = datetime.datetime.now().date()
    future_date = today + datetime.timedelta(days=days_to_add)
    date_str = future_date.strftime("%Y %m %d")

    for root, dirs, files in os.walk(input_folder, topdown=False):
        for directory in dirs:
            directory_path = os.path.join(root, directory)

            # Extract the existing date from the directory name, if present
            match = re.search(r"\[Del By (\d{4}\s\d{2}\s\d{2})\]$", directory)
            if match:
                existing_date = match.group(1)
            else:
                existing_date = None

            # If there's an existing date, skip the directory
            if existing_date:
                continue
            else:
                new_directory_name = f"{directory} [Del By {date_str}]"
                print("Dir renamed from: " + directory_path + " to: " + new_directory_name)

            # Handle conflicts if the directory already exists
            if os.path.exists(os.path.join(root, new_directory_name)):
                i = 1
                while True:
                    new_directory_name = f"{directory} [{i:02d}] [Del By {date_str}]"
                    print("Conflict detected for: " + directory_path + ", changed to: " + new_directory_name)
                    if not os.path.exists(os.path.join(root, new_directory_name)):
                        break
                    i += 1

            # Rename the directory
            os.rename(directory_path, os.path.join(root, new_directory_name))


if __name__ == "__main__":
    input_folder = "D:\Personal\Projects\Programming\Append Delete By Date\Test"
    days_to_add = int(120)

    append_date_to_directory(input_folder, days_to_add)
