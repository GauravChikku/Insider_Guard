const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    username: { type: String, required: true },
    activityLogs: { type: Array, default: [] }
});

module.exports = mongoose.model('User', userSchema);
