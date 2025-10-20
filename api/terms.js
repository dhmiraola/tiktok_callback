module.exports = (req, res) => {
  res.status(200).send(`
    <html>
      <head><title>Terms of Service</title></head>
      <body style="font-family:sans-serif; padding:20px;">
        <h1>Terms of Service</h1>
        <p>This application is for educational and testing purposes only.</p>
        <p>By using this app, you agree that no personal data is stored or shared.</p>
      </body>
    </html>
  `);
};

