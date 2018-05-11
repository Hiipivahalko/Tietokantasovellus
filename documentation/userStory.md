### user can create account
* INSERT INTO Account (username, password, motto, admin, email) VALUES (?,?,?, FALSE,?);

### user can create channel and update it (only user is channel master)
* INSERT INTO Channel (name, introduction, mastre_id, public) VALUES (?,?, user_id,?);
* UPDATE Channel SET name='newName', introduction='newIntroduction', public='newPublic' WHERE Channel.id=?;

### user can join channel
* INSERT INTO Accounts (account_id, channel_id) VALUES (user_id, ?);

### user can write message
* INSERT INTO Message (body, writer, account_id, channel_id) VALUES (?, user_username, user_id, ?)

### user can update their informations
* UPDATE Account SET username='newUsername', password='newPassword', motto='newMotto', email='newEmail' WHERE Account.id = user.id

### user can write comment to message
* INSERT INTO Comment (body, writer, message_id, account_id) VALUES (?, ?, ?, user_id)

### user can delete own message the also all messages comments get delete
* DELETE FROM Message WHERE Message.id = ?
* DELETE FROM Comment WHERE Comment.message_id = ?

### user can delete own comment
* DELETE FROM Comment WHERE Comment.id = ?



### admin can remove users
* DELETE FROM Account WHERE Account.id = ?
* DELETE FROM Message WHERE Message.account_id = ?
* DELETE FROM Comment WHERE Comment.account_id = ?

### admin can add users (also superUsers)
* INSERT INTO Account (username, password, motto, admin, email) VALUES (?,?,?,?,?);

### admin can delete all messages
* DELETE FROM Message WHERE Message.id = ?
* DELETE FROM Comment WHERE Comment.message_id = ?

### admin can delete all comments
* DELETE FROM Comment WHERE Comment.id = ?

### admin can delete channels
* DELETE FROM Channel WHERE Channel.id = ?
* DELETE FROM Message WHERE Message.channel_id = ?
* DELETE FROM Comment WHERE Comment.message_id = ?

### admin can change account admin status
* UPDATE Account SET admin = ? WHERE Account.id = ?
