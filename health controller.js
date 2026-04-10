const db = require("../config/db");

// 👤 Users
exports.getUsers = (req, res) => {
    db.query("SELECT * FROM users LIMIT 10", (err, result) => {
        if (err) return res.status(500).json({ error: err });
        res.json(result);
    });
};

// 😴 Sleep
exports.getSleep = (req, res) => {
    const id = req.params.id;

    db.query(
        "SELECT * FROM sleep_data WHERE user_id = ?",
        [id],
        (err, result) => {
            if (err) return res.status(500).json({ error: err });
            res.json(result);
        }
    );
};

// ❤️ Heart
exports.getHeart = (req, res) => {
    const id = req.params.id;

    db.query(
        "SELECT * FROM heart_data WHERE user_id = ?",
        [id],
        (err, result) => {
            if (err) return res.status(500).json({ error: err });
            res.json(result);
        }
    );
};

// 📱 Phone
exports.getPhone = (req, res) => {
    const id = req.params.id;

    db.query(
        "SELECT * FROM phone_usage_data WHERE user_id = ?",
        [id],
        (err, result) => {
            if (err) return res.status(500).json({ error: err });
            res.json(result);
        }
    );
};

// 😊 Mood
exports.getMood = (req, res) => {
    const id = req.params.id;

    db.query(
        "SELECT * FROM mood_data WHERE user_id = ?",
        [id],
        (err, result) => {
            if (err) return res.status(500).json({ error: err });
            res.json(result);
        }
    );
};

// 🚶 Activity
exports.getActivity = (req, res) => {
    const id = req.params.id;

    db.query(
        "SELECT * FROM activity_data WHERE user_id = ?",
        [id],
        (err, result) => {
            if (err) return res.status(500).json({ error: err });
            res.json(result);
        }
    );
};
exports.getDashboard = async (req, res) => {
    const id = req.params.id;

    if (!id) {
        return res.status(400).json({ error: "User ID required" });
    }

    try {
        const [sleep] = await db.promise().query(
            "SELECT * FROM sleep_data WHERE user_id = ?",
            [id]
        );

        const [heart] = await db.promise().query(
            "SELECT * FROM heart_data WHERE user_id = ?",
            [id]
        );

        const [mood] = await db.promise().query(
            "SELECT * FROM mood_data WHERE user_id = ?",
            [id]
        );

        const [phone] = await db.promise().query(
            "SELECT * FROM phone_usage_data WHERE user_id = ?",
            [id]
        );

        const [activity] = await db.promise().query(
            "SELECT * FROM activity_data WHERE user_id = ?",
            [id]
        );

        res.json({
            sleep,
            heart,
            mood,
            phone,
            activity
        });

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};