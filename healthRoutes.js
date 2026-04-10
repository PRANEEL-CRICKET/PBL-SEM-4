const express = require("express");
const router = express.Router();
const ctrl = require("../controllers/healthController");

router.get("/users", ctrl.getUsers);
router.get("/sleep/:id", ctrl.getSleep);
router.get("/heart/:id", ctrl.getHeart);
router.get("/phone/:id", ctrl.getPhone);
router.get("/mood/:id", ctrl.getMood);
router.get("/activity/:id", ctrl.getActivity);

module.exports = router;
router.get("/dashboard/:id", ctrl.getDashboard);