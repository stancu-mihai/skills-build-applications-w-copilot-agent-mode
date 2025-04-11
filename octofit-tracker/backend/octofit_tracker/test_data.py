# Sample test data for the octofit_db database

test_users = [
    {"email": "user1@example.com", "name": "User One"},
    {"email": "user2@example.com", "name": "User Two"},
    {"email": "user3@example.com", "name": "User Three"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
    {"name": "Team Beta", "members": ["user3@example.com"]},
]

test_activities = [
    {"user": "user1@example.com", "activity_type": "Running", "duration": 30, "date": "2025-04-10"},
    {"user": "user2@example.com", "activity_type": "Cycling", "duration": 45, "date": "2025-04-09"},
]

test_leaderboard = [
    {"user": "user1@example.com", "score": 100},
    {"user": "user2@example.com", "score": 80},
]

test_workouts = [
    {"name": "Morning Yoga", "description": "A relaxing yoga session", "duration": 60},
    {"name": "HIIT", "description": "High-intensity interval training", "duration": 30},
]
