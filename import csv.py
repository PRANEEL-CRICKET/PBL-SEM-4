import pandas as pd
import mysql.connector

# 🔗 CONNECT TO MYSQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="praneel06",
    database="health_tracking_system"
)

cursor = conn.cursor()

# 👉 OPTIONAL: If files are on Desktop, use full path
# base_path = "C:/Users/Praneel Ghosh/Desktop/"
base_path = ""


# =====================================
# 👤 USERS
# =====================================
df = pd.read_csv(base_path + "users_dataset.csv").fillna("")

for _, row in df.iterrows():
    try:
        query = """
        INSERT INTO users (user_id, user_names, email, user_password, age, gender)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            int(row['user_id']),
            str(row['user_names']),
            str(row['email']),
            str(row['user_password']),
            int(row['age']),
            str(row['gender'])
        )

        cursor.execute(query, values)

    except Exception as e:
        print("❌ USERS ERROR:", e)

conn.commit()
print("✅ USERS DONE")


# =====================================
# 🚶 ACTIVITY
# =====================================
df = pd.read_csv(base_path + "activity_dataset.csv").fillna(0)

for _, row in df.iterrows():
    try:
        timestamp = pd.to_datetime(row['timestamp'], errors='coerce')
        if pd.isna(timestamp):
            continue

        query = """
        INSERT INTO activity_data 
        (activity_id, user_id, recorded_at, steps, calories, distance)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            int(row['activity_id']),
            int(row['user_id']),
            timestamp,
            int(row['steps']),
            int(row['calories']),
            float(row['distance'])
        )

        cursor.execute(query, values)

    except Exception as e:
        print("❌ ACTIVITY ERROR:", e)

conn.commit()
print("✅ ACTIVITY DONE")


# =====================================
# ❤️ HEART
# =====================================
df = pd.read_csv(base_path + "heart_dataset.csv").fillna(0)

for _, row in df.iterrows():
    try:
        timestamp = pd.to_datetime(row['timestamp'], errors='coerce')
        if pd.isna(timestamp):
            continue

        query = """
        INSERT INTO heart_data
        (user_id, recorded_at, heart_rate, max_heart_rate, min_heart_rate, heart_rate_variability)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            int(row['user_id']),
            timestamp,
            int(row['heart_rate']),
            int(row['max_heart_rate']),
            int(row['min_heart_rate']),
            float(row['heart_rate_variability'])
        )

        cursor.execute(query, values)

    except Exception as e:
        print("❌ HEART ERROR:", e)

conn.commit()
print("✅ HEART DONE")


# =====================================
# 😊 MOOD
# =====================================
df = pd.read_csv(base_path + "mood_dataset.csv").fillna(0)

for _, row in df.iterrows():
    try:
        timestamp = pd.to_datetime(row['timestamp'], errors='coerce')
        if pd.isna(timestamp):
            continue

        query = """
        INSERT INTO mood_data
        (user_id, recorded_at, mood_rating)
        VALUES (%s, %s, %s)
        """

        values = (
            int(row['user_id']),
            timestamp,
            int(row['mood_rating'])
        )

        cursor.execute(query, values)

    except Exception as e:
        print("❌ MOOD ERROR:", e)

conn.commit()
print("✅ MOOD DONE")


# =====================================
# 📱 PHONE USAGE
# =====================================
df = pd.read_csv(base_path + "phone_usage_dataset.csv").fillna(0)

for _, row in df.iterrows():
    try:
        timestamp = pd.to_datetime(row['timestamp'], errors='coerce')
        if pd.isna(timestamp):
            continue

        query = """
        INSERT INTO phone_usage_data
        (usage_id, user_id, recorded_at, screen_time, app_usage_time)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            int(row['usage_id']),
            int(row['user_id']),
            timestamp,
            float(row['screen_time']),
            float(row['app_usage_time'])
        )

        cursor.execute(query, values)

    except Exception as e:
        print("❌ PHONE ERROR:", e)

conn.commit()
print("✅ PHONE DONE")


# =====================================
# 😴 SLEEP (UPDATED 🔥)
# =====================================
df = pd.read_csv(base_path + "sleep_dataset.csv").fillna(0)

for _, row in df.iterrows():
    try:
        sleep_start = pd.to_datetime(row['sleep_start'], errors='coerce')
        sleep_end = pd.to_datetime(row['sleep_end'], errors='coerce')

        if pd.isna(sleep_start) or pd.isna(sleep_end):
            print("⚠️ Skipping invalid sleep row")
            continue

        query = """
        INSERT INTO sleep_data
        (user_id, sleep_start, sleep_end, total_sleep_hours, sleep_efficiency, movement_level, sleep_rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            int(row['user_id']),
            sleep_start,
            sleep_end,
            float(row['total_sleep_hours']),   
            float(row['sleep_efficiency']),
            int(row['movement_level']),
            int(row['sleep_rating'])
        )

        cursor.execute(query, values)

    except Exception as e:
        print("❌ SLEEP ERROR:", e)

conn.commit()
print("✅ SLEEP DONE")


# =====================================
# 🔚 CLOSE CONNECTION
# =====================================
cursor.close()
conn.close()

print("🚀 ALL DATA IMPORTED SUCCESSFULLY")