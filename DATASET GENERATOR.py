import pandas as pd
import random
import string
from faker import Faker
from datetime import timedelta

fake = Faker("en_IN")

NUM_USERS = 1000

# ============================
# 🔐 PASSWORD GENERATOR
# ============================
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# ============================
# 😴 SLEEP RATING FUNCTION
# ============================
def get_sleep_rating(hours):
    if hours < 5:
        return 1
    elif hours < 6:
        return 2
    elif hours < 7:
        return 3
    elif hours < 8:
        return 4
    else:
        return 5

# ============================
# 👤 USERS DATA
# ============================
users = []

for user_id in range(1, NUM_USERS + 1):
    users.append([
        user_id,
        fake.name(),
        fake.email(),
        generate_password(),
        random.randint(18, 60),
        random.choice(['Male', 'Female'])
    ])

users_df = pd.DataFrame(users, columns=[
    'user_id', 'user_names', 'email', 'user_password', 'age', 'gender'
])
users_df.to_csv("users_dataset.csv", index=False)

print("✅ Users dataset created")


# ============================
# 🚶 ACTIVITY DATA
# ============================
activity = []

for user_id in range(1, NUM_USERS + 1):
    for i in range(random.randint(10, 20)):
        activity.append([
            len(activity) + 1,
            user_id,
            fake.date_time_between(start_date='-30d', end_date='now'),
            random.randint(1000, 15000),
            random.randint(150, 800),
            round(random.uniform(0.5, 10), 2)
        ])

activity_df = pd.DataFrame(activity, columns=[
    'activity_id', 'user_id', 'timestamp', 'steps', 'calories', 'distance'
])
activity_df.to_csv("activity_dataset.csv", index=False)

print("✅ Activity dataset created")


# ============================
# ❤️ HEART DATA
# ============================
heart = []

for user_id in range(1, NUM_USERS + 1):
    for _ in range(random.randint(10, 20)):
        hr = random.randint(60, 120)

        heart.append([
            user_id,
            fake.date_time_between(start_date='-30d', end_date='now'),
            hr,
            hr + random.randint(5, 30),
            hr - random.randint(5, 20),
            round(random.uniform(20, 100), 2)
        ])

heart_df = pd.DataFrame(heart, columns=[
    'user_id', 'timestamp', 'heart_rate',
    'max_heart_rate', 'min_heart_rate', 'heart_rate_variability'
])
heart_df.to_csv("heart_dataset.csv", index=False)

print("✅ Heart dataset created")


# ============================
# 😊 MOOD DATA
# ============================
mood = []

for user_id in range(1, NUM_USERS + 1):
    for _ in range(random.randint(5, 15)):
        mood.append([
            user_id,
            fake.date_time_between(start_date='-30d', end_date='now'),
            random.randint(1, 5)
        ])

mood_df = pd.DataFrame(mood, columns=[
    'user_id', 'timestamp', 'mood_rating'
])
mood_df.to_csv("mood_dataset.csv", index=False)

print("✅ Mood dataset created")


# ============================
# 📱 PHONE USAGE DATA
# ============================
phone = []

for user_id in range(1, NUM_USERS + 1):
    for i in range(random.randint(10, 20)):
        screen_time = round(random.uniform(1, 10), 2)

        phone.append([
            len(phone) + 1,
            user_id,
            fake.date_time_between(start_date='-30d', end_date='now'),
            screen_time,
            round(screen_time * random.uniform(0.5, 1.0), 2)
        ])

phone_df = pd.DataFrame(phone, columns=[
    'usage_id', 'user_id', 'timestamp', 'screen_time', 'app_usage_time'
])
phone_df.to_csv("phone_usage_dataset.csv", index=False)

print("✅ Phone usage dataset created")


# ============================
# 😴 SLEEP DATA (FINAL FIXED)
# ============================
sleep = []

movement_map = {
    'Low': 1,
    'Medium': 2,
    'High': 3
}

for user_id in range(1, NUM_USERS + 1):
    for _ in range(random.randint(5, 15)):

        sleep_start = fake.date_time_between(start_date='-30d', end_date='now')

        # Sleep duration (4–10 hrs)
        sleep_hours = round(random.uniform(4, 10), 2)

        sleep_end = sleep_start + timedelta(hours=sleep_hours)

        sleep_rating = get_sleep_rating(sleep_hours)

        sleep_efficiency = round(random.uniform(70, 100), 2)

        movement_level = movement_map[random.choice(['Low', 'Medium', 'High'])]

        sleep.append([
            user_id,
            sleep_start,
            sleep_end,
            sleep_hours,
            sleep_efficiency,
            movement_level,
            sleep_rating
        ])

sleep_df = pd.DataFrame(sleep, columns=[
    'user_id',
    'sleep_start',
    'sleep_end',
    'total_sleep_hours',
    'sleep_efficiency',
    'movement_level',
    'sleep_rating'
])

sleep_df.to_csv("sleep_dataset.csv", index=False)

print("✅ Sleep dataset created")


# ============================
# 🎉 DONE
# ============================
print("\n🚀 ALL DATASETS GENERATED SUCCESSFULLY!")