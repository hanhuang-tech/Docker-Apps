const express = require('express');
const app = express();
app.get('/', (req, res) => {
  res.send('Express App is running on default port 9000!')

})
app.listen(9000, () => console.log('Server is up and running on 9000'));
